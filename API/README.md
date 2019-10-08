# Face Recognition API

## Python environement

**Python version:** `Python 3.6.8`

For this project, we used `virtualenv` as enviroment.
You can find it in `API/env`.
You can **activate** it with: `$ source env/bin/activate` and disable it with `$ deactivate`.

## Python depencies

You can install all the dependencies with `$ pip install -r requirements.txt`
Be carefull to have `CMake` installed before trying to install `face_recognition`. You can install it with `$ pip3 install CMake`.

## How to use it

There are two components in the backend: `app.py` and `get_name_from_camera_feed.py`.

    - **app.py:** This is the API itself, it handle routes. You can run it with `$ python3 app.py`.
    - **get_name_from_camera_feed.py:** This is the algorithm that read the video feed and apply face recognition. You can run it with `$ python3 get_name_from_camera_feed.py`. By default it will select the camera of your computer, but you can change it by any video feed, just change the value of `video_capture = VideoCapture(0)` 0 is the prinary webcam of your computer. You can also add multiple feeds.