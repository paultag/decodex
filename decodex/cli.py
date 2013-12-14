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

import sys
from decodex.stream import Stream
from decodex.decoders import iter_decoders


def main():
    print("OK. What are you working on?")
    stream = Stream(sys.stdin.readline().rstrip("\n"), "string")
    # Let's grab some input.

    for decoder in iter_decoders():
        for result in decoder.decode(stream):
            print(result)
