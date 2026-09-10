from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
return {"message": "Hello World"}

@app.get("/about")
def about():
return {
"Institute": "BanoQabil",
"Course": "pytho"
}
@app.get("/downloads")
def downloads():
return {"message": "Here we store downloads items"}

@app.get("/summary")
def summary():
return {
"Institute": "BanoQabil",
"Course": "IT_courses",
"location":"pakistan"
}