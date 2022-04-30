from django.shortcuts import render
from .models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import datetime 
from django.http import HttpResponse, JsonResponse
# Create your views here.
from selenium import webdriver
def Snap(request):
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get('https://www.snapptrip.com/%D8%B1%D8%B2%D8%B1%D9%88-%D9%87%D8%AA%D9%84/%D9%85%D8%B4%D9%87%D8%AF?gclid=CjwKCAiAgbiQBhAHEiwAuQ6Bkkj7yFFiBg8j09tkzZbeQM2WHDbO9liJMIeOz80BmDdXVUPlRsLRThoCw_MQAvD_BwE&price_from=0&price_to=0&page=1')
from . import jalali
today_date = datetime.datetime.now()
tommorow_date = today_date + datetime.timedelta(days= +1)
l = datetime.datetime.now() + datetime.timedelta(days= +1)
b = jalali.Gregorian(l.date()).persian_string()
import time as ti
def Snap_task(request):
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
                    # /html/body/div[1]/main/div/div[1]/div[1]/div[4]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[1]/span
                    # /html/body/div[1]/main/div/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span
                    print('----------')
                    print(conj)
                    # print(index)
                    print(sn[1])
                    print(sn[2])
                    print(sn[3])
                    # print(sn[4])
                    # print(sn[])
                    print(sn)
                    print('----------')
                    room_team_snap,created = Room_Detail.objects.update_or_create(site=hotel_snap,Day=l.date(),Second_Day=l_next.date(),Path=path,Room_Name=conj,Night=sn[0],Future='',Person_Number=sn[3],Price_Origin='',Off='',Price_Off=sn[1][:-6])
        except:
            pass
    return HttpResponse('con.text')

def price(request):
    get_all = Room_Detail.objects.all().order_by('Price_Off')
    # for ra in get_all:
    #     print(ra.Price_Off)
    one = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره'))))
    king = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Q(Room_Name__contains='دو تخته') & Q(Room_Name__contains='کینگ')))
    lak = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Q(Room_Name__contains='یک تخته لاکچری')))
    stan = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    standard = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره'))))
    return render(request,'price.html',{'one':one,'king':king,'lak':lak,'stan':stan,'standard':standard,'get_all':get_all})

def Darvish(request):
    one         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره')))).order_by('Price_Off')
    three_rooms = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='سه تخته')  |Q(Room_Name__contains='سه نفره')))).order_by('Price_Off')
    four_rooms  = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='چهارتخته')  |Q(Room_Name__contains='چهار نفره')))).order_by('Price_Off')
    toeen       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    Darvish     = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='دبل') | Q(Room_Name__contains='دابل')))).order_by('Price_Off')
    stan        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    standard    = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره')))).order_by('Price_Off')
    Es          = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='دبل') | Q(Room_Name__contains='دابل')))).order_by('Price_Off')
    three       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='سه تخته'))).order_by('Price_Off')
    four        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='چهار تخته'))).order_by('Price_Off')
    session     = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='سوئیت') & Q(Room_Name__contains='فصل'))).order_by('Price_Off')
    espa        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Room_Name__contains='اسپا')).order_by('Price_Off')
    room        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سه تخته') | Q(Room_Name__contains='اتاق')))).order_by('Price_Off')
    imp         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت')))).order_by('Price_Off')

    context = {'one':one,'three_rooms':three_rooms,'four_rooms':four_rooms,'toeen':toeen,'Darvish':Darvish,'stan':stan,'standard':standard,'Es':Es,'three':three,'four':four,'session':session,
    'espa':espa,'room':room,'imp':imp
    }

    return render(request,'darvish.html',context)

def Almas(request):
    almas       = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name='اتاق یک تخته الماس'))
    sue         = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='یک خوابه') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    saf         = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='صفویه') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    turk        = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='ترکیه') & Q(Q(Room_Name__contains='سوئیت')  |Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    iran        = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='ایران باستان') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    Berelian    = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Q(Room_Name__contains='اتاق دو تخته برلیان') | Q(Room_Name__contains='اتاق دوتخته برلیان'))).order_by('Price_Off')
    Emperial    = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال')).order_by('Price_Off')
    India       = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='هند')).order_by('Price_Off')
    Africa      = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='آفریقا')).order_by('Price_Off')
    Tailand     = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='تایلند')).order_by('Price_Off')
    Russa       = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='روسیه')).order_by('Price_Off')
    Turkish     = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='ترکیه')).order_by('Price_Off')
    Italian     = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='ایتالیا')).order_by('Price_Off')
    Arabic      = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='عرب')).order_by('Price_Off')
    tamaddon    = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Q(Room_Name__contains='سبک معماری تمدن') & Q(Q(Room_Name__contains='اتاق دوتخته') | Q(Room_Name__contains='اتاق دو تخته')))).order_by('Price_Off')
    context = {
        'almas':almas,'sue':sue,'saf':saf,'turk':turk,'iran':iran,'Berelian':Berelian,'Emperial':Emperial,'India':India,'Africa':Africa,'Tailand':Tailand,'Russa':Russa,'Turkish':Turkish,'Italian':Italian,
        'Arabic':Arabic,'tamaddon':tamaddon
    }
    return render(request,'almas.html',context)