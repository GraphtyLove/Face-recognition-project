from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
from werkzeug.utils import secure_filename
import psycopg2
import time



FILE_PATH = os.path.dirname(os.path.realpath(__file__))

# * ---------- Create App --------- *
app = Flask(__name__)
CORS(app, support_credentials=True)

# * ---------- DATABASE CONFIG --------- *
# DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = "postgres://tuuiojqb:0ocbMkkVWOKIrfMenjjakNLT5JNQpWu8@manny.db.elephantsql.com:5432/tuuiojqb"





# * --------------------  ROUTES ------------------- *
@app.route('/hello_world', methods=['GET'])
def hello_world():
    print("hi")
    print(request.get_json())
    return "hello world"


@app.route('/receive_data', methods=['POST'])
def get_receive_data():
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)

        # Check if the user is already in the DB
        try:
            connection = psycopg2.connect(user="tuuiojqb",
                                          password="0ocbMkkVWOKIrfMenjjakNLT5JNQpWu8",
                                          host="manny.db.elephantsql.com",
                                          port="5432",
                                          database="tuuiojqb")

            cursor = connection.cursor()
            is_user_is_there_today = f"SELECT * FROM users WHERE date = '{json_data['date']}' AND name = '{json_data['name']}'"

            cursor.execute(is_user_is_there_today)
            result = cursor.fetchall()
            connection.commit()

            print('result is: ', result)

            if result:
               print('user IN')
               update_user_querry = f"UPDATE users SET departure_time = '{json_data['hour']}' WHERE name = '{json_data['name']}' AND date = '{json_data['date']}'"
               cursor.execute(update_user_querry)
            else:
                print("user OUT")
                insert_user_querry = f"INSERT INTO users (name, date, arrival_time) VALUES ('{json_data['name']}', '{json_data['date']}', '{json_data['hour']}')"
                cursor.execute(insert_user_querry)

        except (Exception, psycopg2.DatabaseError) as error:
            print("ERROR DB: ", error)
        finally:
            connection.commit()
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

        return jsonify(json_data)
        # return 'lol'





# * ---------- Run Server ---------- *
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=os.environ['PORT']) -> DOCKER