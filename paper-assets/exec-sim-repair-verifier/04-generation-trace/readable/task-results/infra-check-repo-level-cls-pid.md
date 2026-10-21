# infra check repo level cls pid

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-repo-level-cls-pid_20260512T141455_result.json`
- **Structured JSON:** [`331721178053febd023b.json`](../../sessions/33/331721178053febd023b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。两个实验状态：

---

**1. repo-level-cls (seetacloud-westd-4x5090)**
- **PID: 34681**
- 命令: `python3 train_repo_verifier.py --max_seq_length 4096 --no_wandb --device cuda:0`
- GPU 0: RTX 5090, 31124MiB/32607MiB, 100% 利用率
- 训练进度: **step 1104/6633 (~17%)**, epoch 1, 已运行约 2h42m, ~8.5s/step
- 预计剩余: ~13h

**2. cls8b-seed456 (home-1x5090)**
- **PID 2810143 存活**, 确认是 train_verifier.py (Qwen3-8B, seed 456)
- 训练进度: **step 303/1434 (~21%)**, epoch 1, 已运行约 17m25s, ~3.5s/step
- 预计剩余: ~1h6m

---
