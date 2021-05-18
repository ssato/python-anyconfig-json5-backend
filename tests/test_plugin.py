#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring
import unittest

import anyconfig

from . import CNF_FILES


class TestCase(unittest.TestCase):

    def _try_loads(self, files):
        for path in files:
            cnf = anyconfig.load(path, ac_parser='json5')
            self.assertTrue(cnf)

            exp_path = path.parent / path.name.replace('.json5', '.json')
            ref = anyconfig.load(exp_path, ordered=True)
            self.assertEqual(cnf, ref)

    def test_load_with_plugin(self):
        self._try_loads(CNF_FILES)

# vim:sw=4:ts=4:et:
