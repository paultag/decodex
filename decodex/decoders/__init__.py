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

import importlib


ACTIVE_DECODERS = [
    'decodex.decoders.strings.alphabetize.AlphabetizingDecoder',
    'decodex.decoders.strings.anagram.AnagramDecoder',
    'decodex.decoders.strings.rot13.Rot13Decoder',
    #'decodex.decoders.strings.interesting.InterestingDecoder',
    'decodex.decoders.strings.acrostic.AcrosticDecoder',
    'decodex.decoders.numbers.ascii.AsciiDecoder',
    'decodex.decoders.numbers.latlon.LatLonDecoder',
]


def iter_decoders():
    for decoder in ACTIVE_DECODERS:
        module, class_ = decoder.rsplit(".", 1)
        mod = importlib.import_module(module)
        yield getattr(mod, class_)()
