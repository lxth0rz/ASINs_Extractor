# Movies Quotes

This actor allows you to collect quotes from movies by a keyword of your choice.
 
## Input configuration

The actor has the following input options:

- **Keyword** - type the keyword(s) you would like to a quotes for.
- **Proxy** - Optionally, select a proxy to be used by the actor,
  in order to avoid IP address-based blocking by the target website.
  The actor automatically executes all the Scrapy's HTTP(S) requests through the proxy.

## Results:

Each record represent a title. The following fields is the current data you will get from the scraper...

```json
{
    "id": "tt4574334",
    "title": "Stranger Things",
    "quotes": ["Friends don't lie"],
    "year": "2016–",
    "runtime": "51 min",
    "genre": "Drama, Fantasy, Horror",
    "rating": "8.7",
    "url": "https://www.imdb.com/title/tt4574334/",
    "poster_url": "https://m.media-amazon.com/images/M/MV5BODZlYjQ4NzYtZTg1MC00NGY4LTg4NjQtNGE3ZjRkMjk3YjMyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UY98_CR5,0,67,98_AL_.jpg",
    "big_poster_url": "https://m.media-amazon.com/images/M/MV5BODZlYjQ4NzYtZTg1MC00NGY4LTg4NjQtNGE3ZjRkMjk3YjMyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg"
  }
```

If you have any problem or anything does not work,
please file an [issue on Apify](https://console.apify.com/actors/ZZQ9zLu3lwula6mup#/issues).
