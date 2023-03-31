#necessary imports ----->
from flask import jsonify

#function definition ----->
#serialize data function
def serialize_raw_query_data(raw_data):
    """ serialize raw data retrieved from the data base to send it as a json. Raw data is returned as a list of tuples """
    serialized_data = []
    #iterate through each tuple to serialize it in a list of dictionaries
    for _tuple in raw_data:
        serialized_data.append({'id':_tuple.videogame_id,'title':_tuple.title,'description':_tuple.description,'developer':_tuple.developer,'release_year':_tuple.release_year.year,'clasification':_tuple.clasification,'image':_tuple.image,'banner':_tuple.banner})
    return jsonify(serialized_data)
