from plyer import notification
import requests
from bs4 import BeautifulSoup 
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon ="C:\\Users\\DELL\\Desktop\\Notification System\\COVID-19-Notification-System\\icon.ico",
        timeout = 6
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        #notifyMe("Hey Smile", "Enjoying vacations?")
        myHTMLData = getData('https://www.mohfw.gov.in/')
        #print(myHTMLData)
        soup = BeautifulSoup(myHTMLData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            #print(tr.get_text())
            myDataStr +=tr.get_text()
        myDataStr=myDataStr[1:]
        itemList= myDataStr.split("\n\n")

        states=['Punjab', 'Uttar Pradesh', 'Chandigarh', 'Haryana']
        for item in itemList[0:23]:
            dataList= item.split("\n")
            if dataList[1] in states:
                #print(dataList)
                nTitle = 'Cases of COVID-19'
                nText =f"State {dataList[1]}\n Indian : {dataList[2]} & Foreign : {dataList[3]}\n Cured : {dataList[4]}\n Deaths : {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)