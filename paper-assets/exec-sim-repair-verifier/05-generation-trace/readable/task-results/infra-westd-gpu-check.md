# infra westd gpu check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-gpu-check_20260516T010909_result.json`
- **Structured JSON:** [`2510f550a324d920c4a8.json`](../../sessions/25/2510f550a324d920c4a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

| GPU | 型号 | 显存占用 | GPU 利用率 | PID | 进程 |
|-----|------|---------|-----------|-----|------|
| 0 | RTX 5090 | 17609/32607 MiB (54%) | 99% | 444502 | `eval_repo_cls.py` — CLS 8B ckpt1000 test mutation eval (s42) |
| 1 | RTX 5090 | 17609/32607 MiB (54%) | 85% | 444130 | `eval_repo_cls.py` — CLS 8B ckpt1000 test mutation eval (s42_resume) |
| 2 | RTX 5090 | 29273/32607 MiB (90%) | 97% | 442200 | `train_repo_cwm.py` — CWM 8B 训练 (从 ckpt-6100 恢复, epoch 3) |
| 3 | RTX 5090 | 21133/32607 MiB (65%) | 100% | 443221 | `eval_repo_cwm.py` — CWM 8B ckpt400 test eval |

**4 块 GPU 全部占满，无空闲。**

### CWM 8B 训练 (GPU 2)
- 进度：6198/6633 steps (93%)，已训练约 6h15m
- 速度：~12s/it，预计剩余约 1h43m

### CWM 8B ckpt400 test eval (GPU 3)
- 结果文件：`/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/results_incremental.jsonl`
- 已完成：5472 样本（5287 new + resumed），总计 9784 样本
- 进度：约 54%，running_acc=57.1%

### CLS 8B eval (GPU 0 & 1)
- 两个并行的 CLS 8B s42 ckpt1000 test mutation eval，分别输出到不同目录

### Orphan 进程
- 无 orphan 进程。旧的 `eval_cwm_seed123` tmux session (PID 194398) 仍在，但无对应 python 进程运行。
- `auto_backup_checkpoints.sh` 后台脚本在运行（PID 228420）。

---
