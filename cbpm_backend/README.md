# CBPM backend server

This little fastapi server mocks our "proxy"-service-server.

obtains information for Data Gathering:

- weather data
  - incident location (Bodensee, Nordsee, Ostsee, See, Fluss)
- route gps data
- get investigators
- check proposed investagor
- get applicable jurisdiction data by country

## setup

```cmd
conda create -n cbpm python=3.7
conda activate cbpm
python -m pip install fastapi uvicorn pytest starlette==0.12.9
python -m pip install -U fastapi black gmplot
```

## execution

```cmd
REM execution: make sure you are in the dir
python app\main.py
REM open http://127.0.0.1:8000/docs
```
