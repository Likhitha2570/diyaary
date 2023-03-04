from django.contrib import admin

# Register your models here.
from django.contrib import admin
from diyaaryapp.models import  customerReviews
from diyaaryapp.models import  diaryentries
from diyaaryapp.models import  Imagesuploader
# Register your models here.
admin.site.register(customerReviews),
admin.site.register(diaryentries),
@admin.register(Imagesuploader)
class ImageAdmin(admin.ModelAdmin):
    list_display=['Allimages','date','caption']
