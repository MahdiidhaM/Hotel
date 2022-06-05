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


Hotels_List = ['هتل مدینه الرضا مشهد','هتل الماس 2 مشهد','هتل مجلل درویشی مشهد','هتل هما 1 مشهد','هتل قصر طلایی مشهد',
                'هتل سی نور مشهد','هتل بین المللی قصر مشهد','هتل هما 2 مشهد','هتل پردیسان مشهد','هتل جواد']
# for _ in Hotels_List:
#     if 'هتل هما' in _:
#         print(_)



today_date = datetime.datetime.now()
tommorow_date = today_date + datetime.timedelta(days= +1)
def Eghamat_task(request):
    driver = webdriver.Chrome('calculation/chromedriver')
    driver.get('https://www.eghamat24.com/MashhadHotels.html')
    Eghamat,created = Site.objects.update_or_create(site_name='Eghamat')
    for cli in range(1,30):
        new =  driver.find_element(By.XPATH,f'/html/body/main/div[3]/div/div/section/div/article[1]/a[{cli}]/div[2]/div/h4')
        # /html/body/main/div[3]/div/div/section/div/article[1]/a[1]/div[2]/div/h4

        for _ in Hotels_List:
            if new.text in _ :
                print('2------------')
                print(new.text)
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
                        room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=l_next_second.date(),Day=l_next.date(),Path=driver.current_url,Room_Name=elements[0],Night='برای 1 شب',Extra_Person=elements[-7],Person_Number=num_of,Price_Origin=elements[-5],Bed_Type=elements[-8][9:],Price_Off=int(convert_price))
                    except:
                        room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=l_next_second.date(),Day=l_next.date(),Path=driver.current_url,Room_Name=elements[0],Night='برای 1 شب',Extra_Person=elements[-5],Person_Number=num_of,Price_Origin=elements[-4],Bed_Type=elements[-6][9:],Price_Off=elements[-3])
                    driver.find_elements(By.CLASS_NAME,'view_other_room_price')[num-1].click()
                    for table in range(1,6):
                        t = driver.find_element(By.XPATH,f'//*[@id="hotel_reservation"]/div/div/div[2]/div[1]/div[2]/div[{num}]/section[7]/div/div[{table}]')
                        tab = ''.join(t.text)
                        tabs = tab.split('\n')
                        times = jalali.Persian(f'1401{tabs[0][-6:]}').gregorian_string()
                        times_end = datetime.datetime.strptime(times,'%Y-%m-%d')
                        times_Second = times_end + datetime.timedelta(days=+1)
                        try:
                            convert_price_next = re.sub(',','',tabs[2][:-6])
                            room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=times_Second.date(),Day=times_end,Room_Name=elements[0],Path=driver.current_url,Night='برای 1 شب',Extra_Person=elements[-7],Person_Number=num_of,Price_Origin=tabs[1],Bed_Type=elements[-8][9:],Price_Off=int(convert_price_next))
                        except:
                            room_team,created = Room_Detail.objects.update_or_create(site=hotel_eghamat,Second_Day=times_Second.date(),Day=times_end,Room_Name=elements[0],Path=driver.current_url,Night='برای 1 شب',Extra_Person=elements[-5],Person_Number=num_of,Bed_Type=elements[-6][9:],Price_Off=tabs[1])
                driver.back()
                break
    ti.sleep(500)
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

    three_rooms = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='سه تخته') | Q(Room_Name__contains='سه نفره')))).order_by('Price_Off')
    four_rooms  = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='چهار تخته') | Q(Room_Name__contains='چهار نفره')))).order_by('Price_Off')
    standard    = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره')| Q(Room_Name__contains='سینگل')))).order_by('Price_Off')
    Darvish     = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='دبل') | Q(Room_Name__contains='دابل')))).order_by('Price_Off')
    session     = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Q(Room_Name__contains='سوئیت')| Q(Room_Name__contains='سوییت')) & Q(Room_Name__contains='استاندارد'))).order_by('Price_Off')
    toeen       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    three       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='سه تخته'))).order_by('Price_Off')
    four        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='چهار تخته'))).order_by('Price_Off')
    espa        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اسپا')).order_by('Price_Off')
    room        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سه تخته') | Q(Room_Name__contains='اتاق')))).order_by('Price_Off')
    stan        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    one         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره')| Q(Room_Name__contains='سینگل')))).order_by('Price_Off')
    imp         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت')))).order_by('Price_Off')
    Es          = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='دبل') | Q(Room_Name__contains='دابل')))).order_by('Price_Off')
    final = [three_rooms,four_rooms,standard,Darvish,session,toeen,three,four,espa,room,stan,one,imp,Es]

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
        
        # form = TimeForm()
        context.update({'custom':custom})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('second')})
    else:
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=first))
        context.update({'custom':custom})
    return render(request,'darvish.html',context)

def Almas2(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Almas_hotel = Information.objects.get(hotel__contains='الماس 2')
    all_hotel = Almas_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()
        
    Berelian    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='برلیان'))).order_by('Price_Off')
    tamaddon    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name__contains='سبک معماری تمدن') & Q(Q(Room_Name__contains='اتاق دوتخته') | Q(Room_Name__contains='اتاق دو تخته')))).order_by('Price_Off')
    # Emperial    = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='اتاق امپریال')).order_by('Price_Off')
    Tailand     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='تایلند')).order_by('Price_Off')
    Turkish     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='ترکیه')).order_by('Price_Off')
    Italian     = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='ایتالیا')).order_by('Price_Off')
    Africa      = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='آفریقا')).order_by('Price_Off')
    Arabic      = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='عرب')).order_by('Price_Off')
    almas       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Q(Room_Name='اتاق یک تخته الماس')|Q(Room_Name='یک تخته الماس')))
    India       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='هند')).order_by('Price_Off')
    Russa       = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='امپریال') & Q(Room_Name__contains='روسیه')).order_by('Price_Off')
    turk        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='ترکیه') & Q(Q(Room_Name__contains='سوئیت')  |Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    iran        = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='ایران باستان') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    sue         = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='یک خوابه') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    saf         = Room_Detail.objects.filter(Q(Q(site__hotel_name__contains='الماس 2') | Q(site__hotel_name__contains='الماس ۲')) & Q(Day=first) & Q(Second_Day=second) & Q(Room_Name__contains='صفویه') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    final = [Berelian,tamaddon,Tailand,Turkish,Italian,Africa,Arabic,almas,India,Russa,turk,iran,sue,saf]

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

    return render(request,'almas.html',context)

def Homa(request):
    form = TimeForm()
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Homa_hotel = Information.objects.get(hotel__contains='هما')
    all_hotel = Homa_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    tooenss     = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='اتاق سینیور دوتخته (حداقل سه شب اقامت)')|Q(Room_Name='دو تخته دابل سینیور (اقامت حداقل 3 شب یا بیشتر)'))).order_by('Price_Off')
    double      = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='دو تخته دابل')|Q(Room_Name__contains='دو تخته دبل'))).order_by('Price_Off')
    tooens      = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='اتاق سینیور دوتخته')|Q(Room_Name='دو تخته دابل سینیور'))).order_by('Price_Off')
    house       = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='ساعته') & Q(Room_Name__contains='اقامت'))).order_by('Price_Off')
    tooen       = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name='دو تخته تویین')|Q(Room_Name__contains='دوتخته توئین'))).order_by('Price_Off')
    sen         = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما')& Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='سه تخته سینیور')|Q(Room_Name__contains='اتاق سینیور سه تخته (حداقل سه شب اقامت)'))).order_by('Price_Off')
    final = [tooenss,double,tooens,house,tooen,sen]

    context = {
        'Homa_hotel':Homa_hotel,'all_hotel':all_hotel,'final':final,'today_shamsi':first,
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
    return render(request,'homa.html',context)

def Javad(request):
    
    houses      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Q(Room_Name__contains='یک تخته رویال') | Q(Room_Name='اتاق یک تخته'))).order_by('Price_Off')
    king        = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Q(Room_Name__contains='دو تخته') & Q(Room_Name__contains='کینگ'))).order_by('Price_Off')

    context = {
        'houses':houses,'king':king
    }
    return render(request,'javad.html',context)

def Ghasr_Tala(request):
    first = datetime.datetime.now().date()
    second = datetime.datetime.now().date()+datetime.timedelta(days=1)
    Ghasr_tala_hotel = Information.objects.get(hotel__contains='قصر طلایی')
    all_hotel = Ghasr_tala_hotel.imagesm.all()

    if request.method == 'POST':
        first = jalali.Persian(request.POST.get('first')).gregorian_string()
        second = jalali.Persian(request.POST.get('second')).gregorian_string()

    lak         = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='یک تخته لاکچری'))).order_by('Price_Off')
    jonior      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='جونیور')).order_by('Price_Off')
    eco         = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='یک تخته اکونومی')).order_by('Price_Off')
    classic     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='یک تخته لاکچری')).order_by('Price_Off')
    Atriom      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='دو تخته') & Q(Room_Name__contains='آتریوم'))).order_by('Price_Off')
    bed         = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='دو تخته') & Q(Room_Name__contains='لاکچری'))).order_by('Price_Off')
    land        = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='لندسکیپ')).order_by('Price_Off')
    vestern     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='وسترن')).order_by('Price_Off')
    roy         = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='پرنسس رویال')).order_by('Price_Off')
    senior      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='سنیور')).order_by('Price_Off')
    prances     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Q(Room_Name__contains='پرنسس') & Q(Room_Name__contains='سوئیت'))).order_by('Price_Off')
    cancat      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='کانکت')).order_by('Price_Off')
    presedent   = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=first)& Q(Second_Day=second) & Q(Room_Name__contains='پرزیدنت')).order_by('Price_Off')
    final = [lak,jonior,eco,classic,Atriom,bed,land,vestern,roy,senior,prances,cancat,presedent]

    context = {
        'Ghasr_t_hotel':Ghasr_tala_hotel,'all_hotel':all_hotel,'final':final,'today_shamsi':first,
        'tommorow_shamsi':second,
    }
    if request.method == 'POST':
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Day=date_one)& Q(Second_Day=date_two))

        form = TimeForm()
        context.update({'custom':custom})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('second')})
    return render(request,'ghasr_tala.html',context)

# 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

from jalali_date import datetime2jalali, date2jalali
from .forms import TimeForm, User_Form
def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

def cal(request):
    Hotels = Information.objects.all()
    if request.method == 'POST':
        Hotels = Information.objects.filter(star=int(request.POST.get('star')))
        
    l = 2
    n = []
    for x in range(2):
        print(l)
        c = []
        for index,i in enumerate(Hotels):
            print(index)
            if l-2 <= index < l:
                c.append(i)
        n.append(c)
        l*=2

    site_number = Site.objects.all().count()
    rooms = Room_Detail.objects.filter(site__hotel__site_name='Eghamat').count()
    rooms_number = Room_Detail.objects.all().count()

    context = {'Hotels':n,'hotels_number':Hotels.count(),'site_number':site_number,
    'rooms_number':rooms_number,'rooms':rooms}
    
    return render(request,'index.html',context)


# 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
# https://darvishiroyal.com/media/motionslider/photo_1485637257.jpg

def main(request):
    return render(request,'main.html')


from django.contrib.auth import login,logout

from .forms import User_Form
def sign_up(request):
    form = User_Form()
    if request.method == 'POST':
        form = User_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'cal.html')
        else:
            form = User_Form()
            return redirect('cal')
    return redirect('cal')
    

