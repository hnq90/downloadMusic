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
########################################################################
class MP3:
    #----------------------------------------------------------------------
    def __init__(self, HTML):
        try:
            regex_xml = search(r'xmlPath=(.+?)&adsLink', HTML)
            xml_file = regex_xml.group(1)
            h = hrequest.hrequest()
            cookie, xml_data = h.request(xml_file, data=None, HTMLResponse=True)
            self.xml_data = xml_data
        except:
            print 'Can not get xml data file'
            sys.exit(1)
    #----------------------------------------------------------------------
    def parse(self):
        litem = []
        tree = etree.parse(StringIO(self.xml_data))
        try:            
            items = tree.findall('//song')
            for item in items:
                try:                
                    name = item.find('name').text
                    artist = item.find('artist').text
                    mp3link = item.find('mp3link').text
                    item_data = (name, artist, mp3link)
                    litem.append(item_data)
                except:
                    print 'Can not parse xml item'
            return litem
        except:
            print 'Can not parse xml data'
            sys.exit(1)
            