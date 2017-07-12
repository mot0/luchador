"""Define base Operation type"""
from __future__ import absolute_import

from .store import register, retrieve

__all__ = ['BaseOperation', 'get_operation']


class BaseOperation(object):
    """Wrapps theano updates or tensorflow operation"""
    def __init__(self, op, name=None):
        self.op = op
        self.name = name
        if name:
            register('operation', name, self)

    def unwrap(self):
        """Returns the underlying backend-specific operation object"""
        return self.op


def get_operation(name):
    """Get ``Operation`` instance from the current scope or the global scope

    Parameters
    ----------
    name : str
        name of ``Operation`` instance to get

    Returns
    -------
    Operation
    """
    return retrieve('operation', name)
