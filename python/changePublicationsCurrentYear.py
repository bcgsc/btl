from bs4 import SoupStrainer, BeautifulSoup
from datetime import datetime
import sys

def divwrap(wrapid):
    return soup.new_tag('div', **{"id":wrapid, "class":"tabcontent"})

def makebutton(tage):
    soup=BeautifulSoup(tage,'lxml;
    return BeautifulSoup(tage,'lxml').wrap(soup.new_tag('button', **{"class":"tablinks", "onClick":"openYear(event,'{0}'".format(tage)}))

year = int(sys.argv[1])
pubs = open('../pubdraft', 'w+')
soup = BeautifulSoup(open('publicationsource').read(), 'lxml')

categories = ["All"] + list(map(str, [year-1, year-2, year-3])) + ["Older"]

pubs.write('<script src="js/tabs.js">\n</script><div class = "tab">\n<button class="tablinks" onclick="openAll()">All</button>')
pubs.write('</div>\n<span style="font-size:13px"><em>For more details, see our page on <a href="https://scholar.google.ca/citations?user=Svk1wjsAAAAJ&hl=en">Google Scholar</a></em></span>')
pubs.write('{% include current-year-pubs.html %}'.wrap(divwrap(str(year))))

for cat in categories:
    pubs.write(soup.find_all('p',{"class":cat}).wrap(divwrap(cat)))
    
    
    
