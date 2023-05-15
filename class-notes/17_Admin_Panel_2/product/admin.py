from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(Product)

admin.site.site_title="Clarusway Admin Panel Session"
admin.site.site_header="Welcome Product Admin Panel"
admin.site.index_title="Admin panel customization exampels"

class ProductAdmin(admin.ModelAdmin):
    # admin panelde;
    #görünmesini istediğimiz field lar (başıklardan sırlama yapabilirisniz)
    list_display=['name','id','description','is_in_stock','slug','create_date','slug']
    #ar yüz üzerinde field güncelleme izni 
    list_editable=['is_in_stock']
    #instince a erişmek için link (link veredi iseniz editable yapılamaz)
    list_display_links=['id','name','slug']
    #filterelem yapılacak filedlar (gruplama için kullanılan field lar mantıklı)
    list_filter=['is_in_stock','create_date']
    # arama yapılmasını istediğiniz fieldlar 
    search_fields=['name','description']
    # default sıralama id 
    ordering=['id','name'] #ordering=['-id']
    #sayfada görüntülencek kayıt sayısı
    list_per_page=20
    # tümünü göstermesi istendiğinde görüntülenecek max kayıt sayısı
    list_max_show_all=100
    # tarih filtresi (ör: seçilen yıl sonra seçilen ay)
    date_hierarchy='create_date'
    #otomatik üretme  
    # slug filed harf, sayı, alt çizgi, kısa çizgi içerebilir
    prepopulated_fields={'slug':['name']}
    # form üzerinde elementleri konumlandırma
    # tuple içindeki her bir tuple bir satırda
    fields=(
        ('name','is_in_stock'),
        ('slug'),
        ('description')
    )
    # filter_horizontal=('')
    #ekstra field ekeleme
    def added_days_ago(self,object):
        from django.utils import timezone
        diffrent=timezone.now()-object.create_date
        return diffrent.days
    list_display+=['added_days_ago']

admin.site.register(Product,ProductAdmin)