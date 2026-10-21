# exp steering qwen L18 check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_steering-qwen-L18-check_20260523T103758_result.json`
- **Structured JSON:** [`c5d5d9087d788880bb04.json`](../../sessions/c5/c5d5d9087d788880bb04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen L18 (122)

**状态: 完成**（进程 568435 已退出，GPU 2 空闲）

**Probe accuracy: 73.8%**

| Alpha | Steering flips | Control flips | Fisher p |
|-------|---------------|---------------|----------|
| +5 | 3/84 (3.6%) | 1/84 (1.2%) | 0.6205 |
| +10 | 3/84 (3.6%) | 1/84 (1.2%) | 0.6205 |
| +20 | 3/84 (3.6%) | 2/84 (2.4%) | 1.0000 |

**注意：只跑了正方向 alpha，没有负方向（-5, -10, -20）。** 所有条件下 p→c 和 c→p 方向性 flip 均为 0。

**Bonferroni 显著: 无**（所有 p 值远大于 0.0083 阈值）

Steering 效果本质上与 control 无显著差异——L18 的 probe 方向在 Qwen3-8B 上无法有效引导行为翻转。

**JSON 路径:** `/root/clkc_mech_interp/data/qwen3/steering_results_L18_last.json`
**Log 路径:** `/root/clkc_mech_interp/logs/steering_qwen_L18.log`

---
