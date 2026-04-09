from fastapi import FastAPI, HTTPException

import redis 

app = FastAPI()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.post("/crear_cita")
def crear_cita():
    lock = r.set("cita_10 am", "Ocupado", nx=True, ex=10)
    if not lock:
        raise HTTPException(status_code=400, detail="Cita ya reservada")
    return {"mensaje": "Cita creada exitosamente"}

@app.get("/ver_cita")
def ver_cita():
    estado = r.get("cita_10 am")
    if estado is None:
        return {"mensaje": "Cita disponible"}
    return {"mensaje": f"Cita {estado}"}

@app.delete("/cancelar_cita")
def cancelar_cita():
    r.delete("cita_10 am")
    return {"mensaje": "Cita cancelada"}

@app.post("/renovar_cita")
def renovar_cita():
    lock = r.set("cita_10 am", "Ocupado", nx=True, ex=10)
    if not lock:
        raise HTTPException(status_code=400, detail="Cita ya reservada")
    return {"mensaje": "Cita renovada exitosamente"}