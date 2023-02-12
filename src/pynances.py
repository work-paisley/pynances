#!/usr/bin/env python3

import os

import yaml

from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def render(data, context, template_file, ofile):
    print(f'Rendering {ofile}')
    template_dir = '.'
    env = Environment(loader=FileSystemLoader(template_dir))

    j2_template = env.get_template(os.path.basename(template_file))
    with open(ofile, 'w') as f:
        f.write(j2_template.render(data=data, context=None))



with open('finances.yml', 'r') as f:
    data = yaml.safe_load(f)

print(data)
render(data, None, 'finances.j2html', 'finances.html')


