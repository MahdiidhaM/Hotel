from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import datetime 
import re

# @shared_task(name="data_checking")
# def data_add():
#     json_data = GetData.objects.get_data_from_db()
#     return json_data
# @shared_task()
# def sample_task():
#     # print('okkkkkkkk')
#     main.objects.create(text='main')
#     return 'ok'

from . import jalali
l = datetime.datetime.now() + datetime.timedelta(days= +1)
b = jalali.Gregorian(l.date()).persian_string()
import time as ti
@shared_task()
def Snap_task():
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get('https://www.snapptrip.com/%D8%B1%D8%B2%D8%B1%D9%88-%D9%87%D8%AA%D9%84/%D9%85%D8%B4%D9%87%D8%AF?gclid=CjwKCAiAgbiQBhAHEiwAuQ6Bkkj7yFFiBg8j09tkzZbeQM2WHDbO9liJMIeOz80BmDdXVUPlRsLRThoCw_MQAvD_BwE&price_from=0&price_to=0&page=1')
    Snap,created = Site.objects.update_or_create(site_name='SnapTrip')
    details = driver.find_elements(By.ID,'resultpage-hotelcard-hotelname')
    items_trip = []
    num = 0
    # for snap trip site
    for item in details[:8]:
        num+=1
        driver.switch_to.window(driver.window_handles[0])
        item.click()
        driver.switch_to.window(driver.window_handles[num])
        path = driver.current_url
        o = 0
        for j in driver.find_elements(By.ID,'hotelprofile-roomcards-cta-instantbookcomplete'):
            o+=1
        h = driver.find_element(By.TAG_NAME,'h1')
        star = driver.find_element(By.XPATH,'//*[@id="sec_hotel-info"]/div[1]/div[2]/div[1]/div[1]/div/meta').get_attribute('content')
        vote = driver.find_element(By.XPATH,'//*[@id="hotelSomeComment"]/div[1]/div[2]/div/div/div[1]')
        hotel_snap,created = Hotel.objects.update_or_create(hotel=Snap,hotel_name=f'{h.text} SnapTrip',hotel_vote=vote.text,hotel_star=star)
        for datea in range(9):
            l = datetime.datetime.now() + datetime.timedelta(days=datea)
            l_next = datetime.datetime.now() + datetime.timedelta(days=datea+1)
            bb1 = jalali.Gregorian(l.date()).persian_string()
            bb2 = jalali.Gregorian(l_next.date()).persian_string()
            numb1 = bb1.split('-')[-1]
            numb2 = bb2.split('-')[-1]
            driver.find_element(By.CLASS_NAME,'date-peacker').click()
            calender = driver.find_elements(By.XPATH,f"//td[text()='{numb1}']")
            if calender[0].get_attribute('class') == 'off disabled':
                em = 1
            else:
                em = 0
            calender[em].click()
            driver.find_element(By.XPATH,'//*[@id="topNavHotel"]/div[2]/form/div/div/div[5]/button').click()
            ti.sleep(3)
            day_1 = driver.find_elements(By.CLASS_NAME,'form-control')[1].get_attribute('value')
            day_2 = driver.find_elements(By.CLASS_NAME,'form-control')[2].get_attribute('value')
            convert_day_1 = jalali.Persian(day_1).gregorian_string()
            convert_day_2 = jalali.Persian(day_2).gregorian_string()
            convert_price = driver.find_elements(By.CLASS_NAME,'span-prices')
            if driver.find_elements(By.CLASS_NAME,'price')[1].text == '':
                multi = 2                    
            else:
                multi = 1
            for index,t in enumerate(driver.find_elements(By.CLASS_NAME,'room-item')):
                snap_room_name = driver.find_elements(By.CLASS_NAME,'text-ellipsis')[index].text
                snap_price = driver.find_elements(By.CLASS_NAME,'price')[index*multi].text
                convert_price = re.sub(',','',snap_price)
                room_team_snap,created = Room_Detail.objects.update_or_create(site=hotel_snap,Day=convert_day_1,Second_Day=convert_day_2,Path=path,Room_Name=snap_room_name,Off='',Price_Off=int(convert_price))
    return 'ok'

today_date = datetime.datetime.now()
tommorow_date = today_date + datetime.timedelta(days= +1)

@shared_task()
def Ali_task():
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get(f'https://www.alibaba.ir/hotel/ir-mashhad?destination=City_5be3f68be9a116befc66701b_%D9%85%D8%B4%D9%87%D8%AF+-+%D8%A7%DB%8C%D8%B1%D8%A7%D9%86&departing={today_date.date()}&returning={tommorow_date.date()}&rooms=30')
    site,created = Site.objects.update_or_create(site_name='AliBaba')
    ti.sleep(10)
    links = driver.find_elements(By.CLASS_NAME,'ho-available-card__title')
    for link in links[:6]:
        click_link = link.find_element(By.XPATH,'.//*')
        driver.execute_script("arguments[0].click();", click_link)
        
    page = len(driver.window_handles)
    
    for i in range(2,page):
        driver.switch_to.window(driver.window_handles[i])
        path_ali = driver.current_url
        title = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/main/div/div[2]/div/h1')
        hotel,created = Hotel.objects.update_or_create(hotel=site,hotel_name=title.text)
        day_range = 7
        for day in range(day_range):
            l_next = datetime.datetime.now() + datetime.timedelta(days=day)
            l_next_second = datetime.datetime.now() + datetime.timedelta(days=day+1)
            bb2 = jalali.Gregorian(l_next.date()).persian_string()
            bb3 = jalali.Gregorian(l_next_second.date()).persian_string()
            numb2 = int(bb2.split('-')[-1])
            numb3 = int(bb3.split('-')[-1])
            driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[2]/span').click()
            firstm = driver.find_element(By.XPATH,f"//span[text()='{numb2}']")
            d = 0
            if firstm.find_element(By.XPATH,'..').get_attribute('class') == 'calendar-cell is-disabled is-first is-passed':
                d = 1
            first = driver.find_elements(By.XPATH,f"//span[text()='{numb2}']")
            driver.execute_script("arguments[0].click();", first[d])
            decond = driver.find_elements(By.XPATH,f"//span[text()='{numb3}']")
            driver.execute_script("arguments[0].click();", decond[d])
            element = driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[3]/div/div[3]/button')
            driver.execute_script("arguments[0].click();", element)
            butt = driver.find_element(By.XPATH,'//*[@id="ho_sidebar"]/div/div/div/button')
            driver.execute_script("arguments[0].click();", butt)
            his = driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[2]/span').text
            try:
                convert_date = jalali.Persian(his.split('–')[0][:-1]).gregorian_string()
                convert_date_next = jalali.Persian(his.split('–')[1][1:]).gregorian_string()
            except:
                pass
            ti.sleep(5)
            try:
                driver.find_element(By.XPATH,'//*[@id="ho_main"]/div/section[3]/button').click()
                driver.find_element(By.XPATH,'//*[@id="ho_main"]/div/section[3]/button').click()
                driver.find_element(By.XPATH,'//*[@id="ho_main"]/div/section[3]/button').click()
            except:
                pass
            
            try:
                for index,mar in enumerate(driver.find_elements(By.TAG_NAME,'h5')):
                    price = driver.find_elements(By.CLASS_NAME,'text-5')[index]
                    convert_price = re.sub(',','',price.text)
                    room_team,created = Room_Detail.objects.update_or_create(site=hotel,Day=convert_date,Second_Day=convert_date_next,Path=path_ali,Room_Name=mar.text,Price_Off=int(convert_price)/10)
            except:
                pass
            ti.sleep(10)
    return 'ali ok'

@shared_task()
def Eghamat_task():
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get('https://www.eghamat24.com/MashhadHotels.html')
    Eghamat,created = Site.objects.update_or_create(site_name='Eghamat')
    for cli in range(1,8):
        new =  driver.find_element(By.XPATH,f'/html/body/main/div[3]/div/div/section/div/article[1]/a[{cli}]')
        new.click()
        cous = 0
        for cou in driver.find_elements(By.CLASS_NAME,'icon-shopping-cart'):
            cous+=1
        hotel_title = driver.find_element(By.CLASS_NAME,'hotel_name')
        hotel_eghamat,created = Hotel.objects.update_or_create(hotel=Eghamat,hotel_name=f'{hotel_title.text} Eghamat')
        for num in range(1,cous-4):
            try:
                x = driver.find_element(By.XPATH,f'//*[@id="hotel_reservation"]/div/div/div[2]/div[1]/div[2]/div[{num}]')
                pesrons = driver.find_elements(By.CLASS_NAME,'room-capacity')[num-1]
            except:
                pass
            num_of = 0
            for inj in pesrons.find_elements(By.CLASS_NAME,'icon-man'):
                num_of+=1
            element = ''.join(x.text)
            elements = element.split('\n')
            l_next = datetime.datetime.now() + datetime.timedelta(days=0)
            l_next_second = datetime.datetime.now() + datetime.timedelta(days=+1)
            try:
                convert_price = re.sub(',','',elements[-3][:-5])
                room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=l_next_second.date(),Day=l_next.date(),Path=driver.current_url,Room_Name=elements[0],Night='برای 1 شب',Future=elements[-7],Person_Number=num_of,Price_Origin=elements[-5],Off=elements[-8],Price_Off=int(convert_price))
            except:
                room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=l_next_second.date(),Day=l_next.date(),Path=driver.current_url,Room_Name=elements[0],Night='برای 1 شب',Future=elements[-5],Person_Number=num_of,Price_Origin=elements[-4],Off=elements[-6],Price_Off=elements[-3])
            driver.find_element(By.XPATH,f'//*[@id="hotel_reservation"]/div/div/div[2]/div[1]/div[2]/div[{num}]/section[5]/div[2]/a').click()
            for table in range(1,6):
                t = driver.find_element(By.XPATH,f'//*[@id="hotel_reservation"]/div/div/div[2]/div[1]/div[2]/div[{num}]/section[7]/div/div[{table}]')
                tab = ''.join(t.text)
                tabs = tab.split('\n')
                times = jalali.Persian(f'1401{tabs[0][-6:]}').gregorian_string()
                times_end = datetime.datetime.strptime(times,'%Y-%m-%d')
                times_Second = times_end + datetime.timedelta(days=+1)
                try:
                    convert_price_next = re.sub(',','',tabs[2][:-6])
                    room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=times_Second.date(),Day=times_end,Room_Name=elements[0],Path=driver.current_url,Night='برای 1 شب',Future=elements[-7],Person_Number=num_of,Price_Origin=tabs[1],Off=elements[-8],Price_Off=int(convert_price_next))
                except:
                    room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=times_Second.date(),Day=times_end,Room_Name=elements[0],Path=driver.current_url,Night='برای 1 شب',Future=elements[-5],Person_Number=num_of,Off=elements[-6],Price_Off=tabs[1])
        driver.back()
    return 'Eghamat ok'