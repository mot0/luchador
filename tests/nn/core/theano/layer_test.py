import unittest

import theano
import numpy as np

from luchador.nn.core.theano.scope import _reset as reset_scope
from luchador.nn.core.theano.layer import Conv2D, Flatten
from luchador.nn.core.theano.tensor import Input

# import logging
# logging.getLogger('luchador.nn.core.theano.layer').setLevel(logging.DEBUG)


theano.config.optimizer = 'None'


class TestConv2D(unittest.TestCase):
    def setUp(self):
        reset_scope()

    def _test_shape_inference(
            self, input_shape, filter_shape, n_filters, strides, padding):
        reset_scope()
        conv2d = Conv2D(filter_height=filter_shape['height'],
                        filter_width=filter_shape['width'],
                        n_filters=n_filters,
                        strides=strides, padding=padding)
        input = Input(shape=input_shape)()
        output = conv2d(input)

        f = theano.function([input.get()], output.get())
        input_value = np.zeros(input_shape)
        output_value = f(input_value)

        expected = output_value.shape
        found = output.shape
        self.assertEqual(
            found, expected,
            'Shape inference failed. Expected: {}, Found: {}. '
            'input_shape: {}, filter_shape: {}, n_filters: {}, '
            'strides: {}, padding: {}'
            .format(expected, found, input_shape, filter_shape,
                    n_filters, strides, padding))

    def test_shape_inference_odd_valid(self):
        """output_shape is correct when filter+image:odd, mode:valid"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 6, 'width': 9}
        n_filters = 4
        padding = 'valid'
        strides = (1, 1)
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)
        strides = (2, 1)
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)
        strides = (1, 2)
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_odd_half(self):
        """output_shape is correct when filter+image:odd and mode:half"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 6, 'width': 9}
        n_filters = 4
        padding = 'half'

        strides = (1, 1)
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)
        strides = (2, 1)
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)
        strides = (1, 2)
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_odd_full(self):
        """output_shape is correct when filter+image:odd and mode:full"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 6, 'width': 9}
        n_filters = 4
        padding = 'full'

        strides = (1, 1)
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)
        strides = (2, 1)
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)
        strides = (1, 2)
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_valid_1(self):
        """output_shape is correct when filter+image:even, mode:valid, pad=1"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'valid'
        strides = 1
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_valid_2(self):
        """output_shape is correct when filter+image:even, mode:valid, pad=2"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'valid'
        strides = 2
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_valid_3(self):
        """output_shape is correct when filter+image:even, mode:valid, pad=3"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'valid'
        strides = 3
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_valid_5(self):
        """output_shape is correct when filter+image:even, mode:valid, pad=5"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'valid'
        strides = 5
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_full_1(self):
        """output_shape is correct when filter+image:even, mode:full, pad=1"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'full'
        strides = 1
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_full_2(self):
        """output_shape is correct when filter+image:even, mode:full, pad=2"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'full'
        strides = 2
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_full_3(self):
        """output_shape is correct when filter+image:even, mode:full, pad=3"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'full'
        strides = 3
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_full_5(self):
        """output_shape is correct when filter+image:even, mode:full, pad=5"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'full'
        strides = 5
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_half_1(self):
        """output_shape is correct when filter+image:even, mode:half, pad=1"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'half'
        strides = 1
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_half_2(self):
        """output_shape is correct when filter+image:even, mode:half, pad=2"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'half'
        strides = 2
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_half_3(self):
        """output_shape is correct when filter+image:even, mode:half, pad=3"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'half'
        strides = 3
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)

    def test_shape_inference_even_half_5(self):
        """output_shape is correct when filter+image:even, mode:half, pad=5"""
        input_shape = (32, 4, 73, 84)
        filter_shape = {'height': 5, 'width': 8}
        n_filters = 4
        padding = 'half'
        strides = 5
        self._test_shape_inference(
            input_shape, filter_shape, n_filters, strides, padding)


class TestFlatten(unittest.TestCase):
    def setUp(self):
        reset_scope()

    def test_flatten(self):
        """4D input tensor is flattened to 2D tensor"""
        input_shape = (32, 4, 77, 84)
        flatten = Flatten()
        input = Input(shape=input_shape)()
        output = flatten(input)

        f = theano.function([input.get()], output.get())
        input_value = np.zeros(input_shape)
        output_value = f(input_value)

        expected = output_value.shape
        found = output.shape
        self.assertEqual(
            expected, found)
