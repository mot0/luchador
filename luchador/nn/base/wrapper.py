"""Module to define common interface for Tensor/Operation wrapping"""
from __future__ import absolute_import


class BaseTensor(object):
    """Wraps Tensor or Variable object in Theano/Tensorflow

    This class was introduced to provide easy shape inference to Theano Tensors
    while having the common interface for both Theano and Tensorflow.
    `unwrap` method provides access to the underlying object.
    """
    def __init__(self, tensor, shape, name, dtype):
        self._tensor = tensor
        self.shape = tuple(shape)
        self.name = name
        self.dtype = dtype

    def unwrap(self):
        """Get the underlying tensor object"""
        return self._tensor

    def set(self, obj):
        """Set the underlying tensor object"""
        self._tensor = obj

    def __repr__(self):
        return repr({
            'name': self.name, 'shape': self.shape, 'dtype': self.dtype})


class Operation(object):
    """Wrapps theano updates or tensorflow operation"""
    def __init__(self, op):
        self.op = op

    def unwrap(self):
        """Returns the underlying backend-specific operation object"""
        return self.op