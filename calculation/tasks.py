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
# @shared_task(name='vubon')
# def test():
#     print(' Hello world')
#     return 'test'


# @shared_task(name="data_checking")
# def data_add():
#     json_data = GetData.objects.get_data_from_db()
#     return json_data
from .models import main
@shared_task()
def sample_task():
    # print('okkkkkkkk')
    main.objects.create(text='main')
    return 'ok'

from . import jalali
l = datetime.datetime.now() + datetime.timedelta(days= +1)
b = jalali.Gregorian(l.date()).persian_string()
import time as ti
@shared_task()
def Snap_task():
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get('https://www.snapptrip.com/%D8%B1%D8%B2%D8%B1%D9%88-%D9%87%D8%AA%D9%84/%D9%85%D8%B4%D9%87%D8%AF?gclid=CjwKCAiAgbiQBhAHEiwAuQ6Bkkj7yFFiBg8j09tkzZbeQM2WHDbO9liJMIeOz80BmDdXVUPlRsLRThoCw_MQAvD_BwE&price_from=0&price_to=0&page=1')
    Snap,created = Site.objects.update_or_create(site_name='SnapTrip')
    # Snap_first,created = First.objects.get_or_create(site_name='SnapTrip')
    details = driver.find_elements(By.ID,'resultpage-hotelcard-hotelname')
    items_trip = []
    num = 0
    # for snap trip site
    for item in details[:10]:
        ti.sleep(10)
        num+=1
        driver.switch_to.window(driver.window_handles[0])
        item.click()
        try:
            driver.switch_to.window(driver.window_handles[num])
            path = driver.current_url
            # l2 = datetime.datetime.now() + datetime.timedelta(days= 0)
            # bb = jalali.Gregorian(l.date()).persian_string()
            # numb = bb.split('-')[-1]
            # bb2 = jalali.Gregorian(l.date()).persian_string()
            o = 0
            for j in driver.find_elements(By.ID,'hotelprofile-roomcards-cta-instantbookcomplete'):
                o+=1
            h = driver.find_element(By.TAG_NAME,'h1')
            star = driver.find_element(By.XPATH,'//*[@id="sec_hotel-info"]/div[1]/div[2]/div[1]/div[1]/div/meta').get_attribute('content')
            vote = driver.find_element(By.XPATH,'//*[@id="hotelSomeComment"]/div[1]/div[2]/div/div/div[1]')
            # print(vote.text)
            # print(int(star))
            # print('----------')
            hotel_snap,created = Hotel.objects.update_or_create(hotel=Snap,hotel_name=f'{h.text} SnapTrip',hotel_vote=vote.text,hotel_star=star)
            

            for date in range(0,5):
                l = datetime.datetime.now() + datetime.timedelta(days=date)
                l_next = datetime.datetime.now() + datetime.timedelta(days=date+1)
                bb2 = jalali.Gregorian(l.date()).persian_string()
                numb2 = bb2.split('-')[-1]
                driver.find_element(By.XPATH,'//*[@id="topNavHotel"]/div[2]/form/div/div/div[3]/div[1]/input').click()
                driver.find_element(By.XPATH,f"//td[text()='{numb2}']").click()
                driver.find_element(By.XPATH,'//*[@id="topNavHotel"]/div[2]/form/div/div/div[5]/button').click()
                for t in driver.find_elements(By.CLASS_NAME,'room-item'):
                    # items_trip.append(t.text)
                    s = ''.join(t.text)
                    sn = s.split('\n')
                    room_team_snap,created = Room_Detail.objects.update_or_create(site=hotel_snap,Day=l.date(),Second_Day=l_next.date(),Path=path,Room_Name=sn[0],Night=sn[6],Future=sn[4],Person_Number=sn[3],Price_Origin='',Off='',Price_Off=sn[7])
        except:
            pass
    return 'ok'

today_date = datetime.datetime.now()
tommorow_date = today_date + datetime.timedelta(days= +1)

@shared_task()
def Ali_task():
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get(f'https://www.alibaba.ir/hotel/ir-mashhad?destination=City_5be3f68be9a116befc66701b_%D9%85%D8%B4%D9%87%D8%AF+-+%D8%A7%DB%8C%D8%B1%D8%A7%D9%86&departing={today_date.date()}&returning={tommorow_date.date()}&rooms=30')
    site,created = Site.objects.update_or_create(site_name='AliBaba')
    reserve = []
    add = []
    ti.sleep(20)

    for link in range(1,5):
        try:
            links = driver.find_element(By.XPATH,f'/html/body/div/div[1]/main/div[2]/div/section/div[2]/div[1]/div[{link}]/div[1]/div[2]/div/div[1]/div[2]/a')
            links.click()
        except:
            linkss = driver.find_element(By.XPATH,f'/html/body/div/div[1]/main/div[2]/div/section/div[3]/div[1]/div[{link}]/div[1]/div[2]/div/div[1]/div[2]/a')
            linkss.click()
    page = len(driver.window_handles)
    # print(page)
    
    for i in range(2,page):
        # driver.switch_to.window(driver.window_handles[7])
        
        driver.switch_to.window(driver.window_handles[i])
        path_ali = driver.current_url
        
        # count = 1
        # for number in driver.find_elements(By.CLASS_NAME,'leading-loose'):
        #     count +=1
        # //*[@id="app"]/div[1]/main/div/div[2]/div/h1
        # //*[@id="app"]/div[1]/main/div/div[2]/div/h1
        title = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/main/div/div[2]/div/h1')
        hotel,created = Hotel.objects.update_or_create(hotel=site,hotel_name=title.text)
        end = []
        ti.sleep(10)
        for day in range(5):
            for j in range(2):
                try:
                    # /html/body/div/div[1]/main/div/div[3]/div/section[3]/button
                    # /html/body/div/div[1]/main/div/div[3]/div/section[3]/button
                    driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/div/section[3]/button').click()
                    driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/div/section[3]/button').click()
                    driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/div/section[3]/button').click()
                except:
                    pass
                if j == 1 :
                    week=4
                else:
                    week=0
                l_next = datetime.datetime.now() + datetime.timedelta(days=day)
                l_next_second = datetime.datetime.now() + datetime.timedelta(days=day+1)
                bb2 = jalali.Gregorian(l_next.date()).persian_string()
                bb3 = jalali.Gregorian(l_next_second.date()).persian_string()
                numb2 = bb2.split('-')[-1]
                numb3 = bb3.split('-')[-1]
                driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[2]/span').click()
                first = driver.find_elements(By.XPATH,f"//span[text()='{numb2}']")
                decond = driver.find_elements(By.XPATH,f"//span[text()='{numb3}']")
                # if numb2 == 31:
                #     three = driver.find_elements(By.XPATH,f"//span[text()='31']")
                #     one = driver.find_elements(By.XPATH,f"//span[text()='1']")
                #     three[0].click()
                #     one[1].click()
                # else:
                #     first[0].click()
                #     first[1].click()
                #     decond[0].click()
                #     decond[1].click()
                
                first[j].click()
                decond[j].click()
                element = driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[3]/div/div[3]/button')
                driver.execute_script("arguments[0].click();", element)
                butt = driver.find_element(By.XPATH,'//*[@id="ho_sidebar"]/div/div/div/button')
                driver.execute_script("arguments[0].click();", butt)
                ti.sleep(10)
                for mar in driver.find_elements(By.CLASS_NAME,'a-card__body')[3:-3]:
                    ti.sleep(10)
                    try:
                        p = ''.join(mar.text)
                        items_ali = p.split('\n')
                        add.append(items_ali)
                        room_team,created = Room_Detail.objects.update_or_create(site=hotel,Day=l_next.date(),Second_Day=l_next_second.date(),Path=path_ali,Room_Name=items_ali[0],Night=items_ali[-1],Future=items_ali[1],Person_Number=items_ali[3],Price_Origin=items_ali[6],Off=items_ali[5],Price_Off=items_ali[4])
                    except:
                        pass
    return 'ali ok'

# /html/body/div/div[1]/main/div[2]/div/section/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]/a