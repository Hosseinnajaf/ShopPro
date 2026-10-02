from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to ShopPro"
    }


@app.get("/about")
def about():
    return {
        "name": "ShopPro",
        "version": "1.0"
    }