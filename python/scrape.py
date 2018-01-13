import urllib, requests, re
from bs4 import SoupStrainer, BeautifulSoup
from datetime import datetime

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

#helper functions
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
    a = authors.strip(', ...')
    return a

def clean_journal(journal):
    if journal is None: return 'No Journal Information'
    else:
        j = journal.strip('None')
        j = journal.strip('Detail:')
        return j
#end helpers

if __name__ == "__main__":

    #my_file = open("../testmaking.md", "w+")
    my_file = open("../publications.md","w+")
    #my_file.write('# Publications List\n\n')

    #url = 'https://scholar.google.ca/citations?hl=en&user=Svk1wjsAAAAJ&view_op=list_works&sortby=pubdate'
    #soup = BeautifulSoup(urllib.urlopen(url).read(),"lxml")
    soup = BeautifulSoup(open("inanc.html").read(),"lxml")
    root = 'https://scholar.google.ca'

    for td in soup.find_all('td', {"class":"gsc_a_t"}):
	
        #name of article	
        a = td.find('a', {'class':'gsc_a_at'})
        name = a.string
	
        #date of publication
        entryURL = root + a.attrs['data-href']
        soup2 = BeautifulSoup(urllib.urlopen(entryURL).read(),"lxml")
        date = convert_date((soup2.find_all('div',{'class':'gsc_vcd_value'},limit=2)[1]).string)
        link = soup2.find('div', {'class':'gsc_vcd_title_ggi'}).find('a').attrs['href']

        #authors	
        info = td.find_all('div',{'class':'gs_gray'},limit=2)
        authors = clean_authors(info[0].string)
        authors = authors.replace('I Birol', '**I Birol**')
        	    
        #journal name	
        [x.extract() for x in info[1].find_all('span')]
        journal = clean_journal(info[1].string)
        
        citation = authors + '. ' + name + '. ' + date + '. [_' + journal + '_](' + link + ') \n\n' 
        my_file.write(citation.encode('utf-8'))

    my_file.close()
	

