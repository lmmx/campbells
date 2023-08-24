import sys

from ._htmlparser import HTMLParserTreeBuilder
from .build import TreeBuilder, TreeBuilderRegistry

__all__ = ["builder_registry", "register_treebuilders_from", "HTMLParserTreeBuilder"]

# The BeautifulSoup class will take feature lists from developers and use them
# to look up builders in this registry.
builder_registry = TreeBuilderRegistry()


def register_treebuilders_from(module):
    """Copy TreeBuilders from the given module into this module."""
    this_module = sys.modules[__name__]
    for name in module.__all__:
        obj = getattr(module, name)

        if issubclass(obj, TreeBuilder):
            setattr(this_module, name, obj)
            this_module.__all__.append(name)
            # Register the builder while we're at it.
            this_module.builder_registry.register(obj)


# Builders are registered in reverse order of priority, so that custom
# builder registrations will take precedence. In general, we want lxml
# to take precedence over html5lib, because it's faster. And we only
# want to use HTMLParser as a last resort.

# Don't use dynamic namespace import for _htmlparser.HTMLParserTreeBuilder
#  x  register_treebuilders_from(_htmlparser)
# Instead we already added HTMLParserTreeBuilder to the __all__ list, just register it
builder_registry.register(HTMLParserTreeBuilder)
try:
    from . import _html5lib

    register_treebuilders_from(_html5lib)
except ImportError:
    # They don't have html5lib installed.
    pass
try:
    from . import _lxml

    register_treebuilders_from(_lxml)
except ImportError:
    # They don't have lxml installed.
    pass
