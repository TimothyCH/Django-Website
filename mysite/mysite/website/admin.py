from django.contrib import admin
from website.models import Data,Url,Comments
# Register your models here.

class UrlInline(admin.TabularInline):
	model=Url
	extra=3
	
class CommentsInline(admin.TabularInline):
	model=Comments
	extra=1
	
class DataAdmin(admin.ModelAdmin):
	fieldsets=[
		(None,{'fields':['title']}),
		('Date information',{'fields':['date']}),
		('type',{'fields':['vtag','btag','ptag']}),
		('text',{'fields':['text']})
	]
	inlines=[UrlInline,CommentsInline]
	list_display=('title','date','vtag','btag','ptag','text')

admin.site.register(Url)
admin.site.register(Comments)	
admin.site.register(Data,DataAdmin)