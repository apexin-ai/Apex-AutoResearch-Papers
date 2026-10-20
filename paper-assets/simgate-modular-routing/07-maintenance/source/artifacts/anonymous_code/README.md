# Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld

Anonymous code release for EMNLP 2026 ARR submission.

## Overview

This repository contains the code for reproducing the main results of the paper. We provide:

1. **Counterfactual analysis** (Algorithm 1): Episode-level paired comparison that runs each task under two pure strategies (internal reasoning vs. deterministic tool use) and applies death-aware labeling.
2. **DAF computation**: Death Avoidance Fraction metric with bootstrap confidence intervals.
3. **Death decomposition analysis**: Quantifies the contribution of death avoidance vs. genuine score improvement to the routing signal.
4. **Guided router**: A decomposition-guided router that routes based on task-type death risk.
5. **Router training**: LoRA-based SFT training for classification and generative routing.

## Environment Setup

```bash
# Python 3.10+
pip install -r requirements.txt

# ScienceWorld requires Java (JDK 11+)
# sudo apt-get install openjdk-11-jdk
```

## Data

See `data/README.md` for instructions on obtaining the required datasets:
- **ScienceWorld** v1.2.3 (Apache 2.0) — interactive science simulation
- **ALFWorld** (MIT) — household task environment
- **MATH** (MIT) — competition mathematics

## Reproducing Results

### Step 1: Counterfactual Data Collection (Table 2)

Collect episode-level counterfactual labels on ScienceWorld (paired mode, default):

```bash
python src/counterfactual_analysis.py \
    --task_type "freeze" \
    --n_episodes 30 \
    --max_steps 30 \
    --model_path <path-to-Qwen2.5-7B-Instruct> \
    --output_dir results/counterfactual/
```

Repeat for all 11 task types. See `configs/default.yaml` for the full task list.
Each task produces `results/counterfactual/{task_type}/episodes.jsonl`.

For ALFWorld and MATH extensions (Table 4):
```bash
python src/alfworld_counterfactual.py \
    --n_episodes 50 \
    --output_dir results/alfworld-counterfactual/

python src/math_counterfactual.py \
    --n_problems 200 \
    --output_dir results/math-counterfactual/
```

### Step 2: Death Decomposition Analysis (Table 3, Figure 2)

```bash
python src/death_decomposition.py \
    --data_dir results/counterfactual/ \
    --output results/decomposition/
```

### Step 3: DAF Computation (Section 2.4)

```bash
python src/daf_computation.py \
    --data_path results/counterfactual/ \
    --n_bootstrap 10000 \
    --output results/daf_bootstrap.json
```

Note: `--data_path` accepts a directory containing per-task `episodes.jsonl` files from Step 1.

### Step 4: Guided Router Evaluation (Table 5)

```bash
# Oracle variant
python -m src.guided_router.eval_episode \
    --data_path results/counterfactual/ \
    --variant oracle

# Leave-One-Task-Out evaluation
python -m src.guided_router.loto_eval \
    --data_path results/counterfactual/
```

### Step 5: Router SFT Training (Table 6)

```bash
# Generate training data
python src/router_training/format_implicit_data.py \
    --data_dir results/counterfactual/ \
    --output_dir data/implicit_sft/

# Train generative router (LoRA)
python src/router_training/generative_router_sft.py \
    --data_path data/implicit_sft/implicit_sft.jsonl \
    --model_name Qwen/Qwen3-1.7B \
    --output_dir checkpoints/generative_router/ \
    --epochs 3 --lr 2e-5
```

## License

Code: MIT License.
Datasets: see individual licenses (ScienceWorld: Apache 2.0, ALFWorld: MIT, MATH: MIT).
