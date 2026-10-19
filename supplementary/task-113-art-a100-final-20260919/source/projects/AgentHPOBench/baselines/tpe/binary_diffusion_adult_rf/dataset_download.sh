#!/usr/bin/env bash
set -euo pipefail
BASE=.
mkdir -p "$BASE/data/paper_exact/binary_diffusion_adult_rf"
cp "$BASE/repositories/binary-diffusion-tabular/data/adult_train.csv" "$BASE/data/paper_exact/binary_diffusion_adult_rf/adult_train.csv"
cp "$BASE/repositories/binary-diffusion-tabular/data/adult_test.csv" "$BASE/data/paper_exact/binary_diffusion_adult_rf/adult_test.csv"
