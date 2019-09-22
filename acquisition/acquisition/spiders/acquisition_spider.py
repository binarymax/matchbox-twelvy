import scrapy

class FandomSpider(scrapy.Spider):
	name = 'acquisition'

	start_urls = [
		'https://matchbox.fandom.com/wiki/List_of_2000_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2001_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2002_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2003_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2004_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2005_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2006_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2007_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2008_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2009_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2010_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2011_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2012_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2013_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2014_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2015_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2016_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2017_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2018_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2019_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_2020_Matchbox'
	]

	def parse(self, response):
		for cell in response.css('td>a'):
			url = cell.css('a::attr("href")').get()
			if '.jpg' in url:
				yield {'image_urls': [url]}
