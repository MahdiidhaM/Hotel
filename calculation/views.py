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
import time as ti
import re
today_date = datetime.datetime.now()
tommorow_date = today_date + datetime.timedelta(days= +1)
def Eghamat_task(request):
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
    return HttpResponse('ok')
 
def Darvish(request):
    form = TimeForm()
    today = datetime.datetime.now().date()
    Darvish_hotel = Information.objects.get(hotel__contains='درویش')
    all_hotel = Darvish_hotel.imagesm.all()
    if request.method == 'POST':
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
    else:
        date_one = today
    three_rooms = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='سه تخته') | Q(Room_Name__contains='سه نفره')))).order_by('Price_Off')
    four_rooms  = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='چهار تخته') | Q(Room_Name__contains='چهار نفره')))).order_by('Price_Off')
    standard    = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره')| Q(Room_Name__contains='سینگل')))).order_by('Price_Off')
    Darvish     = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='دبل') | Q(Room_Name__contains='دابل')))).order_by('Price_Off')
    session     = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Q(Room_Name__contains='سوئیت')| Q(Room_Name__contains='سوییت')) & Q(Room_Name__contains='استاندارد'))).order_by('Price_Off')
    toeen       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    three       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='سه تخته'))).order_by('Price_Off')
    four        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='چهار تخته'))).order_by('Price_Off')
    espa        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Room_Name__contains='اسپا')).order_by('Price_Off')
    room        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سه تخته') | Q(Room_Name__contains='اتاق')))).order_by('Price_Off')
    stan        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    one         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره')| Q(Room_Name__contains='سینگل')))).order_by('Price_Off')
    imp         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت')))).order_by('Price_Off')
    Es          = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one) & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='دبل') | Q(Room_Name__contains='دابل')))).order_by('Price_Off')
    final = [three_rooms,four_rooms,standard,Darvish,session,toeen,three,four,espa,room,stan,one,imp,Es]
    ralated_hotels = Information.objects.all()
    context = {
        'final':final,'form':form,'all_hotel':all_hotel,'Darvish_hotel':Darvish_hotel,'ralated_hotels':ralated_hotels
    }
    if request.method == 'POST':
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one)& Q(Second_Day=date_two))
        
        # form = TimeForm()
        context.update({'custom':custom})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('second')})
    else:
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=today))
        context.update({'custom':custom})
    return render(request,'darvish.html',context)

def Almas(request):
    form = TimeForm()
    Berelian    = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Q(Room_Name__contains='اتاق دو تخته برلیان') | Q(Room_Name__contains='اتاق دوتخته برلیان'))).order_by('Price_Off')
    tamaddon    = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Q(Room_Name__contains='سبک معماری تمدن') & Q(Q(Room_Name__contains='اتاق دوتخته') | Q(Room_Name__contains='اتاق دو تخته')))).order_by('Price_Off')
    Emperial    = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال')).order_by('Price_Off')
    Tailand     = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='تایلند')).order_by('Price_Off')
    Turkish     = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='ترکیه')).order_by('Price_Off')
    Italian     = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='ایتالیا')).order_by('Price_Off')
    Africa      = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='آفریقا')).order_by('Price_Off')
    Arabic      = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='عرب')).order_by('Price_Off')
    almas       = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name='اتاق یک تخته الماس'))
    India       = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='هند')).order_by('Price_Off')
    Russa       = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='اتاق امپریال') & Q(Room_Name__contains='روسیه')).order_by('Price_Off')
    turk        = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='ترکیه') & Q(Q(Room_Name__contains='سوئیت')  |Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    iran        = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='ایران باستان') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    sue         = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='یک خوابه') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    saf         = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Room_Name__contains='صفویه') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت'))).order_by('Price_Off')
    final = [Berelian,tamaddon,Emperial,Tailand,Turkish,Italian,Africa,Arabic,almas,India,Russa,turk,iran,sue,saf]


    context = {
        'almas':almas,'sue':sue,'saf':saf,'turk':turk,'iran':iran,'Berelian':Berelian,'Emperial':Emperial,'India':India,'Africa':Africa,'Tailand':Tailand,'Russa':Russa,'Turkish':Turkish,'Italian':Italian,
        'Arabic':Arabic,'tamaddon':tamaddon,'form':form,'final':final
    }
    if request.method == 'POST':
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='الماس') & Q(Day=date_one)& Q(Second_Day=date_two))

        form = TimeForm()
        context.update({'custom':custom})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('second')})

    return render(request,'almas.html',context)

def Homa(request):
    tooenss     = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما') & Q(Q(Room_Name='اتاق سینیور دوتخته (حداقل سه شب اقامت)')|Q(Room_Name='دو تخته دابل سینیور (اقامت حداقل 3 شب یا بیشتر)'))).order_by('Price_Off')
    double      = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما') & Q(Q(Room_Name='دو تخته دابل')|Q(Room_Name__contains='دو تخته دبل'))).order_by('Price_Off')
    tooens      = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما') & Q(Q(Room_Name='اتاق سینیور دوتخته')|Q(Room_Name='دو تخته دابل سینیور'))).order_by('Price_Off')
    house       = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما') & Q(Q(Room_Name__contains='ساعته') & Q(Room_Name__contains='اقامت'))).order_by('Price_Off')
    tooen       = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما') & Q(Q(Room_Name='دو تخته تویین')|Q(Room_Name__contains='دوتخته توئین'))).order_by('Price_Off')
    sen         = Room_Detail.objects.filter(Q(site__hotel_name__contains='هما') & Q(Q(Room_Name__contains='سه تخته سینیور')|Q(Room_Name__contains='اتاق سینیور سه تخته (حداقل سه شب اقامت)'))).order_by('Price_Off')

    context = {
        'tooenss':tooenss,'double':double,'tooens':tooens,'house':house,'tooen':tooen,'sen':sen
    }

    return render(request,'homa.html',context)

def Javad(request):
    houses      = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Q(Room_Name__contains='یک تخته رویال') | Q(Room_Name='اتاق یک تخته'))).order_by('Price_Off')
    king        = Room_Detail.objects.filter(Q(site__hotel_name__contains='جواد') & Q(Q(Room_Name__contains='دو تخته') & Q(Room_Name__contains='کینگ'))).order_by('Price_Off')

    context = {
        'houses':houses,'king':king
    }
    return render(request,'javad.html',context)

def Ghasr(request):
    lak         = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Q(Room_Name__contains='یک تخته لاکچری'))).order_by('Price_Off')
    jonior      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Room_Name__contains='جونیور')).order_by('Price_Off')
    eco         = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Room_Name__contains='یک تخته اکونومی')).order_by('Price_Off')
    classic     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Room_Name__contains='یک تخته لاکچری')).order_by('Price_Off')
    Atriom      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Q(Room_Name__contains='دو تخته') & Q(Room_Name__contains='آتریوم'))).order_by('Price_Off')
    bed         = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Q(Room_Name__contains='دو تخته') & Q(Room_Name__contains='لاکچری'))).order_by('Price_Off')
    land        = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Room_Name__contains='لندسکیپ')).order_by('Price_Off')
    vestern     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Room_Name__contains='وسترن')).order_by('Price_Off')
    roy         = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Room_Name__contains='پرنسس رویال')).order_by('Price_Off')
    senior      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Room_Name__contains='سنیور')).order_by('Price_Off')
    prances     = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Q(Room_Name__contains='پرنسس') & Q(Room_Name__contains='سوئیت'))).order_by('Price_Off')
    cancat      = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Room_Name__contains='کانکت')).order_by('Price_Off')
    presedent   = Room_Detail.objects.filter(Q(site__hotel_name__contains='قصر طلایی') & Q(Room_Name__contains='پرزیدنت')).order_by('Price_Off')
    context = {
        'lak':lak,'jonior':jonior,'eco':eco,'classic':classic,'Atriom':Atriom,'bed':bed,'land':land,'vestern':vestern,'roy':roy,'senior':senior,'prances':prances,
        'cancat':cancat,'presedent':presedent
    }
    return render(request,'ghasr.html',context)

# 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

from jalali_date import datetime2jalali, date2jalali
from .forms import TimeForm
def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

def cal(request):
    Hotels = Information.objects.all()
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

    return render(request,'index.html',{'Hotels':n})


# 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
# https://darvishiroyal.com/media/motionslider/photo_1485637257.jpg


def main(request):
    return render(request,'main.html')
