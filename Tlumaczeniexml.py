from lxml import etree
from deep_translator import GoogleTranslator

def add_polish_translation_to_xml(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()

    for en_elem in root.xpath('//en'):
        english_text = en_elem.text
        if english_text:
            # Tłumaczenie tekstu na język polski
            polish_text = GoogleTranslator(source='en', target='pl').translate(english_text)

            # Tworzenie nowego elementu <pl> z tłumaczeniem
            pl_elem = etree.Element('pl')
            pl_elem.text = polish_text

            # Dodawanie <pl> za <en>
            parent = en_elem.getparent()
            parent.insert(parent.index(en_elem) + 1, pl_elem)

    # Zapisywanie zmodyfikowanego pliku
    output_path = "C:/xampp/htdocs/MADTV/translated_output.xml"
    tree.write(output_path, encoding="UTF-8", xml_declaration=True)
    print(f"Tłumaczenie dodane do pliku '{output_path}'.")

add_polish_translation_to_xml("C:/xampp/htdocs/MADTV/database_scripts.xml")
