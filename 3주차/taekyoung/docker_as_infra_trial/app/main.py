from fastapi import FastAPI, Response, Request
from fastapi.responses import ORJSONResponse, HTMLResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/test/page/", response_class=HTMLResponse)
def get_legacy_data():
    return page

page = \
"""
<!DOCTYPE html>
<html>
<head>
</head>
<body>
    this is new test page.
</body>
</html>
"""


@app.get("/test/")
def api_test(req: Request):
    return {"request_header": req.headers}

@app.get("/test/json/", status_code=200)
def test_api():

    return {"data": "test_value_1", "data_2": "test_value_2"}

@app.get("/test/text/", status_code=200)
def test_api():

    return "this is test text"
