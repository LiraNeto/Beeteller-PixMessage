python -m pip install virtualenv;
python -m virtualenv -p python .venv;
. ./.venv/Scripts/activate;
python -m pip install -r requirements.txt;
pre-commit install;
