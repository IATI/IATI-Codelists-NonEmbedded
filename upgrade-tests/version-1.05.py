import tests

#Test Policy Significance codelist changes
filepath = "../xml/PolicySignificance.xml"
print (filepath)
tests.check_value_exists(filepath,'//codelist-items/codelist-item/name/text()','Explicit primary objective') 
tests.check_value_exists(filepath,'//codelist-items/codelist-item/code/text()','4')
#Maybe need a check that there should/shouldn't be a description


