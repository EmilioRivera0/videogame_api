"""-----------------------------------------------------------------------------------------------------------------------------------
- Software Name: Videogame API
- Language: Python
- Developers: Emilio Rivera Macías and Carlos Cancino Escobar
- Date: March 27, 2023
- Contacts: emilioriveramacias@gmail.com
-----------------------------------------------------------------------------------------------------------------------------------"""

# *I know that it is classification and not clasification as it is written in this code, sorry for this little mistake :)

#necessary imports ----->
from flask import Flask, abort, request
from flask_cors import CORS
import sql_functions

#object declaration ----->
#URI of the API
URI = '/api/videogames/'

#creating the Flask object app
app = Flask(__name__)

#enable CORS
CORS(app)

#function definition ----->
#GET request to view all videogames from the Data Base, POST request to append new videogames to the Data Base 
#and DELETE request to remove the specified videogame from the Data Base
@app.route(URI, methods=['GET','POST','DELETE','PUT'])
def get_all_videogames():
    """ main API function for GET, POST and DELETE methods """
    #GET method
    if request.method == 'GET':
        #return dictionary containing the serialized data of all videogames
        return sql_functions.select_everything()
    #POST  method
    elif request.method == 'POST':
        #initialize the necessary variables to insert a new video game in the data base with the data of the received HTTP packet
        _title = request.json.get('title')
        _description = request.json.get('description')
        _developer = request.json.get('developer')
        _release_year = request.json.get('release_year') 
        _clasification = request.json.get('clasification')
        _image = request.json.get('image')
        _banner = request.json.get('banner')
        data_dictionary = {'_title':_title,'_description':_description,'_developer':_developer,'_release_year':_release_year,'_clasification':_clasification,'_image':_image,'_banner':_banner}
        return sql_functions.insert_videogame(data_dictionary) 
    #DELETE method
    elif request.method == 'DELETE':
        #initialize the id variable with the HTTP packet data to delete the specified videogame from the data base
        _id = request.json.get('id')
        return sql_functions.delete_videogame(_id)
    #PUT method
    elif request.method == 'PUT':
        #initialize the necessary variables to modify the specified videogame in the data base with the data of the received HTTP packet
        _id = request.json.get('id')
        _title = request.json.get('title')
        _description = request.json.get('description')
        _developer = request.json.get('developer')
        _release_year = request.json.get('release_year') 
        _clasification = request.json.get('clasification')
        _image = request.json.get('image')
        _banner = request.json.get('banner')
        data_dictionary = {'_title':_title,'_description':_description,'_developer':_developer,'_release_year':_release_year,'_clasification':_clasification,'_image':_image,'_id':_id,'_banner':_banner}
        return sql_functions.update_videogame_data(data_dictionary)
    return abort(505)

#GET request to view the specified videogame searching by title and developer 
@app.route(URI+'<string:_name>',methods=['GET'])
def get_specific_videogame(_name):
    #initialize the different string variables to improve the search engine that accepts different user input formats
    _name_upper = '%'+_name.upper()+'%'
    _name_lower = '%'+_name.lower()+'%'
    _name_title = '%'+_name.title()+'%'
    _name = '%'+_name+'%'
    string_dictionary = {'_name_upper':_name_upper,'_name_lower':_name_lower,'_name_title':_name_title,'_name':_name}
    return sql_functions.search_on_database(string_dictionary)

#API program start point ----->
#check if current module is running as main
if __name__ == '__main__':
    #run Flask object with debug output on terminal
    app.run(debug=True,port=5000)
