# -*- coding: utf-8 -*-
import os
import sys
import math
import time
import sqlite3

import Image


image_width_px  = 1980
lat_min         = 45.8180306
lat_max         = 47.8082639
lon_min         =  5.9563028
lon_max         = 10.491944
km_west_east    = 348
km_south_north  = 220
image_height_px = int(float(image_width_px) / km_west_east * km_south_north)


db_filename = sys.argv[1]

if not os.path.isfile(db_filename):
   print db_filename + ' does not exist'
   sys.exit(0)

db  = sqlite3.connect(db_filename)
db.text_factory = str

cur = db.cursor()

def count_per_pixel_table_ch():

    cur.execute('drop table if exists count_per_pixel_ch')

    t_ = time.time()

    cur.execute( """

       create table count_per_pixel_ch as

          select
              count(*) cnt,
              cast ( ( lon - {lon_min}) / ({lon_max} - {lon_min}) * {image_width_px}  as int) x,
              cast ( ( lat - {lat_min}) / ({lat_max} - {lat_min}) * {image_height_px} as int) y
          from
            node
          group by
            x, y;

       """.format (image_width_px  = image_width_px ,
                   image_height_px = image_height_px,
                   lat_min         = lat_min        ,
                   lat_max         = lat_max        ,
                   lon_min         = lon_min        ,
                   lon_max         = lon_max        ,
                   ))

    print("creating table took " +
          "{:d} seconds".format(int(time.time() - t_)))


def select_avg_count_per_pixel():

    for r in cur.execute('select avg(cnt) from count_per_pixel_ch'):
        return r[0]


count_per_pixel_table_ch();           

#  TODO: Adjust avg_count_per_pixel here.
avg_count_per_pixel = select_avg_count_per_pixel() * 2.2

print "Avg count per pixel: " + str(avg_count_per_pixel)
log_ = math.log(avg_count_per_pixel ** (1.0/255.0));

im = Image.new('RGB', (image_width_px, image_height_px), 'black')

pixels = im.load()


for r in cur.execute("""
  select x, y, cnt 
    from count_per_pixel_ch 
   where x >= 0 and x <  {image_width_px}  and
         y >= 0 and y <  {image_height_px}
""".format(
     image_width_px  = image_width_px ,
     image_height_px = image_height_px)):

   x   = r[0]
   y   = image_height_px - r[1] - 1
   cnt = float(r[2])


   blue = int(float(cnt)/float(avg_count_per_pixel) * 255.0)

   green = 0

   if blue  > 255:
      green = blue - 255
      blue  = 255
 
   pixels[x, y] = (blue/2, green, blue)


im.show()
im.save('switzerland_node_density.png')
