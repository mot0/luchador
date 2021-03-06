"""Implement miscellaneous Layer classes in Theano"""
from __future__ import division
from __future__ import absolute_import

from ..wrapper import Tensor

__all__ = [
    'NHWC2NCHW', 'NCHW2NHWC',
]
# pylint: disable=too-few-public-methods, no-self-use


class NHWC2NCHW(object):
    """See :any:`BaseNHWC2NCHW` for detail."""
    def _build(self, input_tensor):
        output_tensor = input_tensor.unwrap().dimshuffle(0, 3, 1, 2)

        shape = input_tensor.shape
        output_shape = (shape[0], shape[3], shape[1], shape[2])
        return Tensor(output_tensor, shape=output_shape, name='output')


class NCHW2NHWC(object):
    """See :any:`BaseNCHW2NHWC` for detail."""
    def _build(self, input_tensor):
        output_tensor = input_tensor.unwrap().dimshuffle(0, 2, 3, 1)

        shape = input_tensor.shape
        output_shape = (shape[0], shape[2], shape[3], shape[1])
        return Tensor(output_tensor, shape=output_shape, name='output')
