# Open Street Map pbf Parser

The parser consists of the following three files:
[`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/fileformat_pb2.py`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/fileformat_pb2.py),
[`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/osmformat_pb2.py`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/osmformat_pb2.py), both
of which are generated and
[`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/OSMpbfParser.py`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/OSMpbfParser.py) which depends
on the former two files and does the actual parsing.
See also [my blog entry](http://renenyffenegger.blogspot.ch/2014/09/parsing-open-street-map-pbf-file-with.html).

## Scripts

Scripts that use `OSMpbfParser.py`:

- [`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/pbf2xml.py`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/pbf2xml.py): convert pbf files into xml files. See also [this blog entry](http://renenyffenegger.blogspot.ch/2014/09/open-street-map-convert-pbf-to-xml.html).

- [`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/pbf2sqlite.py`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/pbf2sqlite.py): create an sqlite database and fill it with the content of the pbf. 
[`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/pbf2sqlite-erd.dia`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/pbf2sqlite-erd.dia) contains an ERD drawing for [dia](https://wiki.gnome.org/Apps/Dia).
See also [this blog entry](http://renenyffenegger.blogspot.ch/2014/09/openstreetmap-convert-pbf-to-sqlite.html).

## Installing google's protocol buffers

### On Windows

#### protoc.exe

Download Protocol Buffers Compiler (`protoc.exe`): https://protobuf.googlecode.com/files/protoc-2.5.0-win32.zip

set `%PATH%` so that it points to protoc.exe.

#### Protocol-Buffer sources

Download Protocol Buffers 2.5.0 full source from https://code.google.com/p/protobuf/downloads/list/protobuf-2.5.0.tar.bz2

Extract sources and `cd` into python directory:

    cd protobuf-2.5.0\protobuf-2.5.0\python

then execute

    python setup.py build
    python setup.py test
    python setup.py install


### On Ubuntu

    sudo apt-get install python-protobuf

## Links

Links that were helpful:
  - http://pbf.raggedred.net/
  - http://blog.lifeeth.in/2011/02/extract-pois-from-osm-pbf.html
