from flask import Flask , jsonify , request
from connect import connectiontest; 
# from Whatpy import  webdmclose 
import datetime
import random
from bson.objectid import ObjectId

import asyncio
import websockets

app = Flask(__name__)

client = connectiontest()

@app.route("/hello", methods=["GET", "POST"  , "PUT" , "DELETE"] )
def hello():
    print("hello world")
    return "hello world" 
    
    
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
    
# @app.route("/sendwamsg")
# def sendwa():
#     current_time = datetime.datetime.now()
#     print(current_time)
#     # sendwhatmsg_instantly("+919819535276", "Message-2", current_time.hour, current_time.minute+1)
#     webdmclose("+919819535276", "Message-2");
#     return f"{current_time.hour}:{current_time.minute}"

bananaCategory = ["All Green", "Light Green", "More Yellow Than Green", "Yellow With Green Tips", "Full Yellow", "Full Yellow With Spots"]
tomatoCategry = ["Mature Green", "Breaker", "Turning", "Pink", "Light Red", "Red Ripe"]
@app.route("/categoryData", methods=["GET", "POST", "PUT", "DELETE"] )
def category():
    categoryList = [""]
    returnList = []
    dbConnect = client.get_database("flask_data").get_collection("testData")
    
    # Add Data
    if request.method == 'POST':
        randomList = []
        typeValue = request.form.get("type")
        if typeValue == "banana":
            categoryList = bananaCategory
        elif typeValue == "tomato":
            categoryList = tomatoCategry
            
        for i in range(6):
            randomList.append(random.randint(1, 1000))
        print(randomList)
        categoryRandomValue = random.choice(categoryList)
        addData = dbConnect.insert_one({ 
            "r1": randomList[0],
            "r2": randomList[1],
            "r3": randomList[2],
            "r4": randomList[3],
            "r5": randomList[4],
            "r6": randomList[5],
            "typeValue": typeValue,
            "category": str(categoryRandomValue)
        })
        returnList.append({
            "_id": str(addData.inserted_id),
            "r1":randomList[0],
            "r2":randomList[1],
            "r3":randomList[2],
            "r4":randomList[3],
            "r5":randomList[4],
            "r6":randomList[5],
            "typeValue": typeValue,
            "category": str(categoryRandomValue)
        })
        return returnList
    
    # Get Data
    if request.method == 'GET':
        resultData = []
        findId = request.form.get("findId")
        for data in dbConnect.find({"_id": ObjectId(findId)}):
            resultData.append({ 
                "r1":data["r1"],
                "r2":data["r2"],
                "r3":data["r3"],
                "r4":data["r4"],
                "r5":data["r5"],
                "r6":data["r6"],
                "typeValue":data["typeValue"],
                "category":data["category"]
            })
        return resultData
    
    # Update Data
    if request.method == 'PUT':
        findId = request.form.get("findId")
        typeValue = request.form.get("type")
        
        updateData = dbConnect.find_one({"_id": ObjectId(findId)}, {"_id":0})
        print("updateData\n", updateData)
        updateData['_id'] = str(ObjectId())
        collections = {
            "banana": client.get_database("flask_data").get_collection("banana"),
            "tomato": client.get_database("flask_data").get_collection("tomato")
        }

        if typeValue in collections:
            dbConnect = collections[typeValue]
            dbConnect.insert_one(updateData)
        print(dbConnect)
        
        return updateData
      
    
    
# async def connect(websocket, path):
#     name = await websocket.recv()
#     print(f"< {name}")
#     greeting = f"Hello {name}!"
#     await websocket.send(greeting)
#     print(f"> {greeting}")
#     print(f"WebSocket connection established with {name}")  
async def demo():
    server = await websockets.serve("localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()
    # async with websockets.serve(connect,"192.168.0.141", 8765):
    #     print("WebSocket server started on ws://localhost:8765")
    #     await asyncio.Future()  # Run forever  

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    websocket_task = loop.create_task(demo())
    app.run(debug=True , host="0.0.0.0")


