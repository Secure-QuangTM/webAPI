from fastapi import FastAPI
from pydantic import BaseModel

class TaxIn(BaseModel):
    cost: int
    tax_rate: float

class LogIn(BaseModel):
    login_id: str
    password: str

# login_user = {
#     "Allice": {
#         "login_id": "admin1",
#         "password": "Admin1234"
#     }, 
# }

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

    if data.login_id == "admin" and data.password == "Admin1234":
        return res_data_success
    else: 
        return res_data_fail

    # for user in login_user:
    #     print(user)
    #     # if data.login_id == user.login_id and data.password == user.password:
    #     #     return res_data_success
    #     # else: 
    #     #     return res_data_fail