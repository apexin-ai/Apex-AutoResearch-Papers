# analysis exp 035 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-035-results_20260518T190358_result.json`
- **Structured JSON:** [`abf08ebf1801b5869d24.json`](../../sessions/ab/abf08ebf1801b5869d24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整分析报告。

---

## exp-035 分析报告：Qwen2.5-7B-Instruct FOLIO-204 SICA vs SC

### 实验状态
- **EXIT_CODE=0**，正常完成
- 0 ERROR / 0 Traceback
- 203/204 题有结果（1 题缺失），JSON summary 是 stale 的（n=195 时计算），以下所有数字从 results 数组 203 条逐题计算

### 核心指标

| 指标 | 值 |
|---|---|
| **SC accuracy** | **77.34%** (157/203) |
| **SICA accuracy** | **76.85%** (156/203) |
| **Delta (SICA - SC)** | **-0.49pp** (-1 problem) |
| McNemar p-value | **1.000** (完全不显著) |
| Discordant pairs | b=1 (SICA-only), c=2 (SC-only) |
| C0 (non-unanimous rate) | **0.5517** (112/203) |
| Extraction rate | 98.19% |
| Contradiction rate | 1.58% (60/203 problems) |
| Constraints | 12,950 total / 6,515 unique (dedup 50.3%) |
| Wall time | 78.2 min (avg 23.1s/problem) |

### Baseline 对比

| 实验 | 模型 | SC | SICA | Delta | C0 |
|---|---|---|---|---|---|
| exp-001/026 | Qwen2.5-14B | 75.49% | 74.51% | -0.98pp | — |
| exp-004 | Qwen2.5-7B (D012 pilot) | — | — | 0 | — |
| **exp-035** | **Qwen2.5-7B** | **77.34%** | **76.85%** | **-0.49pp** | **0.55** |

### 结论：**Negative**（假设验证通过）

1. **SICA 无法 outperform SC on 7B**：delta=-0.49pp，p=1.0，仅 3 个 discordant pairs。SICA 和 SC 在 203 题中有 200 题给出相同正误结果，差异极小。

2. **C0 确实更高**（0.55 vs 14B 通常更低），说明 7B 模型的 trace 多样性更大，但这没有转化为 SICA 优势——符合假设中"constraint quality 更差"的预期。

3. **意外发现**：7B SC (77.34%) 高于 14B SC (75.49%)。这可能因为：(a) 203 vs 204 题的微小差异；(b) FOLIO 数据集特性使 7B 不劣于 14B（可能 14B 在某些题上过度推理）。

4. **Capability trap 进一步确认**：无论 7B 还是 14B，SICA 在 FOLIO 上都无法超过 SC，constraint extraction 的质量不足以提供额外信号。

---
