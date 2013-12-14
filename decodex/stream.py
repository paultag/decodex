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


class Stream(object):
    def __init__(self, stream, type_):
        self.stream = stream
        self.type_ = type_

    def __iter__(self):
        for el in self.stream:
            yield el

    def iter_split(self):
        if self.type_ != "string":
            raise ValueError("Stream isn't of type string")

        buf = ""
        for ch in self:
            if ch == " " or ch == "\n" or ch == "\t":
                if buf:
                    yield buf
                buf = ""
                continue
            buf += ch
        yield buf
