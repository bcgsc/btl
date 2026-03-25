#!/usr/bin/env python
'''
Generate and update the software-content.html file for birollab.ca
3-column layout with category headings, proper wrapping, and alignment.
'''
import glob
import os
import sys
from collections import defaultdict

# HTML elements
TD_START = '<td style="vertical-align:top; word-break:break-word; overflow-wrap:anywhere;">'
START = '<img class="software-logo" src="assets/logos/'
P1 = '"><span class="software-title" style="white-space:nowrap;">'
P2 = ' <a href="'
P3 = '"><img class="git" src="assets/githubicon.svg"></a></span>'

DIV_START = '<div style="text-align:center;"><div class="downloadinfo" style="word-break:break-word;">'
LINUXBREW_DIV = '<br>{% include linuxbrew-icon.html%}'
CONDA_DIV = '<br>{% include bioconda-icon.html%}'
DOCKER_DIV = '<br>{% include docker-icon.html%}'
DIV_END = '</div></div>'

P4 = '<p style="padding-top:0">'
END = '</p></td>'

def downloads(lin, bio, dock):
    """Format string with installation options, preserving alignment"""
    return_string = DIV_START

    if lin:
        return_string += (LINUXBREW_DIV + lin)
    else:
        return_string += "<br>&nbsp;"

    if bio:
        return_string += (CONDA_DIV + bio)
    else:
        return_string += "<br>&nbsp;"

    if dock:
        return_string += (DOCKER_DIV + dock)
    else:
        return_string += "<br>&nbsp;"

    return return_string + DIV_END


def write_html(softwareblurbs_path):
    """Write the software-content.html file with 3 columns and highlighted category headings"""
    categories = defaultdict(list)

    # Read tools
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

        # Ensure table behaves within page width
        software.write('<table style="width:100%; table-layout:fixed;">\n')

        for category in sorted(categories.keys()):
            # Highlighted header row (no nowrap!)
            software.write(
                '<tr>'
                '<td colspan="3" style="background-color:#87C1F9; '
                'padding:10px; font-weight:bold;">'
                f'{category}'
                '</td>'
                '</tr>\n'
            )

            i = 0
            for tool in categories[category]:
                logofile, name, github, linuxbrew, bioconda, docker, desc = tool

                if i % 3 == 0:
                    software.write("<tr>\n")

                html = (
                    TD_START +
                    START + logofile + P1 + name + P2 + github + P3 +
                    downloads(linuxbrew, bioconda, docker) +
                    P4 + desc + END
                )

                software.write(html)

                if i % 3 == 2:
                    software.write("</tr>\n")

                i += 1

            # Pad final row
            if i % 3 != 0:
                remaining = 3 - (i % 3)
                for _ in range(remaining):
                    software.write('<td></td>')
                software.write("</tr>\n")

            software.write("\n")

        software.write('</table>\n')


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
