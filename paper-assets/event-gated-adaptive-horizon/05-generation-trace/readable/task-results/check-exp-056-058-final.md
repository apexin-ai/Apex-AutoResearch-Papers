# check exp 056 058 final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_056_058_final_20260523T234447_result.json`
- **Structured JSON:** [`362684845698cec0981a.json`](../../sessions/36/362684845698cec0981a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验数据全部拿到。注意 exp_056 仍在运行但已超过目标步数，exp_058 还差 ~5K 步。

---

## exp_056 PegInsertion frozen s1（bjb1-40020）

| 项目 | 值 |
|------|-----|
| **进程状态** | 运行中（PID 346430，已运行 14h44m） |
| **目标步数** | 210,000 |
| **当前 total_steps** | 218,800（已超过目标，可能在做最终 eval/checkpoint） |
| **metrics.jsonl 行数** | 1,160 |
| **最后 checkpoint** | `checkpoint_202500.pt` |

### ve_ratio 轨迹（key: `civo/ve_ratio`）

| Step | ve_ratio |
|------|----------|
| 12,500 | 0.316 |
| 22,500 | 0.975 |
| 32,500 | 1.839 |
| 42,500 | 1.966 |
| 52,500 | **5.422** |
| 62,500 | 4.047 |
| 72,500 | **8.408** |
| 82,500 | **11.321** ← peak |
| 92,500 | 3.724 |
| 102,500 | 3.034 |
| 112,500 | 2.204 |
| 122,500 | 2.425 |
| 132,500 | 0.842 |
| 142,500 | 2.194 |
| 152,500 | 2.203 |
| 162,500 | 0.651 |
| 172,500 | 1.085 |
| 182,500 | 1.070 |
| 192,500 | 0.467 |
| 202,500 | 0.708 |
| 212,500 | 1.193 |

- **ve_ratio_peak**: 11.321 @ step 82,500
- **ve_ratio_final**: 1.193 @ step 212,500
- **NVE 分类**: **burst**（peak 11.321 > 5，52.5K-82.5K 区间出现连续 burst）

### eval_return 轨迹（key: `eval_return`）

| Step | eval_return |
|------|------------|
| 2,500 | 2.01 |
| 12,500 | 5.75 |
| 22,500 | 9.30 |
| 32,500 | 9.23 |
| 42,500 | 12.30 |
| 52,500 | 5.90 |
| 62,500 | 9.98 |
| 72,500 | 5.41 |
| 82,500 | 3.57 |
| 92,500 | 8.68 |
| 102,500 | 9.60 |
| 112,500 | 12.33 |
| 122,500 | 10.13 |
| 132,500 | **24.42** ← peak |
| 142,500 | 7.73 |
| 152,500 | 6.20 |
| 162,500 | 16.93 |
| 172,500 | 8.75 |
| 182,500 | 7.54 |
| 192,500 | 15.36 |
| 202,500 | 8.70 |
| 212,500 | 4.37 |

- **eval_return_peak**: 24.42 @ step 132,500
- **eval_return_final**: 4.37 @ step 212,500

---

## exp_058 Cheetah frozen s1（bjb1-45299）

| 项目 | 值 |
|------|-----|
| **进程状态** | 运行中（PID 164830，已运行 5h36m） |
| **目标步数** | 210,000 |
| **当前 total_steps** | 205,000（还差 ~5K 步未完成） |
| **metrics.jsonl 行数** | 267 |
| **最后 checkpoint** | `checkpoint_175000.pt` |

### ve_ratio 轨迹（key: `civo/ve_ratio`）

| Step | ve_ratio |
|------|----------|
| 15,000 | 0.011 |
| 25,000 | 0.030 |
| 35,000 | 0.054 |
| 45,000 | **0.231** ← peak |
| 55,000 | 0.081 |
| 65,000 | 0.127 |
| 75,000 | 0.139 |
| 85,000 | 0.188 |
| 95,000 | 0.223 |
| 105,000 | 0.166 |
| 115,000 | 0.138 |
| 125,000 | 0.102 |
| 135,000 | 0.129 |
| 145,000 | 0.103 |
| 155,000 | 0.103 |
| 165,000 | 0.127 |
| 175,000 | 0.113 |
| 185,000 | 0.142 |
| 195,000 | 0.111 |
| 205,000 | 0.112 |

- **ve_ratio_peak**: 0.231 @ step 45,000
- **ve_ratio_final**: 0.112 @ step 205,000
- **NVE 分类**: **clean**（全程 < 1.5，峰值仅 0.231）

### eval_return 轨迹（key: `eval_return`）

| Step | eval_return |
|------|------------|
| 5,000 | 13.48 |
| 15,000 | 99.83 |
| 25,000 | **191.74** ← peak |
| 35,000 | 190.57 |
| 45,000 | 49.75 |
| 55,000 | 145.32 |
| 65,000 | 91.48 |
| 75,000 | 82.39 |
| 85,000 | 58.47 |
| 95,000 | 49.76 |
| 105,000 | 63.53 |
| 115,000 | 71.63 |
| 125,000 | 92.57 |
| 135,000 | 73.98 |
| 145,000 | 92.37 |
| 155,000 | 91.37 |
| 165,000 | 74.84 |
| 175,000 | 83.41 |
| 185,000 | 66.26 |
| 195,000 | 82.54 |
| 205,000 | 80.46 |

- **eval_return_peak**: 191.74 @ step 25,000
- **eval_return_final**: 80.46 @ step 205,000

---

## 注意事项

1. **exp_056 尚未完全结束**：进程仍在运行，已过 210K 目标步数（当前 218.8K），最后 checkpoint 停在 202,500。可能正在做最终 eval 或写最后一个 checkpoint。建议等进程退出后再做一次确认，锁定最终 checkpoint。
2. **exp_058 还差 ~5K 步**：当前 205K/210K，预计约 1-2 小时内完成。最终数据需等完成后再确认。
3. **metrics key 名称**：两个实验的 ve_ratio 都记录在 `civo/ve_ratio`（不是 `agent/ve_ratio`），eval 记录在 `eval_return`（不是 `eval/return`）。

---
