from wasabi import Printer
import sys

with(open(sys.argv[1])) as fd:
    thesolution = fd.read()
with(open(sys.argv[2])) as fd:
    thetest = fd.read()

__msg__ = Printer()
__solution__ = """{}""".format(thesolution)

exec(thesolution)

exec(thetest)

print(globals().keys())
try:
    test()
except AssertionError as e:
    __msg__.fail(e)

