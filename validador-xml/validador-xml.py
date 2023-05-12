from lxml import etree

def validate_xml_with_relaxed_mode(xml_file, xsd_file):

    xmlschema = etree.XMLSchema(file=xsd_file)

    xmlparser = etree.XMLParser(schema=xmlschema)

    try:
        tree = etree.parse(xml_file, xmlparser)
        print("The XML file is valid according to the XSD schema, ignoring specific errors.")
    except etree.XMLSchemaError as e:
        if len(e.error_log.filter_from_level(etree.ErrorLevels.ERROR)) == 0:
            print("The XML file is valid according to the XSD schema, ignoring specific errors.")
        else:
            print("The XML file is not valid according to the XSD schema.")
            for error in e.error_log:
                print(error.message)

# Replace 'your_xml_file.xml' with the path to your XML file and 'your_xsd_file.xsd' with the path to your XSD file
validate_xml_with_relaxed_mode('arquivo 2.4 correto jundai_08-05-modificado.xml', 'schema-nfse-v2-04-modificado.xsd')
