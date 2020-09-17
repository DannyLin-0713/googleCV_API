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
                  "maxResults": 1,
                  "type": "SAFE_SEARCH_DETECTION"
                }
              ]
            }
          ]
        }
    after_call = requests.post(url, json=requestData, headers=headers)
    text=json.loads(after_call.text)
    paragum=int(0)
    paragum_a=len(text['responses'][0]['safeSearchAnnotation'])
    print ("\033[1;32;40m RESULT of this picture is \033[0m")
    
    while paragum < 1:
        if after_call.status_code == 200:
            audlt_pic=text['responses'][0]['safeSearchAnnotation']['adult']
            spoof_pic=text['responses'][0]['safeSearchAnnotation']['spoof']
            medical_pic=text['responses'][0]['safeSearchAnnotation']['medical']
            violence_pic=text['responses'][0]['safeSearchAnnotation']['violence']
            racy_pic=text['responses'][0]['safeSearchAnnotation']['racy']
            print ("\033[1;32;40m for this picture, ADULT(成人向) component is \033[0m" + audlt_pic )
            print ("\033[1;32;40m for this picture, SPOOF(惡意惡搞) component is \033[0m" + spoof_pic )
            print ("\033[1;32;40m for this picture, MEDICAL(藥物相關) component is \033[0m" + medical_pic )
            print ("\033[1;32;40m for this picture, VIOLENCE(暴力) component is \033[0m" + violence_pic )
            print ("\033[1;32;40m for this picture, RACY(性暗示、性挑逗) component is \033[0m" + racy_pic )
            paragum = paragum + 1
        else:
            print("error, pls check the file or your autho id")
            print (text)
    print ("\n New Search")
