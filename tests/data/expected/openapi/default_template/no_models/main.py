# generated by fastapi-codegen:
#   filename:  no_models.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(
    version='1.0.0',
    title='Swagger Petstore',
    license={'name': 'MIT'},
    description=None,
    servers=[{'url': 'http://petstore.swagger.io/v1'}],
)


@app.get('/hello', response_model=str)
def hello() -> str:
    """
    get hello message
    """
    pass
