# Copyright (C) 2019 - 2020 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# Ref. python -c "import json; help(json)"
#
"""JSON5 Backend.

- Format to support: JSON5, https://json5.org/
- Requirements: pyjson5
- Development Status :: 3 - Alpha
- Limitations: None obvious

Changelog:

.. versionadded:: 0.0.1
"""
import json5
import anyconfig.backend.base


_LOAD_OPTS = """object_hook parse_float parse_int
parse_constant object_pairs_hook""".split()

_DUMP_OPTS = """skipkeys ensure_ascii check_circular allow_nan
indent separators default sort_keys""".split()

_DICT_OPTS = 'object_pairs_hook object_hook'.split()


class Parser(anyconfig.backend.base.StringStreamFnParser):
    """
    Parser for JSON5 data files.
    """
    _cid = 'json5'
    _type = 'json5'
    _ordered = True
    _allow_primitives = True

    _load_opts = _LOAD_OPTS
    _dump_opts = _DUMP_OPTS
    _dict_opts = _DICT_OPTS

    _load_from_string_fn = anyconfig.backend.base.to_method(json5.loads)
    _load_from_stream_fn = anyconfig.backend.base.to_method(json5.load)
    _dump_to_string_fn = anyconfig.backend.base.to_method(json5.dumps)
    _dump_to_stream_fn = anyconfig.backend.base.to_method(json5.dump)

# vim:sw=4:ts=4:et:
