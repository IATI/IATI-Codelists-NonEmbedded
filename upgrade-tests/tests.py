# coding=UTF-8
from __future__ import print_function
import sys
from lxml import etree as ET

#  
#  name: check_value_exists
#  @param filepath      Path to the codelist we want to check
#  @param xpathString   xpath to the element we want to check
#  @param value         The value we want to check the existence of
#  @return yes/no
# 
def check_value_exists (filepath, xpathString, value, root=None):
  if root is None:
    root = 'codelist-items'
  #print(root)
  for items in ET.parse(filepath).getroot().findall(root):
    values = items.xpath(xpathString)
    #print(values)
    #print (', '.join(values))
    if value.decode('utf-8') in values:
      print ('pass')
    else:
      print ('fail')

#  
#  name: check_value_does_not_exists
#  @param filepath      Path to the codelist we want to check
#  @param xpathString   xpath to the element we want to check
#  @param value         The value we want to check does not exists
#  @return yes/no
#  

def check_value_does_not_exist (filepath, xpathString, value):
  
  for items in ET.parse(filepath).getroot().findall('codelist-items'):
    values = items.xpath(xpathString)
    #print (', '.join(values))
    if value.decode('utf-8') in values:
      print ('fail')
    else:
      print ('pass')

#  
#  name: check_element_is_empty
#  @param filepath      Path to the codelist we want to check
#  @param xpathString   xpath to the element we want to check
#  @return yes/no
#

def check_element_is_empty (filepath, xpathString):

  for items in ET.parse(filepath).getroot().findall('codelist-items'):
    values = items.xpath(xpathString)
    #print (', '.join(values))
    if not values:
      print ('pass')
    else:
      print ('fail')


#  
#  name: check_element_is_not_empty
#  @param filepath      Path to the codelist we want to check
#  @param xpathString   xpath to the element we want to check
#  @return yes/no
#
def check_element_is_not_empty (filepath, xpathString):

  for items in ET.parse(filepath).getroot().findall('codelist-items'):
    values = items.xpath(xpathString)
    #print (', '.join(values))
    if not values:
      print ('fail')
    else:
      print ('pass')
