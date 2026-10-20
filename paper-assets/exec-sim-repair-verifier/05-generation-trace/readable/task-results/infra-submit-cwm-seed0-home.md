# infra submit cwm seed0 home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_submit-cwm-seed0-home_20260512T125007_result.json`
- **Structured JSON:** [`f425c82f7cca0302871d.json`](../../sessions/f4/f425c82f7cca0302871d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cwm-seed0 已成功启动：

- **PID**: 2764835
- **tmux session**: cwm-seed0
- **GPU**: cuda:0 (home-1x5090)
- **Log**: `~/runs/exec-sim-repair-verifier/cwm-seed0.log`
- **命令**: `cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name .../Qwen3-4B/...1cfa9a72... --output_dir checkpoints_cwm_seed0/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 0 && python3 eval_cwm_baseline.py --checkpoint_dir checkpoints_cwm_seed0/best/ --output eval_cwm_seed0.json`

Log 确认正常加载：
```
Loading tokenizer: .../Qwen3-4B/snapshots/1cfa9a72...
Chat template kwargs: {'enable_thinking': False}
Loaded train=15290, val=1896
```

模型正在加载到 GPU，nvidia-smi 尚未显示占用（CPU 阶段），启动正常。CWM 5-seed 最后一个已提交。

---
