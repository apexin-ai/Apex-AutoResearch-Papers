# ops random soft control

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_random_soft_control_20260515T235714_result.json`
- **Structured JSON:** [`081140f824e9b3930e67.json`](../../sessions/08/081140f824e9b3930e67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 已更新为 DONE。结果汇总：

| | mean PPL | std |
|---|---|---|
| **random_soft** (随机 4422) | 16.0615 | ± 0.0794 |
| **rf_soft** (深度筛选 4422) | 15.7334 | ± 0.0420 |

- **Δ PPL = 0.3281**（rf_soft 更低 = 更好）
- **Paired t-test**: t = 17.98, **p = 5.6 × 10⁻⁵**
- **Cohen's d = 8.04**（极大效应量）
- **显著：是 (p < 0.001)**

5 个 seed 全部一致：rf_soft 优于 random_soft（逐 seed Δ 范围 0.277–0.381），排除了"rf_soft 优势仅因样本量减少"的混淆解释，确认深度感知筛选是性能提升的原因。

---
