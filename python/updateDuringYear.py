import urllib, requests, re
from bs4 import SoupStrainer, BeautifulSoup
from datetime import datetime
import sys

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

thisyear = datetime.now().year

#helper functions

def is_current(date):
    if not date or int(date[:4])< thisyear:
        return False
    else: return True

def convert_date(date):
    if date is None: return ''
    elif re.match('^\d{4}$',date):
        return date
    elif re.match('\d{4}\/\d{1,2}\/\d{1,2}',date):
        newdate = datetime.strptime(date,'%Y/%m/%d').strftime('%Y %b %d')
        return newdate
    elif re.match('\d{4}\/\d{1,2}',date):
        newdate = datetime.strptime(date,'%Y/%m').strftime('%Y %b')
        return newdate
    else: 		
        return ''

def clean_authors(authors):
    a = authors.replace(', ...',', et. al')
    return a

def clean_journal(journal):
    if journal is None: return 'No Journal Information'
    else:
        j = journal.strip('None')
        j = journal.strip('Detail:')
        return j
#end helpers

if __name__ == "__main__":

    my_file = open("test","w+")
    #my_file = open('../_includes/current-year-pubs.html', 'w+')
    url = 'https://scholar.google.ca/citations?hl=en&user=Svk1wjsAAAAJ&view_op=list_works&sortby=pubdate'
    soup = BeautifulSoup(urllib.urlopen(url).read(), 'lxml')
    root = 'https://scholar.google.ca'

    pubsource = open('publicationsource', "w+")
    mysoup = BeautifulSoup(pubsource.read(),"html.parser")
    for p in mysoup.find_all("p", {'class':str(thisyear)}):
        p.decompose()
     
    pubsource.write(str(mysoup))

    for td in soup.find_all('td', {'class':'gsc_a_t'}):
	
        #name of article	
        a = td.find('a', {'class':'gsc_a_at'})
        name = a.string
	
        #date of publication
        entryURL = root + a.attrs['data-href']
        soup2 = BeautifulSoup(urllib.urlopen(entryURL).read(),"lxml")
        date = convert_date((soup2.find_all('div',{'class':'gsc_vcd_value'},limit=2)[1]).string)
        if is_current(date) is False: 
            my_file.close()
            sys.exit()
        if soup2.find('div', {'class':'gsc_vcd_title_ggi'}) is not None:
            link = soup2.find('div', {'class':'gsc_vcd_title_ggi'}).find('a').attrs['href']

        #authors	
        info = td.find_all('div',{'class':'gs_gray'},limit=2)
        authors = clean_authors(info[0].string)
        authors = authors.replace('I Birol', '<strong>I Birol</strong>')
        	    
        #journal name	
        [x.extract() for x in info[1].find_all('span')]
        journal = clean_journal(info[1].string)
        
        citation = '<p>' + authors + '. ' + name + '. ' + date + '. <a href=\"' + link + '\">' + journal + '</a></p>\n' 
        my_file.write(citation.encode('utf-8'))
        pubsource.write(citation.encode('utf-8'))

    my_file.close()
	

