import sys
import time

import OSMpbfParser

def xml_escape(s_):
    s_=s_.replace ("&", "&amp;" )
    s_=s_.replace ("<", "&lt;"  )
    s_=s_.replace (">", "&gt;"  )
    s_=s_.replace ('"', '&quot;')
    return s_


def callback_node(node):

    stamp=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime(node.time))

    if len(node.Tags)>0:

      fh.write('  <node id="%d" version="%d" timestamp="%s" uid="%d" user="%s" changeset="%d" lat="%.7f" lon="%.7f">\n' % (node.NodeID, node.version, stamp, node.uid, xml_escape(node.user), node.changeset, node.Lat, node.Lon))

      for t in node.Tags.keys():
          fh.write('    <tag k="%s" v="%s"/>\n' % (t, xml_escape(node.Tags[t])))

      fh.write('  </node>\n')

    else:
      fh.write('  <node id="%d" version="%d" timestamp="%s" uid="%d" user="%s" changeset="%d" lat="%.7f" lon="%.7f"/>\n' % (node.NodeID, node.version, stamp, node.uid, xml_escape(node.user), node.changeset, node.Lat, node.Lon))


def callback_way(way):

    stamp=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime(way.time))

    fh.write('  <way id="%d" version="%d" timestamp="%s" uid="%d" user="%s" changeset="%d">\n' % (way.WayID, way.version, stamp, way.uid, xml_escape(way.user), way.changeset))

    for n in way.Nds:
      fh.write('    <nd ref="%d"/>\n' % (n))

    for t in way.Tags.keys():
      fh.write('    <tag k="%s" v="%s"/>\n' % (t,xml_escape(way.Tags[t])))

    fh.write('  </way>\n')



def callback_relation(relation):

    stamp=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime(relation.time))

    fh.write('  <relation id="%d" version="%d" timestamp="%s" uid="%d" user="%s" changeset="%d">\n' % (relation.RelID, relation.version, stamp, relation.uid, xml_escape(relation.user), relation.changeset))

    for m in relation.Members:
      fh.write('    <member type="%s" ref="%d" role="%s"/>  \n' % (m.type, m.ref, xml_escape(m.role)))

    for t in relation.Tags.keys():
      fh.write('    <tag k="%s" v="%s"/>\n' % (t,xml_escape(relation.Tags[t])))

    fh.write('  </relation>\n')


# First argument is *.pbf file name
pbf_filename = sys.argv[1]

# Second (optional) argument is output file
if len(sys.argv) > 2: 
   fh = open(sys.argv[2], 'w')
else:
   fh = sys.stdout


fh.write('<?xml version="1.0" encoding="UTF-8"?>\n')
fh.write('<osm version="0.6" generator="dump_xml_stdout.py">\n')

OSMpbfParser.go(pbf_filename, callback_node, callback_way, callback_relation)

fh.write('</osm>\n')

fh.close()
