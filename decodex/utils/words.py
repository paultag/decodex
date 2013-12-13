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

from collections import defaultdict


def cleanup(what):
    return what.strip().lower().replace("'", "")


def issubset(superstr, substr):
    superstr = list(superstr)
    for ch in substr:
        if ch not in superstr:
            return False
        superstr.remove(ch)
    return True


def strsub(superstr, substr):
    superstr = list(superstr)
    substr = list(substr)
    for k in substr:
        superstr.remove(k)
    return "".join(superstr)


class Words(object):
    def __init__(self, dictionary):
        self.path = "/usr/share/dict/%s" % (dictionary)
        self.mapping = defaultdict(set)
        self._build_map()

    def _build_map(self):
        for line in (cleanup(x) for x in open(self.path, 'r')):
            self.mapping["".join(sorted(line))].add(line)

    def anagram(self, word, depth=2):
        if depth == 0:
            return

        l_hash = "".join(sorted(word))
        # OK. Let's start simple.
        if l_hash in self.mapping:
            for entry in self.mapping[l_hash]:
                yield [entry]

        # Meh, Let's do our best and find l_hash in r_hash.
        for r_hash, entries in self.mapping.items():
            if issubset(l_hash, r_hash):
                leftover = strsub(l_hash, r_hash)
                # OK. So, this is a word if we can match the rest.
                for anagram in self.anagram(leftover, depth=(depth - 1)):
                    for entry in entries:
                        yield [entry] + anagram
