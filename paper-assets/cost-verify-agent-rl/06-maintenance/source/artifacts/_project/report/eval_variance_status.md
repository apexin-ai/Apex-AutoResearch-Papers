# P1 Eval Variance Experiment Status

## h-sweep Kill
- **Status**: ✅ Completed
- PIDs killed: 42499 (parent), 42504 (train.py), 44710 (ray worker zombie), 16984 (TaskRunner), 43044/43045/43110 (ray support)
- GPU confirmed free: 0 MiB, 0% utilization

## Available Checkpoints (verified on bjb1-17606)

| Checkpoint | Path | Think | Notes |
|-----------|------|-------|-------|
| seed300 step5 | `/root/autodl-tmp/checkpoints/qwen_exp029_seed300_step5_hf` | False | Stagnant seed |
| seed7 high_kl step5 | `/root/autodl-tmp/checkpoints/exp029_seed7_high_kl_step5_hf` | True | Pre-collapse / generalized |
| seed200 step5 | `/root/autodl-tmp/checkpoints/qwen_exp029_seed200_step5_hf` | True | Another seed |

All checkpoints contain `model.safetensors` + tokenizer files (Qwen3 1.7B).

## Existing OOD Eval Configs Used as Templates

| Config | Checkpoint | Think |
|--------|-----------|-------|
| `_alfworld_seed300_step5_ood_eval.yaml` | seed300 step5 | False |
| `_alfworld_seed7_ood_precollapse.yaml` | seed7 high_kl step5 | True |
| `_alfworld_seed200_step5_ood_eval.yaml` | seed200 step5 | True |

All configs share:
- 134 OOD tasks (`AlfworldSG_OOD`)
- `context_window_mode: full` (episode-level)
- `temperature: 0.4`, `do_sample: True`
- `max_turn: 50`
- Single GPU (`cuda:0`)

## 3×3 Eval Variance Design

**Variance source**: `seed.val` override (0, 1, 2) — affects random state for task ordering and torch/numpy seeding; combined with `do_sample=True, temperature=0.4` produces stochastic sampling.

| Run | Config | seed.val | Experiment Name |
|-----|--------|----------|-----------------|
| 1 | _alfworld_seed300_step5_ood_eval | 0 | evalvar-seed300-s0 |
| 2 | _alfworld_seed300_step5_ood_eval | 1 | evalvar-seed300-s1 |
| 3 | _alfworld_seed300_step5_ood_eval | 2 | evalvar-seed300-s2 |
| 4 | _alfworld_seed7_ood_precollapse | 0 | evalvar-seed7hk-s0 |
| 5 | _alfworld_seed7_ood_precollapse | 1 | evalvar-seed7hk-s1 |
| 6 | _alfworld_seed7_ood_precollapse | 2 | evalvar-seed7hk-s2 |
| 7 | _alfworld_seed200_step5_ood_eval | 0 | evalvar-seed200-s0 |
| 8 | _alfworld_seed200_step5_ood_eval | 1 | evalvar-seed200-s1 |
| 9 | _alfworld_seed200_step5_ood_eval | 2 | evalvar-seed200-s2 |

## Execution

- **Script**: `/root/cost-verify-agent-rl/RAGEN/run_eval_variance.sh`
- **PID**: 46188 (nohup bash wrapper) → 46205 (python train.py)
- **Log**: `/root/autodl-tmp/eval_variance_logs/nohup.log`
- **Summary log**: `/root/autodl-tmp/eval_variance_logs/summary.log`
- **Per-run logs**: `/root/autodl-tmp/eval_variance_logs/seed300_s{0,1,2}.log`, `seed7hk_s{0,1,2}.log`, `seed200_s{0,1,2}.log`
- **wandb project**: `cost-verify-agent-rl` (team: xiaoyucorynne-)
- **Started**: 2026-05-24 02:40 (BJB1 server time)

### Timing Observations (Run 1: evalvar-seed300-s0)
- Initialization (model load + AlfWorld env setup): ~5.5 minutes
- Inference: **in progress** (GPU bursts to 100%, multi-turn agent eval)
- Single eval time estimate: **TBD** (will update after first run completes)

### Estimated Total Time
- Per run: ~5.5 min init + X min inference
- Total 9 runs: 9 × (5.5 + X) min
- Will update once first run completes

## Monitoring Commands
```bash
# Check progress
tail -20 /root/autodl-tmp/eval_variance_logs/nohup.log
cat /root/autodl-tmp/eval_variance_logs/summary.log

# GPU status
nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv,noheader

# Process status
ps aux | grep train.py | grep -v grep
```
