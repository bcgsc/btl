#!/usr/bin/env python
'''
Generate and update the software-content.html file for birollab.ca
'''
import glob
import os
import sys

# Defining different html elements
START = '<td><img class="software-logo" src="assets/logos/'
P1 = '"><span class="software-title">'
P2 = ' <a href="'
P3 = '"><img class="git" src="assets/githubicon.svg"></a></span>'

DIV_START = '<div style="text-align:center;"><div class="downloadinfo">'
LINUXBREW_DIV = '<br>{% include linuxbrew-icon.html%}'
CONDA_DIV = '<br>{% include bioconda-icon.html%}'
DOCKER_DIV = '<br>{% include docker-icon.html%}'
DIV_END = '</div></div>'

P4 = '<p style="padding-top:0">'
END = '</p></td>'

def downloads(lin, bio, dock):
    "Format string with installation options"
    return_string = ""
    if not lin and not bio and not dock:
        return return_string
    return_string += DIV_START
    if lin:
        return_string += (LINUXBREW_DIV + lin)
    if bio:
        return_string += (CONDA_DIV + bio)
    if dock:
        return_string += (DOCKER_DIV + dock)
    return return_string + DIV_END


def write_html(softwareblurbs_path):
    "Write the software-content.html file"
    i = 0

    with open(softwareblurbs_path + "/../_includes/software-content.html", "w+") as software:
        for my_file in sorted(glob.glob("*.txt")):
            with open(my_file, 'r') as fin:
                lines = [line.strip() for line in fin.readlines()]

                logofile, name, github, linuxbrew, bioconda, docker, desc = lines[:7]

                if i % 2 == 0:
                    software.write("<tr>")

                html = START + logofile + P1 + name + P2 + github + P3 +\
                    downloads(linuxbrew, bioconda, docker) + P4 + desc + END
                software.write(html)

                if i % 2 == 1:
                    software.write("</tr>")

                software.write("\n\n")
                i += 1

        software.seek(0, os.SEEK_END)
        software.seek(software.tell()-7, os.SEEK_SET)

        if i % 2 == 0:
            software.write("</tr>")


def main():
    "Generate the birollab.ca software html"
    if len(sys.argv[1:]) != 1:
        print("Usage:", sys.argv[0], "<path to softwareblurbs directory>")
        sys.exit()

    softwareblurbs_path = sys.argv[1]
    os.chdir(softwareblurbs_path)

    write_html(softwareblurbs_path)


if __name__ == "__main__":
    main()
