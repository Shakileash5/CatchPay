import json

fileName = "userDetails.json"
userDetails = {}


def read_json():
    global userDetails
    print("Reading Data")
    with open(fileName, "r") as read_file:
        data = json.load(read_file)
    print(data)
    userDetails = data
    return

def read_json_Uid(Uid):
    read_json()
    keys = userDetails.keys()
    print(keys,"keys\n")
    if Uid not in keys:
        return -1
    return userDetails[Uid]

def write_json(tempData):
    print("Writing into json")
    read_json()
    global userDetails
    print(userDetails)
    keys = userDetails.keys()
    for key in keys:
        if key == tempData["Uid"]:
            return -1
    userDetails[tempData["Uid"]] = tempData["data"]

    with open(fileName, "w") as write_file:
        data = json.dump(userDetails,write_file)
    
    return

def update_json(Uid,id,value):
    keys = userDetails.keys()
    for key in keys:
        if key == Uid:
            userDetails[key ][id] = value
            with open(fileName, "w") as write_file:
                data = json.dump(userDetails,write_file)
            return
    return -1 
    

data = {
    "Uid":"142-892-232",
    "data":{
        "name":"Atshaya",
        "Balance":4532
    }
}
#read_json()
#update_json("142-892-232","Balance",10000)
#print(userDetails)
#write_json(data)


