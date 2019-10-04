from datetime import date
import face_recognition
import numpy as np
import cv2, queue, threading, time, json
import requests

# bufferless VideoCapture
class VideoCapture:
    def __init__(self, name):
        self.cap = cv2.VideoCapture(name)
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()

    # read frames as soon as they are available, keeping only most recent one
    def _reader(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()   # discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            self.q.put(frame)

    def read(self):
        return self.q.get()

# Select the webcam of the computer
# video_capture = VideoCapture('https://stream-eu1-charlie.dropcam.com:443/nexus_aac/b85a6ec812c045cd921f4164e8e7ecc0/playlist.m3u8?public=GqJifk6U25')
video_capture = VideoCapture(0)

# video_capture.set(5,1)

# * -------------------- USERS -------------------- *

# * ---------- MAXIM ---------- *
# Select an image to teach to the machine how to recognize
maxim_face = face_recognition.load_image_file("assets/img/users/maxim.jpg")
maxim_face_encoding = face_recognition.face_encodings(maxim_face)[0]


# * ---------- GEOFFREY ---------- *
# Load a second sample picture and learn how to recognize it.
Geoffrey_face = face_recognition.load_image_file("assets/img/users/geoffrey.jpg")
Geoffrey_face_encoding = face_recognition.face_encodings(maxim_face)[0]


# * ---------- XAVIER ---------- *
# Select an image to teach to the machine how to recognize
xavier_face = face_recognition.load_image_file("assets/img/users/xavier.jpg")
xavier_face_encoding = face_recognition.face_encodings(xavier_face)[0]


# * ---------- JEREMY ---------- *
# Select an image to teach to the machine how to recognize
jeremy_face = face_recognition.load_image_file("assets/img/users/jeremy.jpg")
jeremy_face_encoding = face_recognition.face_encodings(jeremy_face)[0]


# * ---------- giuliano ---------- *
# Select an image to teach to the machine how to recognize
giuliano_face = face_recognition.load_image_file("assets/img/users/giuliano.jpg")
giuliano_face_encoding = face_recognition.face_encodings(giuliano_face)[0]


# * ---------- MATHIEU ---------- *
# Select an image to teach to the machine how to recognize
mathieu_face = face_recognition.load_image_file("assets/img/users/mathieu.jpg")
mathieu_face_encoding = face_recognition.face_encodings(mathieu_face)[0]

# * ---------- CASSANDRA ---------- *
# Select an image to teach to the machine how to recognize
cassandra_face = face_recognition.load_image_file("assets/img/users/cassandra.jpg")
cassandra_face_encoding = face_recognition.face_encodings(cassandra_face)[0]




# Create arrays of known face encodings and their names
known_face_encodings = [
    maxim_face_encoding,
    Geoffrey_face_encoding,
    xavier_face_encoding,
    jeremy_face_encoding,
    giuliano_face_encoding,
    mathieu_face_encoding,
    cassandra_face_encoding
]
known_face_names = [
    "Maxim Berge",
    "Geoffrey",
    "Xavier",
    "Jeremy",
    "Giuliano",
    "Mathieu",
    "Cassandra"
]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


while True:
    # for i in range(5):
    #     video_capture.grab()
    # Grab a single frame of video
    frame = video_capture.read()
    
    # # Resize frame of video to 1/4 size for faster face recognition processing
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # print(sys.exc_info())
    # # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    # frame = small_frame[:, :, ::-1]
    
    # Process every frame only one time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        # Initialize an array for the name of the detected users
        face_names = []


        # * ---------- Initialyse JSON to EXPORT --------- *
        json_to_export = {}
        
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                # * ---------- SAVE data to send to the API -------- *
                json_to_export['name'] = name
                json_to_export['hour'] = f'{time.localtime().tm_hour}:{time.localtime().tm_min}'
                json_to_export['date'] = f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}'
                json_to_export['picture_array'] = frame.tolist()

                # * ---------- SEND data to API --------- *
                test = {
                    "test": 1
                }
                r = requests.post(url='http://127.0.0.1:5000/receive_data', json=json_to_export)
                print("Status: ", r.status_code)

            face_names.append(name)
        
    process_this_frame = not process_this_frame
            
            # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        # top *= 4
        # right *= 4
        # bottom *= 4
        # left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
        
        
        
