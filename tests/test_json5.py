#
# Copyright (C) 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring,invalid-name,too-few-public-methods
import collections
import pathlib
import tempfile
import unittest

import anyconfig
import anyconfig.ioinfo
import anyconfig_json5_backend.json5_ as TT

from . import CNF_FILES


class TestCase(unittest.TestCase):

    maxDiff = None

    def test_load(self):
        self.assertTrue(CNF_FILES)

        for in_path in CNF_FILES:
            exp_path = in_path.parent / in_path.name.replace('.json5', '.json')

            with tempfile.TemporaryDirectory() as tmp_path:
                out_path = pathlib.Path(tmp_path) / 'out.json'

                if not exp_path.exists():
                    continue  # The reference test data is not ready.

                try:
                    cnf = TT.Parser().load(anyconfig.ioinfo.make(in_path),
                                           ac_ordered=True)
                    self.assertTrue(cnf)
                    self.assertTrue(isinstance(cnf, collections.OrderedDict))

                    anyconfig.dump(cnf, out_path)
                    self.assertEqual(anyconfig.load(out_path,
                                                    ac_ordered=False),
                                     anyconfig.load(exp_path,
                                                    ac_ordered=False))
                except AssertionError as exc:
                    raise AssertionError("file: {}, "
                                         "exc={!s}".format(in_path, exc))

# vim:sw=4:ts=4:et:
