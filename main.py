from fastapi import FastAPI
import uvicorn

from utils.log import pretty_print

# Create a FastAPI app
app = FastAPI()

# Single end point which just returns a string and prints
# the body
@app.get("/")
def read_root(data):
    print(pretty_print(data))
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
