#!/usr/bin/env python
'''
Generate and update the software-content.html file for birollab.ca
3-column layout with aligned install blocks and improved styling.
'''
import glob
import os
import sys
from collections import defaultdict

# HTML elements
TD_START_BASE = 'style="vertical-align:top; padding:6px; word-break:break-word; overflow-wrap:anywhere;"'
START = '<img class="software-logo" src="assets/logos/'
P1 = '"><span class="software-title" style="white-space:nowrap;">'
P2 = ' <a href="'
P3 = '"><img class="git" src="assets/githubicon.svg"></a></span>'

# Install block styling
DIV_START = '<div style="text-align:center; margin-top:4px;">'
LINE_STYLE = 'style="font-size:12px; font-family:monospace; height:18px; line-height:18px; white-space:nowrap;"'

LINUXBREW_ICON = '{% include linuxbrew-icon.html%}'
CONDA_ICON = '{% include bioconda-icon.html%}'
DOCKER_ICON = '{% include docker-icon.html%}'

DIV_END = '</div>'

# Bold description
P4 = '<p style="padding-top:4px; margin:0; font-weight:bold;">'
END = '</p></td>'

def line(icon, text):
    if text:
        return f'<div {LINE_STYLE}>{icon} {text}</div>'
    else:
        return f'<div {LINE_STYLE}>&nbsp;</div>'

def downloads(lin, bio, dock):
    return (
        DIV_START +
        line(LINUXBREW_ICON, lin) +
        line(CONDA_ICON, bio) +
        line(DOCKER_ICON, dock) +
        DIV_END
    )


def write_html(softwareblurbs_path):
    categories = defaultdict(list)

    for my_file in sorted(glob.glob("*.txt")):
        with open(my_file, 'r') as fin:
            lines = [line.strip() for line in fin.readlines()]

            if len(lines) < 8:
                print(f"Skipping {my_file}, not enough lines")
                continue

            logofile, name, github, linuxbrew, bioconda, docker, desc, category = lines[:8]
            categories[category].append((logofile, name, github, linuxbrew, bioconda, docker, desc))

    with open(os.path.join(softwareblurbs_path, "../_includes/software-content.html"), "w+") as software:

        # Add hover + row separator styles once
        software.write('''
<style>
td.software-cell:hover { background-color:#F5F9FF; cursor:pointer; }
tr.software-row { border-bottom:1px solid #E5E5E5; }
</style>
''')

        software.write('<table style="width:100%; table-layout:fixed; border-collapse:collapse;">\n')

        for category in sorted(categories.keys()):
            software.write(
                '<tr>'
                '<td colspan="3" style="background-color:#DCEEFF; '
                'padding:10px; font-weight:bold; font-size:20px; color:black;">'
                f'{category}'
                '</td>'
                '</tr>\n'
            )

            i = 0
            for tool in categories[category]:
                logofile, name, github, linuxbrew, bioconda, docker, desc = tool

                if i % 3 == 0:
                    software.write('<tr class="software-row">\n')

                # ✅ Clickable cell via onclick (no nested <a> issue)
                TD_START = f'<td class="software-cell" onclick="window.open(\'{github}\', \'_blank\')" {TD_START_BASE}>'

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

            if i % 3 != 0:
                remaining = 3 - (i % 3)
                for _ in range(remaining):
                    software.write('<td></td>')
                software.write("</tr>\n")

            software.write("\n")

        software.write('</table>\n')


def main():
    if len(sys.argv[1:]) != 1:
        print("Usage:", sys.argv[0], "<Full path to softwareblurbs directory>")
        sys.exit()

    softwareblurbs_path = sys.argv[1]
    os.chdir(softwareblurbs_path)

    write_html(softwareblurbs_path)


if __name__ == "__main__":
    main()
