from bs4 import BeautifulSoup
import urllib
from datetime import datetime
import re

root='https://scholar.google.ca'

def printDate(url):

	soup2 = BeautifulSoup(urllib.urlopen(url).read(),"lxml")
	print soup2.text
#	try: 
	#thedate = soup2.findAll("div",{"id":"gsc_ocd_bdy"})
	#print thedate
#	except: 
#		date = '' 
#		pass
#	print date

def convertDate(date):
	if re.match('^\d{4}$',date):
		return date
	elif re.match('\d{4}\/\d{1,2}\/\d{1,2}',date):
		newdate=datetime.strptime(date,'%Y/%m/%d').strftime('%Y %b %d')
		return newdate
	else: 		
		return ''

url1= root + '/citations?view_op=view_citation&hl=en&user=WMhS0lAAAAAJ&citation_for_view=WMhS0lAAAAAJ:_kc_bZDykSQC'
url2= root + '/citations?view_op=view_citation&hl=en&user=WMhS0lAAAAAJ&citation_for_view=WMhS0lAAAAAJ:TFP_iSt0sucC'
url3= root + '/citations?view_op=view_citation&hl=en&user=WMhS0lAAAAAJ&cstart=20&pagesize=80&citation_for_view=WMhS0lAAAAAJ:kNdYIx-mwKoC'
url4= root + '/citations?view_op=view_citation&hl=en&user=WMhS0lAAAAAJ&cstart=20&pagesize=80&citation_for_view=WMhS0lAAAAAJ:3fE2CSJIrl8C'

printDate(url1)
printDate(url2)
printDate(url3)
printDate(url4)
