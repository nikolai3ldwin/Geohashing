# https://medium.com/bukalapak-data/geolocation-search-optimization-5b2ff11f013b

# https://www.movable-type.co.uk/scripts/geohash.html

# https://en.wikipedia.org/wiki/Longyearbyen

# https://www.analyticsvidhya.com/blog/2020/06/guide-geospatial-analysis-folium-python/

# %%
import geohash
import folium
from branca.element import Figure

# %%
# creates geohash Svalbard / Longyearbyen
geohash.encode(
    latitude=78.2232,
    longitude=15.6267,
    precision=6
)

# %%
# get the center of the geohash
lat, long = geohash.decode('umgj58')

# %%
# get bounding box corner coordinates
geohash.bbox('umgj58')

# %%
# create a map canvas
m = folium.Map(
    # set the center of the map
    location=[lat, long],
    zoom_start=3,
)
m
# %%
