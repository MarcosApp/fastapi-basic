# FastAPI Basic

Simple CRUD-style example using FastAPI with an in-memory fake database.

## Setup

1. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:
```bash
pip install fastapi uvicorn
```

## Run

```bash
python -m uvicorn main:app --reload
```

Open:
- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`

## Endpoints

- `GET /` list items
- `POST /` create item
- `PUT /` update item by id
- `DELETE /` delete item by id

## Example payloads

```json
POST /
{ "name": "Item 1", "description": "demo" }
```

```json
PUT /
{ "id": 1, "name": "Item 1 editado" }
```

```json
DELETE /
{ "id": 1 }
```

Note: data is stored in memory and resets on restart.
