"""Use the HTMLParser library to parse HTML files that aren't too bad."""

from .builder import HTMLParserTreeBuilder
from .parser import CampbellsSoupHTMLParser

__all__ = ["CampbellsSoupHTMLParser", "HTMLParserTreeBuilder"]
