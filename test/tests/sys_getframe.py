"""
Frame Hack Recipe #1: Ruby-style string interpolation (version 1)
"""
# from http://farmdev.com/src/secrets/framehack/interpolate/solutions/interpolate1.py
import sys
from string import Template

def interpolate(templateStr):
    frame = sys._getframe(1)
    framedict = frame.f_locals

    t = Template(templateStr)
    return t.substitute(**framedict)

name = 'Feihong'
place = 'Chicago'
print interpolate("My name is ${name}. I work in ${place}.")

def f1():
    def sysframetest():
        return sys._getframe(0)

    def sysframetestwrapper():
        return sysframetest()

    fr = sysframetest()
    print sysframetest.__name__
    print fr.f_code.co_name
    print fr.f_code.co_filename

    fr = sysframetestwrapper()
    print sysframetestwrapper.__name__
    print fr.f_code.co_name
    print fr.f_code.co_filename
f1()

# Make sure we can throw exceptions through frame we called _getframe
def f2():
    def g():
        sys._getframe(1)
        1/0

    def f():
        g()

    try:
        f()
    except Exception as e:
        print e
f2()

def f3():
    fr = sys._getframe(0)

    print fr.f_lineno
    print fr.f_lineno
    print sorted(fr.f_locals.keys())
    a = 1
    print sorted(fr.f_locals.keys())
f3()

def f4():
    f1 = sys._getframe(0)

    # trigger osr:
    for i in xrange(20000):
        pass
    assert f1 is sys._getframe(0)
f4()

assert sys._getframe(0).f_globals is globals()
def f5():
    assert sys._getframe(0).f_globals is globals()
f5()
