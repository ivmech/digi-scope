###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013, John McNamara, jmcnamara@cpan.org
#

import unittest
from ...compatibility import StringIO
from ...styles import Styles


class TestInitialisation(unittest.TestCase):
    """
    Test initialisation of the Styles class and call a method.

    """

    def setUp(self):
        self.fh = StringIO()
        self.styles = Styles()
        self.styles._set_filehandle(self.fh)

    def test_xml_declaration(self):
        """Test Styles xml_declaration()"""

        self.styles._xml_declaration()

        exp = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n"""
        got = self.fh.getvalue()

        self.assertEqual(got, exp)


if __name__ == '__main__':
    unittest.main()
