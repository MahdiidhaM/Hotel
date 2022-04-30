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
                x = 0
                for t in driver.find_elements(By.CLASS_NAME,'info-room'):
                    x += 1
                    # items_trip.append(t.text)
                    # inc = index+1
                    con = driver.find_element(By.XPATH,f"/html/body/div[1]/main/div/div[1]/div[1]/div[4]/div[2]/div/div/div[{x}]/div/div[1]/div[1]/div[1]/span")
                    conj = ''.join(con.text)
                    s = ''.join(t.text)
                    sn = s.split('\n')
                    convert_price = re.sub(',','',sn[1][:-6])
                    room_team_snap,created = Room_Detail.objects.update_or_create(site=hotel_snap,Day=l.date(),Second_Day=l_next.date(),Path=path,Room_Name=conj,Night=sn[0],Future='',Person_Number=sn[3],Price_Origin='',Off='',Price_Off=int(convert_price))
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
                        convert_price = re.sub(',','',items_ali[4][12:-5])
                        add.append(items_ali)
                        room_team,created = Room_Detail.objects.update_or_create(site=hotel,Day=l_next.date(),Second_Day=l_next_second.date(),Path=path_ali,Room_Name=items_ali[0],Night=items_ali[-1],Future=items_ali[1],Person_Number=items_ali[3],Price_Origin=items_ali[6],Off=items_ali[5],Price_Off=int(convert_price)/10)
                    except:
                        pass
    return 'ali ok'

# /html/body/div/div[1]/main/div[2]/div/section/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div[2]/a
@shared_task()
def Eghamat_task():
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get('https://www.eghamat24.com/MashhadHotels.html')
    Eghamat,created = Site.objects.update_or_create(site_name='Eghamat')
    egh = []
    his = []
    main = []
    timess = []
    for cli in range(1,5):
        new =  driver.find_element(By.XPATH,f'/html/body/main/div[3]/div/div/section/div/article[1]/a[{cli}]')
        
        new.click()
        cous = 0
        for cou in driver.find_elements(By.CLASS_NAME,'icon-shopping-cart'):
            cous+=1
        hotel_title = driver.find_element(By.CLASS_NAME,'hotel_name')
        hotel_eghamat,created = Hotel.objects.update_or_create(hotel=Eghamat,hotel_name=f'{hotel_title.text} Eghamat')
        egh.append(hotel_title.text)
        for num in range(1,cous-4):
            try:
                x = driver.find_element(By.XPATH,f'//*[@id="hotel_reservation"]/div/div/div[2]/div[1]/div[2]/div[{num}]')
                egh.append(x.text)
                element = ''.join(x.text)
                elements = element.split('\n')
                convert_price = re.sub(',','',elements[7][:-5])
                l_next = datetime.datetime.now() + datetime.timedelta(days=0)
                l_next_second = datetime.datetime.now() + datetime.timedelta(days=+1)
                room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=l_next_second.date(),Day=l_next.date(),Path=driver.current_url,Room_Name=elements[0],Night='برای 1 شب',Future=elements[2],Person_Number='1نفر',Price_Origin=elements[5],Off='',Price_Off=int(convert_price))
                driver.find_element(By.XPATH,f'//*[@id="hotel_reservation"]/div/div/div[2]/div[1]/div[2]/div[{num}]/section[5]/div[2]/a').click()
                # if num < 6:
                for table in range(1,6):
                    t = driver.find_element(By.XPATH,f'//*[@id="hotel_reservation"]/div/div/div[2]/div[1]/div[2]/div[{num}]/section[7]/div/div[{table}]')
                    tab = ''.join(t.text)
                    tabs = tab.split('\n')
                    convert_price_next = re.sub(',','',tabs[2][:-6])
                    main.append(t.text)
                    times = jalali.Persian(f'1401{tabs[0][-6:]}').gregorian_string()
                    times_end = datetime.datetime.strptime(times,'%Y-%m-%d')
                    times_Second = times_end + datetime.timedelta(days=+1)
                    print('date----------------------')
                    print(times_Second.date())
                    print(driver.current_url)
                    room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=times_Second.date(),Day=times_end,Room_Name=elements[0],Path=driver.current_url,Night='برای 1 شب',Future=elements[5],Person_Number='1نفر',Price_Origin=tabs[1],Off='',Price_Off=int(convert_price_next))
                    his.append(f'1400{tabs[0][-6:]}')
                    # print(tabs[0][:-6])
                    timess.append(times)
            except:
                pass
        driver.back()
    return 'Eghamat ok'