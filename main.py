import os

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API MediConnect", version="1.0.0")


class LoginRequest(BaseModel):
    rut: str
    password: str


@app.get("/")
def inicio():
    return {"status": "OK", "sistema": "MediConnect", "version": "1.0.0"}


@app.post("/api/v1/auth/login")
def login(data: LoginRequest):
    expected_rut = os.getenv("MEDICONNECT_RUT")
    expected_password = os.getenv("MEDICONNECT_PASSWORD")
    token = os.getenv("MEDICONNECT_TOKEN")

    if not expected_rut or not expected_password or not token:
        return {
            "status": "error",
            "code": 503,
            "message": "Autenticación no configurada"
        }

    if data.rut == expected_rut and data.password == expected_password:
        return {
            "status": "success",
            "code": 200,
            "message": "Autenticación exitosa en MediConnect",
            "data": {
                "usuario": data.rut,
                "rol": "PACIENTE",
                "token": token
            }
        }
    return {"status": "error", "code": 401, "message": "Credenciales inválidas"}


@app.get("/api/v1/citas/overall")
def listar_citas():
    return {"total_citas": 100, "disponibles": 25, "estado": "OK"}
