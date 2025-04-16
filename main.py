from fastapi import FastAPI

app = FastAPI()

# ======= ARTICLES =======
articles = []

@app.get("/get-studies")
async def getList():
    return articles

@app.post("/add-study")
async def addStudy(study: str):
    articles.append(study)
    return {"Study added. Total Count:": len(articles)}

@app.delete("/remove-study")
async def removeStudy(index: int):
    articles.pop(index)
    return {"Study removed. Total Count:": len(articles)}

# ======= HIGHLIGHTS =======
highlights = []

@app.get("/get-highlights")
async def getHighlights():
    return highlights

@app.post("/add-highlight")
async def addHighlight(snippet: str):
    highlights.append(snippet)
    return {"Highlight added. Total Count:": len(highlights)}

@app.delete("/remove-highlight")
async def removeHighlight(index: int):
    highlights.pop(index)
    return {"Highlight removed. Total Count:": len(highlights)}

# ======= COMMENTS =======
comments = []

@app.get("/get-comments")
async def getComments():
    return comments

@app.post("/add-comment")
async def addComment(comment: str):
    comments.append(comment)
    return {"Comment added. Total Count:": len(comments)}

@app.delete("/remove-comment")
async def removeComment(index: int):
    comments.pop(index)
    return {"Comment removed. Total Count:": len(comments)}
