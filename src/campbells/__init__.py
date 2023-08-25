"""Campbells - A condensed web scraping library.

https://www.github.com/lmmx/campbells

Campbells is adapted from Beautiful Soup under the MIT license.

Campbells uses a pluggable XML or HTML parser to parse a
(possibly invalid) document into a tree representation. Campbells
provides methods and Pythonic idioms that make it easy to navigate,
search, and modify the parse tree.

Like Beautiful Soup, Campbells works with Python 3.6 and up. It works
better if lxml and/or html5lib is installed.

For more than you ever wanted to know about Beautiful Soup, see their
documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

__version__ = "0.2.1"

__all__ = ["CampbellsSoup"]

import sys
import warnings
from collections import Counter

from .builder import HTMLParserTreeBuilder
from .builder.build import ParserRejectedMarkup, XMLParsedAsHTMLWarning
from .dammit import UnicodeDammit
from .element import (
    CSS,
    DEFAULT_OUTPUT_ENCODING,
    PYTHON_SPECIFIC_ENCODINGS,
    CData,
    Comment,
    Declaration,
    Doctype,
    NavigableString,
    PageElement,
    ProcessingInstruction,
    ResultSet,
    Script,
    SoupStrainer,
    Stylesheet,
    Tag,
    TemplateString,
)
from .main import (
    CampbellsSoup,
    FeatureNotFound,
    GuessedAtParserWarning,
    MarkupResemblesLocatorWarning,
    StopParsing,
)

# If this file is run as a script, act as an HTML pretty-printer.
if __name__ == "__main__":
    soup = CampbellsSoup(sys.stdin)
    print(soup.prettify())
