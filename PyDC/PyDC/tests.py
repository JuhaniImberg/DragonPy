#!/usr/bin/env python2
# coding: utf-8

"""
    PyDC - unittests
    ~~~~~~~~~~~~~~~~

    :copyleft: 2013 by Jens Diemer
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

import logging
import os
import sys
import unittest
import itertools

# own modules
from __init__ import wav2bas, bas2cas, cas2bas, bas2wav
import configs
from wave2bitstream import Wave2Bitstream


class TestDragon32Conversion(unittest.TestCase):

    def setUp(self):
        print
        print " <<<<<< unittest setUp() <<<<<< "
        self.base_path = os.path.normpath(
            os.path.join(os.path.split(configs.__file__)[0], "..")
        )
        self.cfg = configs.Dragon32Config()

    def tearDown(self):
        print "\n"*2
        print " >>>unittest tearDown() >>>",

    def _src_file_path(self, filename):
        return os.path.relpath(
            os.path.join(self.base_path, "test_files", filename)
        )

    def _dst_file_path(self, filename):
        return os.path.relpath(
            os.path.join(self.base_path, filename)
        )

    def _get_and_delete_dst(self, destination_filepath, delete=True):
        f = open(destination_filepath, "r")
        dest_content = f.read()
        f.close()
        if delete:
            os.remove(destination_filepath)
        return dest_content

    def test_wav2bas01(self):
        source_filepath = self._src_file_path("HelloWorld1 xroar.wav")
        destination_filepath = self._dst_file_path("unittest_wav2bas01.bas")
        wav2bas(source_filepath, destination_filepath, self.cfg)

        # no filename used in CSAVE:
        destination_filepath = self._dst_file_path("unittest_wav2bas01_.bas")

        dest_content = self._get_and_delete_dst(destination_filepath)

        self.assertEqual(dest_content, (
            '10 FOR I = 1 TO 10\n'
            '20 PRINT I;"HELLO WORLD!"\n'
            '30 NEXT I\n'
        ))

    def test_wav2bas02(self):
        source_filepath = self._src_file_path("HelloWorld1 origin.wav")
        destination_filepath = self._dst_file_path("unittest_wav2bas02.bas")
        wav2bas(source_filepath, destination_filepath, self.cfg)

        # no filename used in CSAVE:
        destination_filepath = self._dst_file_path("unittest_wav2bas02_.bas")

        dest_content = self._get_and_delete_dst(destination_filepath)

        self.assertEqual(dest_content, (
            '10 FOR I = 1 TO 10\n'
            '20 PRINT I;"HELLO WORLD!"\n'
            '30 NEXT I\n'
        ))

    def test_wav2bas03(self):
        source_filepath = self._src_file_path("LineNumber Test 01.wav")
        destination_filepath = self._dst_file_path("unittest_wav2bas03.bas")
        wav2bas(source_filepath, destination_filepath, self.cfg)

        # filename 'LINENO01' used in CSAVE:
        destination_filepath = self._dst_file_path("unittest_wav2bas03_LINENO01.bas")

        dest_content = self._get_and_delete_dst(destination_filepath)

        self.assertEqual(dest_content, (
            '1 PRINT "LINE NUMBER TEST"\n'
            '10 PRINT 10\n'
            '100 PRINT 100\n'
            '1000 PRINT 1000\n'
            '10000 PRINT 10000\n'
            '32768 PRINT 32768\n'
            '63999 PRINT "END";63999\n'
        ))

    def test_wav2bas04(self):
        source_filepath = self._src_file_path("LineNumber Test 02.wav")
        destination_filepath = self._dst_file_path("unittest_wav2bas03.bas")
        wav2bas(source_filepath, destination_filepath, self.cfg)

        # filename 'LINENO02' used in CSAVE:
        destination_filepath = self._dst_file_path("unittest_wav2bas03_LINENO02.bas")

        dest_content = self._get_and_delete_dst(destination_filepath)

        self.assertEqual(dest_content, (
            '1 PRINT "LINE NUMBER TEST"\n'
            '10 PRINT 10\n'
            '100 PRINT 100\n'
            '1000 PRINT 1000\n'
            '10000 PRINT 10000\n'
            '32768 PRINT 32768\n'
            '63999 PRINT "END";63999\n'
        ))

    def test_statistics(self):
        source_filepath = self._src_file_path("HelloWorld1 xroar.wav")
        wb = Wave2Bitstream(source_filepath, self.cfg)
        statistics = wb._get_statistics(128)
        self.assertEqual(
            statistics, {10: 17, 11: 44, 12: 4, 19: 5, 20: 44, 21: 15}
        )

    def test_bas2cas01(self):
        # create cas
        source_filepath = self._src_file_path("HelloWorld1.bas")
        destination_filepath = self._dst_file_path("unittest_HelloWorld1.cas")

        cfg = configs.Dragon32Config()
        cfg.LEAD_BYTE_LEN = 35
        bas2cas(source_filepath, destination_filepath, cfg)

        dest_content = self._get_and_delete_dst(destination_filepath)
#         print repr(dest_content)

        cas = (
            ("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU", "35x Leadin bytes 0x55"),
            ("<", "Sync byte 0x3C"),

            ("\x00", "block type: filename block (0x00)"),
            ("\x0f", "block length (15Bytes)"),

            ("HELLOWOR", "filename"),
            ("\x00", "File type: BASIC programm (0x00)"),
            ("\xff", "format: ASCII BASIC (0xff)"),
            ("\x00", "gap flag (00=no gaps, FF=gaps)"),
            ("\x0c\x00", "machine code starting address"),
            ("\x0c\x00", "machine code loading address"),

            ("\x92", "block checksum"),
            ("U", "magic byte block terminator 0x3C"),

            ("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU", "35x Leadin bytes 0x55"),
            ("<", "Sync byte 0x3C"),

            ("\x01", "block type: data block (0x01)"),
            (":", "block length 0x3a (58Bytes)"),
            (
                '\r10 FOR I = 1 TO 10\r20 PRINT I;"HELLO WORLD!"\r30 NEXT I\r',
                "Basic code in ASCII format"
            ),
            ("\x00\x00", "code end terminator"),
            ("\x91", "block checksum"),
            ("U", "magic byte block terminator 0x3C"),

            ("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU", "35x Leadin bytes 0x55"),
            ("<", "Sync byte 0x3C"),

            ("\xff", "block type: end-of-file block (0xff)"),
            ("\x00", "block length (0Bytes)"),
            ("\xff", "block checksum"),
            ("U", "magic byte block terminator 0x3C"),
        )

        dest_content = iter(dest_content)
        for no, data in enumerate(cas):
            part, desc = data
            part_len = len(part)
            dest_part = "".join(tuple(itertools.islice(dest_content, part_len)))
            self.assertEqual(part, dest_part,
                msg="Error in part %i '%s': %s != %s" % (no, desc, repr(part), repr(dest_part))
            )

    def test_cas01(self):
        # create cas
        source_filepath = self._src_file_path("LineNumberTest.bas")
        cas_filepath = self._dst_file_path("unittest_LineNumberTest.cas")
        bas2cas(source_filepath, cas_filepath, self.cfg)

        # create bas from created cas file
        destination_filepath = self._dst_file_path("unittest_LineNumberTest.bas")
        cas2bas(cas_filepath, destination_filepath, self.cfg)

        os.remove(cas_filepath)

        # filename 'LINENUMB' used in CSAVE:
        destination_filepath = self._dst_file_path("unittest_LineNumberTest_LINENUMB.bas")
        dest_content = self._get_and_delete_dst(destination_filepath)

        self.assertMultiLineEqual(dest_content, (
            '1 PRINT "LINE NUMBER TEST"\n'
            '10 PRINT 10\n'
            '100 PRINT 100\n'
            '1000 PRINT 1000\n'
            '10000 PRINT 10000\n'
            '32768 PRINT 32768\n'
            '63999 PRINT "END";63999\n'
        ))

    def test_bas2ascii_wav(self):
        # create wav
        source_filepath = self._src_file_path("HelloWorld1.bas")
        destination_filepath = self._dst_file_path("unittest_HelloWorld1.wav")

        cfg = configs.Dragon32Config()
        cfg.LEAD_BYTE_LEN = 128
        bas2wav(source_filepath, destination_filepath, cfg)

        # read wave and compare
        source_filepath = self._dst_file_path("unittest_HelloWorld1.wav")
        destination_filepath = self._dst_file_path("unittest_bas2ascii_wav.bas")
        wav2bas(source_filepath, destination_filepath, self.cfg)

        # filename 'HELLOWOR' used in CSAVE:
        destination_filepath = self._dst_file_path("unittest_bas2ascii_wav_HELLOWOR.bas")

        dest_content = self._get_and_delete_dst(destination_filepath)

        self.assertEqual(dest_content, (
            '10 FOR I = 1 TO 10\n'
            '20 PRINT I;"HELLO WORLD!"\n'
            '30 NEXT I\n'
        ))


if __name__ == '__main__':
#     log = logging.getLogger("PyDC")
#     log.setLevel(
# #         logging.ERROR
# #         logging.INFO
# #         logging.WARNING
#         logging.DEBUG
#     )
#     log.addHandler(logging.StreamHandler())

    unittest.main(
        argv=(
            sys.argv[0],
#             "TestDragon32Conversion.test_wav2bas01",
#             "TestDragon32Conversion.test_wav2bas04",
#             "TestDragon32Conversion.test_statistics",
#             "TestDragon32Conversion.test_bas2cas01",
#             "TestDragon32Conversion.test_cas01",
#             "TestDragon32Conversion.test_bas2ascii_wav",
        ),
#         verbosity=1,
        verbosity=2,
        failfast=True,
    )
