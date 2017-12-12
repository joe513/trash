trace = True


def rangetest(**argchecks):

    def onDecorator(func):
        if not __debug__:
            return func
        else:
            import sys
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__

            def onCall(*pargs, **kargs):
                positional = list(allargs)
                positional = positional[:len(pargs)]

                for (argname, (low, high)) in argchecks.items():
                    if argname in kargs:

                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '%s argument "%s" not in %s .. %s ' % (funcname, argname, low, high)

                            raise TypeError(errmsg)

                    elif argname in positional:
                        position = positional.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            raise TypeError("ERRRMSG")

                    else:
                        if trace:
                            print('Arg')
                return func(*pargs, **kargs)
            return onCall
    return onDecorator


@rangetest(age=(0, 120))
def baby(name, age):
    print('%s is %s years old' % (name, age) )


baby('Jack', 1143)
