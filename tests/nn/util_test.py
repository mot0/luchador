from __future__ import absolute_import

import unittest

from tests.fixture import (
    get_layers,
    get_optimizers,
    get_initializers,
)

from luchador.nn.util import (
    get_layer,
    get_optimizer,
    get_initializer,
    get_model_config,
    make_model,
)


OPTIMIZERS = get_optimizers()
N_OPTIMIZERS = 4


class UtilTest(unittest.TestCase):
    longMessage = True
    maxDiff = None

    def test_optimizer_test_coverage(self):
        """All initializers are tested"""
        self.assertEqual(
            len(OPTIMIZERS), N_OPTIMIZERS,
            'Number of optimizers are changed. (New optimizer is added?) '
            'Fix unittest to cover new optimizers'
        )

    def test_get_initalizer(self):
        """get_initializer returns correct initalizer class"""
        for name, Initializer in get_initializers().items():
            expected = Initializer
            found = get_initializer(name)
            self.assertEqual(
                expected, found,
                'get_initializer returned wrong initializer Class. '
                'Expected: {}, Found: {}.'.format(expected, found)
            )

    def test_get_optimzier(self):
        """get_optimizer returns correct optimizer class"""
        for name, Optimizer in OPTIMIZERS.items():
            expected = Optimizer
            found = get_optimizer(name)
            self.assertEqual(
                expected, found,
                'get_optimizer returned wrong optimizer Class. '
                'Expected: {}, Found: {}.'.format(expected, found)
            )

    def test_get_layer(self):
        """get_layer returns correct layer class"""
        for name, Layer in get_layers().items():
            expected = Layer
            found = get_layer(name)
            self.assertEqual(
                expected, found,
                'get_layer returned wrong layer Class. '
                'Expected: {}, Found: {}.'.format(expected, found)
            )

    def test_create_model(self):
        """Deserialized model is equal to the original"""
        cfg1 = get_model_config('vanilla_dqn', n_actions=5)
        m1 = make_model(cfg1)
        m2 = make_model(m1.serialize())
        self.assertEqual(m1, m2)
