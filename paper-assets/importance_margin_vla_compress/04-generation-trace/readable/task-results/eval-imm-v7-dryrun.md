# eval imm v7 dryrun

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_imm-v7-dryrun_20260515T174706_result.json`
- **Structured JSON:** [`f8191d773191baea1894.json`](../../sessions/f8/f8191d773191baea1894.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. Baseline eval 结果
**不存在** — `eval_baseline_v5.json` 文件未找到，baseline 评估仍在运行中（或未启动）。

### 2. IMM v7 训练状态
- **当前 step**: 2000/30000（~6.7%），loss=0.0089，lr=9.97e-05，3.2 steps/sec
- **Checkpoints**: `step_002000`（已保存，`latest` 软链接指向它）

### 3. IMM dry-run 结果 — **成功**

完整 JSON 已保存至 `results/eval_imm_v7_dryrun.json`。关键指标摘要：

| 条件 | action_loss | preservation_rate | kendall_tau | L·ε·k/Δ_k (mean) |
|------|-------------|-------------------|-------------|-------------------|
| eps0.0_pruneFalse | 0.0605 | 1.000 | 1.000 | 1.218 |
| eps0.0_pruneTrue | 0.0872 | 1.000 | 1.000 | 0.794 |
| eps0.01_pruneFalse | 0.0986 | 0.917 | 0.845 | 0.991 |
| eps0.01_pruneTrue | 0.0344 | 0.932 | 0.841 | 0.818 |
| eps0.02_pruneFalse | 0.0136 | 0.844 | 0.638 | 0.728 |
| eps0.02_pruneTrue | 0.0588 | 0.878 | 0.672 | 3.927 |
| eps0.05_pruneFalse | 0.0677 | 0.707 | 0.221 | 2.484 |
| eps0.05_pruneTrue | 0.0424 | 0.715 | 0.247 | 2.214 |

**Meta**: Lipschitz spectral=1.067, empirical=0.096, max_batches=5, seed=42

**注意**: 首次运行遇到 xet_get 401 错误，加 `HF_HUB_DISABLE_XET=1` 后解决。后续正式评估也需要加此环境变量。

---
