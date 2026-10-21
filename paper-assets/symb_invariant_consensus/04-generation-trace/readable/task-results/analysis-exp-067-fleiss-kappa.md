# analysis exp 067 fleiss kappa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-067-fleiss-kappa_20260519T115457_result.json`
- **Structured JSON:** [`e20f5c51fc6de909361d.json`](../../sessions/e2/e20f5c51fc6de909361d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 值 |
|---|---|
| **Fleiss' κ (raw-answer)** | **0.4124** |
| **Eff-K** | **2.17** |
| P_bar (mean agreement) | 0.6049 |
| P_e (chance agreement) | 0.3277 |
| Unique answer categories | 117 |

**Per-problem P_i 分布**: mean=0.6049, std=0.2478, min=0.1071, max=1.0000

**类别分布**: 93.8% 的回答集中在 True/False/Unknown 三个标准类别，但有 117 个 unique 类别（Mistral 产生了大量非标准答案如 "Tom is an Ocellated wild turkey."、"Djokovic lives in a tax haven" 等）。

**对比之前 seed 的参考值**（κ≈0.71-0.76），这次 raw-answer κ=0.41 显著低很多。主要原因是 raw-answer 不做 T/F/U 归一化，117 个杂乱类别极大地降低了 inter-rater agreement。只有 49/204 个问题的全部 12 个 trace 都产生了有效答案（mean=10.4 raters/problem）。

---
