FROM python:3.10.4-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

# this is to help prevent installing requirements everytime we update our
# source code, this is cause docker has a caching system.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# uvicorn app.main:app --host 0.0.0.0 --port 8000 
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]