# encoding: utf-8
#----------------------------------------------------------------------
# Author: HieuHT
# Email: hieuht@vnoss.org
#----------------------------------------------------------------------
from re import search, findall
from hmodule import hrequest
import sys
import xml.dom.minidom
from base64 import b64decode
from StringIO import StringIO
########################################################################
class MP3:
    #----------------------------------------------------------------------
    def __init__(self, HTML):
        try:
            self.HTML = HTML
            regex_link = search(r'<meta property="og:url" content="(.+?)" />', self.HTML)
            id_link = regex_link.group(1)
            id_link = id_link.split('/')[-1].replace('.html', '')
            xml_file = 'http://www.keeng.vn/album/get-album-xml?album_identify=' + id_link
            h = hrequest.hrequest()
            cookie, xml_data = h.request(xml_file, data=None, HTMLResponse=True)
            self.xml_data = xml_data 
        except:
            print 'Can not get xml data file'
            sys.exit(1)
    #----------------------------------------------------------------------
    def parse(self):
        try:            
            litem = []
            doc = xml.dom.minidom.parse(StringIO(self.xml_data))
            tracks = doc.getElementsByTagName('track')
            for track in tracks:
                title = track.getElementsByTagName('title')[0].childNodes[0].data
                creator = track.getElementsByTagName('creator')[0].childNodes[0].data
                location = track.getElementsByTagName('location')[0].childNodes[0].data
                item_data = (title, creator, location)
                litem.append(item_data)
            if litem == []:
                try:                    
                    regex_location = search(r'var audioPlayerLink = \"(.+?)\"\;', self.HTML)
                    regex_title = search(r'<title>(.+?)<\/title>', self.HTML)
                    title = regex_title.group(1).split('-')[0]
                    creator = regex_title.group(1).split('-')[1]
                    location = regex_location.group(1)
                    location = b64decode(location)
                    item_data = (title, creator, location)
                    litem.append(tuple(item_data))
                    return litem
                except:
                    print 'Can not get link audio'
            else:
                return litem
        except:
            print 'Can not parse xml data'
            sys.exit(1)        