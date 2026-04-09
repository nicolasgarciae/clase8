# 📅 Clase 8 – API de Gestión de Citas con FastAPI + Redis

API REST construida con **FastAPI** y **Redis** para gestionar la reserva de citas usando bloqueos distribuidos (`SET NX`), garantizando que una misma cita no pueda ser tomada dos veces al mismo tiempo.


---

## 📡 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `POST` | `/crear_cita` | Reserva la cita de las 10 am (expira en 10 seg) |
| `GET` | `/ver_cita` | Consulta el estado actual de la cita |
| `DELETE` | `/cancelar_cita` | Cancela y libera la cita |
| `POST` | `/renovar_cita` | Renueva la cita si está disponible |

---

## 🔍 Ejemplos de uso

### Crear una cita
```http
POST /crear_cita
```
**Respuesta exitosa:**
```json
{ "mensaje": "Cita creada exitosamente" }
```
**Si ya está ocupada:**
```json
{ "detail": "Cita ya reservada" }
```

### Ver estado de la cita
```http
GET /ver_cita
```
```json
{ "mensaje": "Cita Ocupado" }
// o
{ "mensaje": "Cita disponible" }
```

### Cancelar la cita
```http
DELETE /cancelar_cita
```
```json
{ "mensaje": "Cita cancelada" }
```
