# diagnose exp 010b s0 exit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_010b_s0_exit_20260518T050747_result.json`
- **Structured JSON:** [`23cc1899d4c4c0f0e8ce.json`](../../sessions/23/23cc1899d4c4c0f0e8ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成，cron 已删除。

---

## 实验报告: exp_010b_cheetah_civo_trigger_s0

**状态**: SUCCESS | **结论**: CIVO 复现成功，seed=0 比 seed=1 更严重

### Eval Return 轨迹

| Step | eval_return |
|------|-------------|
| 5K   | 8.26 |
| 15K  | 44.72 |
| 25K  | 107.17 |
| **35K** | **247.77** (峰值) |
| 45K  | 205.85 |
| 55K  | 135.43 |
| 65K  | 5.04 |
| 75K  | 63.42 |
| 85K  | 36.14 |
| 95K  | 10.35 |
| **105K** | **0.83** (崩溃) |

### CIVO 指标

| Step | NVE (ve_ratio) | alert |
|------|----------------|-------|
| 75K  | 1.28 | 0 |
| 85K  | 2.04 | 0 |
| **95K** | **6.34** | **1** (首次触发) |
| **105K** | **70.64** | **1** |

### 与 seed=1 对比

| 指标 | seed=1 | seed=0 |
|------|--------|--------|
| 最终 NVE | 8.27× | **70.64×** |
| 峰值 eval_return | ~250 | 247.77 |
| 最终 eval_return | ~2 | 0.83 |

### 关键观察
- **Gate 完全锁死**: dt=2 占 100%，entropy=0，全程无自适应行为
- **CIVO 严重程度**: seed=0 的 NVE=70.64× 远超 seed=1 的 8.27×，value_mean=58.58 而实际 return=0.83
- **崩溃更早**: eval_return 在 65K 就出现首次剧烈下降（5.04），之后短暂回升再持续崩溃
- **两个 seed 均确认**: Cheetah CIVO 在 dt_emb+subsample+H=8 配置下可稳定复现

---
