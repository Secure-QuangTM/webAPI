from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
import requests

class TaxIn(BaseModel):
    cost: int
    tax_rate: float

class LogIn(BaseModel):
    login_id: str
    password: str

login_user = {
    "Allice": {
        "login_id": "admin1",
        "password": "Admin1234"
    }, 
    "Quang": {
        "login_id": "admin",
        "password": "Admin1234"
    }, 
}

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.post("/")
def calc(data: TaxIn):
    in_tax_cost = data.cost * (1 + data.tax_rate)
    return {'税込み価格': in_tax_cost}

@app.post("/login")
def login(data: LogIn):
    res_data_success= {
        "status.code" : "200",
        "body": {
            "User": {
                "user_id": "1",
                "name": "Administrator",
                "gender": "1",
                "birthday": "1977-10-08T04:00:00.00Z",
                "photo_exists": "false",
                "pin_exists": "false",
                "login_id": "admin",
                "password_exists": "true"
            }
        },
        "header": {
            "bs-session-id": "18db5f67d2df4ad0a8a2bd9a851f61c7"
        }
    }

    res_data_fail= {
        "status.code" : "400",
        "message": "Login Fail"
    }

    for user in login_user.values():
        if data.login_id == user["login_id"] and data.password == user["password"]:
            return res_data_success
            break
        else: 
            continue

@app.post("/search")
# def search(bs_session_id: str = Header(...)):
#     print()
#     if not bs_session_id:
#         print(1)
#         raise HTTPException(status_code=401, detail='Header is missing')
#     else:
#         if bs_session_id == "18db5f67d2df4ad0a8a2bd9a851f61c7":
#             print('Login Success')
#         else: 
#             raise HTTPException(status_code=401, detail='Authentication Fail')
def search(request: Request):
    if not request._headers.get('bs-session-id'):
        raise HTTPException(status_code=401, detail='Authentication Require')
    else:
        if request._headers.get('bs-session-id') == "18db5f67d2df4ad0a8a2bd9a851f61c7":
            print('Login Success')
        else: 
            raise HTTPException(status_code=401, detail='Authentication Fail')


