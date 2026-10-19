# ops argmin k5 harvest bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_argmin-k5-harvest-bjb1_20260519T132505_result.json`
- **Structured JSON:** [`c2030886e97f422b5c1f.json`](../../sessions/c2/c2030886e97f422b5c1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部完成，registry 已更新。以下是汇总分析：

---

## 实验状态

| exp_id | seed | SR | 状态 |
|--------|------|----|------|
| eval-argmin-object-k5-seed42 | 42 | **15%** | DONE |
| eval-argmin-object-k5-seed43 | 43 | **13%** | DONE |
| eval-argmin-object-k5-seed45 | 45 | **13%** | DONE |

## K=5 Decomposition 分析

### K=5 argmin 统计
- **Mean SR = 13.7% ± 1.2%** (seeds: 15, 13, 13)

### Decomposition（VLA-only ≈ 11.6%）

| 分量 | K=5 | K=10 |
|------|-----|------|
| **Selection effect** (argmin − VLA-only) | **+2.1pp** (13.7% − 11.6%) | **≈ 0pp** (12.0% − 11.6%) |
| **Correction effect** (CRM − argmin) | **+2.3pp** (16.0% − 13.7%) | **+5.2pp** (17.2% − 12.0%) |
| **Total CRM gain** (CRM − VLA-only) | **+4.4pp** | **+5.6pp** |

### 关键发现

**K=5 与 K=10 的 decomposition 呈现截然不同的模式：**

1. **K=5 selection effect 显著（+2.1pp）**，而 K=10 几乎为零。这说明从 5 个候选中选最好的 vs 从 10 个中选最好的，效果差异大——K=5 候选池小，argmin 选择能有效避开最差轨迹，带来真实增益。

2. **K=5 correction effect 减半（+2.3pp vs +5.2pp）**。CRM 在 K=5 时可发挥的矫正空间更小，因为候选池本身就小，最优轨迹的质量上限受限。

3. **总增益 K=5（+4.4pp）< K=10（+5.6pp）**，但差距不大。K=5 用一半的候选数实现了约 79% 的 K=10 增益，且增益来源更均衡（selection 和 correction 各贡献约一半）。

---
