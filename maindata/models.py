from django.db import models
from datetime import datetime
import random
# class Category(models.Model):
#     name = models.CharField(verbose_name = " التصنيف",max_length=200,null=True,blank=True)
    
#     class Meta:
#         verbose_name_plural = '  تصنيف المنتجات '
#         verbose_name='   تصنيف'
#     def __str__(self) :
#         try:
#             return self.name
#         except:
#             return 'غير معروف'

# class Product(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " التصنيف") 
#     name = models.CharField(verbose_name = " الاسم",max_length=200,null=True,blank=True)
#     serial = models.CharField(verbose_name = "  رقم المسلسل",max_length=14 ,null=True,blank=True)
#     notes = models.CharField(verbose_name = "  ملاحظات ",max_length=200,null=True,blank=True )
#     date_added = models.DateTimeField(verbose_name = " تاريخ الاضافة",auto_now_add=True,null=True,blank=True) 
#     native_price = models.IntegerField(verbose_name = "السعر الاصلى ",default = 1 ,null=True,blank=True)
#     sell_price = models.IntegerField(verbose_name = " سعر البيع ",default = 1 ,null=True,blank=True)
#     def expectedprofet(self):
#         if self.native_price and self.sell_price:
#             return self.native_price - self.sell_price
#     expectedprofet.short_description = ' الربح المتوقع '
#     class Meta:
#         verbose_name_plural = '  المنتجات '
#         verbose_name='   منتج'
#     def __str__(self) :
#         try:
#             return self.name
#         except:
#             return 'غير معروف'

# class Client(models.Model):
#     name = models.CharField(verbose_name = " الاسم",max_length=200,null=True,blank=True)
#     phone_number = models.CharField(verbose_name = "  الفون",max_length=14 ,null=True,blank=True)
#     national_id = models.CharField(verbose_name = "  رقم البطاقة ",max_length=200,null=True,blank=True )
#     date_added = models.DateTimeField(verbose_name = " تاريخ الاضافة",auto_now_add=True,null=True,blank=True) 
#     notes = models.CharField(verbose_name = "  ملاحظات ",max_length=200,null=True,blank=True )
#     file = models.FileField(upload_to='client_files/',null=True,blank=True,verbose_name = "  ملف")
#     class Meta:
#         verbose_name_plural = '  العملاء '
#         verbose_name='   عميل'
#     def __str__(self) :
#         try:
#             return self.name
#         except:
#             return 'غير معروف'

# class Pill(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " العميل") 
#     date_added = models.DateTimeField(verbose_name = " تاريخ الاضافة",default=datetime.now(),null=True,blank=True)
#     deposite_months = models.IntegerField(verbose_name = " عدد الاقساط ",default = 0,null=True,blank=True)
#     first_paid = models.IntegerField(verbose_name = "  المقدم ",null=True,blank=True,default = 0)
#     total_paid = models.IntegerField(verbose_name = " مجموع المدفوع حتى الان ",default = 0,null=True,blank=True)
#     # def related_deposit_selloperations(self):
#     #     SellOperation.objects.filter()

#     def deserveddepositformonth(self):
#         total_price = 0
#         all_related_selloperations = SellOperation.objects.filter(pill = self,sell_type = 'D')
#         for operation in all_related_selloperations:
#             total_price += operation.getoperationprice()
#         if total_price == 0:
#             return 0
#         else:
#             return (total_price - self.first_paid) / self.deposite_months
            
#     deserveddepositformonth.short_description = '   القسط الشهرى'
    
#     def totalprice(self):
#         total_price = 0
#         all_related_selloperations = SellOperation.objects.filter(pill = self)
#         for operation in all_related_selloperations:
#             total_price += operation.getoperationprice()
#         if total_price == 0:
#             return 0
#         else:
#             return total_price 
            
#     totalprice.short_description = '   القسط الشهرى'
    
#     def save(self, *args, **kwargs):
#         total_paid_until_now = 0
#         all_paids = Paid.objects.filter(pill = self)
#         for paid in all_paids : 
#             total_paid_until_now += paid.paid
#         self.total_paid = total_paid_until_now + self.first_paid
#         super().save(*args, **kwargs)
    
#     # totalpaid.short_description = '  اجمالى المدفوع حتى الان (مقدم + اقساط) '
#     class Meta:
#         verbose_name_plural = '  الفواتير'
#         verbose_name='   فاتورة'
#     def __str__(self) :
#         try:
#             return self.client.name
#         except:
#             return 'غير معروف'

# class SellOperation(models.Model):
#     selltype = (
#         ('C' , 'كاش'),
#         ('D' , 'قسط'),
#     )
#     pill= models.ForeignKey(Pill, on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " العميل") 
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " المنتج") 
#     quantity = models.IntegerField(verbose_name = "  الكمية",default = 1 ,null=True,blank=True)
#     date_added = models.DateTimeField(verbose_name = " تاريخ العملية",default=datetime.now(),null=True,blank=True)
#     sell_type = models.CharField(verbose_name = "  طريقة الدفع",choices=selltype,default='C',max_length=10,null=True,blank=True)
#     added_value_for_deposite = models.IntegerField(verbose_name = " القيمة المضافة",default = 0 ,null=True,blank=True)
#     def getsellpriceforoneitem(self):
#         return self.product.sell_price
#     def getoperationprice(self):
#         return (self.product.sell_price + self.added_value_for_deposite)* self.quantity
#     getoperationprice.short_description = 'مجموع سعر العملية' 
#     getsellpriceforoneitem.short_description = ' سعر البيع للوحده ' 
#     class Meta:
#         verbose_name_plural = '  عمليات البيع'
#         verbose_name='   عملية'
#     def __str__(self) :
#         try:
#             return self.patient.pill.client.name
#         except:
#             return 'غير معروف'
         
# class Paid(models.Model):
#     pill = models.ForeignKey(Pill, on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " الفاتورة") 
#     paid = models.IntegerField(verbose_name = " المدفوع" ,null=True,blank=True)
#     date_added = models.DateTimeField(verbose_name = " تاريخ الدفع",auto_now_add=True,null=True,blank=True) 

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         self.pill.total_paid += self.paid
#         self.pill.save()
        
    
#     class Meta:
#         verbose_name_plural = ' المدفوعات'
#         verbose_name=' دفعة'
#     def __str__(self) :
#         try:
#             return self.session.patient.name
#         except:
#             return 'غير معروف'



###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
class User(models.Model):
    name = models.CharField(verbose_name = " الاسم",max_length=200,null=True,blank=True)
    phone_number = models.CharField(verbose_name = "  الفون",max_length=14 ,null=True,blank=True)
    national_id = models.CharField(verbose_name = "  رقم البطاقة ",max_length=14,null=True,blank=True )
    address = models.CharField(verbose_name = "   العنوان ",max_length=200,null=True,blank=True )
    date_added = models.DateTimeField(verbose_name = " تاريخ الاضافة",auto_now_add=True,null=True,blank=True) 
    notes = models.CharField(verbose_name = "  ملاحظات ",max_length=200,null=True,blank=True )
    file = models.FileField(upload_to='client_files/',null=True,blank=True,verbose_name = "  ملف")
    def __str__(self) :
        try:
            return self.name
        except:
            return 'غير معروف'
class Client(User):
    class Meta:
        verbose_name_plural = '  العملاء '
        verbose_name='   عميل'

class Worker(User):
    class Meta:
        verbose_name_plural = '  عمال '
        verbose_name='   عامل'

class Package(models.Model):
    chargeoperation = models.OneToOneField('ChargeOperation', on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " الشحنة") 
    code = models.CharField(verbose_name="كود الطلب", max_length=14, editable=False, null=True, blank=True)
    discription = models.CharField(verbose_name = " وصف",max_length=200,null=True,blank=True)
    weight = models.FloatField(verbose_name = "  الوزن",null=True,blank=True)
    price = models.FloatField(verbose_name = "  السعر",null=True,blank=True)
    pill = models.FileField(upload_to='package_pill_files/',null=True,blank=True,verbose_name = "  صورة من الفاتورة")
    notes = models.CharField(verbose_name = "  ملاحظات ",max_length=200,null=True,blank=True )
    date_added = models.DateTimeField(verbose_name = " تاريخ الطلب",auto_now_add=True,null=True,blank=True) 

    def save(self, *args, **kwargs):
        if not self.code:
            # Generate the code
            current_date = datetime.now()
            year = current_date.strftime("%y")
            month = current_date.strftime("%m")
            day = current_date.strftime("%d")
            random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(6))
            self.code = f"{year}{month}{day}{random_numbers}"

        super().save(*args, **kwargs)

    def __str__(self) :
        try:
            return self.code
        except:
            return 'غير معروف'
    class Meta:
        verbose_name_plural = '  الطلبات '
        verbose_name='   طلب'

class ChargeOperation(models.Model): # عملية شحن
    deliveringstatus = (
        ('1' , 'انتظار'),
        ('2' , 'خروج'),
        ('3' , 'تم'),
        ('4' , 'مرتجع'),
    )
    # deliveringtype = (
    #     ('1' , 'ذهاب'),
    #     ('2' , 'عودة'),
    #     ('3' , 'ذهاب و عودة'),
    # )
    from_client = models.ForeignKey(Client, on_delete=models.SET_NULL,related_name = 'from_client_relation', null=True,blank=True,verbose_name = " من العميل") 
    to_client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " الى العميل") 
    from_place = models.CharField(verbose_name = " من عنوان",max_length=200,null=True,blank=True)
    to_place = models.CharField(verbose_name = " الى عنوان",max_length=200,null=True,blank=True)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True,blank=True,verbose_name = " العامل الموكل") 
    delivering_status = models.CharField(verbose_name = " موقف التوصيل",choices=deliveringstatus,default='1',max_length=10,null=True,blank=True)
    # delivering_type = models.CharField(verbose_name = "  نوع العملية",choices=deliveringtype,default='1',max_length=10,null=True,blank=True)
    charge_price = models.FloatField(verbose_name = "  سعر التوصيل",null=True,blank=True)


    code = models.CharField(verbose_name="كود العملية", max_length=14, editable=False, null=True, blank=True)
    notes = models.CharField(verbose_name = "  ملاحظات ",max_length=200,null=True,blank=True )
    date_added = models.DateTimeField(verbose_name = " تاريخ تسجيل العملية",auto_now_add=True,null=True,blank=True) 

    def save(self, *args, **kwargs):
        if not self.code:
            # Generate the code
            current_date = datetime.now()
            year = current_date.strftime("%y")
            month = current_date.strftime("%m")
            day = current_date.strftime("%d")
            random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(6))
            self.code = f"{year}{month}{day}{random_numbers}"
        if self.from_client and not self.from_place:
            if self.from_client.address:
                self.from_place = self.from_client.address
        if self.to_client and not self.to_place:
            if self.to_client.address:
                self.to_place = self.to_client.address
        super().save(*args, **kwargs)


    def __str__(self) :
        try:
            return self.from_client.name
        except:
            return 'غير معروف'
    class Meta:
        verbose_name_plural = '  عمليات الشحن '
        verbose_name='   عملية شحن'