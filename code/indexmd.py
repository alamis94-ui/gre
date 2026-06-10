# Replace any empty _index.md files with a stub file,
# using the template at archetypes/place.md
#
# NOTE: this script should be run from the main gre directory:
#     python code/indexmd.py

import os
import re
import subprocess

def run(s):
    """Run the command"""
    if s:
        subprocess.run(s, shell=True)

for root, dirs, files in os.walk('content/place'):
    for f in files:
        if f == '_index.md':
            p = os.path.join(root, f)
            if os.path.getsize(p) == 0:
                p = p.replace('content.place', 'content place')
                run(f'hugo new content {p} -k place -f')

    # make sure sublocation exists
    if 0:
        spath = os.path.join('content', 'place', p, s, '_index.md')
        if not os.path.exists(spath) or os.path.getsize(spath)==0:
            run(f'hugo new content place/{p}/{s}/_index.md -k place -f')
        # create the garden
        if g:
            run(f'hugo new content place/{p}/{s}/{g}.md -k garden')
