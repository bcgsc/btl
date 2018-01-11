from bs4 import BeautifulSoup
import urllib
from datetime import datetime
import re



def convertDate(date):
	if re.match('^\d{4}$',date):
		return date
	elif re.match('\d{4}\/\d{1,2}\/\d{1,2}',date):
		newdate=datetime.strptime(date,'%Y/%m/%d').strftime('%Y %b %d')
		return newdate
	elif re.match('\d{4}\/\d{1,2}',date):
		newdate=datetime.strptime(date,'%Y/%m').strftime('%Y %b')
		return newdate
	else: 		
		return ''


root='https://scholar.google.ca'

soup2 = BeautifulSoup(open("one.html").read(),"lxml")
date = convertDate((soup2.findAll('div',{'class':'gsc_vcd_value'},limit=2)[1]).string)

print date



'''
url1= root + '/citations?view_op=view_citation&hl=en&user=WMhS0lAAAAAJ&citation_for_view=WMhS0lAAAAAJ:_kc_bZDykSQC'
url2= root + '/citations?view_op=view_citation&hl=en&user=WMhS0lAAAAAJ&citation_for_view=WMhS0lAAAAAJ:TFP_iSt0sucC'
url3= root + '/citations?view_op=view_citation&hl=en&user=WMhS0lAAAAAJ&cstart=20&pagesize=80&citation_for_view=WMhS0lAAAAAJ:kNdYIx-mwKoC'
url4= root + '/citations?view_op=view_citation&hl=en&user=WMhS0lAAAAAJ&cstart=20&pagesize=80&citation_for_view=WMhS0lAAAAAJ:3fE2CSJIrl8C'

printDate(url1)
printDate(url2)
printDate(url3)
printDate(url4)
'''


