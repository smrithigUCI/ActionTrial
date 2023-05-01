from datetime import date

  
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
def main():
  strCumGDD=[]
  daysArray=[]
  reducedRain=[]
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--ignore-certificate-errors')
  chrome_options.add_argument('--incognito')
  chrome_options.add_argument('--headless')
  i=0;
  indDayNo=0;
  base_temperature=48;
  Temp=[];
  cumGDD=[];
  avgTemp=[]
  gDD=[];
  cumGDD=[];
  driver = webdriver.Chrome(options = chrome_options)
  source =driver.get('https://weather.com/weather/tenday/l/7f3924e156afb7814c8d12d1e4ea0138b2e46869a57075ebc763c2963d75ec82')
  source_code=driver.page_source

  soup = BeautifulSoup(source_code,'lxml')
  tempFromWeb =soup.find_all('div',class_='DailyContent--ConditionSummary--2gdfo')
  rainFromWeb =soup.find_all('div',class_='DailyContent--label--30_yg')
  rainPrecipitaion=[]
  rain=[]
  rainTotal=[]
  dayNumber=0;
  lowTemp=[]
  highTemp=[]
  for tempExtraction in tempFromWeb:
    Temp.append(tempExtraction.find('span',{'class' : 'DailyContent--temp--1s3a7'}).get_text())
  for rainChance in rainFromWeb:
    rainTotal.append(rainChance.find('span',{'class' : 'DailyContent--value--1Jers'}).get_text())
  for r in rainTotal:
    if "%" in r:
      rain.append((r.replace("%","")));
  while i<=25:
    rainPrecipitaion.append((int(rain[i])+int(rain[i+1]))*0.5)
    i=i+2
    print('\n inside high low')
  with open('.github/workflows/outputFile1.txt','r+') as f:
    contents = f.readlines()
    contents = contents.pop();
    contents = contents.rstrip();
    if(contents==''):
      j=0;
      k=0;
      dayNo = dayNumber
      ht = [];
      lt = [] ;
      del lowTemp[dayNo:len(Temp)]
      del highTemp[dayNo:len(Temp)]
      del avgTemp[dayNo:len(Temp)]
      del gDD[dayNo:len(Temp)]
      del cumGDD[dayNo:len(Temp)]
      while j<len(Temp)-2:
        highTemp.insert(dayNo,Temp[j].replace("°",""));
        lowTemp.insert(dayNo,Temp[j+1].replace("°",""));
        avgTemp.insert(dayNo,(float(highTemp[dayNo])+float(lowTemp[dayNo]))/2.0)
        gDD.insert(dayNo,avgTemp[dayNo] - base_temperature);
        if (dayNo==0):
          cumGDD.insert(indDayNo,0)
          strCumGDD.append(str(cumGDD[0]))
        else :
          daycount = dayNo;
          daysArray.append(daycount)
          strCumGDD.append(str(cumGDD[len(cumGDD)-1]))
          if(cumGDD[len(cumGDD)-1]>140):
            print(cumGDD)
            i=0;
            while i<daycount:
              reducedRain.append(rainPrecipitaion[i])
              i=i+1;
             print('reducedRain->',reducedRain)
             min_value = min(reducedRain)
             perfectDay = reducedRain.index(min_value)
             print(perfectDay)
             thresholdDate = date.today()+ datetime.timedelta(days=perfectDay)
             print(thresholdDate)
             break
           cumGDD.insert(dayNo,cumGDD[dayNo-1]+gDD[dayNo])
           j=j+2
           dayNo = dayNo+1
       dayNumber = dayNumber+1
     if (str(date.today())==contents):
          print("today's date is-> SG is awesome->",contents);
          print(f'The dates match : content of file:->{contents} \n today date :{date.today()}');
if __name__=='__main__':
  main()
