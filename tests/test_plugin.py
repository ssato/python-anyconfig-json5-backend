#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring,invalid-name
import unittest
import anyconfig
from . import CNF_FILES


class Test_90(unittest.TestCase):

    def _try_loads(self, files):
        for filepath in files:
            try:
                cnf = anyconfig.load(filepath, ac_parser='json5')
                self.assertTrue(cnf)

                exp_path = filepath.parent / filepath.name.replace('.json5',
                                                                   '.json')
                ref = anyconfig.load(exp_path, ordered=True)

            except anyconfig.UnknownFileTypeError:
                print('all types=%r' % anyconfig.list_types())
                raise

            self.assertEqual(cnf, ref)

    def test_10_load(self):
        self._try_loads(CNF_FILES)

# vim:sw=4:ts=4:et:
