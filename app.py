"""-----------------------------------------------------------------------------------------------------------------------------------
- Software Name: Videogame API
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
from flask_cors import CORS

#object declaration ----->
#URI of the API
URI = '/api/videogames/'

#data base engine to establishing connection
engine = create_engine('postgresql://emilio:C4iIa5Wr5BngpdmjpUwoF3BicwJX6ZAw@dpg-cgeusjpmbg568r4g3plg-a.oregon-postgres.render.com/examen2')

#creating the Flask object app
app = Flask(__name__)

#enable CORS
CORS(app)

#function definition ----->
#serialize data function
def serialize_raw_query_data(raw_data):
    """ serialize raw data retrieved from the data base to send it as a json. Raw data is returned as a list of tuples """
    serialized_data = []
    #iterate through each tuple to serialize it in a list of dictionaries
    for _tuple in raw_data:
        serialized_data.append({'id':_tuple.videogame_id,'title':_tuple.title,'description':_tuple.description,'developer':_tuple.developer,'release_year':_tuple.release_year.year,'clasification':_tuple.clasification,'image':_tuple.image,'banner':_tuple.banner})
    return jsonify(serialized_data)

#GET request to view all videogames from the Data Base, POST request to append new videogames to the Data Base 
#and DELETE request to remove the specified videogame from the Data Base
@app.route(URI, methods=['GET','POST','DELETE','PUT'])
def get_all_videogames():
    """ main API function for GET, POST and DELETE methods """
    #start session wit the database
    with Session(engine) as session:
        #GET method
        if request.method == 'GET':
            #return dictionary containing the serialized data of all videogames
            return serialize_raw_query_data(session.execute(text('SELECT * FROM public.videogames')))
        #POST  method
        elif request.method == 'POST':
            #initialize the necessary variables to insert a new video game in the data base with the data of the received HTTP packet
            _title = request.form.get('title')
            _description = request.form.get('description')
            _developer = request.form.get('developer')
            _release_year = request.form.get('release_year') 
            _clasification = request.form.get('clasification')
            _image = request.form.get('image')
            _banner = request.form.get('banner')
            #insert new videogame row in the data base
            session.execute(text('INSERT INTO public.videogames (title,description,developer,release_year,clasification,image,banner) VALUES (:_title, :_description, :_developer, :_release_year, :_clasification, :_image, :_banner)'),{'_title':_title,'_description':_description,'_developer':_developer,'_release_year':_release_year,'_clasification':_clasification,'_image':_image,'_banner':_banner})
            #commit changes on the data base
            session.commit()
            #return dictionary containing the serialized data of all videogames
            return serialize_raw_query_data(session.execute(text('SELECT * FROM public.videogames')))
        #DELETE method
        elif request.method == 'DELETE':
            #initialize the id variable with the HTTP packet data to delete the specified videogame from the data base
            _id = request.form.get('id')
            #remove the specified videogame from the data base by its id
            session.execute(text('DELETE FROM public.videogames WHERE videogame_id=:_id'),{'_id':_id})
            #commit changes on the data base
            session.commit()
            #return dictionary containing the serialized data of all videogames
            return serialize_raw_query_data(session.execute(text('SELECT * FROM public.videogames')))
        #PUT method
        elif request.method == 'PUT':
            #initialize the necessary variables to modify the specified videogame in the data base with the data of the received HTTP packet
            _id = request.form.get('id')
            _title = request.form.get('title')
            _description = request.form.get('description')
            _developer = request.form.get('developer')
            _release_year = request.form.get('release_year') 
            _clasification = request.form.get('clasification')
            _image = request.form.get('image')
            _banner = request.form.get('banner')
            #modify the specified videogame row in the data base
            session.execute(text('UPDATE public.videogames SET title = :_title, description = :_description, developer = :_developer, release_year = :_release_year, clasification = :_clasification, image = :_image, banner = :_banner WHERE videogame_id = :_id'),{'_title':_title,'_description':_description,'_developer':_developer,'_release_year':_release_year,'_clasification':_clasification,'_image':_image,'_id':_id,'_banner':_banner})
            #commit changes on the data base
            session.commit()
            #return dictionary containing the serialized data of all videogames
            return serialize_raw_query_data(session.execute(text('SELECT * FROM public.videogames')))
    return abort(505)

#GET request to view the specified videogame searching by title and developer 
@app.route(URI+'<string:_name>',methods=['GET'])
def get_specific_videogame(_name):
    #initialize the different string variables to improve the search engine that accepts different user input formats
    _name_upper = '%'+_name.upper()+'%'
    _name_lower = '%'+_name.lower()+'%'
    _name_capitalize = '%'+_name.lower().capitalize()+'%'
    _name_title = '%'+_name.title()+'%'
    _name = '%'+_name+'%'
    #start session wit the database
    with Session(engine) as session:
        #search query to retrieve the matching rows
        return serialize_raw_query_data(session.execute(text("SELECT * FROM public.videogames WHERE title LIKE :_name_upper OR title LIKE :_name_lower OR title LIKE :_name_capitalize OR title LIKE :_name_title OR title LIKE :_name OR developer LIKE :_name_upper OR developer LIKE :_name_lower OR developer LIKE :_name_capitalize OR developer LIKE :_name_title OR developer LIKE :_name"),{'_name_upper':_name_upper,'_name_lower':_name_lower,'_name_capitalize':_name_capitalize,'_name_title':_name_title,'_name':_name}))

#API program start point ----->
#check if current module is running as main
if __name__ == '__main__':
    #run Flask object with debug output on terminal
    app.run(debug=True,port=5000)
