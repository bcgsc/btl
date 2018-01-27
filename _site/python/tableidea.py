import glob, os

os.chdir("../softwareblurbs")

#software = open("/_includes/software-content.html", "w+")
software = open("thing.txt", "w+")

for myfile in glob.glob("*.txt"):
    f = open(myfile)

    info = []	
    for x in range(0,5):
	    info.append(f.readline().strip())
	    if x == 5: 
		    info.append(f.read().strip())

    idname = info[0]
    logo = info[1]
    github = info[2]
    name = info[3]
    desc = info[4]

    html = name + '\n' + desc + ' <a href = "' + github + '">See on Github</a>'
    software.write(html)

software.close()


'''
    html = '<tr class = "software" id="'+ idname + '"> <td class = "logo" id="' + idname + '"><img style="width:200px;height=auto;" src="' + logo + '"></td><td><strong>' + name + '</strong></td><td>' + desc + ' <a href = "' + github + '">See on Github</a></td></tr>'
'''
