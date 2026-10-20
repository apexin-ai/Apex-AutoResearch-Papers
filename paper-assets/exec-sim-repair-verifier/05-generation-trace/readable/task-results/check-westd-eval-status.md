# check westd eval status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-eval-status_20260514T052141_result.json`
- **Structured JSON:** [`3853a670f8192bbb7bad.json`](../../sessions/38/3853a670f8192bbb7bad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU 使用

| GPU | 型号 | 显存占用 | 利用率 | 状态 |
|-----|------|---------|--------|------|
| 0 | RTX 5090 | 13.0/32.6 GB | 85% | eval_cwm_seed123 |
| 1 | RTX 5090 | 13.0/32.6 GB | 100% | eval_cwm_v12 |
| 2 | RTX 5090 | 0/32.6 GB | 0% | **空闲** |
| 3 | RTX 5090 | 0/32.6 GB | 0% | **空闲** |

### Eval 进度

| 会话 | 进度 | Running Acc | 预计剩余 |
|------|------|-------------|----------|
| eval_cwm_seed123 | 2424/9784 (24.8%) | **57.2%** | ~5.2h（~52s/8样本） |
| eval_cwm_v12 | 2448/9784 (25.0%) | **58.4%** | ~5.1h |

两个 eval 均从 09:03 开始运行，已跑约 4.3 小时，完成约 25%。结果目录已创建但尚无输出文件（predictions 在全部跑完后才写入）。

- Checkpoint: seed123 → `checkpoints_repo_cwm_seed123_conda/checkpoint-500`，v12 → `checkpoints_repo_cwm_conda_v12/checkpoint-500`
- 输出目录: `/root/autodl-tmp/results/repo_cwm_seed123_conda_eval/` 和 `repo_cwm_v12_conda_eval/`
- GPU 2、3 空闲可用

---
