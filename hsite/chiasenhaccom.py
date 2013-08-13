# encoding: utf-8
#----------------------------------------------------------------------
# Author: HieuHT
# Email: hieuht@vnoss.org
#----------------------------------------------------------------------
from re import search, findall
from hmodule import hrequest
import sys
from lxml import etree
from StringIO import StringIO
from urllib import unquote
########################################################################
class MP3:
    #----------------------------------------------------------------------
    def __init__(self, HTML):
        self.HTML = HTML
    #----------------------------------------------------------------------
    def parse(self):
        litem = []
        try:            
            regex_title = search(r'<title>(.+?)</title>', self.HTML)
            group_data = regex_title.group(1).replace('~', '-').split(' - ')
            title = group_data[0]
            artist = group_data[1]
            regex_source = search(r'"file": decodeURIComponent\("(.+?)"\),', self.HTML)
            source = unquote(regex_source.group(1))
            item_data = (title, artist, source)
            litem.append(tuple(item_data))
            return litem
        except:
            print 'Can not parse xml data'
            sys.exit(1)