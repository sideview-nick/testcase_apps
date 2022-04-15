APP = "bbb_test_app"

import sys
import os
SPLUNK_HOME = os.environ["SPLUNK_HOME"]
sys.path.insert(1,os.path.join(SPLUNK_HOME, "etc", "apps", APP, "bin", APP))
import baz

def provenance():
    return "bar.py from the %s's bin/bbb_test_app_regular_package directory" % APP


def secondary_provenance():
    return baz.provenance()