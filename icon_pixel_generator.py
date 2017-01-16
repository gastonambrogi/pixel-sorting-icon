from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
import os

flikr = 'http://www.flickr.com'
header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '+
        '(KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'
}
    
requ = Request(flikr+"/explore/interesting/7days/", headers=header)
soup = BeautifulSoup(urlopen(requ).read(), "lxml")
imgs = soup.findAll('img', "pc_img")

for qi, query in enumerate(imgs):
            
    requ = Request(flikr+query.parent['href']+'sizes/s/', headers=header)
    soup = BeautifulSoup(urlopen(requ).read(), "lxml")

    os.system('wget --no-check-certificate %s -O temp' % 
    soup.findAll('img')[2]['src'])

    import numpy as np
    import scipy.misc as misc

    img = misc.imread('temp')
    img = misc.imresize(img, (16, 16), 'nearest')
    img = np.sort(img, axis=0)
    img = misc.imresize(img, (64, 64), 'nearest')
    misc.imsave('icon_%03i.png' % qi, img)

    os.system('rm temp')
