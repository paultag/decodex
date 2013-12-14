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


class LatLonDecoder(Decoder):

    def decode(self, stream):
        if stream.type_ not in ['number', 'float']:
            return

        stream = list(stream)
        if len(stream) != 2:  # Handle z
            return

        def _(lat, lon):
            if lat < -90 or lat > 90:
                return None
            if lon < -180 or lon > 180:
                return None
            return Result(stream, "lat:%s, lon:%s" % (lat, lon), 'Lat/Lon')

        lat, lon = stream
        result = _(lat, lon)
        if result:
            yield result

        lon, lat = stream
        result = _(lat, lon)
        if result:
            yield result
