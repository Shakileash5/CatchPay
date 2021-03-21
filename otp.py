import math
import time

val={}
val["seed"] = time.perf_counter()
def rnd():
  val["seed"] = ( val["seed"]*9301+49297 ) % 233280; 
  return val["seed"]/ (233280.0)
def rand(number):
    return math.ceil( rnd () * number )

def generateOTPNum(OtpSize) : 
    OTP = "" 
    otpString = '0123456789'
    length = len(otpString) 
    for i in range(OtpSize) : #to add each random character to result string , otpSize set the size
        OTP += otpString[math.floor(rand(length))-1]  
  
    return OTP 

def generateOTPAlpha(OtpSize) : 
    OTP = "" 
    otpString = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(otpString) 
    for i in range(OtpSize) : #to add each random character to result string , otpSize set the size
        OTP += otpString[math.floor(rand(length))-1]  
  
    return OTP 
    
def generateOTPAlphaNum(OtpSize) : 
    OTP = "" 
    otpString = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(otpString) 
    for i in range(OtpSize) : #to add each random character to result string , otpSize set the size
        OTP += otpString[math.floor(rand(length))-1] 
  
    return OTP 



