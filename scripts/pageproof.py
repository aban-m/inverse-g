import os
from shutil import copy
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

if not os.path.exists('pageproof'):
    print(f'No directory pageproof, creating...')
    os.mkdir('pageproof')

count = len([f for f in os.listdir('pageproof') if f.lower().startswith('pure')])

copy('ren.pdf', f'pageproof/pure-{count + 1}.pdf')

print('Copied successfully.')
