# encoding: utf-8
#----------------------------------------------------------------------
# Author: HieuHT
# Email: hieuht@vnoss.org
#----------------------------------------------------------------------
from urlparse import urlparse
from hmodule import hrequest
import sys
from os import system
import string
import re
from urllib2 import Request, HTTPError, urlopen
#----------------------------------------------------------------------
# URL TEST
#url = 'http://mp3.zing.vn/album/Nhac-Viet-Moi-Thang-08-2013-Various-Artists/ZWZAD9IZ.html'
#url = 'http://www.nhaccuatui.com/bai-hat/mat-em-trong-doi-the-men.uXN1cMeRQCZn.html'
#url = 'http://www.keeng.vn/album/Hit-Tuan-02-Thang-08-2013-Nhieu-Ca-Sy-nhieu-ca-sy/TWXC7MG7.html'
#url = 'http://www.keeng.vn/audio/Mat-Em-Trong-Doi-The-Men-320Kbps/E0CLL1DV.html'
#url = 'http://nhacso.net/nghe-album/anh-rat-yeu-em.WV1WU0ZZ.html'
#url = 'http://nhacso.net/nghe-nhac/hanh-phuc-do-em-khong-co.X1pYUUFdbw==.html'
#url = 'http://nhac.vui.vn/album-em-muon-remix-bich-phuong-a28962p1023.html'
#url = 'http://nhac.vui.vn/nguoi-toi-yeu-chi-dan-m304833c2p8224a25588.html'
#----------------------------------------------------------------------
def wget(url, file_name):
    try:
        u = urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
    except HTTPError, e:    
        print "Error: " + str(e.code)

if len(sys.argv) > 1:
    url = sys.argv[1]
    print "Download: " + url
    domain = urlparse(url).netloc.replace('.', '').replace('www', '')
    h = hrequest.hrequest()
    if domain:    
        from hsite import *
        cookie, html = h.request(url, data=None, HTMLResponse=True)
        try:
            domain = eval(domain)
            mp3 = domain.MP3(html)
            hlist = mp3.parse()
            for item in hlist:
                title, artist, source = item
                source = source.strip()
                print "\t[+] " + title.strip()
                file_name = title.strip().replace(' ', '-')
                wget(source, file_name)
        except:
            print 'Can not parse ' + str(domain)    
else:
    sys.exit(1)