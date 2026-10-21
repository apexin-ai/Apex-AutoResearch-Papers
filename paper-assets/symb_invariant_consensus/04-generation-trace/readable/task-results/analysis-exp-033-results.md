# analysis exp 033 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-033-results_20260518T191648_result.json`
- **Structured JSON:** [`4834386aa7dc0a673ba3.json`](../../sessions/48/4834386aa7dc0a673ba3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

---

## exp-033 分析报告：Mistral-7B-Instruct-v0.3 FOLIO-204

### 核心结果

| 指标 | 值 |
|------|-----|
| **SICA accuracy** | **59.31%** (121/204) |
| **SC accuracy** | **54.41%** (111/204) |
| **delta (SICA - SC)** | **+4.90pp** |
| **McNemar p-value** | **0.013** (显著, α=0.05) |
| n | 204 |
| k | 12 |

### 诊断指标

| 指标 | 值 |
|------|-----|
| extraction_rate | 97.14% |
| contradiction_rate | 3.50% (128/204 problems) |
| avg_unique_constraints | 39.3 |
| maxsat_mean_sat_ratio | 0.9609 |
| C0 (non-unanimous rate) | **81.37%** |
| avg_majority_frac | 0.7515 |
| Discordant: SICA-only wins | **12** |
| Discordant: SC-only wins | **2** |
| wall_time | 81.4 min |

### Baseline 对比

| 实验 | 模型 | 数据集 | SICA | SC | Delta | C0 |
|------|------|--------|------|-----|-------|-----|
| exp-026 | Qwen2.5-14B | FOLIO-204 | 74.51% | 75.00% | -0.49pp | ~45% |
| exp-035 | Qwen2.5-7B | FOLIO-204 | 76.85% | 77.34% | -0.49pp | 55.17% |
| exp-010-v3 | Mistral-7B | D012 (n=60) | 48.33% | 48.33% | 0pp | — |
| **exp-033** | **Mistral-7B** | **FOLIO-204** | **59.31%** | **54.41%** | **+4.90pp** | **81.37%** |

### 关键发现

1. **首次 SICA 显著超越 SC** — delta=+4.90pp, McNemar p=0.013, discordant pairs 高度不对称 (12:2)。

2. **Capability trap 非普遍现象** — Qwen 家族 (7B/14B) 上 delta≈-0.49pp (capability trap 成立)，但 Mistral-7B 上 SICA 反而大幅胜出。关键区别在于 **diversity**：
   - Mistral-7B C0=81.37%，Qwen-7B C0=55.17%
   - 高 diversity 导致 SC majority vote 退化（avg majority fraction 仅 75.15%）
   - SICA 的 MaxSAT 在 noisy 但 diverse 的 traces 中仍能提取有用信号

3. **绝对性能低** — Mistral-7B 59.31% 远低于 Qwen-7B 77%，说明基础推理能力弱，但 SICA 在这种条件下反而比 SC 更能容忍 noise。

4. **D012 pilot 有误导性** — n=60 的小样本掩盖了 +4.90pp 的效应。

5. **理论解释** — SICA 的优势区间是 "高 diversity + 中等 quality"：traces 足够多样使 SC 失效，但 constraint extraction 质量仍足以让 MaxSAT 找到一致解。Qwen 模型 diversity 不够高（SC 的 majority vote 仍然 robust），所以 SICA 无法胜出。

---
