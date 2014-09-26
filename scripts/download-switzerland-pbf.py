import urllib
import time

t_0 = time.time()
urllib.urlretrieve  ('http://download.geofabrik.de/europe/switzerland-latest.osm.pbf'  , 'switzerland-latest.osm.pbf'  )
print "Download took {:d} seconds".format(int(time.time() - t_0))
