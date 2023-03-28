"""-----------------------------------------------------------------------------------------------------------------------------------
- Software Name: 
- Language: Python
- Developers: Emilio Rivera Macías and Carlos Cancino Escobar
- Date: March 27, 2023
- Contacts: emilioriveramacias@gmail.com
-----------------------------------------------------------------------------------------------------------------------------------"""

#necessary imports ----->
from flask import Flask, jsonify, abort, request
from sqlalchemy import text, create_engine
from sqlalchemy.orm import Session
import psycopg2

#object declaration ----->

#URI of the API
URI = '/api/videogames/'

#data base engine to establishing connection
engine = create_engine('postgresql://emilio:C4iIa5Wr5BngpdmjpUwoF3BicwJX6ZAw@dpg-cgeusjpmbg568r4g3plg-a.oregon-postgres.render.com/examen2',echo=True)

#creating the Flask object app
app = Flask(__name__)

#function definition ----->
#GET request to view all videogames from the Data Base, POST request to append new videogames to the Data Base 
#and DELETE request to remove the specified videogame from the Data Base
@app.route(URI, methods=['GET','POST','DELETE'])
def get_all_videogames():
    """ main API function for GET, POST and DELETE methods """
    
    with Session(engine) as session:
        if request.method == 'GET':
            all_videogames = session.execute(text('SELECT * FROM public.videogames'))
            print(all_videogames.all())
            return 'Succesful'
        elif request.method == 'POST':
            pass
        elif request.method == 'DELETE':
            pass
    return abort(505)

#GET request to view the specified videogame 
@app.route(URI+'<string:v_name>',methods=['GET'])
def get_specific_videogame(v_name):
    pass

#GET request to return all the videogames from the specified developer
@app.route(URI+'dev/<string:dev_name>',methods=['GET'])
def get_dev_videogames(dev_name):
    pass

#API program start point ----->
#check if current module is running as main
if __name__ == '__main__':
    #run Flask object with debug output on terminal
    app.run(debug=True,port=5000)










#get request to view the tasks
@app.route((URI + 'tasks'), methods=['GET'])
def get_tasks():
    """ Returns the tasks data structure as a json """
    return jsonify({'tasks':tasks})

#get request to view specific task
@app.route((URI + 'tasks/<int:id>'), methods=['GET'])
def get_specific_task(id):
    """ Look for the specified task on tasks data structure and return it as json if found """
    #iterate through each task to look for the specified one
    for n in tasks:
        if n['id'] == id:
            #if task is found, return it as a json
            return jsonify({'task':n})
    #if the task does not exists, 404 HTTP error code is returned
    return abort(404)

#post method to append a task to tasks data structure
@app.route((URI + 'append'), methods=['POST'])
def append_task():
    """ append to tasks the specified task through the received HTTP packet """
    #initialize the necessary variables with its respective value from the variables from the HTTP packet
    post_name = request.form.get('name')
    #check if post_name value is not null
    if post_name == "":
        return jsonify({'tasks':tasks})
    #append the task
    tasks.append({'id':(len(tasks) + 1),'name':post_name,'estado':False})
    #return tasks
    return jsonify({'tasks':tasks})

#delete method to remove the specified task
@app.route((URI + 'delete/<int:delete_id>'), methods=['DELETE'])
def delete_task(delete_id):
    """ remove the specified task through the URI from tasks data structure """
    #iterate through tasks looking for the indicated task to be removed
    for it in range(len(tasks)):
        #if found, delete the indicated task and return tasks as json
        if tasks[it]['id'] == delete_id:
            del tasks[it]
            return jsonify({'tasks':tasks})
            break
    #if task is not found, generate 404 HTTP error code
    return abort(404)

#put method to update a specified task
@app.route((URI + 'update'), methods=['PUT'])
def update_task():
    """ update the specified task with the values of the HTTP packet data """
    #initialize the id variable with the received value in the HTTP packet
    put_id = int(request.form.get('id'))
    #iterate through tasks looking for the indicated task to be updated
    for it in tasks:
        #if found, update the task and return tasks as json
        if it['id'] == put_id:
            it['estado'] = True
            return jsonify({'tasks':tasks})
    #if task does not exists, generate 404 HTTP error code
    return abort(404)

#API program start point ----->
#check if current module is running as main
if __name__ == '__main__':
    #run Flask object with debug output on terminal
    app.run(debug=True,port=5001)
