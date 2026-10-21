# Plan006 Prolog Execution-Only — Final Readiness Checklist

**Date**: 2026-05-14 17:15 UTC
**Server**: westd-39279 (aml-train image, conda base)

## Checklist

| # | Check | Status | Details |
|---|-------|--------|---------|
| 1 | Training data | PASS | `data/train_500_seed42.jsonl` exists, 500 lines, fields: id/context/question/answer/fol_premises/fol_conclusion/depth |
| 2 | Eval data | PASS | `data/proofwriter_fol_100.jsonl` exists, 100 lines |
| 3 | Config `num_steps` | PASS | `num_steps: 500` confirmed in `configs/grpo_prolog_exec_only.yaml` |
| 4 | Config `logic_type` | PASS | `logic_type: prolog` |
| 5 | Config `reward_mode` | PASS | `reward_mode: execution_only` |
| 6 | Config `model_path` | PASS | `/root/autodl-tmp/models/Qwen3-4B` (3 safetensors shards present) |
| 7 | Config `data_path` | PASS | `data/train_500_seed42.jsonl` (C001 compliant) |
| 8 | Config `save_total_limit` | PASS | `save_total_limit=1` hardcoded in train_grpo.py:419 (C003 compliant) |
| 9 | Config `log_completions` | PASS | `log_completions=False` in train_grpo.py:425 (C003 compliant, no parquet) |
| 10 | SWI-Prolog | PASS | swipl 8.4.2, `PrologSolver.is_available()=True` |
| 11 | PrologSolver dry-run | PASS | `prove()` test: success=True, proved=True, time=0.021s |
| 12 | train_grpo.py imports | PASS | `build_prolog_dataset`, `prolog_sta_reward`, `make_reward_fn` all found |
| 13 | Disk space | PASS | `/root/autodl-tmp`: 112G free / 250G total (56% used) |
| 14 | Output dir conflict | PASS | No existing `plan006_*` directories |
| 15 | Model weights | PASS | 3/3 safetensors shards present |

**Result: 15/15 PASS**

## Config Summary (grpo_prolog_exec_only.yaml)

```yaml
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/train_500_seed42.jsonl
logic_type: prolog
reward_mode: execution_only
num_steps: 500
per_device_batch_size: 4
gradient_accumulation_steps: 2
num_generations: 8
max_completion_length: 512
learning_rate: 1.0e-6
exec_weight: 1.0
sta_weight: 0.0
seed: 42
solver: prolog
no_wandb: true
```

Hardcoded in train_grpo.py:
- `save_steps=50`, `save_total_limit=1`, `save_only_model=True`
- `log_completions=False`
- `bf16=True`

## Launch Commands (3-seed)

### Seed 42 (cuda:0)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && export CUDA_VISIBLE_DEVICES=0 && python scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42
```

### Seed 43 (cuda:1)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && export CUDA_VISIBLE_DEVICES=1 && python scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43
```

### Seed 44 (cuda:0 or 1, after earlier seed completes)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && export CUDA_VISIBLE_DEVICES=0 && python scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44
```

## Notes
- Commands use `export CUDA_VISIBLE_DEVICES=N` (not inline assignment) per C002
- `no_wandb: true` in config — wandb disabled for these runs
- vLLM version warning (0.18.1 vs TRL supported 0.11-0.17.1) is non-blocking — previous dry-runs passed
- Each run ~16GB model weight on disk (save_total_limit=1), total ~48GB for 3 seeds. 112G free is sufficient
