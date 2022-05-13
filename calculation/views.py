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
    driver.get(f'https://www.alibaba.ir/hotel/ir-mashhad?destination=City_5be3f68be9a116befc66701b_%D9%85%D8%B4%D9%87%D8%AF+-+%D8%A7%DB%8C%D8%B1%D8%A7%D9%86&departing={today_date.date()}&returning={tommorow_date.date()}&rooms=30')
    site,created = Site.objects.update_or_create(site_name='AliBaba')
    reserve = []
    add = []
    ti.sleep(10)

    for link in range(1,6):
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
        # ti.sleep(10)
        day_range = 7
        for day in range(day_range):
            for j in range(2):
                if j == 1 :
                    week=4
                else:
                    week=0
                l_next = datetime.datetime.now() + datetime.timedelta(days=day)
                l_next_second = datetime.datetime.now() + datetime.timedelta(days=day+1)
                bb2 = jalali.Gregorian(l_next.date()).persian_string()
                bb3 = jalali.Gregorian(l_next_second.date()).persian_string()
                numb2 = bb2.split('-')[-1]
                numb3 = int(bb3.split('-')[-1])
                driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[2]/span').click()
                first = driver.find_elements(By.XPATH,f"//span[text()='{numb2}']")
                first[j].click()
                decond = driver.find_elements(By.XPATH,f"//span[text()='{numb3}']")
                decond[j].click()
                element = driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[3]/div/div[3]/button')
                driver.execute_script("arguments[0].click();", element)
                butt = driver.find_element(By.XPATH,'//*[@id="ho_sidebar"]/div/div/div/button')
                driver.execute_script("arguments[0].click();", butt)
                his = driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div[3]/aside/div/div/div/div[1]/div[1]/div[2]/span').text
                print(his.split('–')[0][:-1])
                print(his.split('–')[1][1:])
                print('###########')
                convert_date = jalali.Persian(his.split('–')[0][:-1]).gregorian_string()
                convert_date_next = jalali.Persian(his.split('–')[1][1:]).gregorian_string()
                print('--------0')
                print(convert_date)
                print('--------1')
                print(convert_date_next)
                ti.sleep(10)
                try:
                    # /html/body/div/div[1]/main/div/div[3]/div/section[3]/button
                    # /html/body/div/div[1]/main/div/div[3]/div/section[3]/button
                    # //*[@id="ho_main"]/div/section[3]/button
                    driver.find_element(By.XPATH,'//*[@id="ho_main"]/div/section[3]/button').click()
                    driver.find_element(By.XPATH,'//*[@id="ho_main"]/div/section[3]/button').click()
                    driver.find_element(By.XPATH,'//*[@id="ho_main"]/div/section[3]/button').click()
                except:
                    pass
                # ti.sleep(10)
                for mar in driver.find_elements(By.CLASS_NAME,'a-card__body')[:-3]:
                    # ti.sleep(10)
                    try:
                        p = ''.join(mar.text)
                        items_ali = p.split('\n')
                        # print('items_ali[1]')
                        # print(items_ali[1])
                        # print('items_ali[2]')
                        # print(items_ali[2])
                        # print('items_ali[3]')
                        # print(items_ali[3])
                        # print('items_ali[4]')
                        # print(items_ali[4])
                        # print('items_ali[5]')
                        # print(items_ali[5])
                        # print('items_ali[6]')
                        # print(items_ali[6])
                        # print('items_ali[7]')
                        # print(items_ali[7])
                        # print('items_ali[8]')
                        # print(items_ali[8])
                        convert_price = re.sub(',','',items_ali[4][12:-5])
                        print(convert_price)
                        print('--------------')
                        add.append(items_ali)
                        # try:
                        room_team,created = Room_Detail.objects.update_or_create(site=hotel,Day=convert_date,Second_Day=convert_date_next,Path=path_ali,Room_Name=items_ali[0],Night=items_ali[-1],Future=items_ali[1],Person_Number=items_ali[3],Price_Origin=items_ali[6],Off=items_ali[5],Price_Off=int(convert_price)/10)
                        # except:
                        #     room_team,created = Room_Detail.objects.update_or_create(site=hotel,Day=convert_date,Second_Day=convert_date_next,Path=path_ali,Room_Name=items_ali[0],Night=items_ali[-1],Future=items_ali[1],Person_Number=items_ali[3],Price_Origin=items_ali[6],Off=items_ali[5],Price_Off=int(convert_price)/10)
                    except:
                        pass
                ti.sleep(5)
    return HttpResponse('ok')

 
def Darvish(request):
    form = TimeForm()
    three_rooms = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='سه تخته') | Q(Room_Name__contains='سه نفره')))).order_by('Price_Off')
    four_rooms  = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='چهارتخته') | Q(Room_Name__contains='چهار نفره')))).order_by('Price_Off')
    standard    = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره')))).order_by('Price_Off')
    Darvish     = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='دبل') | Q(Room_Name__contains='دابل')))).order_by('Price_Off')
    session     = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='سوئیت') & Q(Room_Name__contains='فصل'))).order_by('Price_Off')
    toeen       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    three       = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='سه تخته'))).order_by('Price_Off')
    four        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Room_Name__contains='چهار تخته'))).order_by('Price_Off')
    espa        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Room_Name__contains='اسپا')).order_by('Price_Off')
    room        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سه تخته') | Q(Room_Name__contains='اتاق')))).order_by('Price_Off')
    stan        = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='تویین') | Q(Room_Name__contains='توئین')))).order_by('Price_Off')
    one         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='اکونومی') & Q(Q(Room_Name__contains='یک تخته') | Q(Room_Name__contains='یک نفره')))).order_by('Price_Off')
    imp         = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='امپریال') & Q(Q(Room_Name__contains='سوئیت') | Q(Room_Name__contains='سوییت')))).order_by('Price_Off')
    Es          = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Q(Room_Name__contains='استاندارد') & Q(Q(Room_Name__contains='دبل') | Q(Room_Name__contains='دابل')))).order_by('Price_Off')

    context = {
        'one':one,'three_rooms':three_rooms,'four_rooms':four_rooms,'toeen':toeen,'Darvish':Darvish,'stan':stan,'standard':standard,'Es':Es,'three':three,'four':four,'session':session,
        'espa':espa,'room':room,'imp':imp,'form':form
    }
    if request.method == 'POST':
        date_one = jalali.Persian(request.POST.get('first')).gregorian_string()
        date_two = jalali.Persian(request.POST.get('second')).gregorian_string()
        custom = Room_Detail.objects.filter(Q(site__hotel_name__contains='درویش') & Q(Day=date_one)& Q(Second_Day=date_two))

        # form = TimeForm()
        context.update({'custom':custom})
        context.update({'first':request.POST.get('first')})
        context.update({'second':request.POST.get('second')})

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


    context = {
        'almas':almas,'sue':sue,'saf':saf,'turk':turk,'iran':iran,'Berelian':Berelian,'Emperial':Emperial,'India':India,'Africa':Africa,'Tailand':Tailand,'Russa':Russa,'Turkish':Turkish,'Italian':Italian,
        'Arabic':Arabic,'tamaddon':tamaddon,'form':form
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
    # rooms = Room_Detail.objects.
    return render(request,'main.html')
