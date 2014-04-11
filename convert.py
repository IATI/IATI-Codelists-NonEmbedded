from lxml import etree as ET

template = ET.parse('templates/FileFormat.xml', ET.XMLParser(remove_blank_text=True))
codelist_items = template.find('codelist-items')

media_types = ET.parse('source/media-types.xml')
for registry in media_types.findall('{http://www.iana.org/assignments}registry'):
    registry_id = registry.attrib['id']
    for record in registry.findall('{http://www.iana.org/assignments}record'):
        code = ET.Element('code')
        code.text = registry_id + '/' + record.find('{http://www.iana.org/assignments}name').text
        codelist_item = ET.Element('codelist-item')
        codelist_item.append(code)
        codelist_items.append(codelist_item)

template.write('xml/FileFormat.xml', pretty_print=True)

