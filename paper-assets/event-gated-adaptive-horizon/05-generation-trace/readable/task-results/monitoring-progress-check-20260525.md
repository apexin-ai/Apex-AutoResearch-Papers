# monitoring progress check 20260525

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_progress_check_20260525_20260525T143419_result.json`
- **Structured JSON:** [`7c24cd1e6d0846ff6150.json`](../../sessions/7c/7c24cd1e6d0846ff6150.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常运行，进度报告已保存到 `artifacts/progress_check_20260525.md`。

**bjb1-45299 (Walker Walk):**
- **exp_080 s1**: 84K/105K (80%), eval 846.5, ~46 min 完成
- **exp_081 s2**: 80K/105K (76%), eval 404.5, ~45 min 完成
- 两者 gate 均锁定 dt=1。exp_081 收敛显著慢于 exp_080（不同 seed 差异大）

**westd-19154 (Cheetah Run):**
- **exp_082 no_dt_emb s0**: 25K/105K (24%), eval 108.4, ~77 min 完成
- **exp_083 baseline s1**: 8K/105K (8%), eval 11.6, ~95 min 完成
- exp_082 gate 锁定 dt=2；exp_083 是 baseline 无 gate

GPU 利用率：bjb1 GPU1 98% 接近满载，westd 两块 GPU 利用率偏低 (28%/54%)。

---
