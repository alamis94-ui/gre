# Generate a bunch of stub articles from the stubs.csv file
# also generate any province/sublocation pages that don't already exist
#
# NOTE: this script should be run from the main gre directory:
#     python code/stubs.py
#
# The input.csv file (in the code directory) should be structured as follows:
#
# province,sublocation,garden
# Aegyptus,Alexandria,Kanopos
# Aegyptus,Alexandria,Three Tomb Gardens at Kanopos
# Aegyptus,Fayum,Vineyard at Theadelphia
#
# Given that input, the following files will be created (if they don't already exist)
# 
# /content/place/aegyptus/_index.md
# /content/place/aegyptus/alexandria/_index.md
# /content/place/aegyptus/alexandria/kanopos.md
# /content/place/aegyptus/alexandria/three_tomb_gardens_at_kanopos.md
# /content/place/aegyptus/fayum/_index.md
# /content/place/aegyptus/fayum/vinyard_at_theadelphia.md
# 

import os
import re
import csv
import subprocess

def pathize(s):
    """Convert the string into a simplified for a file path"""
    # lowercase, with all punctuation (except hyphens) converted to underscores
    if s:
        return re.sub(r'[^\w-]+', '_', s.lower().strip())
    
def run(s):
    """Run the command"""
    if s:
        subprocess.run(s, shell=True)

with open('code/stubs.csv', newline='') as f:
    for r in csv.DictReader(f):
        p = pathize(r['province'])
        s = pathize(r['sublocation'])
        g = pathize(r['garden'])

        # make sure province exists
        ppath = os.path.join('content', 'place', p, '_index.md')
        if not os.path.exists(ppath):
            run(f'hugo new place/{p}/_index.md -k place')

        # make sure sublocation exists
        if s:
            spath = os.path.join('content', 'place', p, s, '_index.md')
            if not os.path.exists(spath):
                run(f'hugo new place/{p}/{s}/_index.md -k place')
            # create the garden
            if g:
                run(f'hugo new place/{p}/{s}/{g}.md -k garden --quiet')
        
        # or make a garden without a sublocation
        elif g:
            run(f'hugo new place/{p}/{g}.md -k garden --quiet')
