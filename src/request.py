# *script to test and debug the API

from requests import post, delete, put

#post_data = {'title':'Grand Theft Auto V','description':'When a young street hustler, a retired bank robber, and a terrifying psychopath find themselves entangled with some of the most frightening and deranged elements of the criminal underworld, the U.S. government, and the entertainment industry, they must pull off a series of dangerous heists to survive in a ruthless city in which they can trust nobody — least of all each other.','developer':'Rockstar Games','release_year':'2015-04-14','clasification':'C','image':'https://image.api.playstation.com/vulcan/ap/rnd/202202/2811/x9SuHZAiRn0uJXB1IKteIgcw.png'}

#post('http://127.0.0.1:5000/api/videogames', json=post_data)

#delete_data = {'id':17}

#print(delete('http://127.0.0.1:5000/api/videogames',json=delete_data).json())

put_data = {'id':13,'title':'Resident Evil 8: Village','description':'Set a few years after the horrifying events in the critically acclaimed Resident Evil 7 biohazard, the all-new storyline begins with Ethan Winters and his wife Mia living peacefully in a new location, free from their past nightmares.\nJust as they are building their new life together, tragedy befalls them once again.\nWhen BSAA captain Chris Redfield attacks their home,\nEthan must once again head into hell to get his kidnapped daughter back.','developer':'CAPCOM Co., Ltd.','release_year':'2021-05-06','clasification':'C','image':'https://image.api.playstation.com/vulcan/ap/rnd/202101/0812/FkzwjnJknkrFlozkTdeQBMub.png'}

put('http://127.0.0.1:5000/api/videogames',json=put_data)
