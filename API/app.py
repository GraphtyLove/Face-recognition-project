from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import psycopg2
import cv2
import numpy as np
import json
import sys

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

# Load the horaires to know ho can leave at what time
with open('assets/json/horaires.json', 'r') as f:
    HORAIRES = json.load(f)
# * ---------- Create App --------- *
app = Flask(__name__)
CORS(app, support_credentials=True)


# * ---------- DATABASE CONFIG --------- *
# DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = "postgres://tuuiojqb:0ocbMkkVWOKIrfMenjjakNLT5JNQpWu8@manny.db.elephantsql.com:5432/tuuiojqb"



# * --------------------  ROUTES ------------------- *

# Get data from the face recognition
@app.route('/receive_data', methods=['POST'])
def get_receive_data():
    if request.method == 'POST':
        json_data = request.get_json()

        # Check if the user is already in the DB
        try:
            connection = psycopg2.connect(user="tuuiojqb",
                                          password="0ocbMkkVWOKIrfMenjjakNLT5JNQpWu8",
                                          host="manny.db.elephantsql.com",
                                          port="5432",
                                          database="tuuiojqb")

            cursor = connection.cursor()
            is_user_is_there_today =\
                f"SELECT * FROM users WHERE date = '{json_data['date']}' AND name = '{json_data['name']}'"

            cursor.execute(is_user_is_there_today)
            result = cursor.fetchall()
            connection.commit()

            if result:
               print('user already in db')
               image_path = f"{FILE_PATH}/assets/img/history/{json_data['date']}/{json_data['name']}/departure.jpg"
                # Save image
               os.makedirs(f"{FILE_PATH}/assets/img/history/{json_data['date']}/{json_data['name']}", exist_ok=True)
               cv2.imwrite(image_path, np.array(json_data['picture_array']))

               json_data['picture_path'] = image_path

               # Calculate if the employee left early or not
               right_departure_time = HORAIRES['default']['departure_time']
               for key, value in HORAIRES.items():
                   if key == json_data['name']:
                       right_departure_time = value['departure_time']
               left_early = right_departure_time > json_data['hour']


               update_user_querry = f"UPDATE users SET departure_time = '{json_data['hour']}',departure_picture = '{json_data['picture_path']}',left_early = {left_early} WHERE name = '{json_data['name']}' AND date = '{json_data['date']}'"
               cursor.execute(update_user_querry)

            else:
                print("user not in db")
                # Save image
                image_path = f"{FILE_PATH}/assets/img/history/{json_data['date']}/{json_data['name']}/arrival.jpg"
                os.makedirs(f"{FILE_PATH}/assets/img/history/{json_data['date']}/{json_data['name']}", exist_ok=True)
                cv2.imwrite(image_path, np.array(json_data['picture_array']))
                json_data['picture_path'] = image_path

                # Calculate if the employee was late or not
                right_arrival_time = HORAIRES['default']['arrival_time']
                for key, value in HORAIRES.items():
                    if key == json_data['name']:
                        right_arrival_time = value['arrival_time']
                was_late = right_arrival_time < json_data['hour']

                insert_user_querry = f"INSERT INTO users (name, date, arrival_time, arrival_picture,is_late) VALUES ('{json_data['name']}', '{json_data['date']}', '{json_data['hour']}', '{json_data['picture_path']}',{was_late})"
                cursor.execute(insert_user_querry)

        except (Exception, psycopg2.DatabaseError) as error:
            print("ERROR DB: ", sys.exc_info())
        finally:
            connection.commit()
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

        return jsonify(json_data)

# add new employee
@app.route('/add_employee', methods=['POST'])
def add_employee():
    imagefile = request.files.get('image', '')
    json_data = request.get_json()

    file_path = os.path.join('assets/img/users/', json_data['name'])
    imagefile.save(file_path)

    return 'new employee succesfully added'

# delete employee
@app.route('/delete_employee', methods=['POST'])
def delete_employee():
    json_data = request.get_json()
    file_path = os.path.join('assets/img/users/', json_data['name']+'.jpg')
    os.remove(file_path)

    return 'employee succesfully removed'


# this route is bugged
@app.route('/attendance', methods=['POST'])
def attendance():
    json_data = request.get_json()
    sql_query = "SELECT * FROM users WHERE "
    if json_data['date']:
        sql_query += f"date = '{json_data['date']}' "
    if json_data['date'] and json_data['name']:
        sql_query += 'AND'
    if json_data['name']:
        sql_query += f"name = '{json_data['name']}'"

    connection = psycopg2.connect(user="tuuiojqb",
                                  password="0ocbMkkVWOKIrfMenjjakNLT5JNQpWu8",
                                  host="manny.db.elephantsql.com",
                                  port="5432",
                                  database="tuuiojqb")

    cursor = connection.cursor()
    # is_user_is_there_today = \
    #     f"SELECT * FROM users WHERE date = '{json_data['date']}' AND name = '{json_data['name']}'"

    cursor.execute(sql_query)
    result = cursor.fetchall()
    connection.commit()
    print(result)
    return {'result': i for i in result}
# * ---------- Run Server ---------- *
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=os.environ['PORT']) -> DOCKER