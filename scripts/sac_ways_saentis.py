# -*- coding: utf-8 -*-
import os
import sys
import time
import sqlite3

db_filename = sys.argv[1]

if not os.path.isfile(db_filename):
   print db_filename + ' does not exist'
   sys.exit(0)

db  = sqlite3.connect(db_filename)
db.text_factory = str

cur = db.cursor()
kml = open('sac_saentis.kml', 'w')


node_counter = 0

def create_sac_ways_around_saentis():

    cur.execute('drop table if exists sac_ways_around_saentis')

    t_ = time.time()
    cur.execute(
       """
       create table 
         sac_ways_around_saentis as

       select distinct 
         wy.id  way_id

       from
         tag          tg                        join
         way          wy on wy.id = tg.way_id   join
         node_in_way  nw on wy.id = nw.way_id   join
         node         nd on nd.id = nw.node_id

       where
         nd.lat > 47.2210118322 and 
         nd.lat < 47.2604651483 and
         nd.lon >  9.3149215728 and
         nd.lon <  9.3959004678 and
         tg.k   = 'sac_scale'

       """
    )


    print("creating sac_ways_around_saentis took " +
          "{:d} seconds".format(int(time.time() - t_)))



def node(node_id):
    cur2 = db.cursor()

    global node_counter
    node_counter += 1

    for r in cur2.execute('select lat, lon from node where id = ?', (node_id, )):
        # Note: kml has first the longitude, then the
        # lattitude
        kml.write("{:10.7f},{:10.7f} ".format(r[1], r[0]))


def draw_way(way_id):

    kml.write("  <Placemark>\n")

    cur2 = db.cursor()

    kml.write("    <name>{:s}</name>\n".format(str(way_id)))
    kml.write("    <styleUrl>#m_ylw-pushpin</styleUrl>\n")

    kml.write("    <LineString>\n")
    kml.write("     <tessellate>1</tessellate>\n")
    kml.write("     <coordinates>")
    for r in cur2.execute('select node_id from node_in_way where way_id = ? order by order_', (way_id, )):
        node(r[0]) 

    kml.write("     </coordinates>")
    kml.write("    </LineString>\n")
    kml.write("  </Placemark>\n")

def draw_ways():

    for way in cur.execute('select way_id from sac_ways_around_saentis'):
        draw_way(way[0])

kml.write(
"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
<name>Saentis.kml</name>
	<Style id="s_ylw-pushpin_hl">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff00aaff</color>
			<width>4</width>
		</LineStyle>
	</Style>
	<StyleMap id="m_ylw-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#s_ylw-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#s_ylw-pushpin_hl</styleUrl>
		</Pair>
	</StyleMap>
	<Style id="s_ylw-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff00aaff</color>
			<width>4</width>
		</LineStyle>
	</Style>
""")

create_sac_ways_around_saentis()
draw_ways()

print "node_counter: " + str(node_counter)

kml.write(
"""</Document>
</kml>""")

kml.close()
