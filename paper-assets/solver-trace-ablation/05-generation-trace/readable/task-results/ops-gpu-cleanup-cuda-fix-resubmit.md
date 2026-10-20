# ops gpu cleanup cuda fix resubmit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-cleanup-cuda-fix-resubmit_20260514T002048_result.json`
- **Structured JSON:** [`1912ff2b029a89d70a07.json`](../../sessions/19/1912ff2b029a89d70a07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**GPU 清理**：kill PID 122801（占用两张 GPU 的 zombie 进程），显存归零。

**CUDA 修复**：两个 config 的 `data_path` 都是错误的 `proofwriter_fol_500.jsonl`，通过 CLI `--data_path data/train_500_seed42.jsonl` 覆盖（符合 C001）。提交命令用 `export CUDA_VISIBLE_DEVICES=N`（符合 C002）。

**验证结果**：
- GPU 0: PID 126466, 25.8GB, 91% util → `plan013-random-reward-s42-r2`
- GPU 1: PID 126546, 25.5GB, 91% util → `plan001-exec-only-s43-r2`
- 每张 GPU 只有一个进程，无越界。

两个实验均已注册 RUNNING 状态。

---
