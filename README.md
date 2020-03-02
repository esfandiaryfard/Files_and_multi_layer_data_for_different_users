# Files_and_multi_layer_data_for_different_users
This is a project for a job interview. To implement this project I used python and flask upon request.

Note1: Make sure you enter the path of your project inside app.py

Note2: For all endpoints you need to add username as a params in the end of each endpoint like : ?username=user1

* For the first api, user can upload a file into given username folder.If the folder doese not exist the program create one. The endpoint for upload is: api/upload.

* For the second api, user can downlaod a file from users folder.filename should give as params in addition to username. The endpoint for download is: /api/download 

* For the third api, user can create and update a json data file.If json already exist in given username folder json will update if not a json file will create in user's folder. Notice that forms should have items 'name' and 'value' and if name already exists in json file value will replace with new item.The endpoint for set user data is: /api/setUserData 

* For the fourth api, user can create or update global data json file.notice that for this api there is no need to give username as parameter.Json file will create if not exists and if data with same name exists value will replace.The endpoint for this api is: /api/setGlobalData 

*Fifth api returns given user data in addition to global data.values for similar names between user data and global data will replace with user value. endpoint is accessable via: /api/getUserData
