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
from selenium.webdriver.firefox.options import Options
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
# l = datetime.datetime.now() + datetime.timedelta(days= +1)
# b = jalali.Gregorian(l.date()).persian_string()
import time as ti

@shared_task()
def test_task():
    print('teeeeeeeeeeeeeeeeeeeeeeeeeeeeeest')
    Site.objects.create(site_name='teeeeest')
@shared_task()
def Snap_task():
    Hotels_List = ['هتل مدینه الرضا مشهد','هتل الماس 2 مشهد','هتل مجلل درویشی مشهد','هتل هما 1 مشهد','هتل قصر طلایی مشهد',
                'هتل سی نور مشهد','هتل بین المللی قصر مشهد','هتل هما 2 مشهد','هتل پردیسان مشهد','هتل جواد']
    SnapTrip = 'SnapTrip'
    Site.objects.filter(site_name=SnapTrip).delete()
    driver = webdriver.Chrome('calculation/chromedriver')
    # https://www.snapptrip.com/%D8%B1%D8%B2%D8%B1%D9%88-%D9%87%D8%AA%D9%84/%D9%85%D8%B4%D9%87%D8%AF?gclid=CjwKCAiAgbiQBhAHEiwAuQ6Bkkj7yFFiBg8j09tkzZbeQM2WHDbO9liJMIeOz80BmDdXVUPlRsLRThoCw_MQAvD_BwE&price_from=0&price_to=0&page=1
    driver.get('https://www.snapptrip.com/%D8%B1%D8%B2%D8%B1%D9%88-%D9%87%D8%AA%D9%84/%D9%85%D8%B4%D9%87%D8%AF?page=1&stars=5&order_by=max_percent&utm_source=google&utm_medium=cpc&utm_campaign=10819688532&utm_term=snapptrip&utm_content=106926085656&gclid=Cj0KCQjw-daUBhCIARIsALbkjSZve6b8niGZb1RdjkC4C1VedEaE6h4hxvwzzeEyxUrTuAEmZeLl4-kaAggXEALw_wcB')
    Snap,created = Site.objects.update_or_create(site_name=SnapTrip)
    details = driver.find_elements(By.ID,'resultpage-hotelcard-hotelname')
    items_trip = []
    num = 0
    # for snap trip site
    for item in details:
        for _ in Hotels_List:
            driver.switch_to.window(driver.window_handles[0])
            if item.text in _:
                num+=1
                item.click()
                driver.switch_to.window(driver.window_handles[num])

                h = driver.find_element(By.TAG_NAME,'h1')
                hotel_snap,created = Hotel.objects.update_or_create(hotel=Snap,hotel_name=f'{h.text} SnapTrip')
                for datea in range(20):
                    path = driver.current_url
                    l = datetime.datetime.now() + datetime.timedelta(days=datea)
                    l_next = datetime.datetime.now() + datetime.timedelta(days=datea+1)
                    bb1 = jalali.Gregorian(l.date()).persian_string()
                    numb1 = bb1.split('-')[-1]
                    driver.find_element(By.CLASS_NAME,'date-peacker').click()
                    calender = driver.find_elements(By.XPATH,f"//td[text()='{numb1}']")
                    if calender[0].get_attribute('class') == 'off disabled':
                        em = 1
                    else:
                        em = 0
                    calender[em].click()
                    driver.find_element(By.CLASS_NAME,'search-btn').click()
                    ti.sleep(3)
                    day_1 = driver.find_elements(By.CLASS_NAME,'form-control')[1].get_attribute('value')
                    day_2 = driver.find_elements(By.CLASS_NAME,'form-control')[2].get_attribute('value')
                    convert_day_1 = jalali.Persian(day_1).gregorian_string()
                    convert_day_2 = jalali.Persian(day_2).gregorian_string()
                    convert_price = driver.find_elements(By.CLASS_NAME,'span-prices')
                    try:
                        if driver.find_elements(By.CLASS_NAME,'price')[1].text == '':
                            multi = 2                    
                        else:
                            multi = 1
                    except:
                        pass
                    for index,t in enumerate(driver.find_elements(By.CLASS_NAME,'room-item')):
                        snap_room_name = driver.find_elements(By.CLASS_NAME,'text-ellipsis')[index].text
                        snap_price = driver.find_elements(By.CLASS_NAME,'price')[index*multi].text
                        convert_price = re.sub(',','',snap_price)
                        room_team_snap,created = Room_Detail.objects.update_or_create(site=hotel_snap,Day=convert_day_1,Second_Day=convert_day_2,Path=path,Room_Name=snap_room_name,Price_Off=int(convert_price))
    return 'ok'

today_date = datetime.datetime.now()
tommorow_date = today_date + datetime.timedelta(days= +1)

@shared_task()
def Ali_task():
    AliBaba = 'AliBaba'
    Site.objects.filter(site_name=AliBaba).delete()
    Hotels_List = ['مدینه الرضا مشهد','الماس 2 مشهد','مجلل درویشی مشهد','هما 1 مشهد','قصر طلایی مشهد',
                'سی نور مشهد','بین المللی قصر مشهد','هما 2 مشهد','پردیسان مشهد','هتل جواد']
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get(f'https://www.alibaba.ir/hotel/ir-mashhad?destination=City_5be3f68be9a116befc66701b_%D9%85%D8%B4%D9%87%D8%AF+-+%D8%A7%DB%8C%D8%B1%D8%A7%D9%86&departing={today_date.date()}&returning={tommorow_date.date()}&rooms=30')
    site,created = Site.objects.update_or_create(site_name=AliBaba)
    driver.execute_script("window.scrollTo(0, 7000)")
    ti.sleep(5)
    links = driver.find_elements(By.CLASS_NAME,'ho-available-card__title')[:30]
    for link in links:
        
        for hotel in Hotels_List:
            if link.text in hotel:
                click_link = link.find_element(By.XPATH,'.//*')
                driver.execute_script("arguments[0].click();", click_link)
        
    page = len(driver.window_handles)
    
    for i in range(2,page): # page ----------
        driver.switch_to.window(driver.window_handles[i])
        
        title = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/main/div/div[2]/div/h1')
        hotel,created = Hotel.objects.update_or_create(hotel=site,hotel_name=title.text)
        day_range = 20
        for day in range(day_range):
            ali_path = driver.current_url
            l_next = datetime.datetime.now() + datetime.timedelta(days=day)
            l_next_second = datetime.datetime.now() + datetime.timedelta(days=day+1)
            bb2 = jalali.Gregorian(l_next.date()).persian_string()
            bb3 = jalali.Gregorian(l_next_second.date()).persian_string()
            numb2 = int(bb2.split('-')[-1])
            numb3 = int(bb3.split('-')[-1])
            span = driver.find_element(By.CSS_SELECTOR,'.datepicker-text span')
            driver.execute_script("arguments[0].click();", span)
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
                    room_team,created = Room_Detail.objects.update_or_create(site=hotel,Day=convert_date,Second_Day=convert_date_next,Path=ali_path,Room_Name=mar.text,Price_Off=int(convert_price)/10)
            except:
                pass
            ti.sleep(5)
    return 'ali ok'

Hotels_List = ['الرضا','الماس 2','درویشی','هما','هما 2 ','بین المللی قصر','قصر طلایی','سی نور','پردیسان','جواد']
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
@shared_task()
def Eghamat_task():



    
    options = Options()
    options.add_argument("--headless")
    options.binary_location = r'/usr/bin/google-chrome-stable'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options = options)
    driver.get('https://www.eghamat24.com/MashhadHotels.html')





    egh = 'Eghamat'
    Site.objects.filter(site_name=egh).delete()
    Eghamat,created = Site.objects.get_or_create(site_name=egh)
    #     # new =  driver.find_element(By.XPATH,f'/html/body/main/div[3]/div/div/section/div/article[1]/a[{cli}]')
    # for ho in Hotels_List:
    #     for cli in driver.find_elements(By.CLASS_NAME,'hotel-name-box')[:40]:
        
    #             if ho in cli.text:
    #                 cli.click()
    #                 cous = 0
    #                 for cou in driver.find_elements(By.CLASS_NAME,'icon-shopping-cart'):
    #                     cous+=1
    #                 hotel_title = driver.find_element(By.CLASS_NAME,'hotel_name')
    #                 hotel_eghamat,created = Hotel.objects.update_or_create(hotel=Eghamat,hotel_name=f'{hotel_title.text} Eghamat')
                    
    #                 for num in range(1,cous-4):
    #                     try:
    #                         x = driver.find_elements(By.CSS_SELECTOR,'.tr')[num]
    #                         pesrons = driver.find_elements(By.CLASS_NAME,'room-capacity')[num-1]
    #                     except:
    #                         pass

    #                     num_of = 0
    #                     for inj in pesrons.find_elements(By.CLASS_NAME,'icon-man'):
    #                         num_of+=1

    #                     prices = x.find_element(By.CLASS_NAME,'hotel_room_price')
    #                     prices_list = ''.join(prices.text)
    #                     prices_final = prices_list.split('\n')
    #                     prices_final_next = re.sub(',','',prices_final[1])

    #                     if 'تومان' in prices_final[1]:
    #                         prices_final_next = re.sub(',','',prices_final[1][:-6])
                            
    #                     info = x.find_element(By.CLASS_NAME,'room-info')
    #                     info_list = ''.join(info.text)
    #                     info_final = info_list.split('\n')
    #                     driver.find_elements(By.CLASS_NAME,'view_other_room_price')[num-1].click()
    #                     if 'میهمان خارجی' in info_final[0]:
    #                         continue
    #                     for table in x.find_elements(By.CLASS_NAME,'hotel_calender_item'):
    #                         # t = driver.find_element(By.XPATH,f'//*[@id="hotel_reservation"]/div/div/div[2]/div[1]/div[2]/div[{num}]/section[7]/div/div[{table}]')
    #                                                 #   /html/body/main/div[4]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/section[7]/div/div[1]
    #                                                 # /html/body/main/div[4]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/section[7]/div/div[2]
    #                                                 # /html/body/main/div[4]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/section[7]/div/div[2]
    #                         tab = ''.join(table.text)
    #                         tabs = tab.split('\n')
    #                         times = jalali.Persian(f'1401{tabs[0][-6:]}').gregorian_string()
    #                         times_end = datetime.datetime.strptime(times,'%Y-%m-%d')
    #                         times_Second = times_end + datetime.timedelta(days=+1)
    #                         try:
    #                             convert_price_next = re.sub(',','',tabs[2][:-6])
    #                             room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=times_Second.date(),Day=times_end,Room_Name=info_final[0],Path=driver.current_url,Night='برای 1 شب',Extra_Person=info_final[-2],Person_Number=num_of,Price_Origin=tabs[1],Bed_Type=info_final[-1][9:],Price_Off=int(convert_price_next))
    #                         except:
    #                             room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=times_Second.date(),Day=times_end,Room_Name=info_final[0],Path=driver.current_url,Night='برای 1 شب',Extra_Person=info_final[-2],Person_Number=num_of,Price_Origin=tabs[1],Bed_Type=info_final[-1][9:],Price_Off=tabs[1])
    #                 driver.back()
    #                 break
    return 'Eghamat ok'

@shared_task
def Eli_task():
    chromeOptions = webdriver.ChromeOptions() 
    chromeOptions.add_argument("--remote-debugging-port=9222")
    EliGasht = 'EliGasht'
    Site.objects.filter(site_name='EliGasht').delete()
    EliGasht,created = Site.objects.update_or_create(site_name='EliGasht')
    for _ in range(19):
        driver = webdriver.Chrome('calculation/chromedriver')    
        l_next = datetime.datetime.now() + datetime.timedelta(days=_)
        l_next_second = datetime.datetime.now() + datetime.timedelta(days=_+1)
        driver.get(f'https://www.eligasht.com/hotels/search?Destination=c349&CheckIn={l_next.date()}&CheckOut={l_next_second.date()}&Rooms=2,0,0,0,0,0')
        ti.sleep(5)

        for num in range(1,20):
            link = driver.find_element(By.XPATH,f'/html/body/main/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/ul/li[{num}]/form/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]')
            try:
                content = link.text
                for hotel in Hotels_List:
                    if hotel in content:
                        link.click()
            except:
                pass
                driver.switch_to.window(driver.window_handles[0])
        pages = len(driver.window_handles)
        
        for i in range(1,pages):
            driver.switch_to.window(driver.window_handles[i])
            hotel_name = driver.find_element(By.CSS_SELECTOR,'h1')
            try:
                driver.find_element(By.CLASS_NAME,'more-detail-room').click()
            except:
                pass
            hotel_ali,created = Hotel.objects.get_or_create(hotel=EliGasht,hotel_name=f'{hotel_name.text} EliGasht')
            try:
                for num_eli in driver.find_elements(By.CLASS_NAME,'room-row'):
                    price = num_eli.find_element(By.CLASS_NAME,'room-price-val')
                    t = ''.join(num_eli.text)
                    items = t.split('\n')
                    convert_price = re.sub(',','',price.text)
                    room_team,created = Room_Detail.objects.update_or_create(site=hotel_ali,Day=l_next.date(),Second_Day=l_next_second.date(),Path=driver.current_url,Room_Name=items[0],Price_Off=convert_price)
            except:
                pass
    return 'Eli Done'

@shared_task
def Jainjas():
    Jainjas = 'Jainjas'
    chromeOptions = webdriver.ChromeOptions() 
    chromeOptions.add_argument("--remote-debugging-port=9222")
    Site.objects.filter(site_name='Jainjas').delete()
    Jainjas,created = Site.objects.get_or_create(site_name='Jainjas')
    for day in range(19):
        l_next = datetime.datetime.now() + datetime.timedelta(days=day)
        l_next_second = datetime.datetime.now() + datetime.timedelta(days=day+1)
        convert_date = jalali.Gregorian(l_next.date()).persian_string().split('-')
        convert_date_next = jalali.Gregorian(l_next_second.date()).persian_string().split('-')
        driver = webdriver.Chrome('calculation/chromedriver')
        driver.get(f'https://jainjas.com/mashhad?from={convert_date[0]}/{convert_date[1]}/{convert_date[2]}&to={convert_date_next[0]}/{convert_date_next[1]}/{convert_date_next[2]}&searched=true&IsCertain=false&star=0')
        ti.sleep(5)
        driver.find_element(By.ID,'loadmoreplaces').click()

        for link in driver.find_elements(By.CLASS_NAME,'card__title')[:35]:
            for hotel in  Hotels_List:
                if hotel in link.text:
                    child_link = link.find_element(By.XPATH,'.//*')
                    driver.execute_script("arguments[0].click();", child_link)
        try:
            pages = len(driver.window_handles)
        except:
            pages = 8
        for page in range(1,pages):
            driver.switch_to.window(driver.window_handles[page])
            hotel_name = driver.find_element(By.CSS_SELECTOR,'h1')
            hotel_ali,created = Hotel.objects.get_or_create(hotel=Jainjas,hotel_name=f'{hotel_name.text} Jainjas')

            try:
                for hotel in driver.find_elements(By.CLASS_NAME,'roomBox'):
                    price = hotel.find_element(By.CLASS_NAME,'ji-price__sale')
                    name = hotel.find_element(By.CSS_SELECTOR,'.roomName span')
                    convert_price = re.sub(',','',price.text[:-6])
                    room_team,created = Room_Detail.objects.update_or_create(site=hotel_ali,Day=l_next.date(),Second_Day=l_next_second.date(),Path=driver.current_url,Room_Name=name.text,Price_Off=int(convert_price))
            except:
                pass
    return 'Jainjas Done'