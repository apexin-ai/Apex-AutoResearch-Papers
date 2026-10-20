# status home val 4096 check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_home-val-4096-check_20260514T121835_result.json`
- **Structured JSON:** [`cbd404d1cddccd89501c.json`](../../sessions/cb/cbd404d1cddccd89501c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## val_4096 ckpt-400 eval 状态报告

### 1. 状态：进行中
- **PID 3083027** 仍在运行，已运行 **13h55m**
- 进度：**4795/9335 = 51.4%**（上次检查 28.8%）
- Running accuracy：**82.0%**
- batch_size=2（命令行参数与之前记录的 bs=4 不同，实际是 bs=2）

### 2. ETA 估算
- 速率：~5.74 samples/min
- 剩余：~4540 samples → ~13h11m
- 预计完成：**~18:30 UTC / ~11:30 AM PDT（May 14）**

### 3. GPU 使用
- cuda:0 被 PID 3083027 占用，**10736 MiB**

### 4. checkpoint-600
- `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123_home/checkpoint-600` **存在**，ckpt-400 完成后可启动 ckpt-600 eval

### 5. 输出路径
- 预测文件：`val_eval_results_4096/seed123_ckpt400/eval_repo_cls_predictions.jsonl`（4748 行已写入）
- 日志：`val_4096_ckpt400.log`

---
