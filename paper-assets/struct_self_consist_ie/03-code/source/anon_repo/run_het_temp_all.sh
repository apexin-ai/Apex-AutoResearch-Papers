#!/bin/bash
set -e
BASE=/root/autodl-tmp/struct_self_consist_ie
SCRIPT_PATH=$BASE/artifacts/experiments/het_temp/run_het_temp.py
OUT_BASE=$BASE/output/exp_backup1_het_temp
PYTHON=/root/miniconda3/bin/python3

echo "=== het_temp Backup 1: SciERC all combos ==="
echo "Started at $(date)"

# T=0.8 vs T=1.0, seed=42
$PYTHON $SCRIPT_PATH \
  --t_low_path $BASE/output/exp_026_t08/samples.jsonl \
  --t_high_path $BASE/output/exp_026_t10_seed42/samples.jsonl \
  --t_low_label "T=0.8" --t_high_label "T=1.0" \
  --output_dir $OUT_BASE/scierc_t08_t10_s42 \
  --n_repeats 10 --seed 42

# T=0.8 vs T=1.0, seed=123
$PYTHON $SCRIPT_PATH \
  --t_low_path $BASE/output/exp_026_t08_seed123/samples.jsonl \
  --t_high_path $BASE/output/exp_026_t10_seed123/samples.jsonl \
  --t_low_label "T=0.8" --t_high_label "T=1.0" \
  --output_dir $OUT_BASE/scierc_t08_t10_s123 \
  --n_repeats 10 --seed 123

# T=0.8 vs T=1.0, seed=456
$PYTHON $SCRIPT_PATH \
  --t_low_path $BASE/output/exp_026_t08_seed456/samples.jsonl \
  --t_high_path $BASE/output/exp_026_t10_seed456/samples.jsonl \
  --t_low_label "T=0.8" --t_high_label "T=1.0" \
  --output_dir $OUT_BASE/scierc_t08_t10_s456 \
  --n_repeats 10 --seed 456

# T=0.5 vs T=1.0, seed=42
$PYTHON $SCRIPT_PATH \
  --t_low_path $BASE/output/exp_026_t05/samples.jsonl \
  --t_high_path $BASE/output/exp_026_t10_seed42/samples.jsonl \
  --t_low_label "T=0.5" --t_high_label "T=1.0" \
  --output_dir $OUT_BASE/scierc_t05_t10_s42 \
  --n_repeats 10 --seed 42

# T=0.5 vs T=1.0, seed=123
$PYTHON $SCRIPT_PATH \
  --t_low_path $BASE/output/exp_026_t05_seed123/samples.jsonl \
  --t_high_path $BASE/output/exp_026_t10_seed123/samples.jsonl \
  --t_low_label "T=0.5" --t_high_label "T=1.0" \
  --output_dir $OUT_BASE/scierc_t05_t10_s123 \
  --n_repeats 10 --seed 123

# T=0.5 vs T=1.0, seed=456
$PYTHON $SCRIPT_PATH \
  --t_low_path $BASE/output/exp_026_t05_seed456/samples.jsonl \
  --t_high_path $BASE/output/exp_026_t10_seed456/samples.jsonl \
  --t_low_label "T=0.5" --t_high_label "T=1.0" \
  --output_dir $OUT_BASE/scierc_t05_t10_s456 \
  --n_repeats 10 --seed 456

echo ""
echo "ALL_DONE at $(date)"
