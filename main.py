from fastapi import FastAPI

app = FastAPI()

articles = []

@app.get("/get-studies")
async def getList():
    global articles
    return articles

@app.post("/add-study")
async def addStudy(study : str):
    global articles
    articles.append(study)
    return {"Study added. Total Count:": len(articles)}

@app.delete("/remove-study")
async def removeStudy(study : str):
    global articles
    articles.pop(study)
    return {"Study removed. Total Count:": len(articles)}
