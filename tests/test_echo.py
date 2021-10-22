#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
__author__ = "Karen Thomas"

import subprocess
import unittest
import argparse
import importlib
import sys

# change this to 'soln.echo' to run this suite against the solution
PKG_NAME = "echo"

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True


def run_capture(pyfile, args=()):
    """
    Runs a python program in a separate process,
    returns the output lines as a list.
    """
    cmd = ["python", pyfile]
    cmd.extend(args)
    try:
        result = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True
        )
        output = result.stdout.decode()
    except subprocess.CalledProcessError as err:
        output = err.stdout.decode()
    assert output, "Nothing was printed!"
    return output.splitlines()


class TestEcho(unittest.TestCase):
    """Main test fixture for 'echo' module"""

    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested (the student's echo.py)
        cls.module = importlib.import_module(PKG_NAME)

    def test_parser(self):
        """Check if create_parser() returns a parser object"""
        result = self.module.create_parser()
        self.assertIsInstance(
            result,
            argparse.ArgumentParser,
            "create_parser() function is not returning a parser object",
        )

    def test_parser_namespace(self):
        """Checks parser_namespace function"""
        parser_namespace = self.module.create_parser()
        self.assertIsInstance(
            parser_namespace,
            argparse.ArgumentParser,
            "create_parser() function is not returning a parser object",
        )

    def test_echo(self):
        """Check if main() function prints anything at all"""
        module_to_test = self.module.__file__
        run_capture(module_to_test)

    def test_simple_echo(self):
        """Check if main actually echoes an input string"""
        args = ["Was soll die ganze Aufregung?"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(
            output[0], args[0], "The program is not performing simple echo"
        )

    def test_lower_short(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-l", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "hello world")

    def test_lower_long(self):
        args = ["--lower", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "hello world")  # replace me

    def test_upper_short(self):
        args = ["-u", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "HELLO WORLD")

    def test_upper_long(self):
        args = ["--upper", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "HELLO WORLD")

    def test_title_short(self):
        args = ["-t", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "Hello World")

    def test_title_long(self):
        args = ["--title", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "Hello World")

    def test_multiple_options(self):
        args = ["-l", "-u", "-t", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "Hello World")

    def test_help_message(self):
        args = ["-h"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(
            output[0], "usage: transforms input text [-h] [-l] [-u] [-t] text"
        )  # noqa

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(["flake8", self.module.__file__])
        self.assertEqual(result.returncode, 0)

    def test_author(self):
        """Checking for author string"""
        self.assertIsNotNone(self.module.__author__)
        self.assertNotEqual(
            self.module.__author__, "???", "Author string is not completed"
        )


if __name__ == "__main__":
    unittest.main()
