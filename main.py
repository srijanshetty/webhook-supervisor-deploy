from fastapi import FastAPI, Request
import uvicorn

from utils.log import pretty_print

# Create a FastAPI app
app = FastAPI()

# Single end point which just returns a string and prints
# the body
@app.get("/")
async def root_get():
    return "OK"

@app.post("/")
async def root_post(request: Request):
    body = await request.body()
    print(pretty_print(body.decode("utf-8")))
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
