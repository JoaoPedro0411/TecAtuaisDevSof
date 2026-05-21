#!/usr/bin/env bash
set -e

echo "======================================"
echo " Verificando Conda e ambiente ativo"
echo "======================================"

if ! command -v conda >/dev/null 2>&1; then
    echo "ERRO: conda não foi encontrado no PATH."
    echo "Abra um terminal com Conda habilitado ou rode: source ~/anaconda3/etc/profile.d/conda.sh"
    exit 1
fi

source "$(conda info --base)/etc/profile.d/conda.sh"

echo "Ambiente Conda ativo: ${CONDA_DEFAULT_ENV:-base}"
echo

echo "======================================"
echo " Verificando bibliotecas faltantes"
echo "======================================"

mapfile -t MISSING_PKGS < <(python - <<'PY'
import importlib

packages = {
    "dash": "dash",
    "plotly.express": "plotly",
    "dash_ag_grid": "dash-ag-grid",
    "dash_bootstrap_components": "dash-bootstrap-components",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
}

for module_name, conda_package in packages.items():
    try:
        importlib.import_module(module_name)
    except Exception:
        print(conda_package)
PY
)

if [ "${#MISSING_PKGS[@]}" -eq 0 ]; then
    echo "Todas as bibliotecas necessárias já estão instaladas."
else
    echo "Pacotes faltantes:"
    printf ' - %s\n' "${MISSING_PKGS[@]}"
    echo

    echo "======================================"
    echo " Configurando canal conda-forge"
    echo "======================================"

    conda config --add channels conda-forge >/dev/null 2>&1 || true
    conda config --set channel_priority strict

    echo
    echo "======================================"
    echo " Instalando pacotes faltantes"
    echo "======================================"

    conda install -y -c conda-forge "${MISSING_PKGS[@]}"
fi

echo
echo "======================================"
echo " Testando imports finais"
echo "======================================"

python - <<'PY'
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd

import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

import base64
from io import BytesIO

print("OK: todos os imports funcionaram.")
print("Dash:", Dash)
print("Pandas:", pd.__version__)
print("Matplotlib:", matplotlib.__version__)
PY

echo
echo "Instalação/verificação concluída."
