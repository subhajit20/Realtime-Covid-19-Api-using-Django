import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/" # scrap usrl

def GetCovid19RealtimeData():
    data = requests.get(url)
    content = BeautifulSoup(data.content,features="html.parser")

    covid19_data = []

    alldata = content.find("tbody")
    listofallvaliddata = list(alldata.children)

    if len(listofallvaliddata) > 0:
        realtimedata = listofallvaliddata[17::2]
        # Pushing all the data into covid19_data list using list comprehension
        covid19_data = [{
                "Number":list(i.children)[1::2][0].text,
                "Country":list(i.children)[1::2][1].text,
                "Total Cases":list(i.children)[1::2][2].text,
                "New Cases":list(i.children)[1::2][3].text,
                "Total Deaths":list(i.children)[1::2][4].text,
                "New Deaths":list(i.children)[1::2][5].text,
                "Total Recovered":list(i.children)[1::2][6].text,
                "New Recovered":list(i.children)[1::2][7].text,
                "Active Cases":list(i.children)[1::2][8].text,
                "Serious Critical":list(i.children)[1::2][9].text
            }  for i in realtimedata]
    else:
        covid19_data = []

    return covid19_data