import time
import sys
from tqdm import trange


def do_something():
    #time.sleep(1)
    pass

def do_another_something():
    #time.sleep(1)
    pass


for i in trange(10, file=sys.stdout, desc='outer loop'):
    do_something()

    #for j in trange(100,file=sys.stdout, leave=False, unit_scale=True, desc='inner loop'):
        #do_another_something()