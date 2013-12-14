# decodex - simple enigma decoder.
#
# Copyright (c) 2013  Paul R. Tagliamonte <tag@pault.ag>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from decodex.stream import Stream


def number_stream(name):
    def ns(fn):
        def _(stream):
            type_ = 'number'
            things = list(fn(stream))
            if not things:
                return None

            if any((isinstance(x, float) for x in things)):
                type_ = 'float'

            s = Stream(things, type_)
            s.frobber = name
            return s
        return _
    return ns


@number_stream("base10")
def base10(stream):
    for block in stream.iter_split():
        try:
            yield int(block)
        except ValueError:
            try:
                yield float(block)
            except ValueError:
                continue


@number_stream("base16")
def base16(stream):
    for block in stream.iter_split():
        try:
            yield int(block, 16)
        except ValueError:
            continue
