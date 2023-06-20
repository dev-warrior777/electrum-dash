# -*- coding: utf-8 -*-

import sys


try:
    from dash_hash import getPoWHash
    import_success = True
    load_libdash_hash = False
except ImportError:
    import_success = False
    load_libdash_hash = True


if load_libdash_hash:
    from ctypes import cdll, create_string_buffer, byref
    # build the libraries - for now this will fail
    if sys.platform == 'darwin':
        name = 'libdash_hash.dylib'
    elif sys.platform in ('windows', 'win32'):
        name = 'libdash_hash-0.dll'
    else:
        name = 'libdash_hash.so'

    try:
        ldash_hash = cdll.LoadLibrary(name)
        dash_hash = ldash_hash.dash_hash
    except:
        load_libdash_hash = False


if load_libdash_hash:
    hash_out = create_string_buffer(32)

    def getPoWHash(header):
        dash_hash(header, byref(hash_out))
        return hash_out.raw


if not import_success and not load_libdash_hash:
    raise ImportError('Can not import dash_hash (x11 hashing library)')
