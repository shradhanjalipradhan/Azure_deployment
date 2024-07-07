from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from iris.iris_classifier import IrisClassifier
from iris.router import iris_classifier_router
from iris.models import Iris

app = FastAPI()
app.include_router(iris_classifier_router.router, prefix='/iris')
templates = Jinja2Templates(directory="iris/templates")


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Iris classifier is all ready to go!'

@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/classify_iris")
def classify_iris(request: Request,
                  sepal_length: float = Form(...),
                  sepal_width: float = Form(...),
                  petal_length: float = Form(...),
                  petal_width: float = Form(...)):
    iris_classifier = IrisClassifier()
    iris = Iris(sepal_length=sepal_length,
                sepal_width=sepal_width,
                petal_length=petal_length,
                petal_width=petal_width)
    result = iris_classifier.classify_iris(iris)
    return templates.TemplateResponse("result.html", {"request": request, "result": result})

