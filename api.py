from fastapi import FastAPI, Body
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
genai.configure(api_key="your-api-key-here")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-2.0-flash")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#   Make a POST request to /ask-model with a JSON body like:
#    {
#        "prompt": "Which of these articles is best for learning about creatine?"
#    }

# ======= AI =======
@app.post("/ask-model")
async def ask_model(prompt: str = Body(...)):
    articles_str = "\n".join(articles)
    full_prompt = f"Here are some article titles:\n{articles_str}\n\nQuestion: {prompt}"
    response = model.generate_content(full_prompt)
    return {"response": response.text}

# ======= ARTICLES =======
articles = ["Creatine supplementation and exercise performance: a meta-analysis", ""
"Muscle hypertrophy and strength gains during resistance training in older adults: a systematic review and meta-analysis",
"Effects of protein supplementation on muscle mass and strength in older adults: a systematic review and meta-analysis", "The effects of omega-3 fatty acids on muscle mass and strength in older adults: a systematic review and meta-analysis", "Vitamin D supplementation and muscle strength in older adults: a systematic review and meta-analysis"]

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


