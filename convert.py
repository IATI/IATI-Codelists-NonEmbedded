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
        code.text = registry_id + '/' + record.find('{http://www.iana.org/assignments}name').text.split(' ')[0]
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

def add_code(code_text, country, withdrawn):
    codelist_item = ET.Element('codelist-item')

    if withdrawn:
        codelist_item.attrib['withdrawn'] = withdrawn

    code = ET.Element('code')
    code.text = code_text
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

countries = ET.parse('source/iso_country_codes.xml')
for country in countries.findall('country'):
    if country.find('status').text == 'officially-assigned':
        add_code(country.find('alpha-2-code').text, country, None)

# Ensure that historic codes come after current codes
for country in countries.findall('country'):
    if country.find('status').text in ['formerly-used', 'transitionally-reserved']:
        add_code(country.find('alpha-2-code').text, country, country.find('validity-end-date').text)
        add_code(country.find('alpha-4-code').text, country, country.find('validity-end-date').text)

indent(template.getroot(), 0, 4)
template.write('xml/Country.xml', pretty_print=True)



"""

ISO Currency Alpha Code

"""

template = ET.parse('templates/Currency.xml', ET.XMLParser(remove_blank_text=True))
codelist_items = template.find('codelist-items')

currency_codes = {}
for source_filename, historic in [ ('source/table_a1.xml', False), ('source/table_a3.xml', True) ]:
    country_currency_xml = ET.parse(source_filename)
    if historic:
        country_currencies = country_currency_xml.find('HstrcCcyTbl').findall('HstrcCcyNtry')
    else:
        country_currencies = country_currency_xml.find('CcyTbl').findall('CcyNtry')
    for country_currency in country_currencies:
        currency_name = country_currency.find('CcyNm').text
        if currency_name == 'No universal currency':
            continue
        currency_code = country_currency.find('Ccy').text
        if currency_code in currency_codes:
            if not currency_codes[currency_code][0] == currency_name:
                print 'Duplicate found for code {}, using name "{}" instead of name "{}" because it occurs first'.format(currency_code, currency_codes[currency_code], currency_name)
        else:
            currency_codes[currency_code] = (currency_name, country_currency.find('WthdrwlDt').text if historic else None)

# Ensure that historic codes come after current codes
for histroic_section in [False, True]:
    for currency_code, (currency_name, withdrawal_date) in sorted(currency_codes.items()):
        if (withdrawal_date is None) == histroic_section:
            continue
        codelist_item = ET.Element('codelist-item')
        if withdrawal_date:
            codelist_item.attrib['withdrawn'] = withdrawal_date

        code = ET.Element('code')
        code.text = currency_code
        codelist_item.append(code)
        
        name = ET.Element('name')
        codelist_item.append(name)
        narrative = ET.Element('narrative')
        narrative.text = currency_name
        name.append(narrative)

        codelist_items.append(codelist_item)

indent(template.getroot(), 0, 4)
template.write('xml/Currency.xml', pretty_print=True)

