#!/bin/bash
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate base
export OPENBLAS_NUM_THREADS=2
export PYTHONPATH="./src/analysis:.:$PYTHONPATH"
cd .
python -u run_reml_500.py > /tmp/reml_500.log 2>&1
