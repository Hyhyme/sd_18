import urllib2

data = urllib2.urlopen( "http://www.gutenberg.org/cache/epub/5200/pg5200.txt" ).read()

book = data.split()

def frequency( x ):
    ans = 0
    reduce( lambda a: ans + 1 if a == x, book )
    return ans

frequency( 'Gregor' )

