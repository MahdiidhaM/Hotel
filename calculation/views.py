from typing import final
from django.shortcuts import redirect, render
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
import time as ti
import re


Hotels_List = ['الرضا','الماس 2','درویشی','هما','قصر',
                'سی نور','پردیسان','جواد']
# for _ in Hotels_List:
#     if 'هتل هما' in _:
#         print(_)



today_date = datetime.datetime.now()
tommorow_date = today_date + datetime.timedelta(days= +1)

convert_date = jalali.Gregorian(today_date.date()).persian_string('%Y/%m/%d')
convert_date_next = jalali.Gregorian(tommorow_date.date()).persian_string()
print(type(today_date))
print(convert_date_next)
def Eghamat_task(request):
    Hotels_List = ['مدینه الرضا مشهد','الماس 2 مشهد','مجلل درویشی مشهد','هما 1 مشهد','قصر طلایی مشهد',
                'سی نور مشهد','بین المللی قصر مشهد','هما 2 مشهد','پردیسان مشهد','هتل جواد']
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get(f'https://www.alibaba.ir/hotel/ir-mashhad?destination=City_5be3f68be9a116befc66701b_%D9%85%D8%B4%D9%87%D8%AF+-+%D8%A7%DB%8C%D8%B1%D8%A7%D9%86&departing={today_date.date()}&returning={tommorow_date.date()}&rooms=30')
    site,created = Site.objects.update_or_create(site_name='AliBaba')
    driver.execute_script("window.scrollTo(0, 7000)")
    ti.sleep(5)
    links = driver.find_elements(By.CLASS_NAME,'ho-available-card__title')[:30]
    print(len(links))
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
            driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[2]/span').click()
            # /html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[2]/span
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
    return HttpResponse('ok')
 
def Darvish(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Darvish_hotel = Information.objects.get(hotel__contains='درویش')
    all_hotel = Darvish_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    standard    = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='سینگل')))).order_by('Price_Off')
    toeen       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Room_Name__contains='چهار'))).order_by('Price_Off')
    three       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='سه تخته'))).order_by('Price_Off')
    four        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='چهار تخته'))).order_by('Price_Off')
    espa        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اسپا') & Q(Room_Name__contains='سه تخته')).order_by('Price_Off')
    Future        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='آینده')).order_by('Price_Off')
    room        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سه تخته') | Q(Room_Name__contains='اتاق')))).order_by('Price_Off')
    stan        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    Eco_One         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='یک') | Q(Room_Name__contains='سینگل')))).order_by('Price_Off')
    Koien         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) &  Q(Q(Room_Name__contains='کویین') | Q(Room_Name__contains='کوئین'))).order_by('Price_Off')
    one         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Room_Name__contains='سه') )).order_by('Price_Off')
    Two_Eco         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='بل') | Q(Room_Name__contains='اتاق دو تخته')))).order_by('Price_Off')
    imp         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت')))).order_by('Price_Off')
    Soit_Two          = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='فصل') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت')))).order_by('Price_Off')
    Es_Two          = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='بل') | Q(Room_Name__contains='اتاق دو تخته فصل')))).order_by('Price_Off')
    Es_Toien          = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='تويین')))).order_by('Price_Off')
    Pent_House          = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='پنت هاوس') & Q(Q(Room_Name__contains='رم') | Q(Room_Name__contains='روم')))).order_by('Price_Off')
    Es_Eco          = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='اکونومی'))).order_by('Price_Off')
    Doblex_P         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='دوبلکس') & Q(Room_Name__contains='پرزیدنتال'))).order_by('Price_Off')
    Doblex_In         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='دوبلکس') & Q(Room_Name__contains='هند'))).order_by('Price_Off')
    Doblex_Ch         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='دوبلکس') & Q(Room_Name__contains='چین'))).order_by('Price_Off')
    Doblex_Es         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='دوبلکس') & Q(Room_Name__contains='اسلام'))).order_by('Price_Off')
    Doblex_Hs         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='دوبلکس') & Q(Room_Name__contains='باستان'))).order_by('Price_Off')
    Doblex_Ar         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='دوبلکس') & Q(Room_Name__contains='عرب'))).order_by('Price_Off')
    Doblex_Eg         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='دوبلکس') & Q(Room_Name__contains='مصر'))).order_by('Price_Off')
    Pent_Spa         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اسپا') & Q(Room_Name__contains='پنت هاوس'))).order_by('Price_Off')
    final = [Doblex_Eg,Doblex_Ar,Doblex_Hs,Doblex_Es,Doblex_Ch,Doblex_In,Es_Eco,Pent_House,Es_Toien,Es_Two,Soit_Two,Eco_One,Two_Eco,Future,Pent_Spa,Koien,standard,Doblex_P,toeen,three,four,espa,room,stan,one,imp]

    ralated_hotels = Information.objects.all()

    context = {
        'final':final,'form':form,'all_hotel':all_hotel,'Darvish_hotel':Darvish_hotel,'ralated_hotels':ralated_hotels,
        'today_shamsi':first,'tommorow_shamsi':second 
        }

    if request.method == 'POST':
        print(request.POST)
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one)& Q(Second_Day=date_two))
        
        context.update({'custom':custom})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('secDoblex_Pond')})
    else:
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first))
        context.update({'custom':custom})
    return render(request,'hotels/darvish.html',context)

def Almas2(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Almas_hotel = Information.objects.get(hotel__contains='الماس 2')
    all_hotel = Almas_hotel.imagesm.all()
 
    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()
        
    almas       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='یک تخته الماس'))
    yaghoot       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='یک تخته یاقوت'))
    Berelian    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='برلیان')).order_by('Price_Off')
    Cankat    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='کانکت')).order_by('Price_Off')
    Double_Yaghoot    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='بل یاقوت')).order_by('Price_Off')
    Three_Bed    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='سه تخته')).order_by('Price_Off')
    Royal    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='هانی مون رویال') | Q(Room_Name__contains='هانی مون (جکوزی)'))).order_by('Price_Off')
    tamaddon    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اتاق دوتخته سبک معماری تمدن ') | Q(Q(Room_Name__contains='بل الماس') | Q(Room_Name__contains='اتاق دو تخته الماس')))).order_by('Price_Off')
    # Emperial    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق امپریال')).order_by('Price_Off')
    Toien     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین'))).order_by('Price_Off')
    Tailand     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='تایلند')).order_by('Price_Off')
    Turkish     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='ترکیه')).order_by('Price_Off')
    Italian     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='ایتالیا')).order_by('Price_Off')
    Africa      = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='آفریقا') | Q(Room_Name__contains='افریقا'))).order_by('Price_Off')
    Arabic      = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='عرب')).order_by('Price_Off')
    India       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='هند')).order_by('Price_Off')
    Russa       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='روسیه')).order_by('Price_Off')
    Moon        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='ماه عسل')  |Q(Room_Name__contains='دو تخته هانی مون'))).order_by('Price_Off')
    sue         = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='یکخوابه') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    Pr_Saf         = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='صفویه') & Q(Room_Name__contains='پرزیدنت')).order_by('Price_Off')
    Pr_Iran         = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='ایران باستان') & Q(Room_Name__contains='پرزیدنت')).order_by('Price_Off')
    Pr_Turkish         = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='ترکیه') & Q(Room_Name__contains='پرزیدنت')).order_by('Price_Off')
    final = [Berelian,tamaddon,Cankat,Royal,Toien,Double_Yaghoot,Three_Bed,Pr_Iran,Pr_Turkish,Tailand,Turkish,Italian,Africa,Arabic,almas,India,Russa,Moon,yaghoot,sue,Pr_Saf]

    ralated_hotels = Information.objects.all()

    context = {
        'form':form,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'Almas_hotel':Almas_hotel,
        'final':final,'today_shamsi':first,'tommorow_shamsi':second,
    }
    # الماس 2
    if request.method == 'POST':
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains=' الماس 2') & Q(Day=date_one)& Q(Second_Day=date_two))

        form = TimeForm()
        context.update({'custom':Room_Detail.objects.filter(site__hotel_name__contains=' الماس 2')})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('second')})

    return render(request,'hotels/almas.html',context)

def Homa(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Homa_hotel = Information.objects.get(hotel__contains='هما 1 ')
    all_hotel = Homa_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    Eghamat     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 1') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='اقامت')).order_by('Price_Off')
    Tooien     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 1') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='توئین')).order_by('Price_Off')
    Royal     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 1') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='رویال')).order_by('Price_Off')
    Single       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 1') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='یک نفر')|Q(Room_Name='اتاق یک تخته'))).order_by('Price_Off')
    double      = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 1') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='دو تخته') & Q(Room_Name__contains='بل'))).order_by('Price_Off')
    Senior_Two        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 1') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='دو') & Q(Q(Room_Name__contains='سینیور') | Q(Room_Name__contains='سنیور'))).order_by('Price_Off')
    Senior_Three        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 1') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains=' سه') & Q(Q(Room_Name__contains='سینیور') | Q(Room_Name__contains='سنیور'))).order_by('Price_Off')
    final = [Senior_Three,Royal,Eghamat,double,Single,Senior_Two,Tooien]
    ralated_hotels = Information.objects.all()

    context = {
        'Homa_hotel':Homa_hotel,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'final':final,'today_shamsi':first,
        'tommorow_shamsi':second,'form':form
    }
    if request.method == 'POST':
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما') & Q(Day=date_one)& Q(Second_Day=date_two))

        form = TimeForm()
        context.update({'custom':custom})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('second')})
    return render(request,'hotels/homa.html',context)


def Ghasr_Talaee(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Ghasr_tala_hotel = Information.objects.get(hotel__contains='قصر طلایی')
    all_hotel = Ghasr_tala_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    jonior      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='جونیور')).order_by('Price_Off')
    eco         = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='اکونومی')).order_by('Price_Off')
    classic     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='بل لاکچری تراس دار')).order_by('Price_Off')
    Senior     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='سنیور') | Q(Room_Name__contains='سینیور'))).order_by('Price_Off')
    Land_Scape     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='لندسکیپ')).order_by('Price_Off')
    Western     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='وسترن')).order_by('Price_Off')
    Prezident     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='پرزیدنت')).order_by('Price_Off')
    Ghagar     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='قاجاری')).order_by('Price_Off')
    Atriom      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='لاکچری') & Q(Room_Name__contains='یک'))).order_by('Price_Off')
    Lactury      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='اتاق دو تخته لاکچری') | Q(Room_Name='دو تخته دابل لاکچری') | Q(Room_Name='دبل لاکچری'))).order_by('Price_Off')
    Perances        = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='سوییت پرنسس') | Q(Room_Name='سوئیت پرنسس') | Q(Room_Name='سوئیت دو تخته پرنسس'))).order_by('Price_Off')
    Perances_Royal        = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='پرنسس رویال')).order_by('Price_Off')
    Royal        = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='رویال') & Q(Q(Room_Name__contains='چهار')  |Q(Room_Name__contains='آپارتمان'))).order_by('Price_Off')
    final = [Senior,jonior,eco,classic,Lactury,Perances,Atriom,Land_Scape,Prezident,Ghagar,Western,Perances_Royal,Royal]
    ralated_hotels = Information.objects.all()

    context = {
        'Ghasr_tala_hotel':Ghasr_tala_hotel,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'final':final,'today_shamsi':first,
        'tommorow_shamsi':second,'form':form
    }
    if request.method == 'POST':
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=date_one)& Q(Second_Day=date_two))

        form = TimeForm()
        context.update({'custom':custom})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('second')})
    return render(request,'hotels/ghasr_talaee.html',context)

# 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

from jalali_date import datetime2jalali, date2jalali
from .forms import TimeForm, User_Form
def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

def cal(request):
    Hotels = Information.objects.all()
    Hotels_list=''
    if 'star' in request.POST:
        Hotels_list = Information.objects.filter(star=int(request.POST.get('star')))
        if len(Hotels_list) > 5:
            Hotels = Information.objects.filter(star=int(request.POST.get('star')))
            Hotels_list = ''
    elif 'hotel_name' in request.POST:
        print(request.POST.get('hotel_name'))
        Hotels_list = Information.objects.filter(hotel__contains=request.POST.get('hotel_name'))
        return render(request,'index.html',{'Hotels_list':Hotels_list})
    print('--------')
    print(Hotels_list)
    l = 5
    n = []
    for x in range(2):
        c = []
        for index,i in enumerate(Hotels):
            if l-5 <= index < l:
                c.append(i)
        n.append(c)
        l+=5

    site_number = Site.objects.all().count()
    rooms = Room_Detail.objects.filter(site__hotel__site_name='Eghamat').count()
    rooms_number = Room_Detail.objects.all().count()

    context = {'Hotels':n,'hotels_number':Hotels.count(),'site_number':site_number,
    'rooms_number':rooms_number,'rooms':rooms,'Hotels_list':Hotels_list}
    
    return render(request,'index.html',context)


# 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
# https://darvishiroyal.com/media/motionslider/photo_1485637257.jpg

def Sinoor(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Sinoor_hotel = Information.objects.get(hotel__contains='سی نور')
    all_hotel = Sinoor_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()
    Prances       = Room_Detail.objects.filter(Q(site__hotel_name__contains='سی نور') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='پرنسس')).order_by('Price_Off')
    Prezident       = Room_Detail.objects.filter(Q(site__hotel_name__contains='سی نور') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='پرزیدنت')).order_by('Price_Off')
    Empreal       = Room_Detail.objects.filter(Q(site__hotel_name__contains='سی نور') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال')).order_by('Price_Off')
    Cancat       = Room_Detail.objects.filter(Q(site__hotel_name__contains='سی نور') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='کانکت')).order_by('Price_Off')
    Razavi       = Room_Detail.objects.filter(Q(site__hotel_name__contains='سی نور') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='رضوی')).order_by('Price_Off')
    Salam       = Room_Detail.objects.filter(Q(site__hotel_name__contains='سی نور') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='سلام')).order_by('Price_Off')
    Three_Beds       = Room_Detail.objects.filter(Q(site__hotel_name__contains='سی نور') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='سه تخته') & Q(Price_Off__lt=2000000)).order_by('Price_Off')
    Two_Beds        = Room_Detail.objects.filter(Q(site__hotel_name__contains='سی نور') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='دو تخته') & Q(Q(Room_Name__contains='اتاق') | Q(Room_Name__contains='بل'))).order_by('Price_Off') # Must be change
    final = [Prances,Prezident,Salam,Three_Beds,Two_Beds,Empreal,Cancat,Razavi,Razavi]
    ralated_hotels = Information.objects.all()

    context = {
        'Sinoor_hotel':Sinoor_hotel,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'final':final,'today_shamsi':first,
        'tommorow_shamsi':second,'form':form
    }
    return render(request,'hotels/sinoor.html',context)

def main(request):
    return render(request,'main.html')


def aj(request):
    print(request.POST)
    return JsonResponse({"name": request.POST}, status=200)

from django.contrib.auth import login,logout

from .forms import User_Form
def sign_up(request):
    form = User_Form()
    if request.method == 'POST':
        print('sign-------')
        print(request.POST)
        form = User_Form(request.POST)
        if form.is_valid():
            form.save()
            redirect('cal')
        else:
            form = User_Form()
    return redirect('cal')
    
def Ghasr(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Ghasr_hotel = Information.objects.get(hotel__contains='بین المللی قصر')
    all_hotel = Ghasr_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    Classic     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='بل کلاسیک')).order_by('Price_Off')
    Luctury     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='بل لاکچری')).order_by('Price_Off')
    Prances     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='پرنسس')).order_by('Price_Off')
    Hakhamanesh     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='هخامنش')).order_by('Price_Off')
    Ghagar     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='قاجار')).order_by('Price_Off')
    Cancat     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='کانکت')).order_by('Price_Off')
    Kids     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='کیدز روم')).order_by('Price_Off')
    Standard        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') | Q(Room_Name='اتاق دو تخته معمولی') | Q(Room_Name='اتاق دو تخته') | Q(Room_Name='دو تخته دابل'))).order_by('Price_Off')
    Apartment        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='آپارتمان دو خوابه') | Q(Room_Name='آپارتمان دو خوابه چهار نفره') | Q(Room_Name='آپارتمان دو خوابه چهارنفره') | Q(Room_Name=' آپارتمان دو خوابه چهار تخته '))).order_by('Price_Off')
    Prezident        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='سوئیت پرزیدنت روم دو نفره') | Q(Room_Name='سوئیت پرزیدنت دونفره')| Q(Room_Name='سوئیت پرزیدنت دو نفره') | Q(Room_Name='سوییت پرزیدنت') | Q(Room_Name='سوئیت دو تخته پرزیدنت')| Q(Room_Name='پرزیدنت'))).order_by('Price_Off')
    Emprial        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='آپارتمان') & Q(Q(Room_Name__contains='منو انتخابی') | Q(Room_Name__contains='امپریال'))).order_by('Price_Off')
    Special       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='پرزیدنت') & Q(Room_Name__contains='ویژه'))).order_by('Price_Off')
    Royal       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='پرزیدنت') & Q(Room_Name__contains='رویال'))).order_by('Price_Off')
    Luctury_Rolyal       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='رویال') & Q(Room_Name__contains='لاکچری'))).order_by('Price_Off')
    Moon      = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='بین المللی قصر') | Q(site__hotel_name__contains='قصر اینترنشنال'))& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='ماه عسل')|Q(Room_Name__contains='هانی مون'))).order_by('Price_Off')
    final = [Classic,Luctury,Prances,Hakhamanesh,Ghagar,Cancat,Kids,Standard,Apartment,Prezident,Emprial,Special,Royal,Luctury_Rolyal,Moon]
    ralated_hotels = Information.objects.all()

    context = {
        'Ghasr_hotel':Ghasr_hotel,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'final':final,'today_shamsi':first,
        'tommorow_shamsi':second,'form':form
    }
    return render(request,'hotels/ghasr.html',context)

# def Ghasr_Talaee(request):
#     form = TimeForm()
#     first = datetime.datetime.now().date()
#     second = datetime.datetime.now().date()+datetime.timedelta(days=1)
#     Ghasr_Talaee_hotel = Information.objects.get(hotel__contains='قصر طلایی')
#     all_hotel = Ghasr_Talaee_hotel.imagesm.all()

#     if request.method == 'POST':
#         first = jalali.Persian(request.POST.get('first')).gregorian_string()
#         second = jalali.Persian(request.POST.get('second')).gregorian_string()

#     tooenss     = Room_Detail.objects.filter(Q(site__hotel_name__contains='بین المللی قصر')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='اتاق سینیور دوتخته (حداقل سه شب اقامت)')|Q(Room_Name='دو تخته دابل سینیور (اقامت حداقل 3 شب یا بیشتر)'))).order_by('Price_Off')
#     double      = Room_Detail.objects.filter(Q(site__hotel_name__contains='بین المللی قصر')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='دو تخته دابل')|Q(Room_Name__contains='دو تخته دبل'))).order_by('Price_Off')
#     tooens      = Room_Detail.objects.filter(Q(site__hotel_name__contains='بین المللی قصر')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='اتاق سینیور دوتخته')|Q(Room_Name='دو تخته دابل سینیور'))).order_by('Price_Off')
#     house       = Room_Detail.objects.filter(Q(site__hotel_name__contains='بین المللی قصر')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='ساعته') & Q(Room_Name__contains='اقامت'))).order_by('Price_Off')
#     tooen       = Room_Detail.objects.filter(Q(site__hotel_name__contains='بین المللی قصر')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='دو تخته تویین')|Q(Room_Name__contains='دوتخته توئین'))).order_by('Price_Off')
#     sen         = Room_Detail.objects.filter(Q(site__hotel_name__contains='بین المللی قصر')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='سه تخته سینیور')|Q(Room_Name__contains='اتاق سینیور سه تخته (حداقل سه شب اقامت)'))).order_by('Price_Off')
#     final = [tooenss,double,tooens,house,tooen,sen]

#     context = {
#         'Ghasr_Talaee_hotel':Ghasr_Talaee_hotel,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'final':final,'today_shamsi':first,
#         'tommorow_shamsi':second,'form':form
#     }
#     return render(request,'hotels/ghast_talaee.html',context)

def Homa_2(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Homa_2_hotel = Information.objects.get(hotel__contains='هما 2')
    all_hotel = Homa_2_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    Eghamat     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='اقامت')).order_by('Price_Off')
    Tooien     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='توئین')).order_by('Price_Off')
    Special_Royal     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='رویال ویژه')).order_by('Price_Off')
    Loux       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='سوییت لوکس دو نفره') | Q(Room_Name='سوئیت یک خوابه دو تخته لوکس') | Q(Room_Name='سوئيت لوكس یکخوابه دو نفره (جکوزی دار)'))).order_by('Price_Off')
    Soite       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='سوئیت یک خوابه دو تخته استاندارد') | Q(Room_Name='سوییت یک خوابه دو نفره') | Q(Room_Name='سوئیت یکخوابه دو نفره'))).order_by('Price_Off')
    Four_Beds       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='سوييت رويال دوخوابه چهار نفره') | Q(Room_Name='سوئیت دو خوابه چهار تخته رویال استاندارد') | Q(Room_Name='سوییت رویال چهار تخته')| Q(Room_Name='سوئیت رویال چهار نفره '))).order_by('Price_Off')
    Soite_Homa       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='سوئیت دو تخته ویژه') | Q(Room_Name='سوییت ویژه دو تخته ') | Q(Room_Name='سوییت ویژه دو نفره') | Q(Room_Name='سوئیت دو نفره هما'))).order_by('Price_Off')
    Royal       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='هما') | Q(Room_Name__contains='رویال'))).order_by('Price_Off')
    Single       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='یک نفر')|Q(Room_Name__contains='اتاق یک تخته'))).order_by('Price_Off')
    double      = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١'))& Q(Day=first)& Q(Second_Day=second) & Q(Room_Name='لوکس') & Q(Room_Name__contains='هما')).order_by('Price_Off')
    Senior_Two        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='هما 2') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='یک') & Q(Q(Room_Name__contains='ویژه') | Q(Room_Name__contains='هما'))).order_by('Price_Off')
    final = [Eghamat,double,Four_Beds,Royal,Soite_Homa,Single,Senior_Two,Tooien,Special_Royal,Loux,Soite]
    ralated_hotels = Information.objects.all()

    context = {
        'Homa_2_hotel':Homa_2_hotel,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'final':final,'today_shamsi':first,
        'tommorow_shamsi':second,'form':form
    }
    return render(request,'hotels/homa_2.html',context)

def Javad(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Javad_hotel = Information.objects.get(hotel__contains='جواد')
    all_hotel = Javad_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    Houses      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='اتاق یک تخته')).order_by('Price_Off')
    Moon      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='اتاق ماه عسل (هانی مون)')).order_by('Price_Off')
    King      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='اتاق دو تخته کینگ')).order_by('Price_Off')
    Soite      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='سوئیت دو نفره')).order_by('Price_Off')
    King_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق دو تخته کینگ فولبرد (منو انتخابی)')).order_by('Price_Off')
    Soite_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='سوئیت دو نفره فولبرد (منو انتخابی)')).order_by('Price_Off')
    Franch      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='اتاق ملل سبک فرانسوی')).order_by('Price_Off')
    Marakesh      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='اتاق ملل سبک مراکشی')).order_by('Price_Off')
    Italia      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='اتاق ملل سبک ایتالیایی')).order_by('Price_Off')
    English      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='اتاق ملل سبک انگلیسی')).order_by('Price_Off')
    Moon_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق ماه عسل فولبرد (هانی مون)')).order_by('Price_Off')
    Italia_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق ملل سبک ایتالیایی فولبرد')).order_by('Price_Off')
    English_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق ملل سبک انگلیسی فولبرد')).order_by('Price_Off')
    Franch_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق ملل سبک فرانسوی فولبرد')).order_by('Price_Off')
    Three_King      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='اتاق سه تخته کینگ')).order_by('Price_Off')
    Cancat_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='سوئیت کانکت چهار نفره فولبرد (منو انتخابی)')).order_by('Price_Off')
    Four_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق چهار تخته فولبرد (سه تخته+سرویس اضافه) (منو انتخابی)')).order_by('Price_Off')
    Cancat      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name='سوئیت کانکت چهار نفره')).order_by('Price_Off')
    Three_King_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق سه تخته کینگ فولبرد (منو انتخابی)')).order_by('Price_Off')
    Four_Beds      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق چهار تخته (سه تخته+سرویس اضافه)')).order_by('Price_Off')
    One_Fool      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Day=first) & Q(Second_Day=second) & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name='فولبرد') & Q(Room_Name='یک')).order_by('Price_Off')

    final = [Houses,Moon,King,Soite,King_Fool,Soite_Fool,Franch,Marakesh,Italia,English,Moon_Fool,Italia_Fool,English_Fool,Franch_Fool,Three_King,Cancat_Fool,Four_Fool,Cancat,Three_King_Fool,Four_Beds,One_Fool]
    ralated_hotels = Information.objects.all()

    context = {
        'Javad_hotel':Javad_hotel,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'final':final,'today_shamsi':first,
        'tommorow_shamsi':second,'form':form
    }
    return render(request,'hotels/javad.html',context)

def Pardisan(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Pardisan_hotel = Information.objects.get(hotel__contains='پردیسان')
    all_hotel = Pardisan_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    Soite        = Room_Detail.objects.filter(Q(site__hotel_name__contains='پردیسان') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='لوکس') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوئيت'))).order_by('Price_Off')
    Double_Royal        = Room_Detail.objects.filter(Q(site__hotel_name__contains='پردیسان') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='بل رویال')).order_by('Price_Off')
    Tooien_Royal        = Room_Detail.objects.filter(Q(site__hotel_name__contains='پردیسان') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='ین رویال')).order_by('Price_Off')
    Tooien_Loux        = Room_Detail.objects.filter(Q(site__hotel_name__contains='پردیسان') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='ین لوکس')).order_by('Price_Off')
    Double_Loux        = Room_Detail.objects.filter(Q(site__hotel_name__contains='پردیسان') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='بل لوکس') | Q(Room_Name__contains='دوتخته لوکس'))).order_by('Price_Off')
    Three_Loux        = Room_Detail.objects.filter(Q(site__hotel_name__contains='پردیسان') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='سه تخته لوکس') | Q(Room_Name__contains='تریپل'))).order_by('Price_Off')
    Single        = Room_Detail.objects.filter(Q(site__hotel_name__contains='پردیسان') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='رویال') & Q(Q(Room_Name__contains='یک') | Q(Room_Name__contains='سینگل'))).order_by('Price_Off')
    Cancat        = Room_Detail.objects.filter(Q(site__hotel_name__contains='پردیسان') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='کانکت چهار')).order_by('Price_Off')
    Single_Loux       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='پردیسان') | Q(site__hotel_name__contains='هما ۱')| Q(site__hotel_name__contains='هما ١')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='سینگل لوکس') | Q(Room_Name='یک تخته لوکس') | Q(Room_Name='اتاق یک تخته لوکس')))


    final = [Soite,Double_Royal,Tooien_Royal,Tooien_Loux,Double_Loux,Three_Loux,Single,Cancat,Single_Loux]
    ralated_hotels = Information.objects.all()

    context = {
        'Pardisan_hotel':Pardisan_hotel,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'final':final,'today_shamsi':first,
        'tommorow_shamsi':second,'form':form
    }
    return render(request,'hotels/pardisan.html',context)

def Madineh(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Madineh_hotel = Information.objects.get(hotel__contains='رضا')
    all_hotel = Madineh_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    Single       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='اتاق یک تخته فصل') | Q(Room_Name='یک تخته استاندارد'))).order_by('Price_Off')
    Loux       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='بل لوکس فصل') | Q(Room_Name='دو تخته دابل لوکس'))).order_by('Price_Off')
    Eco       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='اتاق دبل اکونومی') | Q(Room_Name='اتاق دو تخته دبل اکونومی'))).order_by('Price_Off')
    Soite       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='سوییت یک خوابه فصل') | Q(Room_Name='سوئیت یک خوابه دو تخته لوکس') | Q(Room_Name='سوئیت یکخوابه دو نفره فصل'))).order_by('Price_Off')
    Double_Eco       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name=' اتاق دبل پلاس اکونومی') | Q(Room_Name='اتاق دو تخته دبل پلاس اکونومی'))).order_by('Price_Off')
    Double       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='بل فصل') | Q(Room_Name__contains='بل استاندارد') | Q(Room_Name='دو تخته فصل'))).order_by('Price_Off')
    Toien       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='ین فصل') | Q(Room_Name__contains='ین استاندارد') | Q(Room_Name='دو تخته فصل'))).order_by('Price_Off')
    Three_Concat       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='کانکت سه')).order_by('Price_Off')
    Four_Cancat       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='کانکت چهار')).order_by('Price_Off')
    Five_Cancat       = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='کانکت پنج')).order_by('Price_Off')
    Medrit     = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='مدریت')).order_by('Price_Off')
    Toien_Plas     = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='ین پلاس فصل')).order_by('Price_Off')
    Royal     = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='رویال')).order_by('Price_Off')
    Senior_Two        = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا')  & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='آپارتمان') & Q(Q(Room_Name__contains='فصل') | Q(Room_Name__contains='VIP'))).order_by('Price_Off')
    Apartment        = Room_Detail.objects.filter(Q(site__hotel_name__contains='رضا')  & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='آپارتمان') & Q(Room_Name__contains='اکونومی')).order_by('Price_Off')
    final = [Single,Loux,Eco,Soite,Double_Eco,Double,Toien,Three_Concat,Four_Cancat,Five_Cancat,Medrit,Toien_Plas,Royal,Senior_Two,Apartment]

    ralated_hotels = Information.objects.all()
    context = {
        'Madineh_hotel':Madineh_hotel,'all_hotel':all_hotel,'ralated_hotels':ralated_hotels,'final':final,'today_shamsi':first,
        'tommorow_shamsi':second,'form':form
    }
    if request.method == 'POST':
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما') & Q(Day=date_one)& Q(Second_Day=date_two))

        form = TimeForm()
        context.update({'custom':custom})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('second')})
    return render(request,'hotels/madineh.html',context)