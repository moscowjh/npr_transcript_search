# Search NPR story API for topic using search string
# Print top five results with title and NPR id
# Offer to return transcript of story if user inputs NPR ID of story
# Print transcript of story
# offer to email story transcript if user inputs email address

from urllib2 import urlopen
from urllib import quote
from json import load, dumps

# Search NPR story API for topic using search string
key = "MDE5ODEzODc3MDE0MzYyOTk5NzlmNjM1NQ001"
url = 'http://api.npr.org/query?apiKey='
url += key
url += "&numResults=5&format=JSON"
search_string = raw_input("Enter your search query.")
url += "&searchterm=" + quote(search_string)
#print url

# Print top five results with title and NPR id
response=urlopen(url)
json_obj=load(response)

for story in json_obj['list']['story']:
    print "TITLE:" + story['title']['$text']
    print "DATE: " + story['storyDate']['$text']
    print "TEASER: " + story['teaser']['$text']
    print "NPRID:" + story['id'] + "\n"
