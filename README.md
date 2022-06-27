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
