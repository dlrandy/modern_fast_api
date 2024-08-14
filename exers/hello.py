from fastapi import FastAPI, Body, Header, Response

app = FastAPI()

@app.get("/hi/{who}")
def greet(who,shui):
    return f"Hello?{who}?{shui}?"


@app.post("/hi")
def greet(who:str = Body(embed=True)):
    return f"Hello? {who}"


@app.post("/hello")
def hello(who:str = Header(),user_agent:str = Header()):
    return f"hello? {who}?{user_agent}"

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/inject/response/header/{name}/{value}")
def header(name: str, value: str, response:Response):
    response.headers[name] = value
    return "normasl body"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)