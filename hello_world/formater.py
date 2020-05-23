import json
import xml.etree.cElementTree as e
from hello_world import app

PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
XML = "xml"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON, XML]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    elif format == XML:
        result = format_to_xml(msg, imie)
    return result


def format_to_json(msg, imie):
    json_data = {"Imie": imie, "msg": msg}
    return json.dumps(json_data, sort_keys=True, indent=4)


def format_to_xml(msg, imie):
    greet = e.Element("Greetings")
    e.SubElement(greet, "Name").text = imie
    e.SubElement(greet, "Msg").text = msg
    return app.response_class(e.tostring(greet), mimetype="application/xml")


def plain_text(msg, imie):
    return imie + " " + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
