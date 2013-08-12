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
            regex_xml = search(r'\'playlistfile\': \'(.+?)\',', HTML)
            xml_file = regex_xml.group(1)
            xml_file = 'http://hn.nhac.vui.vn' + xml_file
            h = hrequest.hrequest()
            cookie, xml_data = h.request(xml_file, data=None, HTMLResponse=True)
            self.xml_data = xml_data.replace('jwplayer:file', 'jwplayerfile')
        except:
            print 'Can not get xml data file'
            sys.exit(1)
    #----------------------------------------------------------------------
    def parse(self):
        litem = []
        tree = etree.parse(StringIO(self.xml_data))
        try:            
            items = tree.findall('//item')
            for item in items:
                try:                
                    title = item.find('title').text
                    description = item.find('description').text
                    jwplayerfile = item.find('jwplayerfile').text
                    item_data = (title, description, jwplayerfile)
                    litem.append(item_data)
                except:
                    print 'Can not parse xml item'
            return litem
        except:
            print 'Can not parse xml data'
            sys.exit(1)
            