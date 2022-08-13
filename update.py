import os
from time import sleep

def update_readme():

    os.system('git status')

    sleep(0.5)

    os.system('git add -A')

    sleep(0.5)

    os.system('git status')

    sleep(0.5)

    os.system('git commit -m "update"')

    sleep(0.5)
    
    os.system('git push')


update_readme()
