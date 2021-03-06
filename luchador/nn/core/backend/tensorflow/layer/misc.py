"""Implement Layer classes in Tensorflow"""
from __future__ import division
from __future__ import absolute_import

import logging

import tensorflow as tf

from ..wrapper import Tensor

__all__ = [
    'NHWC2NCHW', 'NCHW2NHWC',
]
_LG = logging.getLogger(__name__)
# pylint: disable=no-self-use


class NHWC2NCHW(object):
    """See :any:`BaseNHWC2NCHW` for detail."""
    def _build(self, input_tensor):
        output = tf.transpose(input_tensor.unwrap(), perm=(0, 3, 1, 2))
        return Tensor(output, name='output')


class NCHW2NHWC(object):
    """See :any:`BaseNCHW2NHWC` for detail."""
    def _build(self, input_tensor):
        output = tf.transpose(input_tensor.unwrap(), perm=(0, 2, 3, 1))
        return Tensor(output, name='output')
