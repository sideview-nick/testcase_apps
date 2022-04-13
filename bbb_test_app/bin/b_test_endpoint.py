# -*- coding: utf-8 -*-
import os
import sys

if sys.platform == "win32":
    import msvcrt
    # Binary mode is required for persistent mode on Windows.
    msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stderr.fileno(), os.O_BINARY)

from splunk.persistconn.application import PersistentServerConnectionApplication

APP = "bbb_test_app"
SPLUNK_HOME = os.environ["SPLUNK_HOME"]

sys.path.insert(1,os.path.join(SPLUNK_HOME, "etc", "apps", APP, "bin"))

# bad.  first one wins
import foo

# good.  even though "as bar" doesn't give it a globally unique name
#    somewhat odd - the docs don't say to create __init__.py but that makes this a
#    "namespace import" which means it will fail on py2
try:
    import bbb_test_app.bar as bar
except ImportError as e:
    import bbb_test_app_regular_package.bar as bar



sys.path.insert(1,os.path.join(SPLUNK_HOME, "etc", "apps", APP, "lib"))
import splunklib

class bTestHandler(PersistentServerConnectionApplication):

    def __init__(self, command_line, command_arg):
        """oh hai"""
        PersistentServerConnectionApplication.__init__(self)

    def handle(self, in_string):
        """ time to make the donuts """

        response_dict = {
            "headers": {"Content-Type": "application/json"}
        }
        response_dict["payload"] = {
            "splunk_home": os.environ["SPLUNK_HOME"],
            "app": APP,
            "whoami" : os.path.realpath (__file__),
            "sys.path" : sys.path,
            "which_foo": foo.provenance(),
            "which_bar": bar.provenance(),
            "which_baz_inside_bar": bar.secondary_provenance(),
            "splunklib_version" : splunklib.__version__,
            "which_splunklib":  splunklib.__random_property__
        }


        return response_dict
