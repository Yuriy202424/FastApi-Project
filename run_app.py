from uvicorn import run

from project import app


if __name__ == "__main__":
    run("run_app:app")