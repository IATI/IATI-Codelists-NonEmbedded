# coding=UTF-8
import tests

#http://support.iatistandard.org/entries/60789269-IATIOrganisationIdentifier-codelist
#Test New IATIOrganisationIdentifier codelist
filepath = "../xml/IATIOrganisationIdentifier.xml"
print (filepath)

tests.check_value_exists(filepath,'//metadata/name/narrative/text()','IATI Organisation Identifier','metadata') 
tests.check_value_exists(filepath,'//metadata/description/narrative/text()',"\n            This is a list of organisation identifiers that is maintained by the IATI Secretariat.\n            The prefix for organisations on this list is XI-IATI \n            Any publisher may apply to the IATI Technical Team for an identifier to be generated.\n            While some of these identifiers have been derived from DAC codes, this 'meaning' is not carried forward. i.e. IATI generated identifiers have no intrinsic meaning.\n            \n            For general guidance about constructing Organisation Identifiers, please see http://iatistandard.org/organisation-identifiers/\n            ",'metadata') 
