"""
Developer Name : Smrithi Ganesh
Last updated on : 28-April-2023
Commit remark : Borders for image done

"""
#importing the required python modules
#git import to push the threshold value
import git


#GUI required import
import tkinter
from tkinter import *
import numpy as np
import tkinter.font as font
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


# importing modules for API call and GDD algorithm implementation
import json
import pandas as pd
import requests
import os
import schedule 
import time
import xlsxwriter
import datetime
from datetime import date
from styleframe import StyleFrame
from selenium import webdriver
from bs4 import BeautifulSoup

#Dark mode for app default since system is in dark mode
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Previoulsy used Gdd code
class temperatureClass :
    
    #constructor
    def __init__(self,base_temperature,url,app):
        
        self.url = url ;
        self.base_temperature = base_temperature ;
        self.dayNumber = 0;
        self.indDayNo = 0;
        self.daysArray =[];
        self.Temp =[]
        self.highTemp = [];
        self.lowTemp = [];
        self.avgTemp = [];
        self.gDD = [];
        self.cumGDD = [];
        self.window = app;
        self.thresholdDate ='';
        self.daycount = 0;
        self.strCumGDD = [];
        self.rain=[];
        self.rainPrecipitaion=[];
        self.reducedRain=[];
        self.app=app;
        
    #Extracting from website        
    def extractTempFromWeb(self):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--headless')
        i=0;
        self.Temp=[];
        driver = webdriver.Chrome(options = chrome_options)
        source =driver.get('https://weather.com/weather/tenday/l/7f3924e156afb7814c8d12d1e4ea0138b2e46869a57075ebc763c2963d75ec82')

        source_code=driver.page_source

        soup = BeautifulSoup(source_code,'lxml')
        tempFromWeb =soup.find_all('div',class_='DailyContent--ConditionSummary--2gdfo')
        rainFromWeb =soup.find_all('div',class_='DailyContent--label--30_yg')
        rainPrecipitaion=[]
        rainTotal=[]
        for tempExtraction in tempFromWeb:
            self.Temp.append(tempExtraction.find('span',{'class' : 'DailyContent--temp--1s3a7'}).get_text())
        for rainChance in rainFromWeb:
            rainTotal.append(rainChance.find('span',{'class' : 'DailyContent--value--1Jers'}).get_text())
        for r in rainTotal:
            if "%" in r:
                self.rain.append((r.replace("%","")));
        print(self.rain)
      
        while i<=25:
            self.rainPrecipitaion.append((int(self.rain[i])+int(self.rain[i+1]))*0.5)
            i=i+2
             
        self.highLowTempExtraction()
        
    
    #Manipulating extracted data to not overwrite existing data    
    def highLowTempExtraction(self):
        print('\n inside high low')
        file1 = open("C:\\Users\\Smrithi Ganesh\\ActionTrial\\.github\\workflows\\outputFile1.txt", "r+")
        if os.path.getsize('C:\\Users\\Smrithi Ganesh\\ActionTrial\\.github\\workflows\\outputFile1.txt') == 0:
            j=0;
            k=0;
            dayNo = self.dayNumber
            
            ht = [];
            lt = [] ;
        
            del self.lowTemp[dayNo:len(self.Temp)]
            del self.highTemp[dayNo:len(self.Temp)]
            del self.avgTemp[dayNo:len(self.Temp)]
            del self.gDD[dayNo:len(self.Temp)]
            del self.cumGDD[dayNo:len(self.Temp)]
            while j<len(self.Temp)-2:
                self.highTemp.insert(dayNo,self.Temp[j].replace("°",""));
                self.lowTemp.insert(dayNo,self.Temp[j+1].replace("°",""));
                self.avgTemp.insert(dayNo,(float(self.highTemp[dayNo])+float(self.lowTemp[dayNo]))/2.0)
                self.gDD.insert(dayNo,self.avgTemp[dayNo] - self.base_temperature);
                if (dayNo==0):
                    self.cumGDD.insert(self.indDayNo,0)
                    self.strCumGDD.append(str(self.cumGDD[0]))
                else :
                    self.daycount = dayNo;
                    self.daysArray.append(self.daycount)
                    self.strCumGDD.append(str(self.cumGDD[len(self.cumGDD)-1]))
                    if(self.cumGDD[len(self.cumGDD)-1]>140): 
                        
                        i=0;
                        while i<self.daycount:
                            self.reducedRain.append(self.rainPrecipitaion[i])
                            i=i+1;
                        print('self.reducedRain->',self.reducedRain)
                        min_value = min(self.reducedRain)
                        perfectDay = self.reducedRain.index(min_value)  
                        self.thresholdDate = date.today()+ datetime.timedelta(days=perfectDay)
                        self.plotGddStatistics()
                        title = f'First spray is schefuled on {self.thresholdDate} becuase of the lowest precipitation chance-{min_value} '
                        body ="Kindly click start pump on this day to eliminate possible weed emergence"
                        self.pushbullet_notification(title, body)
                        break
                    self.cumGDD.insert(dayNo,self.cumGDD[dayNo-1]+self.gDD[dayNo])
                j=j+2
                dayNo = dayNo+1
            self.dayNumber = self.dayNumber+1
        else:
            self.plotGddStatistics()
            
    
    #To call WISE by entering the URL    
    def apiCallToWise(self):
        with open('.github/workflows/outputFile1.txt') as f:
            contents = f.readlines()
            
        #switching the relay 0 ON only on the predicted threshold date
        if (date.today()==contents):
            payload = {
                "Ch": 0,
                "Md": 0,
                "Val": 1,
                "Stat": 1,
                "PsCtn": 1,
                "PsStop": 0,
                "PsIV": 0
            }
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Basic cm9vdDowMDAwMDAwMA==",
                "Cookie": "Cookie=adamsessionid=12965427BA2"
            }


            Flag = True;
            while(Flag):
                response = requests.request("POST", self.url, json=payload, headers=headers)
                time.sleep(3)
                print(response)
                Flag = False;
                
            #switching the relay 0 OFF
            payload1 = {
                "Ch": 0,
                "Md": 0,
                "Val": 0,
                "Stat": 0,
                "PsCtn": 1,
                "PsStop": 0,
                "PsIV": 0
            }
            response = requests.request("POST", url, json=payload1, headers=headers)
            
            if response1.status_code == 200:
                msg = "The first preventive herbicide spray is done kindly place the robot on the field to monitor the further emergence of weed"
                self.pushbullet_notification("First preventive herbicide spray done",msg)
        else:
            msg = f"The preventive spray is predicted for {contents}"
            self.pushbullet_notification("Today is not the predicted date for the preventive herbicide spray",msg)
            
    #To plot GDD and rain percentage curve for visuals
    def plotGddStatistics(self):
        
        main_window=self.app
        main_window.configure(bg='black')
        #main_window.geometry("1280x720")
        file1 = open("C:\\Users\\Smrithi Ganesh\\ActionTrial\\.github\\workflows\\outputFile1.txt", "r+")
        if os.path.getsize('C:\\Users\\Smrithi Ganesh\\ActionTrial\\.github\\workflows\\outputFile1.txt') == 0:
            file1 = open("C:\\Users\\Smrithi Ganesh\\ActionTrial\\.github\\workflows\\outputFile1.txt", "w");
            file1.write(str(self.thresholdDate))
            print('\n written',self.thresholdDate)
            x = range(0,self.daycount,1)
            d=[]
            for i in x:
                print(i)
                d.append(i)
            x1 = d
            y1 = self.reducedRain
            y2 = self.cumGDD;
            fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(8, 5),facecolor='black')
            ax1.plot(x1, y1,linewidth = '2',marker='D',linestyle='-')
            ax2.plot(x1, y2,linewidth = '2',marker='D',linestyle='-')
            plt.tick_params(axis='both', labelsize=16)
            ax1.set_title("Average percentage of precipitation vs days",color='white',size='20')
            ax1.set_xlabel("Day",size='20')
            ax1.set_ylabel("Average Rain Percentage",size='20')
            ax2.set_xlabel("Day",size='20')
            ax2.set_ylabel("Growing Degree Day",size='20')
            ax2.set_title("Cumulative GDD vs days",color='white',size='20')
            ax2.set_facecolor("black")
            ax1.set_facecolor("black")
            ax1.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
            ax1.yaxis.label.set_color('white')  
            ax2.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
            ax2.yaxis.label.set_color('white')  
            ax1.tick_params(axis='x', colors='white')    #setting up X-axis tick color to blue
            ax1.tick_params(axis='y', colors='white')  #setting up Y-axis tick color to black
            ax2.tick_params(axis='x', colors='white')    #setting up X-axis tick color to red
            ax2.tick_params(axis='y', colors='white')  #setting up Y-axis tick color to black
            ax1.spines['left'].set_color('white')    # setting up Y-axis tick color to red
            ax1.spines['bottom'].set_color('white')         #setting up  X-axis tick color to red
            ax2.spines['left'].set_color('white')        # setting up Y-axis tick color to red
            ax2.spines['bottom'].set_color('white')         #setting up  X-axis tick color to red
            line_graph1 = FigureCanvasTkAgg(fig,main_window)
            line_graph1.get_tk_widget().pack(side=customtkinter.BOTTOM,fill=customtkinter.BOTH)
            fig.suptitle('GDD and Preciptitation Percentage vs Days charts')
            
            main_window.mainloop()
            
    def pushbullet_notification(self,title, body):
        """
        TOKEN = 'o.WDQEkWs8Rs5S6WEJq1MhXU69k4rZMuEr'
        # Making a dictionary for type, title and body parameters
        msg = {"type": "note", "title": title, "body": body}
        # Sent a posts request
        response1 = requests.post('https://api.pushbullet.com/v2/pushes',data=json.dumps(msg),headers={'Authorization': 'Bearer ' + TOKEN,'Content-Type': 'application/json'})
        if response1.status_code != 200: # Response code 200 signifies perfect access to app 
            raise Exception('Error', resp.status_code)
"""


#intatntiating app window 
app=customtkinter.CTk()
app.config(bg='black')
#filling 1280x720 pixel page area
app.geometry("1280x720")
#tile for the app window
app.title("Floral Notification Hub")

#instance of temperatureClass with URL of WISE
tc = temperatureClass(48,"http://192.168.1.14",app)



#Welcome message with position
nameLabel = customtkinter.CTkLabel(app,text="Welcome to Floral Hub Notification for Irvine , CA",font=("Arial Bold", 40))
nameLabel.place(relx=0.50, rely=0.45, anchor=tkinter.CENTER)
#image at the top of the page along with its position
image1 = Image.open(".github/workflows/logo5050.jpg")
image2 = Image.open(".github/workflows/advlogoblackbgresize.png")
image3 = Image.open(".github/workflows/samuelilogoblackbgresize.png")
img1 = ImageTk.PhotoImage(image1)
img2 = ImageTk.PhotoImage(image2)
img3 = ImageTk.PhotoImage(image3)
label1 = tkinter.Label(image=img1,borderwidth=1, relief="solid")
label1.image = img1

label2 = tkinter.Label(image=img2,borderwidth=1, relief="solid")
label2.image = img2
label3 = tkinter.Label(image=img3,borderwidth=1, relief="solid")
label3.image = img3
label2.place(x=500,y=80,anchor=tkinter.NE)
label3.place(x=1430,y=10,anchor=tkinter.NW)
label1.place(x=970,y=190,anchor=tkinter.CENTER)


#predicting Gdd and stopping pump system by invoking Wise API on button click and positioned on app window
button1 = customtkinter.CTkButton(app,text="STOP PUMP",command=tc.extractTempFromWeb,font=("Arial Bold", 15))
button2 = customtkinter.CTkButton(app,text="START PUMP",command=tc.apiCallToWise,font=("Arial Bold", 15))
button1.place(relx=0.35, rely=0.55, anchor=tkinter.CENTER)
button2.place(relx=0.65, rely=0.55, anchor=tkinter.CENTER)

#If previous prediction already done , displaying the threshold date alone
if os.path.getsize('.github/workflows/outputFile1.txt') == 0:
    button = customtkinter.CTkButton(app,text="START PREDICTION",command=tc.extractTempFromWeb,font=("Arial Bold", 15))
    button.place(relx=0.50, rely=0.50, anchor=tkinter.CENTER)
else :
    with open('.github/workflowsoutputFile1.txt') as f:
        contents = f.readlines()
        contents = contents.pop();
        contents = contents.rstrip();
    #Labeling the already predicted threshold date on the window
    nameLabel1 = customtkinter.CTkLabel(app,text=f'The first weeed spray will be on {contents}',font=("Arial Bold", 25))
    nameLabel1.place(relx=0.50, rely=0.50, anchor=tkinter.CENTER)

app.mainloop()
