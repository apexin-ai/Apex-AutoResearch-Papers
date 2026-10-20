# ops check sim sweep v5 progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-sim-sweep-v5-progress_20260515T070803_result.json`
- **Structured JSON:** [`ccb4b586f7d94a2c4c15.json`](../../sessions/cc/ccb4b586f7d94a2c4c15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Exp-004 Simulation Sweep 进度报告**

**状态**: v6 正在运行中（14:36 启动，`--parallel 2 --chains-parallel 2 --resume`）

**总量**: 12 条件 × 10 seeds = 120 runs（subset mode）

**已完成 9/12 条件**（结果文件已存在）:
| 条件 | 状态 |
|------|------|
| auc0.55 × n20/n50/n100 | 之前完成 |
| auc0.65 × n20/n50 | 之前完成 |
| auc0.8 × n20/n50 | 之前完成（v6 跳过）|
| auc0.8_n100 | v6 补完 4 seeds |
| auc0.9_n20 | v6 完成全部 10 seeds |

**当前运行 2 条件**（parallel=2）:
- auc0.9_n50：10 seeds，15:01 开始
- 另一条件（可能 auc0.65_n100 或 auc0.9_n100）同时在跑

**剩余 3 条件**: auc0.65_n100, auc0.9_n50, auc0.9_n100

**时间估算**:
- n=20 seeds: ~2.5 min/seed
- n=50 seeds: ~5-15 min/seed
- n=100 seeds: ~15-20 min/seed（auc0.8_n100 有 seed 耗时 1141s）
- 剩余 3 条件中 2 个是 n=100，预计还需 **3-5 小时**完成

进程健康，4 个 zombie 进程是之前 v5 的残留，不影响当前 v6 运行。无需干预。

---
