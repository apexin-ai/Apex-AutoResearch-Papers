# Execution-Free Repair Verification: Classification vs. Generation vs. Trajectory

Code and data for the paper *"Execution-Free Repair Verification: A Systematic Comparison of Classification, Generation, and Trajectory Formulations"* (EMNLP 2026 submission).

## Setup

```bash
pip install -r requirements.txt
```

PyTorch with CUDA is required for training and inference. See [pytorch.org](https://pytorch.org/) for installation instructions matching your CUDA version.

## Data

### Function-level data (HumanEval + MBPP)

```bash
# Build classification data (code, test) -> pass/fail
python build_data.py --output_dir data/

# Convert to CWM generation format (code, test) -> execution output
python build_cwm_data.py --input_dir data/ --output_dir data/
```

### Repository-level data (SWE-bench)

Repository-level data requires the [SWE-bench](https://github.com/princeton-nlp/SWE-bench) package. See `build_data.py --help` for SWE-bench data options.

## Training

All formulations (CLS, CWM, TRAJ) use LoRA fine-tuning via a unified training script:

```bash
# CLS (per-test classification)
python train_unified.py \
  --model_name Qwen/Qwen3-4B \
  --data_dir data/ \
  --formulation cls \
  --output_dir checkpoints/cls_qwen3_4b/ \
  --seed 42

# CWM (execution output generation)
python train_unified.py \
  --model_name Qwen/Qwen3-4B \
  --data_dir data/ \
  --formulation cwm \
  --output_dir checkpoints/cwm_qwen3_4b/ \
  --seed 42

# TRAJ (trajectory-level scoring)
python train_unified.py \
  --model_name Qwen/Qwen3-4B \
  --data_dir data/ \
  --formulation traj \
  --output_dir checkpoints/traj_qwen3_4b/ \
  --seed 42
```

Supported models: `Qwen/Qwen3-4B`, `Qwen/Qwen3-8B`, `Qwen/Qwen3-14B`, `deepseek-ai/deepseek-coder-6.7b-instruct`.

## Evaluation

```bash
# CLS / TRAJ evaluation
python eval_majority_voting.py \
  --checkpoint checkpoints/cls_qwen3_4b/best/ \
  --data_dir data/ \
  --output results/cls_qwen3_4b.json

# CWM evaluation
python eval_cwm_baseline.py \
  --checkpoint checkpoints/cwm_qwen3_4b/best/ \
  --data_dir data/ \
  --output results/cwm_qwen3_4b.json

# 14B zero-shot / few-shot baselines
python eval_14b_baseline.py \
  --model_name Qwen/Qwen3-14B \
  --data_dir data/ \
  --output results/14b_baseline.json
```

## Analysis

```bash
# TOST equivalence testing and sensitivity analysis
python tost_sensitivity.py

# ICC computation for oracle accuracy framework
python compute_deepseek_func_icc.py

# Supplementary statistics (bootstrap CIs, interaction tests)
python compute_supplementary_stats.py

# CWM format compliance and error analysis
python analyze_cwm_eval.py --results_dir results/
python cwm_forced_parse.py --results_dir results/
python cwm_parseable_bias.py --results_dir results/

# Routing analysis (error complementarity)
python routing_analysis.py --results_dir results/
```

## Re-repair (downstream application)

```bash
# Generate re-repair candidates using CLS verifier feedback
python cls_inference_for_rerepair.py \
  --checkpoint checkpoints/cls_qwen3_8b/best/ \
  --data_dir data/

# Run re-repair pipeline
python re_repair_v2.py --data_dir data/ --output_dir results/rerepair/

# Evaluate re-repair results
python re_repair_eval.py --results_dir results/rerepair/
```

## LoRA Adapter Merging

```bash
python merge_lora.py --base_model Qwen/Qwen3-4B --adapter checkpoints/cls_qwen3_4b/best/ --output merged_model/
```

## Repository Structure

```
build_data.py              # Function-level data generation (HumanEval + MBPP mutations)
build_cwm_data.py          # Convert classification data to CWM generation format
train_unified.py           # Unified LoRA fine-tuning for CLS/CWM/TRAJ
train_cwm_baseline.py      # CWM-specific training (legacy, use train_unified.py)
eval_cwm_baseline.py       # CWM generation evaluation
eval_14b_baseline.py       # 14B zero/few-shot baselines
eval_majority_voting.py    # Per-test majority voting evaluation
eval_cwm_constrained.py    # CWM with constrained decoding
tost_sensitivity.py        # TOST equivalence margin sensitivity
compute_deepseek_func_icc.py  # Intra-class correlation for oracle framework
compute_supplementary_stats.py # Bootstrap CIs, interaction z-tests
analyze_cwm_eval.py        # CWM error analysis
cwm_forced_parse.py        # Forced parsing of CWM outputs
cwm_parseable_bias.py      # Parseable output bias analysis
routing_analysis.py        # Error complementarity / routing analysis
cls_inference_for_rerepair.py # CLS inference for re-repair pipeline
re_repair_v2.py            # Re-repair pipeline
re_repair_eval.py          # Re-repair evaluation
merge_lora.py              # Merge LoRA adapter into base model
docs/paper/                # LaTeX source for the paper
```

## License

This repository is released for research purposes under the MIT License.
