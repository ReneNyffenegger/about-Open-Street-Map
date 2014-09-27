# Open Street Map pbf Parser

The parser consists of the following three files:
[`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/fileformat_pb2.py`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/fileformat_pb2.py),
[`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/osmformat_pb2.py`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/osmformat_pb2.py), both
of which are generated and
[`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/OSMpbfParser.py`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/OSMpbfParser.py) which depends
on the former two files and does the actual parsing.
See also [my blog entry](http://renenyffenegger.blogspot.ch/2014/09/parsing-open-street-map-pbf-file-with.html).

[`https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/pbf2xml.py`](https://github.com/ReneNyffenegger/about-Open-Street-Map/blob/master/pbf-parser/pbf2xml.py) is a script
that uses the parser to convert pbf files into xml files. See also [this blog entry](http://renenyffenegger.blogspot.ch/2014/09/open-street-map-convert-pbf-to-xml.html).

## Installing google's protocol buffers

### On Windows

#### protoc.exe

Download Protocol Buffers Compiler (`protoc.exe`): https://protobuf.googlecode.com/files/protoc-2.5.0-win32.zip

set %PATH% so that it points to protoc.exe

#### Protocol-Buffer sources

Download Protocol Buffers 2.5.0 full source from https://code.google.com/p/protobuf/downloads/list/protobuf-2.5.0.tar.bz2

Extract sources and `cd` into python directory:

    cd protobuf-2.5.0\protobuf-2.5.0\python

execute

    python setup.py build
    python setup.py test
    python setup.py install


## Links

Links that were helpful:
  - http://pbf.raggedred.net/
  - http://blog.lifeeth.in/2011/02/extract-pois-from-osm-pbf.html
