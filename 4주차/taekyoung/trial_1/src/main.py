import random
from fastapi import FastAPI, Response, Request
from fastapi.responses import ORJSONResponse, HTMLResponse
from pydantic import BaseModel

app = FastAPI()

data_base = dict()


@app.get("/", response_class=HTMLResponse)
def get_html():
    html = ""
    with open("./src/index.html", "r") as file:
        html = file.read()
    return html

@app.get("/ball")
def api_ball(req: Request, res: Response):
    user_ip = req.client.host

    ex_ball_color = req.cookies.get("new_ball_color")
    ex_ball_color = ex_ball_color if ex_ball_color else ""
    new_ball_color = "blue" if bool(random.getrandbits(1)) else "red"

    if ex_ball_color == "":
        data_base[user_ip] = {"red": 0, "blue": 0}
    elif user_ip not in data_base:
        data_base[user_ip] = {"red": 0, "blue": 0}
        ex_ball_color = ""
    data_base[user_ip][new_ball_color] += 1

    res.set_cookie(key="ex_ball_color", value=ex_ball_color)
    res.set_cookie(key="new_ball_color", value=new_ball_color)

    msg = "Set new ball color success."
    response = {"message": msg, "status": 200, "you": user_ip}
    response.update(data_base[user_ip])
    return response

