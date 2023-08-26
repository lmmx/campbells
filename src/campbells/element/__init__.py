from __future__ import annotations

import warnings
from collections.abc import Callable

# from .attributes import (
#     AttributeValueWithCharsetSubstitution,
#     CharsetMetaAttributeValue,
#     ContentMetaAttributeValue,
#     NamespacedAttribute,
# )
# from .core import PageElement
from .encodings import DEFAULT_OUTPUT_ENCODING, PYTHON_SPECIFIC_ENCODINGS
from .original import (  # DEFAULT_OUTPUT_ENCODING,; PYTHON_SPECIFIC_ENCODINGS,
    AttributeValueWithCharsetSubstitution,
    CData,
    CharsetMetaAttributeValue,
    Comment,
    ContentMetaAttributeValue,
    Declaration,
    Doctype,
    NamespacedAttribute,
    NavigableString,
    PageElement,
    PreformattedString,
    ProcessingInstruction,
    ResultSet,
    RubyParenthesisString,
    RubyTextString,
    Script,
    SoupStrainer,
    Stylesheet,
    Tag,
    TemplateString,
    XMLProcessingInstruction,
    nonwhitespace_re,
    whitespace_re,
)

# from .results import ResultSet, SoupStrainer
# from .tag import Tag
# from .text_strings import (
#     CData,
#     Comment,
#     Declaration,
#     Doctype,
#     NavigableString,
#     PreformattedString,
#     ProcessingInstruction,
#     RubyParenthesisString,
#     RubyTextString,
#     Script,
#     Stylesheet,
#     TemplateString,
#     XMLProcessingInstruction,
# )
# from .whitespace import nonwhitespace_re, whitespace_re

__all__ = [
    "AttributeValueWithCharsetSubstitution",
    "CharsetMetaAttributeValue",
    "ContentMetaAttributeValue",
    "NamespacedAttribute",
    "PageElement",
    "DEFAULT_OUTPUT_ENCODING",
    "PYTHON_SPECIFIC_ENCODINGS",
    "ResultSet",
    "SoupStrainer",
    "Tag",
    "CData",
    "Comment",
    "Declaration",
    "Doctype",
    "NavigableString",
    "PreformattedString",
    "ProcessingInstruction",
    "RubyParenthesisString",
    "RubyTextString",
    "Script",
    "Stylesheet",
    "TemplateString",
    "XMLProcessingInstruction",
    "nonwhitespace_re",
    "whitespace_re",
]
