import pytumblr
import psycopg2

client = pytumblr.TumblrRestClient( #https://api.tumblr.com/console
	'<consumer_key>',
    '<consumer_secret>',
    '<oauth_token>',
    '<oauth_secret>',
)

conn = psycopg2.connect("dbname=sjwbot user=postgres")

blogName = "mrnitrate"


#Connect to database
conn.autocommit = True
db = conn.cursor()



print "Loaded settings."
