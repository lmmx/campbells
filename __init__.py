"""Beautiful Soup Elixir and Tonic - "The Screen-Scraper's Friend".

http://www.crummy.com/software/BeautifulSoup/

Beautiful Soup uses a pluggable XML or HTML parser to parse a
(possibly invalid) document into a tree representation. Beautiful Soup
provides methods and Pythonic idioms that make it easy to navigate,
search, and modify the parse tree.

Beautiful Soup works with Python 3.6 and up. It works better if lxml
and/or html5lib is installed.

For more than you ever wanted to know about Beautiful Soup, see the
documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

__author__ = "Leonard Richardson (leonardr@segfault.org)"
__version__ = "4.12.2"
__copyright__ = "Copyright (c) 2004-2023 Leonard Richardson"
# Use of this source code is governed by the MIT license.
__license__ = "MIT"

__all__ = ["BeautifulSoup"]

import sys
import warnings
from collections import Counter

from .builder import HTMLParserTreeBuilder, ParserRejectedMarkup, XMLParsedAsHTMLWarning
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
    BeautifulSoup,
    FeatureNotFound,
    GuessedAtParserWarning,
    MarkupResemblesLocatorWarning,
    StopParsing,
)

# If this file is run as a script, act as an HTML pretty-printer.
if __name__ == "__main__":
    soup = BeautifulSoup(sys.stdin)
    print(soup.prettify())
