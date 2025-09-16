from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory counter
counter = {"value": 0}

@app.get("/")
def root():
    return {"message": "Counter App Backend running!"}

@app.get("/increment")
def increment():
    counter["value"] += 1
    return {"counter": counter["value"]}

@app.get("/decrement")
def decrement():
    counter["value"] -= 1
    return {"counter": counter["value"]}

@app.get("/value")
def get_value():
    return {"counter": counter["value"]}
