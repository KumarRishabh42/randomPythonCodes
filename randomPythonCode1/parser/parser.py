from bs4 import BeautifulSoup
#from config import makedict
from itertools import *

def parser(raw_list):
		itex=iter([ i.text.replace(u'\xa0', u' ').encode('ascii').split('   ') for i in BeautifulSoup(raw_list).findAll('td') ])
		return [ i   for i in izip(itex,itex,itex)]
#return individualList


			

