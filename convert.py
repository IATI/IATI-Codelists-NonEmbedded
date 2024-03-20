from os.path import join
from lxml import etree


org_id_xml = etree.parse(join('source', 'org-id-guide.xml'))
codelist_items = org_id_xml.find('codelist-items')

parser = etree.XMLParser(strip_cdata=False)
template = etree.parse(
    join('templates', 'OrganisationRegistrationAgency.xml'),
    parser=parser)
placeholder_codelist_items = template.find('codelist-items')

template.getroot().replace(placeholder_codelist_items, codelist_items)

etree.indent(template, space='    ')

template.write(
    join('xml', 'OrganisationRegistrationAgency.xml'),
    encoding='utf-8')
