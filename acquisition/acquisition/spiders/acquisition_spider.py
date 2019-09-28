import scrapy

class FandomSpider(scrapy.Spider):
	name = 'acquisition'

	start_urls = [
		'https://matchbox.fandom.com/wiki/List_of_1980_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1981_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1982_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1983_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1984_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1985_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1986_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1987_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1988_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1989_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1990_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1991_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1992_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1993_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1994_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1995_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1996_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1997_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1998_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1999_Matchbox',
		'https://matchbox.fandom.com/wiki/List_of_1990_Matchbox',
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
