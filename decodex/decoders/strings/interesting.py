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
    'e': 12.7, 't': 9, 'a': 8.1, 'o': 7.5, 'i': 6.9, 'n': 6.7, 's': 6.3,
    'h': 6, 'r': 5.9, 'd': 4.2, 'l': 4, 'c': 2.7, 'u': 2.7, 'm': 2.4, 'w': 2.3,
    'f': 2.2, 'g': 2.0, 'y': 1.9, 'p': 1.9, 'b': 1.4, 'v': 0.9, 'k': 0.7,
    'j': 0.1, 'x': 0.1, 'q': 0.09, 'z': 0.07,
    # Lifted shamelessly from English wikipedia.
}

START_FREQUENCIES = {  # Starting letter freqs
    't': 16.6, 'a': 11.6, 's': 7.7, 'h': 7.2, 'w': 6.7, 'i': 6.2, 'o': 4.7,
    'b': 4.3, 'm': 3.7, 'f': 3.5, 'c': 2.7, 'l': 2.6, 'd': 2.5, 'p': 2.3,
    'n': 2, 'e': 1.9, 'g': 1.6, 'r': 1.6, 'y': 1.4, 'u': 1.4, 'v': 0.6,
    'j': 0.5, 'k': 0.5, 'q': 0.1, 'x': 0.03, 'z': 0.03,
    # Lifted shamelessly from English wikipedia.
}


class InterestingDecoder(Decoder):
    def decode(self, stream):
        chars = "".join(stream.iter_str()).lower()
        words = chars.split()

        ccount = len([x for x in chars if x != ' '])
        freqs = Counter("".join(words))

        cypher = sorted(freqs)
        english = list(reversed([x[0] for x in sorted(FREQUENCIES.items(),
                                                 key=lambda x: x[1])]))
        buf = ""
        mapping = dict(zip(cypher, english))
        for char in chars:
            if char in mapping:  # We leave out spaces.
                buf += mapping[char]

        yield Result(buf, 'Frequency Subst')
