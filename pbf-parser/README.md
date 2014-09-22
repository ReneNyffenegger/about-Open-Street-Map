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
