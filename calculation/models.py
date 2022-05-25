from django.db import models
from django.db.models import Q
from django.utils import timezone
import datetime

# Create your models here.


# class GetDataManager(models.Manager):

#     @staticmethod
#     def check_balance(identify):
#         current_bal = Balances.objects.get(identify=identify).amount
#         return current_bal

#     def get_data_from_db(self):
#         get_data = self.filter(Q(is_disabled=False))

#         for data in get_data:
#             account = data.identify
#             current_bal = self.check_balance(account)
#             if float(data.amount) <= float(current_bal):
#                 TransferAmount.objects.create(
#                     identify=data.identify,
#                     amount=data.amount,
#                     timestamp=timezone.now()
#                 )
#                 get_update_table = self.filter(pk=data.id)
#                 next_date = datetime.datetime.now() + datetime.timedelta(days=30)
#                 get_update_table.update(
#                     last_payment=timezone.now(),
#                     next_payment=next_date
#                 )
#                 balance_table = Balances.objects.filter(identify=data.identify)
#                # balance_table_update = balance_table.pk
#                 new_amount = float(current_bal) - float(data.amount)
#                 balance_table.update(
#                     amount=new_amount
#                 )
#             elif float(data.amount) > float(current_bal):
#                 message = {"message": "You have no balance.", "status": 400}
#                 return message
#             else:
#                 continue

#         message = {"message": "Task has been completed."}
#         return message


# class Balances(models.Model):
#     identify = models.CharField(max_length=20)
#     amount = models.DecimalField(max_digits=14, decimal_places=4)

#     def __str__(self):
#         return self.identify


# class GetData(models.Model):
#     identify = models.CharField(max_length=20)
#     is_disabled = models.BooleanField(default=False)
#     amount = models.DecimalField(max_digits=14, decimal_places=4)
#     last_payment = models.DateTimeField(null=True, blank=True)
#     next_payment = models.DateTimeField(null=True, blank=True)
#     timestamp = models.DateTimeField()

#     objects = GetDataManager()

#     def __str__(self):
#         return self.identify


# class TransferAmount(models.Model):
#     identify = models.CharField(max_length=20)
#     amount = models.DecimalField(max_digits=14, decimal_places=4)
#     timestamp = models.DateTimeField()

#     def __str__(self):
#         return self.identify


class Site(models.Model):
    site_name = models.CharField(max_length=300)
    def __str__(self):
        return self.site_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=300)
    hotel_star = models.CharField(max_length=200,blank=True,null=True)
    hotel_vote = models.CharField(max_length=200,blank=True,null=True)
    hotel = models.ForeignKey(Site,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.hotel_name
        
    
class Room_Detail(models.Model):
    Room_Name = models.CharField(max_length=200)
    Night = models.CharField(max_length=200,blank=True,null=True)
    Future = models.CharField(max_length=300,blank=True,null=True)
    Person_Number = models.CharField(max_length=300,blank=True,null=True)
    Price_Origin = models.CharField(max_length=200,blank=True,null=True)
    Off = models.CharField(max_length=200,blank=True,null=True)
    Price_Off = models.CharField(max_length=200,blank=True,null=True)
    Day = models.DateField(blank=True,null=True)
    Second_Day = models.DateField(blank=True,null=True)
    Path = models.URLField(max_length=400,blank=True,null=True)
    site = models.ForeignKey(Hotel,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.Room_Name


class Information(models.Model):
    image = models.ImageField(upload_to='image',blank=True,null=True)
    hotel = models.CharField(max_length=450)
    star = models.IntegerField()
    text = models.TextField()
    address = models.CharField(max_length=600)
    def __str__(self):
        return self.hotel


class Hotel_Image(models.Model):
    image = models.ImageField(upload_to='image')
    main = models.ForeignKey(Information,related_name='imagesm',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.main)


class History(models.Model):
    birth = models.CharField(max_length=300)
