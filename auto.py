#!/usr/bin/python3
import random
import os


# Ruta absoluta del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta absoluta de themes.txt
themes_path = os.path.join(script_dir, "themes.txt")



with open(themes_path, "r") as file:
    themes = file.readlines()
    theme = random.choice(themes).strip()


bashrc_path = os.path.expanduser("~/.bashrc")

new_theme = f'eval "$(oh-my-posh init bash --config ~/.cache/oh-my-posh/themes/{theme})"\n'

with open(bashrc_path, "r") as bash:
    lines = bash.readlines()
    line_found = None
    for index, line in enumerate(lines):
        if "oh-my-posh init bash" in line:
            line_found = index
            break

    if line_found is not None:
        lines[line_found] = new_theme
    else:
        lines.append(new_theme)


with open(bashrc_path, "w") as bash:
    for line in lines:
        bash.write(line)




