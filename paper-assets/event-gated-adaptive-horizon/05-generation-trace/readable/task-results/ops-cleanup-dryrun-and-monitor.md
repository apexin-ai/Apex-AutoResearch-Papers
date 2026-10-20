# ops cleanup dryrun and monitor

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_dryrun_and_monitor_20260515T164205_result.json`
- **Structured JSON:** [`4d4f2c0c2f7a33de8777.json`](../../sessions/4d/4d4f2c0c2f7a33de8777.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Cheetah Dryrun (PID 389546)
已清理。进程已终止确认。

### 009d Baseline Walker s0

**进程状态**：PID 149708 存活，运行 4h17m，669% CPU（正常多核利用）。

**当前 step**：~80K（最新 train log 在 step 80000）

**Eval 轨迹**：

| Step | eval_return |
|------|-------------|
| 5K   | 35 |
| 8K   | 37 |
| 18K  | 126 |
| 28K  | 184 |
| 38K  | 264 |
| 48K  | 293 |
| 58K  | 326 |
| 68K  | **402** |
| 78K  | **81** |

**78K 之后无新 eval 点**（eval 每 10K steps，下一次 eval 在 88K）。

**Train return @ 80K**：253, 158, 186, 221 — 均值 ~204，相比 76K 的 ~344 均值大幅下降。

**崩溃判断：大概率 persistent collapse，不是 transient dip。** 理由：
1. Eval 从 402 → 81，跌幅 80%，不是正常波动
2. Train return 在 80K 同步暴跌（344 → 204），说明策略本身崩了，不仅是 eval 方差
3. Value 网络的 EMA 仍在 214-226 高位，和实际 return 严重脱节 — 典型的 value overestimation 导致策略崩溃信号

建议等 88K eval 确认，但大概率需要从 68K checkpoint 回滚或放弃此 run。

---
