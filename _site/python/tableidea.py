import glob, os

os.chdir("../softwareblurbs")

software = open("../software.html", "w+")
software.write('---\n layout: default \n title: Software \n --- <!DOCTYPE html><html><head><title>Software</title></head><body> <table>')

for file in glob.glob("*.txt"):

	f=open("../softwareblurbs/nthash.txt")

	info = []	
	for x in range(0,5):
		info.append(f.readline().strip())
		if x==5: 
			info.append(f.read().strip())

	idname = info[0]
	logo = info[1]
	github = info[2]
	name = info[3]
	desc = info[4]

	html = '<tr class = "software" id="'+ idname + '"> <td class = "logo" id="' + idname + '"><img src="' + logo + '"></td> 	<td><strong>' + name + '</strong></td> <td>' + desc + '\n Github link:'+ github + '</td></tr>'

	software.write(html)

software.write('</table></body></html>')
software.close()
