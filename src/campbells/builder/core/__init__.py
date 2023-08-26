from .features import FAST, HTML, HTML_5, PERMISSIVE, STRICT, XML
from .main import (
    HTMLTreeBuilder,
    ParserRejectedMarkup,
    SAXTreeBuilder,
    TreeBuilder,
    TreeBuilderRegistry,
)
from .xml import DetectsXMLParsedAsHTML, XMLParsedAsHTMLWarning

__all__ = [
    "FAST",
    "PERMISSIVE",
    "STRICT",
    "XML",
    "HTML",
    "HTML_5",
    "TreeBuilderRegistry",
    "TreeBuilder",
    "SAXTreeBuilder",
    "HTMLTreeBuilder",
    "ParserRejectedMarkup",
    "DetectsXMLParsedAsHTML",
    "XMLParsedAsHTMLWarning",
]
