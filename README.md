## Project Abstract

Millions of people use Twitter and reddit as a social media web platform tool to express their thoughts and opinions on a range of subjects. As a result, a stream of text data, made up of enormous numbers of tweets, posts, comments, 'r/spotify', 'r/music','r/musican','r/singer'etc is generated. For this project, we’re especially seeking tweets, posts etc that refer to certain Spotify tunes, music, albums and artists. We analyse those tweets, 'r/spotify', 'r/music' ,'r/musican', 'r/singer', posts, and comments and gather track-related data using the Spotify API. Finally, we want to identify the artists who are now trending by using the information we’ve acquired in combination with a particular time frame.

## Tech-stack

- `python` - The project is developed and tested using python v3.8. [Python Website](https://www.python.org/)
- `request` - Request is a popular HTTP networking module(aka library) for python programming language. [Request Website](https://docs.python-requests.org/en/latest/#)
- `datetime` - The datetime library used for manipulating dates and times [Python documentation Website](https://docs.python.org/3/library/datetime.html)
- `Json` - Json is python build in package used to work on JSON data got from different API get request[Python documentation Website](https://docs.python.org/3/library/datetime.html)
- `base64` - base64 is python library used for data encoding [Python documentation Website](https://docs.python.org/3/library/datetime.html)
- `MongoDB` - MongoDB is NoSQL document database used to store data collected from Spotify,Reddit and Twitter websites [MongoDB Website](https://www.mongodb.com/)
- `PyMongo` - PyMongo is Python distribution containing tool used to work with MongoDB using python [PyMongo Website]
  ( https://pymongo.readthedocs.io/en/stable/)
- `System Cron Job` - System Cron Job is used to schedule tasks to run at a specific time in the future [System Cron Job Website]
  ( https://opensource.com/article/17/11/how-use-cron-linux )
- `Numpy` - NumPy is a Python library used for working with arrays.
- `Pandas` - Pandas is a software library written for the Python programming language for data manipulation and analysis.

## Three data-source documentation

- `Twitter`
- [https://developer.twitter.com/en/docs/twitter-api/v2/tweets/sample-realtime/overview](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api) – this end point URL provides an approximately 1% sample of Tweets in real time related to #spotify

- `Reddit` - We are using `r/spotify`,`r/music`, `r/musician`,`r/singer` etc.
- [https://www.reddit.com/api/v1/access_token](https://www.reddit.com/dev/api/) - <this Reddit end point URL provide data for post related to music, musician etc.>

- `spotify` - \*["https://api.spotify.com/v1/search"](https://developer.spotify.com/documentation/web-api/) - <this Spotify end point url provides data for artist and album >
