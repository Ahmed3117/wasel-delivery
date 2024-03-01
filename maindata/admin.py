from django.contrib import admin
from .models import Client,Worker,Package,ChargeOperation
from django.urls import reverse
from django.utils.html import format_html
from django.template.loader import render_to_string


# class PaidInline(admin.TabularInline):
#     model = Paid
#     extra = 1

# class SellOperationInline(admin.TabularInline):
#     model = SellOperation
#     extra = 1

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', )
#     search_fields = ('name',)
   
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('category', 'name', 'serial','native_price','sell_price','expectedprofet','date_added', 'notes')
#     list_filter = ('category',)
#     search_fields = ('category', 'name', 'serial')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'national_id','address','date_added','file','notes')
    search_fields = ('name', 'phone_number', 'national_id')
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'national_id','address','date_added','file','notes')
    search_fields = ('name', 'phone_number', 'national_id')

class PackageAdmin(admin.ModelAdmin):
    list_display = ('code','discription', 'weight', 'price','pill','notes','date_added')
    search_fields = ('code', 'discription')


class PackageInlineAdmin(admin.StackedInline):
    model = Package
    # extra = 1
    # max_num = 1
    show_change_link = True
    # classes = ('collapse',)

class ChargeOperationAdmin(admin.ModelAdmin):
    list_display = ('code','from_place', 'to_place', 'from_client','to_client',
    'worker','delivering_status','charge_price','date_added','printinvoice','notes')
    search_fields = ('from_place', 'to_place', 'from_client__name','to_client__name','from_client__phone_number','to_client__phone_number','from_client__national_id','to_client__national_id',
    'worker__name','code')
    list_filter = ('delivering_status','date_added')
    autocomplete_fields = ('from_client','to_client','worker')
    inlines = [PackageInlineAdmin,]
    list_editable = ('delivering_status',)
    def printinvoice(self, obj):
        chargeoperation_id = obj.id
        url = reverse('maindata:invoice', args=[chargeoperation_id])
        return format_html('<a class="button rounded " href="{}">فاتورة </a>', url)
    
    printinvoice.short_description = ' فاتورة '
    
# class SellOperationAdmin(admin.ModelAdmin):
#     list_display = ('pill', 'product', 'quantity', 'sell_type','getsellpriceforoneitem','added_value_for_deposite','getoperationprice','date_added')
#     search_fields = ('pill__client__name', 'product__name')

# class PaidAdmin(admin.ModelAdmin):
#     list_display = ('pill', 'paid','date_added')
#     search_fields = ('pill__client__name',)

# class PillAdmin(admin.ModelAdmin):
#     list_display = ('client', 'date_added', 'deposite_months', 'first_paid','total_paid','deserveddepositformonth')
#     search_fields = ('client__name', )
#     inlines = [SellOperationInline,PaidInline]

# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Product,ProductAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Worker,WorkerAdmin)
admin.site.register(Package,PackageAdmin)
admin.site.register(ChargeOperation,ChargeOperationAdmin)
# admin.site.register(Pill,PillAdmin)
# admin.site.register(SellOperation,SellOperationAdmin)
# admin.site.register(Paid,PaidAdmin)


