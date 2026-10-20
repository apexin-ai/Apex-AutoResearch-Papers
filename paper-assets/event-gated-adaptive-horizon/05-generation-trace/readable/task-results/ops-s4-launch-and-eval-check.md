# ops s4 launch and eval check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s4-launch-and-eval-check_20260519T172737_result.json`
- **Structured JSON:** [`ce0becbfdbdddd36ce5a.json`](../../sessions/ce/ce0becbfdbdddd36ce5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### s4 启动状态
- **tmux session**: `exp_025_s4` 运行中，已到 [5000] 开始 evaluation
- **PID**: 851587 (bash), 851593 (python, cuda:1 占用 794 MiB，正在初始化)
- **GPU**: cuda:1 当前总占用 ~10.3 GB（含 s2_ext 两个进程各 4757 MiB + s4 794 MiB），空间充裕

### 早期 eval_return（无 value_mean 字段）

| seed | step=5000 | step=15000 |
|------|-----------|------------|
| s1 (bjb1-40020) | 36.7 | — |
| s2 (bjb1-40020) | 35.2 | — |
| s3 (bjb1-45299) | 36.1 | 122.9 |
| s4 (bjb1-45299) | 刚启动，待产出 | — |

metrics.jsonl 中未记录 `value_mean` / `critic/value_mean` 字段，所以 ve_ratio 无法计算。s1/s2 目前只有 5k 一个 eval 点，s3 已到 15k 且 eval 从 36→123 上升明显。

---
