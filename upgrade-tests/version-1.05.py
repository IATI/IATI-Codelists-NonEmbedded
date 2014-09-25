from __future__ import print_function
import sys
from lxml import etree as ET

#  
#  name: check_value_exists
#  @param filepath      Path to the codelist wee want to check
#  @param xpathString   xpath to the element we want to check
#  @param value         The value we want to check the existence of
#  @return yes/no
# 
def check_value_exists (filepath, xpathString, value):
  
  for items in ET.parse(filepath).getroot().findall('codelist-items'):
    values = items.xpath(xpathString)
    #print (', '.join(values))
    if value in values:
      print ('pass')
    else:
      print ('fail')

#  
#  name: check_value_does_not_exists
#  @param filepath      Path to the codelist wee want to check
#  @param xpathString   xpath to the element we want to check
#  @param value         The value we want to check does not exists
#  @return yes/no
#  

def check_value_does_not_exist (filepath, xpathString, value):
  
  for items in ET.parse(filepath).getroot().findall('codelist-items'):
    values = items.xpath(xpathString)
    #print (', '.join(values))
    if value in values:
      print ('fail')
    else:
      print ('pass')


#Test Policy Significance codelist changes
filepath = "../xml/PolicySignificance.xml"
print (filepath)
check_value_exists(filepath,'//codelist-items/codelist-item/name/text()','Explicit primary objective') 
check_value_exists(filepath,'//codelist-items/codelist-item/code/text()','4')
#Maybe need a check that there should/shouldn't be a description


