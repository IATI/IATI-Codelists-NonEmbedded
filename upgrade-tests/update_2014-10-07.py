# coding=UTF-8
import tests

#http://support.iatistandard.org/entries/51952869-Organisational-Identifier-Finland
#Test Organisation Registration Agency codelist changes
filepath = "../xml/OrganisationRegistrationAgency.xml"
print (filepath)

tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "FI-PRO"]/@public-database','1') 
tests.check_value_exists(filepath,'//codelist-items/codelist-item/code/text()','FI-PRO')
tests.check_value_exists(filepath,'//codelist-items/codelist-item/category/text()','FI')
tests.check_value_exists(filepath,'//codelist-items/codelist-item/name/text()','Finnish Patent and Registration office') 
tests.check_value_exists(filepath,'//codelist-items/codelist-item/url/text()','http://www.prh.fi/en/index.html')
#Check that there isn't a description
tests.check_element_is_empty(filepath,'//codelist-items/codelist-item[code = "FI-PRO"]/description/text()') 
 
 
#http://support.iatistandard.org/entries/96520726-Collaboration-Type-addition-of-code-7
filepath = "../xml/CollaborationType.xml"
print (filepath)
#Add code = 7
tests.check_value_exists(filepath,'//codelist-items/codelist-item/code/text()','7')
tests.check_value_exists(filepath,'//codelist-items/codelist-item/name/text()',"Bilateral, ex-post reporting on NGOs' activities funded through core contributions") 
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "7"]/name[@xml:lang = "fr"]/text()',"Contributions bilatérales, notification ex post des activités des ONG financées par des contributions des donneurs au budget général de l'ONG.") 
 
#More French translations
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "1"]/name[@xml:lang = "fr"]/text()',"Bilatéral")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "2"]/name[@xml:lang = "fr"]/text()',"Multilatéral")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "3"]/name[@xml:lang = "fr"]/text()',"Contributions bilatérales au budget général d'organisations non gouvernementales, d'autres organisations de la société civile, de partenariats publics-privés et d'instituts de recherches")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "4"]/name[@xml:lang = "fr"]/text()',"apports des agences multilatérales")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "6"]/name[@xml:lang = "fr"]/text()',"apports du secteur privé")
#..but there are no French descriptions
tests.check_element_is_empty(filepath,'//codelist-items/codelist-item/description[@xml:lang = "fr"]/text()') 

#http://support.iatistandard.org/entries/95684423-Region-codelist-out-of-date-with-DAC-CRS-source
#Test Region codelist changes
filepath = "../xml/Region.xml"
print (filepath)

#88 States Ex-Yugoslavia unspecified
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "88"]/name/text()',"States Ex-Yugoslavia unspecified")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "88"]/name[@xml:lang = "fr"]/text()',"Etats ex-Yougoslavie non spécifié")

#998 Developing countries, unspecified
tests.check_value_does_not_exist(filepath,'//codelist-items/codelist-item[code = "998"]/name/text()',"Bilateral, unspecified")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "998"]/name/text()',"Developing countries, unspecified")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "998"]/name[@xml:lang = "fr"]/text()',"Pays en développement, non spécifié")

#More French translations
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "89"]/name[@xml:lang = "fr"]/text()',"Europe, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "189"]/name[@xml:lang = "fr"]/text()',"Nord du Sahara, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "289"]/name[@xml:lang = "fr"]/text()',"Sud du Sahara, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "298"]/name[@xml:lang = "fr"]/text()',"Afrique, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "380"]/name[@xml:lang = "fr"]/text()',"Indes occ., régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "389"]/name[@xml:lang = "fr"]/text()',"Amérique N. & C., régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "489"]/name[@xml:lang = "fr"]/text()',"Amérique du Sud, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "498"]/name[@xml:lang = "fr"]/text()',"Amérique, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "589"]/name[@xml:lang = "fr"]/text()',"Moyen-Orient, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "619"]/name[@xml:lang = "fr"]/text()',"Asie centrale, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "679"]/name[@xml:lang = "fr"]/text()',"Asie du Sud, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "689"]/name[@xml:lang = "fr"]/text()',"Asie du Sud & C., régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "789"]/name[@xml:lang = "fr"]/text()',"Extrême-Orient, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "798"]/name[@xml:lang = "fr"]/text()',"Asie, régional")
tests.check_value_exists(filepath,'//codelist-items/codelist-item[code = "889"]/name[@xml:lang = "fr"]/text()',"Océanie, régional")

#http://support.iatistandard.org/entries/53429445-Registration-Agencies-Update-Descriptions-To-Remove-Updated-By-
#Test Region codelist changes
filepath = "../xml/OrganisationRegistrationAgency.xml"
print (filepath)

tests.check_value_does_not_exist(filepath,'//codelist-items/codelist-item[code = "US-DOS"]/description/text()',"Added by WR 15/10/2013")
tests.check_element_is_empty(filepath,'//codelist-items/codelist-item[code = "US-DOS"]/description/text()') 
tests.check_value_does_not_exist(filepath,'//codelist-items/codelist-item[code = "ZM-NRB"]/description/text()',"Added by WR 15/10/13. Only just set up in Spring 2013 and is currently facing a lot of objection")
tests.check_element_is_empty(filepath,'//codelist-items/codelist-item[code = "ZM-NRB"]/description/text()') 

