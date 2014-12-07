# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
import shelve

tempbase_pos="E:/websiteProj/tempbase.dat"
feidieshuo_start_url="http://www.feidieshuo.cc/page/1/"
baogaolaoban_start_url="http://www.youku.com/show_page/id_z3a35da1c63ba11e3a705.html"
haowanba_start_url="http://www.9haow.cn/category/video"
juetuzhi_start_url="http://juetuzhi.net/category/video/"

youku_url_pattern="http://player.youku.com/player.php/sid/\w+/v.swf"

def get_url(item): #从视频页面经过xpath得到的string中找到video的url。
    pos1=item.find('http://player.youku.com')
    pos2=item.find('" allowFull')
    video_embed_url=item[pos1:pos2]
    return video_embed_url

def store_to_tempbase(tag,data):
#This is used to store data we parse this time,not to store in the websitebase.
	tempbase=shelve.open(tempbase_pos)
	video_list=[]
	picture_list=[]
	beauty_list=[]
	if type(data)==type([]):
		if tag==1:
			video_list.extend(data)
		if tag==2:
			picture_list.extend(data)
		if tag==3:
			beauty_list.extend(data)
	else:
		if tag==1:
			video_list.append(data)
		if tag==2:
			picture_list.append(data)
		if tag==3:
			beauty_list.append(data)
	tempbase['video']=video_list
	tempbase['picture']=picture_list
	tempbase['beauty']=beauty_list
	tempbase.close()

class fedieshuoInitial(scrapy.Spider):
#This is the spider that parse the initial feidieshuo video.
	name="feidieshuo_initial"
	allow_domains=["feidieshuo.cc"]
	start_urls=[
		feidieshuo_start_url,
	]
	video_append_list=[]
	countpage=0 #As there is some syntax different in the site at page 18,we stop parse at page 17.
	def parse(self,response):#The first called parse_function need to be named parse.
		video_title_list=response.xpath('//*[@class="panel clearfix" or @class="panel clearfix hover"]//div[@class="top clearfix"]/h2/a/text()').extract()
		video_url_list=response.xpath('//*[@class="panel clearfix" or @class="panel clearfix hover"]/div[2]/div/@data-player').extract()
		video_text_list=response.xpath('//*[@class="panel clearfix" or @class="panel clearfix hover"]/div[2]/p/text()').extract()
		next_list_page=response.xpath("/html/body/div[@class='container public']//div[@class='pagination clearfix']//a[@class='next page-numbers']/@href").extract()
		for i in range(len(video_title_list)):
			video={}
			video['title']=video_title_list[i]
			video['url']=video_url_list[i]
			video['text']=video_text_list[i]
			self.video_append_list.append(video)
		self.countpage=self.countpage+1
		if next_list_page and self.countpage!=17: #we stop at page 17.
			next_list_page=next_list_page[0]
			yield Request(next_list_page,callback=self.parse)
		else:
			store_to_tempbase(1,self.video_append_list) #If there is not video left,store all the video to database.
			
			
class feidieshuoUpdata(scrapy.Spider):
#parse the updata of the video of feidieshuo
	name="feidieshuo_updata"
	allow_domains=["feidieshuo.cc"]
	start_urls=[
		feidieshuo_start_url,
	]
	def parse(self,response):
		video_title=response.xpath('//div[@class="home_main_wrap"]/div[3]/div/h2/a/text()').extract()[0]
		video_url=response.xpath('//div[@class="home_main_wrap"]/div[3]//div[@class="main clearfix"]/div[@class="videobox"]/@data-player').extract()[0]
		video_text=response.xpath('//div[@class="home_main_wrap"]/div[3]//div[@class="main clearfix"]/p/text()').extract()[0]
		if video_title and video_url and video_text:
			video={}
			video['title']=video_title
			video['url']=video_url
			video['text']=video_text
			print video['title']
			print video['url']
			print video['text']
			store_to_tempbase(1,video)
			
			
class baogaolaobanInitial(scrapy.Spider):
	name="baogaolaoban_initial"
	allow_domains=["youku.com"]
	start_urls=[
		baogaolaoban_start_url,
	]
	video_append_list=[]
	video_title_list=[]
	video_url_list=[]
	video_text_list=[]
	def store(self):
		for i in range(len(self.video_url_list)):
			self.video_append_list[i]['url']=self.video_url_list[i]
			self.video_append_list[i]['text']=""
		for video in self.video_append_list:
			print video['title']
			print video['url']
		store_to_tempbase(1,self.video_append_list)
			
	def parse_page(self,response):
		video_url=response.xpath('//*[@id="link3"]').extract()[0]
		video_url=get_url(video_url)
		video_text=""
		self.video_url_list.append(video_url)
		self.video_text_list.append(video_text)
		if len(self.video_url_list)==len(self.video_title_list):
			self.store()
		
	def parse(self,response):
		self.video_title_list=response.xpath('//div[@class="series_topic"]//ul[@class="v"]/li[@class="v_title"]/a/text()').extract()
		video_page_list=response.xpath('//div[@class="series_topic"]//ul[@class="v"]/li[@class="v_link"]/a/@href').extract()
		for i in range(len(self.video_title_list)):
			video={}
			video['title']=self.video_title_list[i]
			self.video_append_list.append(video)
		for video_page in video_page_list:
			yield Request(video_page,callback=self.parse_page)

class haowanbaUpdata(scrapy.Spider):
	name="haowanba_updata"
	allow_domains=['9haowan.cn']
	start_urls=[
		haowanba_start_url,
	]
	def parse_page(self,response):
		video_title=response.xpath('//h1[@itemprop="headline"]/text()').extract()[0]
		video_text=response.xpath('//div[@itemprop="articleBody"]/p[2]/text()').extract()
		if video_text:
			video_text=video_text[0]
		else:
			video_text=""
		video_url=response.xpath('//div[@itemprop="articleBody"]/p[3]').extract()[0]
		video_url=re.findall(youku_url_pattern,video_url)[0]
		video={}
		if video_title and video_url:
			video['title']=video_title
			video['url']=video_url
			video['text']=video_text
			store_to_tempbase(1,video)
	def parse(self,response):
		video_page=response.xpath('//div[@class="front-list"]/div[2]/div/a/@href').extract()[0]
		yield Request(video_page,callback=self.parse_page)
		
		
	