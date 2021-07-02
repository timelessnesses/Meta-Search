import flask # Web application creator
from googlesearch import search # Google Search
import aiofiles # Logging
app = flask.Flask("Meta Search") # Set name of application
async def write(thing): # Write log
    async with aiofiles.open("log.log","a") as w: # open log.log file
        w.write(thing) # write stuff
def run(): # Run it
    app.run(host="0.0.0.0",port=80) # Run on your local machine IP address with port 80
@app.route('/',methods=["POST","GET"]) #  Root Path accept methods is POST and GET
async def main(): # Asyncronous function cuz why not?
    try: # Try to get searcg query
        query = flask.request.headers.get("search") # Get search query meta name
        if query == None: # If it is none
            return {"Result":[None]},400 # return none
    except KeyError: # If there's key error
        return {"Result":[None]},400 # return None
    else: # nothing error so far
        result = search(query,num_results=100000000000000) # Search time with limit result to 100000000000000 (modifiable)
        await write(query) # write query log
        return {"Result":True,"Query":result},202 # return result
import threading;threading.Thread(target=run).start()
