# *script to test and debug the API

from requests import post, delete, put

#post_data = {'title':'Resident Evil Village','description':'Set a few years after the horrifying events in the critically acclaimed Resident Evil 7 biohazard, the all-new storyline begins with Ethan Winters and his wife Mia living peacefully in a new location, free from their past nightmares.\nJust as they are building their new life together, tragedy befalls them once again.\nWhen BSAA captain Chris Redfield attacks their home,\nEthan must once again head into hell to get his kidnapped daughter back.','developer':'CAPCOM Co., Ltd.','release_year':'2021-05-06','clasification':'C','image':'https://image.api.playstation.com/vulcan/ap/rnd/202101/0812/FkzwjnJknkrFlozkTdeQBMub.png'}

#print(post('http://127.0.0.1:5000/api/videogames', data=post_data).json())

#delete_data = {'id':1}

#print(delete('http://127.0.0.1:5000/api/videogames',data=delete_data).json())

put_data = {'id':5,'title':'Resident Evil 8: Village','description':'Set a few years after the horrifying events in the critically acclaimed Resident Evil 7 biohazard, the all-new storyline begins with Ethan Winters and his wife Mia living peacefully in a new location, free from their past nightmares.\nJust as they are building their new life together, tragedy befalls them once again.\nWhen BSAA captain Chris Redfield attacks their home,\nEthan must once again head into hell to get his kidnapped daughter back.','developer':'CAPCOM Co., Ltd.','release_year':'2021-05-06','clasification':'C','image':'https://image.api.playstation.com/vulcan/ap/rnd/202101/0812/FkzwjnJknkrFlozkTdeQBMub.png'}

put('http://127.0.0.1:5000/api/videogames',data=put_data)
