from .main import app
from .model import KVSPair, KVSPairUpdateRequest
from .database import FakeDB

__all__ = [
    "app",
    "KVSPair",
    "KVSPairUpdateRequest",
    "FakeDB"
]

from . import _version
__version__ = _version.get_versions()['version']
