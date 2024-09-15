from fastapi import FastAPI
import uvicorn

from pathlib import Path
import yaml

from api import api



app = FastAPI(debug=True)

oas_doc = yaml.safe_load((Path(__file__).parent / "../oas.yaml").read_text())

app.openapi = lambda: oas_doc

app.include_router(api.router, tags=['Order'], prefix='/orders')



if __name__ == '__main__':
    uvicorn.run('app:app', host="127.0.0.1", port=8000, reload=True)