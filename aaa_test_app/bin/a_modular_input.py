
import sys

#first let's try the simplest import.
import foo

# next we'll do what the docs say and do a weird package lacking an __init__.py (called a "namespace package" and it's py3 only)
try:
    import aaa_test_app.bar as bar
# and on py2 we fall back to a regular package but this is basically the same file.
except ImportError as e:
    import aaa_test_app_regular_package.bar as bar

def do_scheme():
    """ Empty introspection routine """

def validate_arguments():
    """ Empty validation routine. This routine is optional. """



def run_script():
    """ actual function that will print() the data to be indexed to stdout"""
    print('app=aaa_test_app script="%s". foo.provenance="%s" bar.provenance="%s" sys.path="%s"' % (__file__, foo.provenance(), bar.provenance(), ",".join(list(sys.path))))

# Script must implement these args: scheme, validate-arguments
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "--scheme":
            do_scheme()
        elif sys.argv[1] == "--validate-arguments":
            validate_arguments()
        else:
            pass
    else:
        run_script()

    sys.exit(0)
