# Copyright (C) 2010-2021 Sideview LLC.  All Rights Reserved.
import sys
import os
APP = "aaa_test_app"


import foo

sys.path.insert(1,os.path.join(os.environ['SPLUNK_HOME'], "etc", "apps", APP, "lib"))
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration #, Option, validators


import splunklib

@Configuration()
class aTestCommand(StreamingCommand):
    """ pylint is our friend. But sometimes it tests our friendship. """



    def stream(self, records):

        for record in records:
            record["splunk_home"] = os.environ['SPLUNK_HOME']
            record["app"] = APP
            record["whoami"] = os.path.realpath (__file__),
            record["sys_path"] = sys.path
            record["which_foo"] = foo.provenance()
            record["splunklib_version"] = splunklib.__version__
            record["which_splunklib"] =  splunklib.__random_property__
            yield record



dispatch(aTestCommand, sys.argv, sys.stdin, sys.stdout, __name__)
