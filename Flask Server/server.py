from flask import Flask
#from flask import request
from DirectKey import PressKey,ReleaseKey,W,A,S,D
import pyautogui
import time
app=Flask(__name__)

global lastPressed
lastPressed=W
@app.route('/<key>', methods=['GET'])
def move(key):
  if key=='one':
    PressKey(W)
    time.sleep(1)
    ReleaseKey(W)   
  if key=='two':
    PressKey(W)
    PressKey(A)
    time.sleep(0.1)
    ReleaseKey(A)
    ReleaseKey(W) 
  if key=='three':
    PressKey(W)
    PressKey(D)
    time.sleep(0.1)
    ReleaseKey(D)
    ReleaseKey(W)
  if key=='five':
    PressKey(S)
    time.sleep(1)
    ReleaseKey(S)
 # print(key,type(key))
  return "Success"


if __name__=='__main__':
    app.run(host='0.0.0.0',port='9595')
