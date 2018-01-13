from bs4 import BeautifulSoup
files = ['one.html','two.html', 'three.html','4.html'] 
journal = 'A Bunch of Journal Info 420-666'

for filename in files:

    soup2 = BeautifulSoup(open(filename).read(),"lxml")
    link = soup2.find('div', {'class':'gsc_vcd_title_ggi'}).find('a').attrs['href']

    citation = 'AuthorAndNameData' + '2918 Jan 32' + '. [_' + journal + '_](' + link + ') \n\n' 
    print citation
