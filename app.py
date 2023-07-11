from flask import Flask , jsonify , request
from connect import connectiontest; 
from Whatpy import  webdmclose 
import datetime

app = Flask(__name__)

client = connectiontest();



@app.route("/user/set", methods=["GET", "POST"  , "PUT" , "DELETE"] )
def setuser():
    userList = [] 
    dbConnect  =  client.get_database("sample_mflix").get_collection("Users")
    if request.method == 'DELETE': 
        userId = request.form.get("idNo")
        if userId is None : 
            return "Please provide proper information"
        dbConnect.find_one_and_delete({"id":int(userId)})
        return f"{userId} is deleted successfully"

    if request.method == 'POST':
        userId = request.form.get("idNo")
        username = request.form.get("username")
        age = request.form.get("age")
        email = request.form.get("email")
        if userId is None or username is None or age is None or email is None : 
            return "Please provide proper information"
        
        dbConnect.insert_one({ 
            "id": int(userId),
            "age":int(age),
            "email":email,
            "username":username,
        })
        for data in dbConnect.find({"id":int(userId)}):
            userList.append({ 
                "id":str( data["_id"]),
                "idNo":str(data["id"]),
                "age":str(data["age"]),
                "email":data["email"],
                "username":data["username"],
            })
        return userList
@app.route("/user", methods=["GET", "POST"] )
def getuser():
    userList = [] 
    dbConnect  =  client.get_database("sample_mflix").get_collection("Users")
    if request.method == 'POST':
        userId = request.form.get("userId")
       
        for data in dbConnect.find({"id":int(userId)}):
            userList.append({ 
                "id":str( data["_id"]),
                "idNo":str(data["id"]),
                "age":str(data["age"]),
                "email":data["email"],
                "username":data["username"],
            })
    if request.method == 'GET':
         for data in dbConnect.find():
            userList.append({ 
                "id":str( data["_id"]),
                "idNo":str(data["id"]),
                "age":str(data["age"]),
                "email":data["email"],
            })
    return userList


@app.route("/movies", methods=["GET", "POST"] )
def getMovieData():
    movieList = [] 
    limit = 10
    if request.method == 'POST':
        limit = request.form.get("limit")
       
        if limit is None:
            return "Please enter an integer value."
       
        dbConnect  =  client.get_database("sample_mflix").get_collection("movies")
        for data in dbConnect.find().limit(int(limit)):
            movieList.append({
            "_id": str( data["_id"]),
            "plot": data["plot"],
            "num_mflix_comments": data["num_mflix_comments"],
            "cast": data["cast"],
            "released": data["released"],
            "lastupdated": data["lastupdated"]
            })
     
        return jsonify(movieList)
    if request.method == 'GET':
        dbConnect  =  client.get_database("sample_mflix").get_collection("movies")
        for data in dbConnect.find().limit(limit):
            movieList.append({
            "_id": str( data["_id"]),
            "plot": data["plot"],
            "num_mflix_comments": data["num_mflix_comments"],
            "cast": data["cast"],
            "released": data["released"],
            "lastupdated": data["lastupdated"]
            })
        return jsonify(movieList)
    
@app.route("/sendwamsg")
def sendwa():
    current_time = datetime.datetime.now()
    print(current_time)
    # sendwhatmsg_instantly("+919819535276", "Message-2", current_time.hour, current_time.minute+1)
    webdmclose("+919819535276", "Message-2");
    return f"{current_time.hour}:{current_time.minute}"


if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0")
