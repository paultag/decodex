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

from decodex.decoder import Decoder
from decodex.result import Result

from collections import Counter


FREQUENCIES = {
    'e': 0.127, 't': 0.09, 'a': 0.081, 'o': 0.075, 'i': 0.069, 'n': 0.067,
    's': 0.063, 'h': 0.06, 'r': 0.059, 'd': 0.042, 'l': 0.04, 'c': 0.027,
    'u': 0.027, 'm': 0.024, 'w': 0.023, 'f': 0.022, 'g': 0.020, 'y': 0.019,
    'p': 0.019, 'b': 0.014, 'v': 0.009, 'k': 0.007, 'j': 0.001, 'x': 0.001,
    'q': 0.0009, 'z': 0.0007,
    # Lifted shamelessly from English wikipedia.
}

START_FREQUENCIES = {
    't': 0.166, 'a': 0.116, 's': 0.077, 'h': 0.072, 'w': 0.067, 'i': 0.062,
    'o': 0.047, 'b': 0.043, 'm': 0.037, 'f': 0.035, 'c': 0.027, 'l': 0.026,
    'd': 0.025, 'p': 0.023, 'n': 0.02, 'e': 0.019, 'g': 0.016, 'r': 0.016,
    'y': 0.014, 'u': 0.014, 'v': 0.006, 'j': 0.005, 'k': 0.005, 'q': 0.001,
    'x': 0.0003, 'z': 0.0003,
    # Lifted shamelessly from English wikipedia.
}


class InterestingDecoder(Decoder):
    def decode(self, stream):
        chars = "".join(stream.iter_str()).lower()
        words = chars.split()

        ccount = len([x for x in chars if x != ' '])
        ccounts = Counter("".join(words))

        freqs = {x: (y / ccount) for x, y in ccounts.items()}
        print(freqs)
