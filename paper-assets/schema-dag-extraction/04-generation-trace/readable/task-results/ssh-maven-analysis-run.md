# ssh maven analysis run

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_maven-analysis-run_20260515T071416_result.json`
- **Structured JSON:** [`1854b517f7a23c2f91e0.json`](../../sessions/18/1854b517f7a23c2f91e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三层分析完成。结果已保存到 `results/maven_analysis.json`。

---

## 三层分析结果

### Layer 1: Pairwise SCS-Confusion

| 指标 | 值 |
|------|------|
| n_pairs | 11,026 |
| Pearson r | -0.0079 (p=0.409) |
| Spearman ρ | 0.0038 (p=0.688) |
| **Nonzero-only** (n=632) | ρ = -0.042 (p=0.291) |

**Top-10 confused pairs:**

| Type A | Type B | SCS | Confusion |
|--------|--------|-----|-----------|
| Achieve | Getting | 0.750 | 73 |
| Departing | Escaping | 0.733 | 49 |
| Death | Killing | 0.704 | 34 |
| Attack | Use_firearm | 0.485 | 33 |
| Action | Removing | 0.906 | 29 |
| Arriving | Conquering | 0.662 | 27 |
| Communication | Expressing_publicly | 0.312 | 25 |
| Arriving | Process_start | 0.693 | 24 |
| Motion | Motion_directional | 0.530 | 24 |
| Expressing_publicly | Statement | 0.388 | 23 |

**结论**: Pairwise 层 SCS 与 confusion 无显著相关。MAVEN 类型间 BCS 压缩严重（均 ≥0.90），pairwise SCS 区分度不足。

---

### Layer 2: Per-type F1 vs Mean BCS

| 指标 | 值 |
|------|------|
| n_types | 149 (freq≥5) |
| Pearson r | 0.175 (p=0.032*) |
| Spearman ρ | 0.184 (p=0.025*) |
| Partial r (控制 log-freq) | 0.189 (p=0.021*) |

**Quartile comparison:**
- Low BCS quartile (≤0.671) mean F1: **0.136**
- High BCS quartile (≥0.747) mean F1: **0.234**
- Delta: **+0.098**

**Confound check:** BCS vs log-freq r = -0.043 (p=0.599) — BCS 与频率无显著相关，confound 排除。

**结论**: 显著正相关——schema 越相似（BCS 越高）的类型 F1 越好。效应量小但稳健，控制频率后依然显著。

---

### Layer 3: Batch-level Percentile Rank BCS

| Count | n | BCS range | r(F1, pctBCS) | p |
|-------|---|-----------|---------------|-------|
| 1 | 149 | 0.000 | N/A | N/A |
| 6 | 5 | 0.068 | -0.036 | 0.954 |
| 12 | 5 | 0.040 | 0.205 | 0.741 |
| 24 | 5 | 0.023 | 0.560 | 0.326 |
| 42 | 5 | 0.005 | -0.572 | 0.313 |
| 84 | 5 | 0.013 | **0.974** | **0.005** |
| 149 | 5 | 0.000 | N/A | N/A |

**结论**: 仅 count_84 达到显著 (r=0.974, p=0.005)。但每组仅 5 个批次，且 BCS range 极窄 (≤0.068)，BCS 压缩限制了 batch-level 分析的统计效力。

---

### 总结

Layer 2 (per-type) 提供了最有力的证据：schema 相似度与 extraction F1 显著正相关 (partial r=0.189, p=0.021)。Layer 1/3 因 Qwen3 BCS 压缩（168 个 MAVEN 类型间 pairwise sim 均 ≥0.90）而缺乏区分度。

---
