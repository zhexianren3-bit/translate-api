from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "翻译API"}
@app.get("/translate")
def translate(text: str = "hello", to: str = "zh"):
    return {"success": True, "result": f"翻译: {text}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
