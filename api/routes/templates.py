from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./templates")

router = APIRouter(tags=["templates"], include_in_schema=False)

# Home Page
@router.get("/", response_class=HTMLResponse)
def landing_page(request: Request):
    data = {"page": "Home page"}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})


# About Page
@router.get("/about", response_class=HTMLResponse)
def landing_page(request: Request):
    data = {"page": "About page"}
    return templates.TemplateResponse("about.html", {"request": request, "data": data})
