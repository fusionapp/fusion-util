from ._version import __version__

__all__ = ['__version__']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
