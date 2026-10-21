# ops check training progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-training-progress_20260516T113514_result.json`
- **Structured JSON:** [`07d4adc1766b8d38e8de.json`](../../sessions/07/07d4adc1766b8d38e8de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### cls-repo (GPU 0, `checkpoints_repo_cls_v5_conda`)
- **Step 643/6633** (~9.7%)
- eval_loss=0.0996 (at step 600 checkpoint)
- Speed: ~7.3s/it
- **ETA: ~12h（约明早 07:40 UTC）**

### cwm-repo (GPU 1, `checkpoints_repo_cwm_seed123_conda`)
- **Step 695/6633** (~10.5%)
- eval完成 step 600 checkpoint
- Speed: ~7.9s/it
- **ETA: ~13h（约明早 08:35 UTC）**

### cuda:2 — 不空闲
- 正在跑 `checkpoints_repo_cls_8b_conda` (PID 499350)
- **Step 662/6633** (~10.0%)
- loss=0.9534, eval_loss=0.0937 (step 600)
- Speed: ~8.1s/it, ETA ~13.4h

### cuda:3 — 空闲
- 0 MiB 显存, 0% 利用率，可用

### eval 脚本
- `eval_repo_verifier.py` ✓
- `eval_repo_cwm.py` ✓
- `run_deepseek_repo_eval.sh` ✓ (支持 `bash run_deepseek_repo_eval.sh [cls|cwm] [gpu_id]`)

---

**注意**: 你给的旧日志 (`train_repo_cls.log` / `train_repo_cwm.log`) 是 5/12 的 crash 记录（DataLoader ValueError，collator 收到 dict 而非 tensor）。当前跑的是修复后的版本，在 `checkpoints_repo_*_conda/train.log` 里。三个训练都刚过 step 600 checkpoint，运行正常。

---
