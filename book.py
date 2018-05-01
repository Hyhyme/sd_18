import urllib2

data = urllib2.urlopen( "http://www.gutenberg.org/cache/epub/5200/pg5200.txt" ).read()

book = data.split()

def frequency( word ):
    return len( [ x for x in book if x == word ] )
print( 'Frequency of "Gregor":' )
print frequency( 'Gregor' ) 
print( 'Frequency of "the":' )
print frequency( 'the' ) 

def groupFreq( group ):
    return reduce( lambda a, b: a+b, [frequency(a) for a in group] )

print( 'Frequency of "Gregor" and "the":' )
print groupFreq( ['Gregor', 'the'] ) 

def most():
    return reduce( lambda a, b: b if frequency(b) > frequency(a) else a, book )

print( 'Most frequent word:' )
print most()
