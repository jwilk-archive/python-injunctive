# encoding=UTF-8

# Copyright © 2013 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import abc
import operator
import sys

__all__ = []

def _bool_op(self, other):
    return bool(self)

class junction(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, iterable):
        self._iterable = iterable

    @abc.abstractmethod
    def _cmp(self, other, op):
        pass

    def __lt__(self, other):
        return self._cmp(other, op=operator.lt)

    def __le__(self, other):
        return self._cmp(other, op=operator.le)

    def __gt__(self, other):
        return self._cmp(other, op=operator.gt)

    def __ge__(self, other):
        return self._cmp(other, op=operator.ge)

    def __eq__(self, other):
        return self._cmp(other, op=operator.eq)

    def __ne__(self, other):
        return self._cmp(other, op=operator.ne)

    def __nonzero__(self):
        return self._cmp(None, op=_bool_op)

    if sys.version_info >= (3,):
        __bool__ = __nonzero__
        del __nonzero__

class all(junction):

    def _cmp(self, other, op):
        for x in self._iterable:
            if not op(x, other):
                return False
        return True

__all__ += ['all']

class any(junction):

    def _cmp(self, other, op):
        for x in self._iterable:
            if op(x, other):
                return True
        return False

__all__ += ['any']

class exactly(junction):

    def __init__(self, n, iterable):
        self._n = n
        junction.__init__(self, iterable)

    def _cmp(self, other, op):
        n = 0
        for x in self._iterable:
            if op(x, other):
                n += 1
            if n > self._n:
                return False
        return n == self._n

__all__ += ['exactly']

class none(exactly):

    def __init__(self, iterable):
        exactly.__init__(self, 0, iterable)

__all__ += ['none']

class one(exactly):

    def __init__(self, iterable):
        exactly.__init__(self, 1, iterable)

__all__ += ['one']

# vim:ts=4 sw=4 et
