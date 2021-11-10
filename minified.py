import flask;from googlesearch import search;import aiofiles;app = flask.Flask("Meta Search")
async def write(thing):async with aiofiles.open("log.log","a") as w:w.write(thing)
def run():app.run(host="0.0.0.0",port=80)
@app.route('/',methods=["POST","GET"])
async def main():
    try:
        query = flask.request.headers.get("search")
        if query == None:return {"Result":[None]},400
    except KeyError:
        return {"Result":[None]},400
    else:
        result = search(query,num_results=10000000000);await write(query);return {"Result":True,"Query":result},202 # Modify num_results to be what the heck ever you want
run()
