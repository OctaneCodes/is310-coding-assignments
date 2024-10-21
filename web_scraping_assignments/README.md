## Scraping TOS
Liquipedia is pleased to provide free access to the information in our wikis through the MediaWiki API for use in your own projects. In order to keep the wiki API available for all users, we ask that you follow these terms of use.

Rate limit your requests to no more than 1 request per 2 seconds.

Use a custom HTTP "User-Agent" header in your requests that identifies your project / use of the API, and includes contact information. Example: "User-Agent: LiveScoresBot/1.0 (http://www.example.com/; email@example.com)". 

Your client must accept gzip encoding (supply an "Accept-Encoding: gzip" HTTP header with every request). 
API action=parse and other requests parsing wiki content to HTML should not exceed 1 request per 30 seconds as these are more resource intensive.

Re-use / cache your API results for as long as possible - do not issue repeated requests which return the same data. 

Only use authenticated (logged in) API calls when necessary — this allows improved caching of commonly requested endpoints. 

Remember that Liquipedia content is licensed under CC-BY-SA 3.0, which requires that you attribute Liquipedia as the source of your data. See Liquipedia:Copyrights for more information.


## Robots.txt

https://liquipedia.net/robots.txt 


### Reasoning

This data about The Major Tournament Winners from each Major over the years of CSGO and now CS2 shows the increase of the prizepool and the number of wins each team who has one one has. It could be used to track the rise of popularit for the game and you could also then start to track who was on each of these teams when they one and get a sense of how much money they have made from just Major tournament prizepools alone. (Not done in this Scraping assignment)