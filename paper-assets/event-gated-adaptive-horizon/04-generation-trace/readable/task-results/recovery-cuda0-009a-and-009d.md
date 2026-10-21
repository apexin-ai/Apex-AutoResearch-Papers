# recovery cuda0 009a and 009d

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recovery_cuda0-009a-and-009d_20260515T061706_result.json`
- **Structured JSON:** [`7b048fd73b947f873113.json`](../../sessions/7b/7b048fd73b947f873113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 产出

### 1. exp_009a_baseline_walker_s2 — DONE ✓

| 指标 | 009a (seed 2) | exp_001 (seed 0/1) | 差异 |
|---|---|---|---|
| Final eval (505K) | 957.87 | 970.41 | -1.3% |
| Peak eval | 966.94@395K | 970.41@505K | -0.4% |
| Last 10 mean | 947.19 | 950.90 | -0.4% |
| v/e stable | 0.69-0.72 | 0.69-0.72 | 匹配 |
| 105K eval | 836.51 | 915.67 | -8.6%* |

*105K 处偏低但 215K+ 完全收敛。跨 seed baseline 一致性确认。

### 2. Registry 已更新
- 009a: status=DONE, conclusion=success, 完整 51 eval trajectory + value/v/e trajectory

### 3. exp_009d_baseline_walker_s1 — 已提交 ✓
- tmux session `exp_009d_baseline_walker_s1` 已创建
- 内置等待逻辑：等 009a (pid 142508) 退出后自动启动
- 配置：seed=1, 500K steps, cuda:0, 与 exp_001 一致
- Registry: status=RUNNING

---
