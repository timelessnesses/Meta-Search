# Meta Search

Welcome to Meta Search. Work like mat1 but you need to use requests ( Actually no building webapplication I am fucking lazy)

Result up to 10000000 results! (Modify it in main.py or minified.py)

## How to use?

Run
```bash
python main.py
```
### Curl Test
You may use curl something like this
```bash
curl -i http://127.0.0.1:80
```
it should return
```json 
{"Result":[null]}
```
and add header with this

```bash
curl -i -H "search: your search query here" http://127.0.0.1:80
```
it may return lots of shit things
### Python Test
You may do something like this
```py
import requests

requests.get("http://127.0.0.1:80",headers={"search" : "metaname you want to search"})
```
### Node.JS Test
You can try something like this
```js
const request = require('request');
request('http://127.0.0.1', function (error, response, body) {
  console.error('error:', error);
  console.log('statusCode:', response && response.statusCode); 
  console.log('body:', body); 
});
```
## Test on this server
The link is https://Meta-Search-But-Only-Request.mooping.repl.co
You can do same as above but replace http://127.0.0.1 with my link
