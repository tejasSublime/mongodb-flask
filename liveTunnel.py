import asyncio
import json
import websockets
from connect import connectiontest; 
import random


client = connectiontest()

def category():
    categoryList = [""]
    returnList = []
    randomList = []
    
    dbConnect = client.get_database("flask_data").get_collection("testData")
    for _ in range(6):
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
        "typeValue": "typeValue",
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
        "typeValue": "typeValue",
        "category": str(categoryRandomValue)
    })
    
    return returnList
    # Add Data
    # if request.method == 'POST':
    #     randomList = []
    #     typeValue = request.form.get("type")
    #     if typeValue == "banana":
    #         categoryList = bananaCategory
    #     elif typeValue == "tomato":
    #         categoryList = tomatoCategry
            
    #     for i in range(6):
    #         randomList.append(random.randint(1, 1000))
    #     print(randomList)
    #     categoryRandomValue = random.choice(categoryList)
    #     addData = dbConnect.insert_one({ 
    #         "r1": randomList[0],
    #         "r2": randomList[1],
    #         "r3": randomList[2],
    #         "r4": randomList[3],
    #         "r5": randomList[4],
    #         "r6": randomList[5],
    #         "typeValue": typeValue,
    #         "category": str(categoryRandomValue)
    #     })
    #     returnList.append({
    #         "_id": str(addData.inserted_id),
    #         "r1":randomList[0],
    #         "r2":randomList[1],
    #         "r3":randomList[2],
    #         "r4":randomList[3],
    #         "r5":randomList[4],
    #         "r6":randomList[5],
    #         "typeValue": typeValue,
    #         "category": str(categoryRandomValue)
    #     })
    #     return returnList
    
    # # Get Data
    # if request.method == 'GET':
    #     resultData = []
    #     findId = request.form.get("findId")
    #     for data in dbConnect.find({"_id": ObjectId(findId)}):
    #         resultData.append({ 
    #             "r1":data["r1"],
    #             "r2":data["r2"],
    #             "r3":data["r3"],
    #             "r4":data["r4"],
    #             "r5":data["r5"],
    #             "r6":data["r6"],
    #             "typeValue":data["typeValue"],
    #             "category":data["category"]
    #         })
    #     return resultData
    
    # # Update Data
    # if request.method == 'PUT':
    #     findId = request.form.get("findId")
    #     typeValue = request.form.get("type")
        
    #     updateData = dbConnect.find_one({"_id": ObjectId(findId)}, {"_id":0})
    #     print("updateData\n", updateData)
    #     updateData['_id'] = str(ObjectId())
    #     collections = {
    #         "banana": client.get_database("flask_data").get_collection("banana"),
    #         "tomato": client.get_database("flask_data").get_collection("tomato")
    #     }

    #     if typeValue in collections:
    #         dbConnect = collections[typeValue]
    #         dbConnect.insert_one(updateData)
    #     print(dbConnect)
        
    #     return updateData
      
async def actionsOnMessage(message, ws):
    print("message  ", message)
    jsonData = json.loads(message)
    if jsonData['cmd'] == "test":
        data = category()
        await ws.send(json.dumps(data))
    
        
        
async def connect(websocket, path):
    try:
        # Your code to handle the connection and send/receive messages
        message = await websocket.recv()
        await actionsOnMessage(message, websocket)
    except websockets.exceptions.ConnectionClosedError as e:
        print("Connection closed unexpectedly",e)
    
async def main():
    async with websockets.serve(connect, "192.168.0.141", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever
        
if __name__ == "__main__":
    asyncio.run(main())