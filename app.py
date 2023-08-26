#!/usr/bin/env python
# -*- coding: utf-8 -*-


                                                                                 
      ##                         ##   ######                     #####           
  ### ##   #####     #####   ### ##  #######   #####    #####   #######   #####  
 #### ##  #######   ######  #### ##  ##       #######  #######  ##   ##  ####### 
 ##   ##  ##  ###  ###  ##  ##   ##  ######   ##   ##  ##  ###  ## ####  ##   ## 
 ##   ##  ##  ##   ##   ##  ##   ##  ##   ##  ##       ##  ##   ## ###   ##   ## 
 ######   ####     #######  ######   #######  ##       ####     ##       ####### 
  #####    #####    #####    #####    #####   ##        #####   ##        #####  

  
                                            #WaktuSolatv1 Project By Ikmal 2023   
                                                                 

from flask import Flask
import requests
import tweepy, time, sys, urllib, json
import urllib.request

app = Flask(__name__)

@app.route("/")
def index():
  
    # config
    api_key = ""
    api_secret = ""
    bearer_token = ""
    access_token = ""
    access_token_secret = ""

    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    #API For KL https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=today&zone=wly01
    
    url = "https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=today&zone=sgr01"
    response = urllib.request.urlopen(url);

    print(response)
    data = json.loads(response.read())

    contents = response.read().decode('utf-8')

    print(contents)

    today = str((data['prayerTime']))

    tweet = today

    print(tweet)

    for num in data['prayerTime']:
        print("Date:", num['date'])
        print("Imsak:", num['imsak'])
        print("Subuh:", num['fajr'])
        print("Zohor:", num['dhuhr'])
        print("Asar:", num['asr'])
        print("Maghrib:", num['maghrib'])
        print("Isyak:", num['isha'])

        Date = num['date']
        Imsak = "Imsak: " + num['imsak']
        Subuh = "Subuh: " + num['fajr']
        Zohor = "Zohor: " + num['dhuhr']
        Asar = "Asar: " + num['asr']
        Maghrib = "Maghrib: " + num['maghrib']
        Isyak = "Isyak: " + num['isha']

        client.create_tweet(text="Waktu Solat for " + Date + " 🌕\n\n" + Imsak + "\n" + Subuh + "\n" + Zohor + "\n" + Asar + "\n" + Maghrib + "\n" + Isyak)

        return "<p>Prayer Time Tweeted !</p>"


if __name__ == "__main__":
	app.run()