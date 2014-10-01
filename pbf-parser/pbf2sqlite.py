import os
import sqlite3
import sys
import time
import OSMpbfParser

cnt_node     =     0
cnt_way      =     0
cnt_relation =     0
cnt_         = 10000

def callback_node(node):

    global cnt_node
    cnt_node += 1
    if cnt_node % cnt_ == 0:
       print "Nodes: " + str(cnt_node)

    cur.execute(
      'insert into node ' +
      '(id, lat, lon) values (?, ?, ?)' , 
      (node.NodeID, node.Lat, node.Lon))

    for k in node.Tags.keys():

        cur.execute(
          'insert into tag ' +
          '(node_id, k, v) values (?, ?, ?)',
          (node.NodeID, k, node.Tags[k]))


def callback_way(way):

    global cnt_way
    cnt_way += 1
    if cnt_way % cnt_ == 0:
       print "Ways: " + str(cnt_way)

    cur.execute(
       'insert into way(id) values (?)',
       (way.WayID, ))


    order_ = 0
    for nd in way.Nds:

        cur.execute(
          'insert into node_in_way ' +
          '(way_id, node_id, order_)'+
          'values (?, ?, ?)',
          (way.WayID, nd, order_))

        order_ += 1


    for k in way.Tags.keys():
        cur.execute(
         'insert into tag (way_id, k, v) values (?, ?, ?)',
        (way.WayID, k, way.Tags[k]))


def callback_relation(relation):

    global cnt_relation
    cnt_relation += 1
    if cnt_relation % cnt_ == 0:
       print "Relations: " + str(cnt_relation)

    cur.execute(
      'insert into relation(id) values (?)',
      (relation.RelID, ))

    for m in relation.Members:

        if    m.type == 'node':

              cur.execute("""
    
                insert into member_in_relation(
                  id_of_relation,
                  node_id,
                  role
                )
                values (?, ?, ?) """,
                
                (relation.RelID, m.ref, m.role))

        elif  m.type == 'way':
        
              cur.execute("""
              
                insert into member_in_relation(
                  id_of_relation,
                  way_id,
                  role
                )
                values (?, ?, ?) """,
              
              (relation.RelID, m.ref, m.role))

        elif  m.type == 'relation': 
        
              cur.execute("""
              
                 insert into member_in_relation(
                   id_of_relation,
                   relation_id,
                   role
                 )
                 values (?, ?, ?)""",
              (relation.RelID, m.ref, m.role))

        else: print "unexpected type: " + m.type


    for k in relation.Tags.keys():

        cur.execute("""
        
            insert into tag (
              relation_id,
              k,
              v
            ) values (?, ?, ?)""",
            (relation.RelID, k, relation.Tags[k]))

def create_schema():
    
    cur.execute("""

        create table node(
          id  integer primary key,
          lat real not null,
          lon real not null
        )""")
      

    cur.execute("""
    
        create table way(
          id integer primary key
        )""")


    cur.execute("""

        create table relation(
          id integer primary key
        )""")


    cur.execute("""
    
        create table node_in_way(
          way_id  integer not null 
                  references way
                  deferrable initially deferred,
          node_id integer not null
                  references node
                  deferrable initially deferred,
          order_  integer not null
        )""")


    cur.execute("""
    
        create table member_in_relation(
          id_of_relation integer not null
                         references relation
                         deferrable initially deferred,
          node_id        integer null 
                         references node
                         deferrable initially deferred,
          way_id         integer null
                         references way
                         deferrable initially deferred,
          relation_id    integer null 
                         references relation
                         deferrable initially deferred,
          role           text
        )""")


    cur.execute("""
    
        create table tag(
          node_id     integer null 
                      references node
                      deferrable initially deferred,
          way_id      integer null
                      references way
                      deferrable initially deferred,
          relation_id integer null
                      references relation
                      deferrable initially deferred,
          k           text not null,
          v           text not null
        )""")


def execute_sql(stmt):

    t_ = time.time()

    cur.execute(stmt)
    
    print "{:d} seconds for {:s}".format(
          int(time.time() - t_), stmt)

#   -----------------------------------------

if len(sys.argv) != 3:
   print "pbf2sqlite.py pbf-file sqlite-db-file"
   sys.exit(0)

# First argument is *.pbf file name
pbf_filename = sys.argv[1]

# second argument is *.db file name
db_filename  = sys.argv[2]

# delete db if exists
if os.path.isfile(db_filename):
   os.remove(db_filename)

db  = sqlite3.connect(db_filename)
db.text_factory = str

# Makes inserts slower, so comment it:
# db.execute('pragma foreign_keys=on')

cur = db.cursor()

create_schema()

t_ = time.time()
OSMpbfParser.go(
  pbf_filename,
  callback_node,
  callback_way,
  callback_relation)

print "pbf file loaded, took {:d} seconds".format(
       int (time.time() -t_))


t_ = time.time()
db.commit()
print "commited, took {:d} seconds".format(
       int (time.time() -t_))

execute_sql('create index node_in_way__way_id '            +
            'on node_in_way (way_id)')

execute_sql('create index node_in_way__node_id '           +
            'on node_in_way (node_id)')

execute_sql('create index tag__v '                         +
            'on tag (v)')

execute_sql('create index tag__k_v on tag '                +
            '(k, v)')

execute_sql('create index tag__node_id '                   +
            'on tag (node_id)')

execute_sql('create index tag__way_id '                    +
            'on tag (way_id)')

execute_sql('create index tag__relation_id '               +
            'on tag (relation_id)')

execute_sql('create index member_in_relation__node_id '    +
            'on member_in_relation (node_id)')
            
execute_sql('create index member_in_relation__way_id '     +
            'on member_in_relation (way_id)')

execute_sql('create index member_in_relation__relation_id '+
            'on member_in_relation (relation_id)')
