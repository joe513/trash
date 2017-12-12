import os
import inspect


def one_argument(func, arg):
    getattr(os, func)(arg)


no_arg = [getattr(os, fun).__code__.co_argcount for fun in dir(os) if inspect.isfunction(getattr(os, fun))]
