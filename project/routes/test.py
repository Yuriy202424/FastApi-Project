from .. import app


@app.get("/")
def index():
    return{"A":"B"}

index()