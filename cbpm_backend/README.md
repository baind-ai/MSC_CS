# CBPM backend server

This little fastapi server mocks our "proxy"-service-server.

## setup

```cmd
conda create -n cbpm python=3.7
conda activate cbpm
python -m pip install fastapi uvicorn pytest starlette==0.12.9
```

```cmd
REM execution: make sure you are in the dir
python app\main.py
REM open http://127.0.0.1:8000/docs
```