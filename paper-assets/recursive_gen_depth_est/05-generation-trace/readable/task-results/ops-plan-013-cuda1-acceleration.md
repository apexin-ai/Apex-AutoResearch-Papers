# ops plan 013 cuda1 acceleration

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan_013_cuda1_acceleration_20260515T225035_result.json`
- **Structured JSON:** [`d38927562da975358d8e.json`](../../sessions/d3/d38927562da975358d8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 进程确认运行正常，正在训练 `oracle_moderate/seed=42`（1/15），471 steps，速度 ~2.13 it/s。

**报告：**

| 项目 | 状态 |
|------|------|
| 已完成 | **11/40** runs（unfiltered 5/5, rf_strict 5/5, rf_moderate 1/5） |
| cuda:0（PID 364466） | 继续跑 rf_moderate 剩余 → rf_soft → oracle_strict（~13 runs） |
| cuda:1（PID 371534） | 已启动 oracle_moderate + random_strict + random_moderate（15 runs） |
| cuda:1 日志 | `/tmp/finetune_cuda1.log` |
| 拆分策略 | 脚本自带 skip-if-done，两卡不会冲突 |

**时间估算：**
- 每 run ~3-4 min（471 steps @2.1 it/s ≈ 3.7 min train + ~1 min eval）
- cuda:0 剩余 ~13 runs ≈ 52 min
- cuda:1 剩余 ~15 runs ≈ 60 min
- 并行后总完成时间 ≈ **60 min**（vs 串行 ~112 min）
- cuda:0 跑完后会触达 oracle_moderate 等条件，skip-if-done 自动跳过

---
