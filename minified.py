import flask;from googlesearch import search;import aiofiles;app = flask.Flask("Meta Search")
async def write(thing):
    async with aiofiles.open("log.log","a") as w:
        w.write(thing)
def run():
    app.run(host="0.0.0.0",port=80)
@app.route('/',methods=["POST","GET"])
async def main():
    try:
        query = flask.request.headers.get("search")
        if query == None:
            return {"Result":[None]}
    except KeyError:
        return {"Result":[None]}
    else:
        result = search(query,num_results=1000);await write(query);return {"Result":True,"Query":result}
import threading;threading.Thread(target=run).start()