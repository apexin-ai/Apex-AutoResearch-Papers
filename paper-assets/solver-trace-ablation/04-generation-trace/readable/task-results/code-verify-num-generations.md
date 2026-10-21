# code verify num generations

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-num-generations_20260516T030412_result.json`
- **Structured JSON:** [`3b9a7c06280135679709.json`](../../sessions/3b/3b9a7c06280135679709.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 实际步数
- **sweep-isr-b01-s45**: 100 步（完成）
- **sweep-isr-b005-s42**: 100 步（完成）

### 实际 K 值：**K=4**（两个实验均是）

判据：所有 prove_rate 值都是 1/8 的整数倍，从未出现 1/16 的值（如 0.0625、0.1875、0.3125）。

batch_size=2 时，prove_rate 粒度 = 1/(2K)：
- K=4 → 粒度 1/8 = 0.125 ✓（与观测吻合）
- K=8 → 粒度 1/16 = 0.0625 ✗（从未观测到）

### prove_rate 分布

**sweep-isr-b01-s45** (β=0.1) — 出现的非零值：

| prove_rate | 对应 | 示例步 |
|---|---|---|
| 0.125 = 1/8 | 1/8 proved | 73, 80, 86, 87, 89 |
| 0.25 = 2/8 | 2/8 proved | 75 |
| 0.375 = 3/8 | 3/8 proved | 76 |
| 0.5 = 4/8 | 4/8 proved | 20, 71, 72, 79, 82, 85, 94, 95 |
| 0.875 = 7/8 | 7/8 proved | 96 |

大量步数 prove_rate=0（前 19 步全是 0），整体训练信号很弱。

**sweep-isr-b005-s42** (β=0.05) — 出现的非零值：

| prove_rate | 对应 | 示例步 |
|---|---|---|
| 0.125 = 1/8 | | 1, 9, 12, 75, 80, 83, 87, 89, 92 |
| 0.25 = 2/8 | | 71, 85, 96 |
| 0.375 = 3/8 | | 3, 79, 81, 95 |
| 0.5 = 4/8 | | 5, 19, 86, 90, 93, 98, 100 |
| 0.625 = 5/8 | | 11, 73, 76, 82, 94 |
| 0.75 = 6/8 | | 20 |

b005-s42 的 prove_rate 分布更丰富，训练信号明显好于 b01-s45。

**结论：K=8 配置未生效，被 argparse 默认值 K=4 覆盖。** 两个实验实际都以 K=4 运行。

---
