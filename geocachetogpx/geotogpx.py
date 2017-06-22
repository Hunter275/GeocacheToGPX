# Hunter Thornsberry www.adventuresintechland.com
version = 1.2

def createGPX(cachecreator, creatorid, datecreated, dateaccess, lat, lon, cachegccode, cachename, cacheid, cachetype, cachedifficulty, cachecontainer, cacheterrain, country, state, longdesc, shortdesc, hints, cacheurl):
    f = open('output/' + cachegccode + '.GPX', 'w')
    f.write('<?xml version="1.0" encoding="utf-8"?> \n')
    f.write('<gpx xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0" creator="Groundspeak, Inc. All Rights Reserved. http://www.groundspeak.com" xsi:schemaLocation="http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd http://www.groundspeak.com/cache/1/0 http://www.groundspeak.com/cache/1/0/cache.xsd" xmlns="http://www.topografix.com/GPX/1/0"> \n')
    f.write('  <name>Cache Listing Created By GeocacheToGPX v' + str(version) + '</name> \n')
    f.write('  <desc>GPX file generated by GeocacheToGPX</desc> \n')
    f.write('  <author>Account "' + cachecreator + '" From Geocaching.com</author> \n')
    f.write('  <email>hunter@hunterthornsberry.com</email> \n')
    f.write('  <url>http://www.adventuresintechland.com</url> \n')
    f.write('  <urlname>AdventuresInTechland</urlname> \n')
    f.write('  <time>' + datecreated + '</time> \n')
    f.write('  <keywords>cache, geocache</keywords> \n')
    f.write('  <bounds minlat="' + lat + '" minlon="'+ lon + '" maxlat="' + lat + '" maxlon="' + lon + '" /> \n')
    f.write('  <wpt lat="' + lat + '" lon="' + lon + '"> \n')
    f.write('    <time>' + dateaccess + '</time> \n')
    f.write('    <name>' + cachegccode + '</name> \n')
    f.write('    <desc>' + cachename + ' by ' + cachecreator + ', ' + cachetype + ' Cache (' + cachedifficulty + '/' + cacheterrain + ')</desc> \n')
    f.write('    <url>' + cacheurl + '</url> \n')
    f.write('    <urlname>' + cachename + '</urlname> \n')
    f.write('    <sym>Geocache</sym> \n')
    f.write('    <type>Geocache|' + cachetype + ' Cache</type> \n')
    f.write('    <groundspeak:cache id="' + cacheid + '" available="True" archived="False" xmlns:groundspeak="http://www.groundspeak.com/cache/1/0"> \n')
    f.write('      <groundspeak:name>' + cachename + '</groundspeak:name> \n')
    f.write('      <groundspeak:placed_by>' + cachecreator + '</groundspeak:placed_by> \n')
    f.write('      <groundspeak:owner id="' + creatorid + '">' + cachecreator + '</groundspeak:owner> \n')
    f.write('      <groundspeak:type>' + cachetype + ' Cache</groundspeak:type> \n')
    f.write('      <groundspeak:container>' + cachecontainer + '</groundspeak:container> \n')
    f.write('      <groundspeak:difficulty>' + cachedifficulty + '</groundspeak:difficulty> \n')
    f.write('      <groundspeak:terrain>' + cacheterrain + '</groundspeak:terrain> \n')
    f.write('      <groundspeak:country>' + country + '</groundspeak:country> \n')
    f.write('      <groundspeak:state>' + state + '</groundspeak:state> \n')
    f.write('      <groundspeak:short_description html="True">' + shortdesc.replace("&", "and") + '</groundspeak:short_description> \n')
    f.write('      <groundspeak:long_description html="True">' + longdesc.replace("&", "and") + '</groundspeak:long_description> \n')
    f.write('      <groundspeak:encoded_hints>' + hints + '</groundspeak:encoded_hints> \n')
    f.write('    </groundspeak:cache> \n')
    f.write('  </wpt> \n')
    f.write('</gpx>')
    f.close()
