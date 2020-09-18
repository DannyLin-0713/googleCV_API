#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import base64

while True:
    AuthoID=input("\033[1;33;40m Please input your autho ID \033[0m \n")
    img_name=input("\033[1;33;40m Please input your img file name \033[0m  \n")
    img_b = str(base64.b64encode(open(img_name,"rb").read()),'utf8')

    url = 'https://vision.googleapis.com/v1/images:annotate?key=' + AuthoID
    headers = {'content-type': 'application/json'}
    requestData={
          "requests": [
            {
              "image": {
                "content": img_b
              },
              "features": [
                {
                  "maxResults": 3,
                  "type": "FACE_DETECTION"
                }
              ]
            }
          ]
        }
    after_call = requests.post(url, json=requestData, headers=headers)
    text=json.loads(after_call.text)
    print ("\033[1;32;40m RESULT of this picture is \033[0m")

    def face_resu(facekey):
        print (text['responses'][0]['faceAnnotations'][0][facekey])

    if after_call.status_code == 200:
        print("\033[1;32;40mIS the face in this img JOY(開心的)?\033[0m"); face_resu('joyLikelihood')
        print("\n\033[1;32;40mIS the face in this img SORROW(傷心的)? \033[0m");face_resu('sorrowLikelihood')
        print("\n\033[1;32;40mIS the face in this img ANGRY(生氣的)? \033[0m");face_resu('angerLikelihood')
        print("\n\033[1;32;40mIS the face in this img SURPRISE(驚訝的)?\033[0m");face_resu('surpriseLikelihood')
        print("\n\033[1;32;40mIS the face in this img UNDEREXPOSED(曝光不足)?\033[0m");face_resu('underExposedLikelihood')
        print("\n\033[1;32;40mIS the face in this img BLURRED(過於模糊)?\033[0m");face_resu('blurredLikelihood')
        print("\n\033[1;32;40mIS the face in this img WEARING HEAD WEAR(佩戴頭飾臉飾)?\033[0m");face_resu('headwearLikelihood')
    else:
        print("error, pls check the file or your autho id")
        print (text)
    print ("\n New Search")
