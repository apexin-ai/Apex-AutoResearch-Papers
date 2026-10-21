# audit s47 duplicate data

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_s47-duplicate-data_20260524T232536_result.json`
- **Structured JSON:** [`01d4690b3a7025f5e946.json`](../../sessions/01/01d4690b3a7025f5e946.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，下面是完整的审计报告。

---

## Part 1: s47 条目清单

### VLA-only s47（2个条目）

| 字段 | 条目 A (旧) | 条目 B (新) |
|------|------------|------------|
| exp_id | `eval-supp-vla-only-spatial-s47` | `eval-supp-spatial-vla-only-s47` |
| created_at | 2026-05-24T07:15:40 | 2026-05-24T10:58:43 |
| updated_at | 2026-05-24T12:04:19 | 2026-05-24T13:41:05 |
| status | DONE/success | DONE/success |
| server | cqa1-32758 | cqa1-32758 |
| gpu | cuda:0 | cuda:0 |
| **K** | **1** | **2** |
| **SR** | **80.0%** | **81.0%** |
| command | `--mode vla_only --seed 47 --n_rollouts 20 --K 1` | `--mode vla_only --seed 47 --n_rollouts 20 --K 2` |

### Adaptive s47（2个条目）

| 字段 | 条目 A (旧) | 条目 B (新) |
|------|------------|------------|
| exp_id | `eval-supp-adapt-tau025-spatial-s47` | `eval-supp-spatial-adapt-tau025-s47` |
| created_at | 2026-05-24T07:15:43 | 2026-05-24T10:58:50 |
| updated_at | 2026-05-24T13:40:40 | 2026-05-24T13:40:50 |
| status | DONE/success | DONE/negative |
| server | cqa1-32758 | cqa1-32758 |
| gpu | cuda:1 | cuda:2 |
| **K** | **10** | **2** |
| **max_correction_norm** | **0.2** | *(未设，用 adaptive_threshold=0.2)* |
| **conformal_threshold** | **0.25** | **0.25** |
| **CRM checkpoint** | **crm_smolvla_3suite_v1** | **crm_unified_4suite_r4** |
| **SR** | **81.5%** | **79.0%** |
| trigger_rate | 20.46% | 18.8% |

---

## Part 2: s47 差异分析

### VLA-only s47 差异
- **唯一参数差异：K=1 vs K=2**（action chunk 长度）
- SR 差异：80.0% vs 81.0%（+1.0pp）
- 同服务器、同 GPU，时间差 ~3.7h
- **结论**：两次是不同配置的实验（K 不同），不是简单重复

### Adaptive s47 差异
- **K=10 vs K=2**
- **CRM checkpoint 不同**：crm_smolvla_3suite_v1 vs crm_unified_4suite_r4
- **参数名不同**：旧版用 `--max_correction_norm 0.2`，新版用 `--adaptive_threshold 0.2`
- SR 差异：81.5% vs 79.0%（-2.5pp）
- **结论**：完全不同的配置（K、checkpoint、参数名），不是重复实验

---

## Part 3: p-value 版本对比

### 关键发现：p-value 差异的根源不是 s47，而是 s45

逐 seed 对比两个版本的 Spatial 数据：

| Seed | p=0.0049版 VLA | p=0.0168版 VLA | VLA差异 | p=0.0049版 Adapt | p=0.0168版 Adapt | Adapt差异 | Δ(A-V) 0.0049版 | Δ(A-V) 0.0168版 |
|------|---------------|---------------|---------|-----------------|-----------------|-----------|-----------------|-----------------|
| s42 | 80.0% | 80.0% | 同 | 82.0% | 82.0% | 同 | +2.0pp | +2.0pp |
| s43 | 79.0% | 79.0% | 同 | 80.0% | 80.0% | 同 | +1.0pp | +1.0pp |
| s44 | 78.5% | 78.5% | 同 | 80.5% | 80.5% | 同 | +2.0pp | +2.0pp |
| **s45** | **77.0%** | **80.0%** | **+3.0pp** | 80.0% | 80.0% | 同 | **+3.0pp** | **+0.0pp** |
| s46 | 80.5% | 80.5% | 同 | 80.0% | 80.0% | 同 | -0.5pp | -0.5pp |
| s47 | 80.0% | 80.0% | 同 | 81.5% | 81.5% | 同 | +1.5pp | +1.5pp |
| s48 | 79.5% | 79.5% | 同 | 81.0% | 81.0% | 同 | +1.5pp | +1.5pp |
| s49 | 78.5% | 78.5% | 同 | 82.0% | 82.0% | 同 | +3.5pp | +3.5pp |

**唯一差异点：s45 VLA-only**

### s45 VLA-only 溯源

s45 VLA-only 在 registry 中也有两个条目：

| 字段 | 旧 (p=0.0049版用) | 新 (p=0.0168版用) |
|------|-------------------|-------------------|
| exp_id | `eval-supp-spatial-vla-only-s45` | `eval-supp-vla-only-spatial-s45` |
| created_at | 2026-05-23T21:31:09 | 2026-05-24T06:48:46 |
| **server** | **cqa1-32758** | **bjb2-28827** |
| K | 1 | 1 |
| **SR** | **77.0%** | **80.0%** |

参数完全相同（都是 K=1），但**不同服务器**上跑出不同结果（77% vs 80%，差 3pp）。

### p-value 变化机制

- p=0.0049 版本：用 cqa1 的 s45（SR=77%），Δ(A-V)=+3.0pp → 8 seed 均值 Δ=+1.75pp
- p=0.0168 版本：用 bjb2 的 s45（SR=80%），Δ(A-V)=+0.0pp → 8 seed 均值 Δ=+1.375pp
- 单个 seed 的 VLA-only SR 变化 3pp，直接把 paired t-test 从 p=0.0049 拉到 p=0.0168

### 根因总结

1. **s47 有重复条目但未影响 p-value**——两个版本的表格都使用了相同的 s47 数据（VLA=80.0%, Adaptive=81.5%）
2. **p-value 差异完全由 s45 VLA-only 驱动**——同一配置（K=1）在不同服务器（cqa1 vs bjb2）上跑出 77% vs 80%
3. **3pp 的跨服务器方差**说明 LIBERO 模拟器结果受硬件环境影响显著，同一 seed + 同一参数在不同机器上可产生实质性差异

---
