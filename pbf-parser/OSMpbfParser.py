"""
       Based on parsepbf.py by
       Chris Hill <osm@raggedred.net>

       This program is free software; you can redistribute it and/or modify
       it under the terms of the GNU General Public License as published by
       the Free Software Foundation; either version 3 of the License, or
       (at your option) any later version.

       This program is distributed in the hope that it will be useful,
       but WITHOUT ANY WARRANTY; without even the implied warranty of
       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
       GNU General Public License for more details.

       You should have received a copy of the GNU General Public License
       along with this program. If not, see <http://www.gnu.org/licenses/>.

       -----

       Thanks also to the person behind
       http://blog.lifeeth.in/2011/02/extract-pois-from-osm-pbf.html


"""

import os
import osmformat_pb2
import fileformat_pb2
from struct import unpack
import zlib


class OSMNode:

  def __init__(self, id=0):

      self.NodeID    = id
      self.Lon       = 0.0
      self.Lat       = 0.0
      self.version   = 0
      self.time      = 0
      self.uid       = 0
      self.user      = ""
      self.changeset = 0
      self.Tags      ={}

  def AddTag(self, Key, Val):
      self.Tags[Key]=Val



class OSMWay:

  def __init__(self, id=0):
      self.WayID     = id
      self.time      = 0
      self.uid       = 0
      self.user      = ""
      self.changeset = 0
      self.Tags      = {}
      self.Nds       = []

  def AddTag(self, Key, Val):
      self.Tags[Key]=Val

  def AddNd(self, NdID):
      self.Nds.append(NdID)


class OSMMember:

  def __init__(self, type, ref, role):
      self.type=type
      self.ref=ref
      self.role=role


class OSMRelation:

  def __init__(self, id=0):
      self.RelID     = id
      self.time      = 0
      self.uid       = 0
      self.user      = ""
      self.changeset = 0
      self.Tags      = {}
      self.Members   = []

  def AddTag(self, Key, Val):
      self.Tags[Key]=Val

  def AddMember(self, Member):
      self.Members.append(Member)



def check_pbf_file_header(pn):

    if readPBFBlobHeader()==False:
        return False

    if readBlob()==False:
        return False

    pb2_header_block.ParseFromString(self_BlobData)

    for rf in pb2_header_block.required_features:
        if rf in ("OsmSchema-V0.6", "DenseNodes"):
            pass
        else:
            print "not a required feature %s"%(rf)
            return False

    return True

def parse():
    # work through the data extracting OSM objects

    while readNextBlock():

        for pg in pb2_primitve_block.primitivegroup:
            if len(pg.dense.id)>0:
                processDense(pg.dense)
            if len(pg.nodes)>0:
                processNodes(pg.nodes)
            if len(pg.ways)>0:
                processWays(pg.ways)
            if len(pg.relations)>0:
                processRels(pg.relations)


def readPBFBlobHeader():
    # Read a blob header, store the data for later
    size=readint()
    if size <= 0:
       return False

    if pb2_blob_header.ParseFromString(pbf_file.read(size))==False:
       return False
    return True

def readBlob():
    global self_BlobData
    # Get the blob data, store the data for later
    size=pb2_blob_header.datasize

    if pb2_blob.ParseFromString(pbf_file.read(size))==False:
       return False

    if pb2_blob.raw_size > 0:
       self_BlobData=zlib.decompress(pb2_blob.zlib_data)
    else:
       self_BlobData=raw

    return True

def readNextBlock():
    # read the next block. Block is a header and blob, then extract the block
    if readPBFBlobHeader()== False:
       return False

    if pb2_blob_header.type != "OSMData":
       print "Expected OSMData, found %s"%(pb2_blob_header.type)
       return False

    if readBlob()==False:
       return False

    pb2_primitve_block.ParseFromString(self_BlobData)
    return True

def processDense(dense):
    # process a dense node block
    NANO=1000000000L
    lastID=0
    lastLat=0
    lastLon=0
    tagloc=0
    cs=0
    ts=0
    uid=0
    user=0
    gran=float(pb2_primitve_block.granularity)
    latoff=float(pb2_primitve_block.lat_offset)
    lonoff=float(pb2_primitve_block.lon_offset)
    for i in range(len(dense.id)):
        lastID+=dense.id[i]
        lastLat+=dense.lat[i]
        lastLon+=dense.lon[i]
        lat=float(lastLat*gran+latoff)/NANO
        lon=float(lastLon*gran+lonoff)/NANO
        user+=dense.denseinfo.user_sid[i]
        uid+=dense.denseinfo.uid[i]
        vs=dense.denseinfo.version[i]
        ts+=dense.denseinfo.timestamp[i]
        cs+=dense.denseinfo.changeset[i]
        suser=pb2_primitve_block.stringtable.s[user]
        tm=ts*pb2_primitve_block.date_granularity/1000
        node=OSMNode(lastID)
        node.Lon=lon
        node.Lat=lat
        node.user=suser
        node.uid=uid
        node.version=vs
        node.changeset=cs
        node.time=tm
        if tagloc<len(dense.keys_vals):  # don't try to read beyond the end of the list
            while dense.keys_vals[tagloc]!=0:
                ky=dense.keys_vals[tagloc]
                vl=dense.keys_vals[tagloc+1]
                tagloc+=2
                sky=pb2_primitve_block.stringtable.s[ky]
                svl=pb2_primitve_block.stringtable.s[vl]
                node.AddTag(sky, svl)
        tagloc+=1
        cb_node(node)

def processNodes(nodes):
    NANO=1000000000L
    gran=float(pb2_primitve_block.granularity)
    latoff=float(pb2_primitve_block.lat_offset)
    lonoff=float(pb2_primitve_block.lon_offset)

    for nd in nodes:
        nodeid=nd.id
        lat=float(nd.lat*gran+latoff)/NANO
        lon=float(nd.lon*gran+lonoff)/NANO
        vs=nd.info.version
        ts=nd.info.timestamp
        uid=nd.info.uid
        user=nd.info.user_sid
        cs=nd.info.changeset
        tm=ts*pb2_primitve_block.date_granularity/1000

        node=OSMNode(lastID)
        node.Lon=lon
        node.Lat=lat
        node.user=suser
        node.uid=uid
        node.version=vs
        node.changeset=cs
        node.time=tm

        for i in range(len(nd.keys)):
            ky=nd.keys[i]
            vl=nd.vals[i]
            sky=pb2_primitve_block.stringtable.s[ky]
            svl=pb2_primitve_block.stringtable.s[vl]
            node.AddTag(sky, svl)

        cb_node(node)

def processWays(ways):
    # process the ways in a block, extracting id, nds & tags
    for wy in ways:
        wayid=wy.id
        vs=wy.info.version
        ts=wy.info.timestamp
        uid=wy.info.uid
        user=pb2_primitve_block.stringtable.s[wy.info.user_sid]
        cs=wy.info.changeset
        tm=ts*pb2_primitve_block.date_granularity/1000
        way=OSMWay(wayid)
        way.user=user
        way.uid=uid
        way.version=vs
        way.changeset=cs
        way.time=tm
        ndid=0
        for nd in wy.refs:
            ndid+=nd
            way.AddNd(ndid)
        for i in range(len(wy.keys)):
            ky=wy.keys[i]
            vl=wy.vals[i]
            sky=pb2_primitve_block.stringtable.s[ky]
            svl=pb2_primitve_block.stringtable.s[vl]
            way.AddTag(sky, svl)

        cb_way(way)

def processRels(rels):
    for rl in rels:
        relid=rl.id
        vs=rl.info.version
        ts=rl.info.timestamp
        uid=rl.info.uid
        user=pb2_primitve_block.stringtable.s[rl.info.user_sid]
        cs=rl.info.changeset
        tm=ts*pb2_primitve_block.date_granularity/1000
        rel=OSMRelation(relid)
        rel.user=user
        rel.uid=uid
        rel.version=vs
        rel.changeset=cs
        rel.time=tm
        memid=0
        for i in range(len(rl.memids)):
            role=rl.roles_sid[i]
            memid+=rl.memids[i]

            member_type = None
            if    rl.types[i] == 0:
                  member_type = 'node'
            elif  rl.types[i] == 1:
                  member_type = 'way'
            elif  rl.types[i] == 2:
                  member_type = 'relation'

            memrole=pb2_primitve_block.stringtable.s[role]

            member=OSMMember(member_type, memid, memrole)

            rel.AddMember(member)
        for i in range(len(rl.keys)):
            ky=rl.keys[i]
            vl=rl.vals[i]
            sky=pb2_primitve_block.stringtable.s[ky]
            svl=pb2_primitve_block.stringtable.s[vl]
            rel.AddTag(sky, svl)
        cb_relation(rel)

def readint():
    # read an integer in network byte order and change to machine byte order. Return -1 if eof
    be_int=pbf_file.read(4)
    if len(be_int) == 0:
       return -1
    else:
       le_int=unpack('!L', be_int)
       return le_int[0]


def go(pbf_filename, callback_node, callback_way, callback_relation):

    global pb2_blob_header
    global pb2_blob
    global pb2_header_block
    global pb2_primitve_block

    global pbf_file

    global cb_node
    global cb_way
    global cb_relation

    cb_node     = callback_node
    cb_way      = callback_way
    cb_relation = callback_relation

    if  not os.path.exists(pbf_filename) :
        print "The binary file %s cannot be found" % (pbf_filename)
        sys.exit(1)

    pbf_file = open(pbf_filename, "rb")

    pb2_blob_header=fileformat_pb2.BlobHeader()
    pb2_blob=fileformat_pb2.Blob()
    pb2_header_block=osmformat_pb2.HeaderBlock()

    pb2_primitve_block=osmformat_pb2.PrimitiveBlock()

    if check_pbf_file_header("pbfparser.py 1.3")==False:
        print "Header trouble"
        exit(1)

    parse()

    pbf_file.close()
