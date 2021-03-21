from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
from crud_csv import *
from crud_json import *
from mail import *
from otp import *
from uuid import uuid4

app = Flask(__name__)
CORS(app)

userDict = {}

@app.route('/register',methods=["GET"])
def register():
    try:
        data = dict(request.args)
        uname = data["uname"]
        mail = data["mail"]
        password = data["password"]
        upiId = mail.split('@')
        upiId = upiId[0]+'@ytc'
        Uid = str(uuid4())
        userDatas = read_data()
        res = writeData(uname,mail,password,Uid,upiId)
        tempData = {
            'Uid':Uid,
            'data':{
                'UpiId':upiId,
                'Balance':0,
                'Transactions':[]
            }
        }
        print(res,tempData)
        if res == -1:
            return jsonify({"result":"Email Already exists"})
        res = write_json(tempData)
        if res == -1:
            return jsonify({"result":"Email Already exists"})
        send_mail(mail,uname,0)
        return jsonify({"result":"succesfully"})
    except:
        return jsonify({"result":"400 something went wrong"})

@app.route("/Login",methods=["GET"])
def Login():
        
        data = dict(request.args)
        mail = data["mail"]
        password = data["password"]
        userDatas = read_data()
        print(userDatas)
        Uid = None
        for i in userDatas:
            if i[1]==mail:
                if i[2] == password:
                    return jsonify({"result":"succesfully"})
        return jsonify({"result":"Check your id"})


@app.route('/send_otp',methods=["GET"])
def send_otp():
    try:
        data = dict(request.args)
        uname = data["uname"]
        mail = data["mail"]
        password = data["password"]
        read_data()
        #writeData(uname,mail,password)
        otp = generateOTPAlpha(6)
        userDict[otp] = {"uname":uname,"mail":mail,"password":password}
        send_mail(mail,otp,1)
        return jsonify({"result":"succesfully"}) 
    except:
        return jsonify({"result":"400 something went wrong"})

@app.route('/changePassword',methods=["GET"])
def changePassword():
    try:
        data = dict(request.args)
        uname = data["otp"]
        read_data()
        #writeData(uname,mail,password)
        keys = userDict.keys()
        for i in keys:
            if i == uname:
                temp = userDict[i]
                update(temp["uname"],temp['mail'],temp['password'])
        #send_mail(mail,otp,1)
                return jsonify({"result":"succesfully"}) 
        return jsonify({"result":"Unsuccesfully"}) 
    except:
        return jsonify({"result":"400 something went wrong"})

@app.route("/",methods=["GET"])
def home():
    return render_template("login.html")

@app.route("/SignUp",methods=["GET"])
def SignUp():
    return render_template("SignUp.html")

if __name__ == '__main__':
	app.run(debug = True)