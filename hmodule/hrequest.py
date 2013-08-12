# encoding: utf-8
#----------------------------------------------------------------------
# Author: HieuHT
# Email: hieuht@vnoss.org
#----------------------------------------------------------------------
import json
from urllib2 import Request, HTTPCookieProcessor, HTTPHandler, build_opener, urlopen, URLError
from urllib import urlencode
from cookielib import CookieJar
from datetime import datetime
from StringIO import StringIO
import sys
########################################################################
class hrequest:
    def __init__(self):
        self.hr_cookie = CookieJar()
        self.hr_opener = build_opener(HTTPCookieProcessor(self.hr_cookie), HTTPHandler())
        self.hr_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0','Referer': 'https://www.facebook.com/'}
    #----------------------------------------------------------------------
    def request(self, url, data, HTMLResponse=True):
        if data:            
            hr_data = urlencode(data)
        else:
            hr_data = None
        try:            
            hr_request = Request(url, data=hr_data, headers=self.hr_headers)
            hr_response = self.hr_opener.open(hr_request)
            if HTMLResponse:
                hr_html = hr_response.read()
                return self.hr_cookie, hr_html
            else:
                return 
        except URLError, e:
            print e
            sys.exit()