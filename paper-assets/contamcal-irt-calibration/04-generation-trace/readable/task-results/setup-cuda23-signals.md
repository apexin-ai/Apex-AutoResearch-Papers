# setup cuda23 signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_cuda23_signals_20260515T225943_result.json`
- **Structured JSON:** [`9a28659679271ba56482.json`](../../sessions/9a/9a28659679271ba56482.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:2 上 v7 已正常启动（PID 652247，585 MiB），正在算 d005_s123/mmlu 的 s1_embedding 信号。

---

## 汇报

### 发现

**GPU 实际状态（与预期不符）：**
- cuda:2: 空闲 → 已提交 v7
- cuda:3: **不空闲** — PID 630891 在跑 d000_v2_s42 signals (v6 脚本, mmlu/s4)，占用 7.6GB

**3B Checkpoint 完整列表（含 alpha/lr）：**

| Checkpoint | alpha | lr | seed | 状态 |
|---|---|---|---|---|
| d000_s123 | 32 | 2e-4 | 123 | 完整 |
| d000_v2_s42 | 16 | 5e-5 | 42 | 完整 (alpha 不符) |
| d000_v2_s123 | 16 | 5e-5 | 123 | 完整 (alpha 不符) |
| d000_a32_s42 | - | - | 42 | 训练中 cuda:5 |
| d005_s123 | 32 | 2e-4 | 123 | 完整 |
| d005_s42 | 32 | 2e-4 | 42 | 完整 (旧 lr) |
| d005_a32_s42 | - | - | 42 | 训练中 cuda:0 |
| d025_s123 | - | - | 123 | 完整 |
| d025_a32_s42 | - | - | 42 | 无 train_config |
| d100_a32_s123 | 32 | 5e-5 | 123 | **完整 ✓ 唯一新 spec** |
| d100_a32_s42 | - | - | 42 | 训练中 cuda:1 |

**Signals 完成情况（3B only）：**
- 0.5B/1.5B: 全部完成 (4 dosage × 3 bench = 12/12)
- 3B d005_s42: 部分 (merged 仅 arc_challenge)
- 3B d025_s42: 部分 (merged 仅 mmlu，v5 在补)
- 3B d100_s42: 部分 (v5 在算)
- 3B d000_v2_s42: cuda:3 在算
- 3B d005_s123 / d000_s123 / d100_a32_s123: **无 signals**

### 提交的任务

| exp_id | GPU | 内容 | PID |
|---|---|---|---|
| exp_002_signals_3B_v7 | cuda:2 | d005_s123 signals (3 bench × all signals) | 652247 |

### cuda:3 无法提交

PID 630891 在 cuda:3 上跑 v6 (d000_v2_s42 signals)。v6 脚本遍历 3 benchmarks × 3 signals = 9 tasks，当前在 mmlu/s4，估计还需数小时。

### 建议

1. **cuda:3 空出后**：优先跑 d000_s123 signals（或等 d000_a32_s42 训练完跑新 spec 版本）
2. **注意 lr 风险**：d005_s123 和 d000_s123 均为 lr=2e-4（与旧 s42 相同），如果 D076 的 lr 约束同样适用于 s123，这些 signals 结果可能需要重算
3. **d100_a32_s123 是唯一完整的新 spec checkpoint**（alpha=32, lr=5e-5），但无 signals，v5 目前在算旧 d100_s42 而非 d100_a32_s123

---
