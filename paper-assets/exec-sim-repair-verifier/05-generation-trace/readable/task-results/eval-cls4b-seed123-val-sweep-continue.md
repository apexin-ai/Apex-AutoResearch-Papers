# eval cls4b seed123 val sweep continue

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls4b-seed123-val-sweep-continue_20260514T205947_result.json`
- **Structured JSON:** [`6acc374d14ab7202130c.json`](../../sessions/6a/6acc374d14ab7202130c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4B CLS seed123 val@5120 sweep 最终结果

| Checkpoint | Accuracy | F1 macro | F1 fail | F1 pass | Gap vs baseline |
|-----------|----------|----------|---------|---------|----------------|
| ckpt-400 | 86.01% | 79.66 | 68.30 | 91.02 | +10.13pp |
| ckpt-600 | 81.89% | 77.01 | 66.43 | 87.60 | +6.01pp |
| **ckpt-800** | **87.92%** | **81.95** | **71.57** | **92.33** | **+12.04pp** |

### 关键发现

**Val@5120 best = ckpt-800**，但与 test 结果严重不一致：

| | Val@5120 best | Test@2048 best |
|--|--------------|----------------|
| Checkpoint | ckpt-800 (87.92%) | ckpt-600 (80.73%) |
| ckpt-800 表现 | **最佳** (87.92%) | **严重退化** (74.27%) |

这与 val@2048 趋势一致（val@2048 best acc = ckpt-1000）。**Val-test distribution shift 显著——不能只靠 val 选 checkpoint。**

所有 3 个 checkpoint unparseable = 0（vs val@2048 的 20%），truncated 均 234/9335 (2.5%)。

### 当前状态
- Sweep 脚本自动继续跑 v5 (seed42) checkpoints（v5-ckpt600 正在运行）
- Registry 已更新

---
