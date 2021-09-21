#!/usr/bin/env python

import glob, os

os.chdir("../softwareblurbs")
software = open("../_includes/software-content.html", "w+")

start = '<td><img class="software-logo" src="assets/logos/'
p1 = '"><span class="software-title">'
p2 = ' <a href="'
p3 = '"><img class="git" src="assets/githubicon.svg"></a></span>'

ds = '<div style="text-align:center;"><div class="downloadinfo">'
d1 = '<br>{% include linuxbrew-icon.html%}'
d2 = '<br>{% include bioconda-icon.html%}'
d3 = '<br>{% include docker-icon.html%}'
de = '</div></div>'

p4 = '<p style="padding-top:0">'
end= '</p></td>'

i = 0

def downloads(lin, bio, dock):
    if not lin and not bio and not dock: return ''
    else: return ds + ((d1 + lin) if lin else '') + ((d2 + bio) if bio else '') + ((d3 + dock) if dock else '') + de

for myfile in sorted(glob.glob("*.txt")):
    f = open(myfile)

    info = []
    for x in range(0,8):
        info.append(f.readline().strip())
        if x == 8:
            info.append(f.read().strip())

    logofile = info[0]
    name = info[1]
    github = info[2]
    linuxbrew = info[3]
    bioconda = info[4]
    docker = info[5]
    desc = info[6]

    if i % 2 is 0:
        software.write("<tr>")

    html = start + logofile + p1 + name + p2 + github + p3 + downloads(linuxbrew, bioconda, docker) + p4 + desc + end
    software.write(html)

    if i % 2 is 1:
        software.write("</tr>")

    software.write("\n\n")
    i += 1

software.seek(0, os.SEEK_END)
software.seek(software.tell()-7, os.SEEK_SET)

if i % 2 is 0:
   software.write("</tr>")

software.close()
