from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Any
from back.database import DataBase

app = FastAPI()
templates = Jinja2Templates(directory='front/html')
app.mount('/css', StaticFiles(directory="front/css"), name="static")
app.mount('/images', StaticFiles(directory="front/images"), name="static")
app.mount('/js', StaticFiles(directory="front/js"), name="static")


@app.get("/")
async def get_start_page(request: Request) -> Any:
    return templates.TemplateResponse(
        'start.html', {'request': request}
    )


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


@app.post('/reservation')
async def do_reservation(request: Request) -> Any:
    data_from_form = dict(await request.form())
    database = DataBase()
    table_number = int(data_from_form.get('table').strip())
    name = data_from_form.get('name')
    date = data_from_form.get('date')
    if not database.tableReserved(date, table_number):
        telephone = data_from_form.get('phone')
        comments = data_from_form.get('message')
        email = data_from_form.get('email')
        database.insert(name=name, table=table_number, telephone=telephone, comments=comments, date=date, email=email)
        return templates.TemplateResponse('reservation.html', {'request': request,
                                                               'result': f'Столик №{table_number} на имя {name} забронирован {date}.'})
    return templates.TemplateResponse('reservation.html', {'request': request,
                                                           'result': f'{name}, к сожалению столик №{table_number} забронирован на данную дату. Выберите другой или забронируйте на другое число.'})
