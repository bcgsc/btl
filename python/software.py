import glob, os

os.chdir("../softwareblurbs")
software = open("../_includes/software-content.html", "w+")

start = '<td><img class="software-logo" src="assets/logos/'
p1 = '"><span class="software-title">'
p2 = ' <a href="'
p3 = '"><img class="git" src="assets/githubicon.svg"></a></span><p>'
end= '</p></td>'

i = 0

for myfile in sorted(glob.glob("*.txt")):
    f = open(myfile)

    info = []	
    for x in range(0,5):
	    info.append(f.readline().strip())
	    if x == 5: 
		    info.append(f.read().strip())

    logofile = info[0]
    github = info[1]
    name = info[2]
    desc = info[3]

    if i%2 is 0: 
        software.write("<tr>")

    html = start + logofile + p1 + name + p2 + github + p3 + desc + end
    software.write(html)
    
    if i%2 is 1:
        software.write("</tr>")
    
    software.write("\n\n")
    i += 1
    
software.seek(-7,2) 

if i%2 is 0:
   software.write("</tr>") 

software.close()






