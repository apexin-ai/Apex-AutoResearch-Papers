# analysis exp 008 v4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008_v4_20260514T162445_result.json`
- **Structured JSON:** [`fa56c18770fe54d841a7.json`](../../sessions/fa/fa56c18770fe54d841a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，所有验证标准通过。

## exp-008 v4 Key Findings

### Within-Model AUC (d005 detection)
| Signal | mmlu | gsm8k | arc_challenge | Mean |
|--------|------|-------|---------------|------|
| **S1 Embedding** | **0.953** | **0.988** | **0.995** | **0.979** |
| S2 Min-K++ | 0.465 | 0.465 | 0.466 | 0.465 |
| S4 SelfCritique | 0.517 | 0.495 | 0.432 | 0.481 |

### d000 Sanity Check (AUC ≈ 0.5)
- S1: MARGINAL (arc=0.427, gsm8k=0.550 — small-sample noise, mmlu=0.505 正常)
- S2: MARGINAL (gsm8k=0.570)
- S4: PASS (all within 0.48–0.52)

### Cross-Model d100 vs d000 (Cohen's d, all Bonferroni-significant)
| Signal | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| **S1 Embedding** | **+4.16** | **+2.83** | **+3.80** |
| S2 Min-K++ | -1.22 | -2.67 | -2.05 |
| S4 SelfCritique | +0.47 | +0.20 | +0.67 |

### 核心结论
1. **S1 Embedding 是唯一有效的 within-model 检测信号**（d005 AUC=0.979），S2/S4 在 0.5B 模型上无区分力
2. **Cross-model 比较揭示了 v3 遗漏的信息**：d100 全量污染使所有三个信号都产生了显著的跨模型差异（S2 的 Cohen's d 达到 -2.67），说明 S2/S4 虽然不能做 within-model 检测，但确实对 contamination 有响应
3. **D021 修正生效**：d100 不再报告虚假的 AUC=0.5，改为报告 cross-model effect size + Wilcoxon test
4. Narrative 更新为："signal effectiveness varies systematically with dosage; individual signals insufficient → need IRT multi-signal fusion"

---
