# code plan 001 dif analysis

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_001_dif_analysis_20260520T205627_result.json`
- **Structured JSON:** [`f1bcc8c5cd60d4b5d52e.json`](../../sessions/f1/f1bcc8c5cd60d4b5d52e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 9 个产出文件已注册。以下是核心结果摘要：

## 结果总览

| 指标 | Temporal (2023→2024) | Ability (Q1-2 vs Q4-5) |
|------|---------------------|------------------------|
| ETS C | **3918 (31.3%)** | **363 (2.9%)** |
| FPR vs Li clean | 0.3184 | 0.0269 |
| Enrichment | **0.96** | **1.19** |

**Sanity check 通过**: 随机分半 0.18% C（远低于 5% 阈值）

## 关键发现

1. **Temporal cohort DIF 不是在检测污染**：31.3% C 率 + enrichment ≈ 1.0（clean 和 contaminated items 被标记的概率相同）。MH-DIF 在 temporal cohort 上捕获的是 2023→2024 模型的系统性能力提升，而非污染信号。

2. **Ability cohort 更合理**：2.9% C，enrichment = 1.19（contaminated items 被标记概率高 19%），FPR = 2.7%。

3. **Within-family 证实了混淆**：Llama-2 vs Llama-3 高达 61.3% C — 代际能力差异远超 temporal cohort 的 DIF 幅度。没有同一 family 内的 temporal split 可用（所有 family 只落在单个时间段内）。

4. **Domain 分析**：ρ(C_rate, Δacc) = 0.307, p = 0.02 — 准确率提升越大的 subject DIF 越高，与 "能力驱动而非污染驱动" 一致。

5. **Neg-disc 敏感性**：移除 negative-disc items 后 C 率略升（32.4% vs 31.3%），neg-disc items 本身反而 C 率较低（25.7%）。

---
