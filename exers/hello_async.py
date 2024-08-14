from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/hi")
async def greet():
    await asyncio.sleep(3)
    return "Hello world?"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello_async:app")

