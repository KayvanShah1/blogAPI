# BlogIt API

## Setup of development environment

1. Create a new Python environment and activate.

    **Conda** (from scratch)

    ```bash
    export PYTHON_VERSION=3.10.4
    conda create --name fastapi python=PYTHON_VERSION
    conda activate fastapi
    ```

    **Conda environment.yml file**

    ```bash
    conda env create -f conda-environment.yml
    ```

    **Virtual environment**

    ```bash
    python -m venv ENV
    source ENV/bin/activate
    ```

2. Install dependencies in your environments

    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

## Run the APP

Run the command below in the terminal

1. Linux

    ```bash
    scripts/fastapi-server.sh
    ```

2. Windows

    ```cmd
    uvicorn app.main:app --reload
    ```

3. Run with Uvicorn multiple workers

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
    ```

4. Run with Gunicorn & Uvicorn
    ```bash
    gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
    ```
