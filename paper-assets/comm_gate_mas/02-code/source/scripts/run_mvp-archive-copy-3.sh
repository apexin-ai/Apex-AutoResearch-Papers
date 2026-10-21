#!/bin/bash
set -e
export PYTHONPATH="src:$PYTHONPATH"
echo "=== Step 1: Trace Collection ==="
python src/trace_collection.py --config configs/mvp.yaml
echo "=== Step 2: Local Impact Measurement ==="
python src/local_impact.py --config configs/mvp.yaml
echo "=== Step 3: Functional Annotation (cross-model) ==="
python src/functional_annotation.py --config configs/mvp.yaml --cross-model
echo "=== Step 4: Correctness Annotation ==="
python src/correctness_annotation.py --config configs/mvp.yaml
echo "=== Step 5: Statistical Analysis ==="
python src/analysis.py --config configs/mvp.yaml
echo "=== MVP Pipeline Complete ==="
