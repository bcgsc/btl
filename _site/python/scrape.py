import urllib
import requests
import re
from bs4 import SoupStrainer, BeautifulSoup
from datetime import datetime

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

#helper functions
def convertDate(date):
	if re.match('^\d{4}$',date):
		return date
	elif re.match('\d{4}\/\d{1,2}\/\d{1,2}',date):
		newdate=datetime.strptime(date,'%Y/%m/%d').strftime('%Y %b %d')
		return newdate
	else: 		
		return ''

def cleanAuthors(authors):
	a = authors.strip(', ...')
	return a

def cleanJournal(journal):
	j = journal.strip('None')
	j = journal.strip('Detail:')
	return j

#end helpers

my_file = open("../publications.md", "w")

url='https://scholar.google.ca/citations?hl=en&user=Svk1wjsAAAAJ&view_op=list_works&sortby=pubdate'
#soup=BeautifulSoup(urllib.urlopen(url).read(),"lxml")
soup=BeautifulSoup(open("inanc.html").read(),"lxml")
root='https://scholar.google.ca'

for td in soup.findAll('td', {"class":"gsc_a_t"}):
	
	#name of article	
	a = td.find('a', {'class':'gsc_a_at'})
	name = a.string
	
	#date of publication
	entryURL=root + a.attrs['data-href']
	soup2 = BeautifulSoup(urllib.urlopen(entryURL).read(),"lxml")
	try: date = convertDate((soup2.findAll('div',{'class':'gsc_vcd_value'},limit=2)[1]).string)
	except: 
		date = '' 
		pass

	#authors	
	info = td.findAll('div',{'class':'gs_gray'},limit=2)
	authors = cleanAuthors(info[0].string)
	authors = authors.replace('I Birol', '**I Birol**')
	
	#journal name	
	[x.extract() for x in info[1].findAll('span')]
	journal = cleanJournal(info[1].string)
	try: journal = cleanJournal(info[1].string)
	except: 
		journal = '' 
		pass	

	citation = authors + '. ' + name + '. ' + date + '. _' + journal + '_  \n\n' 
	my_file.write(citation.encode('utf-8'))

my_file.close()
	

