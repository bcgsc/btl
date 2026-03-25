#!/usr/bin/env python
'''
Generate and update the software-content.html file for birollab.ca
3-column layout with category headings from the last line of each software TXT.
'''
import glob
import os
import sys
from collections import defaultdict

# HTML elements
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
    """Format string with installation options"""
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
    """Write the software-content.html file with 3 columns and category headings"""
    # Organize tools by category
    categories = defaultdict(list)

    for my_file in sorted(glob.glob("*.txt")):
        with open(my_file, 'r') as fin:
            lines = [line.strip() for line in fin.readlines()]

            if len(lines) < 8:
                print(f"Skipping {my_file}, not enough lines")
                continue

            logofile, name, github, linuxbrew, bioconda, docker, desc, category = lines[:8]
            categories[category].append((logofile, name, github, linuxbrew, bioconda, docker, desc))

    # Write HTML
    with open(os.path.join(softwareblurbs_path, "../_includes/software-content.html"), "w+") as software:
        for category in sorted(categories.keys()):
            # Add category heading
            software.write(f'<tr><td colspan="3"><h3>{category}</h3></td></tr>\n')

            i = 0
            for tool in categories[category]:
                logofile, name, github, linuxbrew, bioconda, docker, desc = tool

                if i % 3 == 0:
                    software.write("<tr>\n")

                html = START + logofile + P1 + name + P2 + github + P3 + \
                       downloads(linuxbrew, bioconda, docker) + P4 + desc + END
                software.write(html)

                if i % 3 == 2:
                    software.write("</tr>\n")
                i += 1

            # Pad last row if not multiple of 3
            if i % 3 != 0:
                remaining = 3 - (i % 3)
                for _ in range(remaining):
                    software.write("<td></td>")
                software.write("</tr>\n")

            software.write("\n")

def main():
    """Generate the birollab.ca software html"""
    if len(sys.argv[1:]) != 1:
        print("Usage:", sys.argv[0], "<Full path to softwareblurbs directory>")
        sys.exit()

    softwareblurbs_path = sys.argv[1]
    os.chdir(softwareblurbs_path)

    write_html(softwareblurbs_path)

if __name__ == "__main__":
    main()
