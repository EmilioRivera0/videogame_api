#necessary imports ----->
from sqlalchemy import text, create_engine
from sqlalchemy.orm import Session
import psycopg2
from serialize_data import serialize_raw_query_data

#constants declaration ----->
#SELECT * SQL query
SELECT = 'SELECT * FROM public.videogames'

#INSERT SQL query
INSERT = 'INSERT INTO public.videogames (title,description,developer,release_year,clasification,image,banner) VALUES (:_title, :_description, :_developer, :_release_year, :_clasification, :_image, :_banner)'

#DELETE SQL query
DELETE = 'DELETE FROM public.videogames WHERE videogame_id=:_id'

#UPDATE SQL query
UPDATE = 'UPDATE public.videogames SET title = :_title, description = :_description, developer = :_developer, release_year = :_release_year, clasification = :_clasification, image = :_image, banner = :_banner WHERE videogame_id = :_id'

#SEARCH SQL query
SEARCH = 'SELECT * FROM public.videogames WHERE title LIKE :_name_upper OR title LIKE :_name_lower OR title LIKE :_name_title OR title LIKE :_name OR developer LIKE :_name_upper OR developer LIKE :_name_lower OR developer LIKE :_name_title OR developer LIKE :_name'

#object declaration ----->
#data base engine to establishing connection
engine = create_engine('postgresql://emilio:C4iIa5Wr5BngpdmjpUwoF3BicwJX6ZAw@dpg-cgeusjpmbg568r4g3plg-a.oregon-postgres.render.com/examen2')

#function definition ----->
#SQL query to retrieve all videogames data
def select_everything():
    """ SELECT * FROM videogames """
    #start session with the database
    with Session(engine) as session:
        #return dictionary containing the serialized data of all videogames
        return serialize_raw_query_data(session.execute(text(SELECT)))

#SQL query to insert a new videogame
def insert_videogame(data_dictionary):
    """ INSERT new videogame """
    #start session with the database
    with Session(engine) as session:
        #return dictionary containing the serialized data of all videogames
        #insert new videogame row in the data base
        session.execute(text(INSERT),data_dictionary)
        #commit changes on the data base
        session.commit()
        #return dictionary containing the serialized data of all videogames
        return serialize_raw_query_data(session.execute(text(SELECT)))

#SQL query to delete a specified videogame
def delete_videogame(videogame_id):
    """ DELETE specified videogame """
    #start session with the database
    with Session(engine) as session:
        #remove the specified videogame from the data base by its id
        session.execute(text(DELETE),{'_id':videogame_id})
        #commit changes on the data base
        session.commit()
        #return dictionary containing the serialized data of all videogames
        return serialize_raw_query_data(session.execute(text(SELECT)))

#SQL query to update the data of the specified videogame
def update_videogame_data(data_dictionary):
    """ UPDATE the specified videogame data """
    #start session with the database
    with Session(engine) as session:
        #modify the specified videogame row in the data base
        session.execute(text(UPDATE), data_dictionary)
        #commit changes on the data base
        session.commit()
        #return dictionary containing the serialized data of all videogames
        return serialize_raw_query_data(session.execute(text(SELECT)))

#SQL query to search for a videogame by its title or developer
def search_on_database(string_dictionary):
    """ SELECT videogames WHERE title or developer match the input strings """
    #start session with the database
    with Session(engine) as session:
        #search query to retrieve the matching rows
        return serialize_raw_query_data(session.execute(text(SEARCH),string_dictionary))
