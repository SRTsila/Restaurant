from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Any

app = FastAPI()
templates = Jinja2Templates(directory='restaurant/front/html')
app.mount('/css', StaticFiles(directory="restaurant/front/css"), name="static")
app.mount('/images', StaticFiles(directory="restaurant/front/images"), name="static")


@app.get("/")
async def get_start_page(request: Request) -> Any:
    return {'start.html', {'request': request}}


@app.get('/menu')
async def get_menu_page(request: Request) -> Any:
    return templates.TemplateResponse(
        'menu.html', {'request': request}
    )


@app.get('/contacts')
async def get_contact_page(request: Request) -> Any:
    return templates.TemplateResponse(
        'contacts.html', {'request': request}
    )


@app.get('/reservation')
async def get_reservation_page(request: Request) -> Any:
    return templates.TemplateResponse(
        'reservation.html', {'request': request}
    )
