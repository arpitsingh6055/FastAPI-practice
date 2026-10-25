from fastapi import FastAPI

# This is the variable name FastAPI looks for by default
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "FastAPI is working!"}
