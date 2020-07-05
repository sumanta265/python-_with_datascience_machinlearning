# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 01:40:32 2020

@author: SUMANTA KR MAJI
"""


from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title,message):
    notification.notify(
            title = title,
            message= message,
            app_icon= "C:\\Users\SUMANTA KR MAJI\Desktop\corona.ico",
            timeout = 5
    )
    
    
def getData(url):
     r = requests.get(url)
     return r.text
    
if __name__ == "__main__" :
     while True:
         myhtmlData=getData("https://www.mohfw.gov.in/")
         soup = BeautifulSoup(myhtmlData, 'html.parser')
         myDatastr =""
         for tr in soup.find_all('tbody')[1].find_all('tr'):
             myDatastr  += tr.get_text()
         myDatastr = myDatastr[1:]
         itemList=myDatastr.split("\n\n")
         dataList=[]   
         states = ['Gujarat','West Bengal','Chhattisgarh','Gujarat','Haryana','Karnataka','Kerala'] 
         for item in itemList[0:24]:
             dataList=item.split("\n")
             if dataList[1] in states:
                 
                 nTitle="Case of Covid-19"
                 nText=f"\nState: {dataList[1]} \nIndian: {dataList[2]}  Foreign: {dataList[3]} \nCured: {dataList[4]} \nDeaths: {dataList[5]}"
                 notifyMe(nTitle,nText)
                 time.sleep(3)
         time.sleep(10)  