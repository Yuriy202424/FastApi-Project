from fastapi import FastAPI

app = FastAPI(debug=True)

from . import routes