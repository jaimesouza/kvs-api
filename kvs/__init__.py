from .main import app

__all__ = ["app"]

from . import _version
__version__ = _version.get_versions()['version']
