"""

Converts codelist files from external sources into the format used by IATI.

Note not all external codelists are converted automatically yet.

"""

from lxml import etree as ET

# Adapted from code at http://effbot.org/zone/element-lib.htm
def indent(elem, level=0, shift=2):
    i = "\n" + level*" "*shift
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "*shift
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1, shift)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

"""

IANA Media Types (FileFormat)

"""

template = ET.parse('templates/FileFormat.xml', ET.XMLParser(remove_blank_text=True))
codelist_items = template.find('codelist-items')

media_types = ET.parse('source/media-types.xml')
for registry in media_types.findall('{http://www.iana.org/assignments}registry'):
    registry_id = registry.attrib['id']
    for record in registry.findall('{http://www.iana.org/assignments}record'):
        codelist_item = ET.Element('codelist-item')

        code = ET.Element('code')
        code.text = registry_id + '/' + record.find('{http://www.iana.org/assignments}name').text
        codelist_item.append(code)

        category = ET.Element('category')
        category.text = registry_id
        codelist_item.append(category)

        codelist_items.append(codelist_item)

indent(template.getroot(), 0, 4)
template.write('xml/FileFormat.xml', pretty_print=True)



"""

ISO Country Alpha 2

"""

XML_LANG = '{http://www.w3.org/XML/1998/namespace}lang'

template = ET.parse('templates/Country.xml', ET.XMLParser(remove_blank_text=True))
codelist_items = template.find('codelist-items')

countries = ET.parse('source/iso_country_codes.xml')
for country in countries.findall('country'):
    if country.find('status').text == 'officially-assigned':
        codelist_item = ET.Element('codelist-item')

        code = ET.Element('code')
        code.text = country.find('alpha-2-code').text
        codelist_item.append(code)
        
        name = ET.Element('name')
        codelist_item.append(name)
        for short_name in country.findall('short-name'):
            if XML_LANG in short_name.attrib:
                narrative = ET.Element('narrative')
                narrative.attrib[XML_LANG] = short_name.attrib[XML_LANG]
                narrative.text = short_name.text
                name.append(narrative)

        description = ET.Element('description')
        codelist_item.append(description)
        for full_name in country.findall('full-name'):
            if XML_LANG in full_name.attrib:
                narrative = ET.Element('narrative')
                narrative.attrib[XML_LANG] = full_name.attrib[XML_LANG]
                narrative.text = full_name.text
                description.append(narrative)

        codelist_items.append(codelist_item)

indent(template.getroot(), 0, 4)
template.write('xml/Country.xml', pretty_print=True)

