# analysis icc and progress check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_icc-and-progress-check_20260522T134428_result.json`
- **Structured JSON:** [`3b8d35af3bef7c5e1349.json`](../../sessions/3b/3b8d35af3bef7c5e1349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the results.

---

## Part A: ICC(3,1) — Mistral-7B FOLIO (K=12)

| Subset | n | ICC(3,1) | 95% CI |
|--------|---|----------|--------|
| **All 204 problems** (col-mean imputed) | 204 | **0.530** | [0.477, 0.586] |
| ≥8 valid traces (imputed) | 198 | 0.537 | [0.483, 0.593] |
| ≥10 valid traces (imputed) | 142 | 0.589 | [0.528, 0.653] |
| All 12 traces valid (no imputation) | 37 | 0.786 | [0.701, 0.864] |
| exp033 original (all 12 valid) | 47 | 0.704 | [0.613, 0.794] |

**vs Fleiss' κ = 0.46:**
- ICC(3,1) = **0.53** on full dataset, ~0.07 higher than Fleiss' κ
- Gap因为 ICC 利用了 ordinal 结构 (True=1, Unknown=0, False=-1)，而 Fleiss' κ 视三类为无序 nominal
- 两者都落在 "moderate agreement" 区间 (0.4–0.6)
- 当只看所有 12 条 trace 都产出标准答案的子集 (n=37/47) 时，ICC 跳到 0.70–0.79，说明 parse failure 集中在高分歧的难题上

~17% 的 trace (291/2448) 输出了空或非标准答案无法 parse，这些主要落在分歧大的问题上，拉低了全集 ICC。

---

## Part B: 多种子实验进度

所有 4 个 PID 存活，正在运行。

| GPU | 实验 | Seed | 进度 | 状态 |
|-----|------|------|------|------|
| **cuda:0** (PID 552333, 6h11m) | Qwen2.5 PW | 123 | 328/600 | 运行中 |
| | | 456 | 600/600 | ✅ |
| | | 789 | 600/600 | ✅ |
| **cuda:1** (PID 596151, 2h38m) | LLaMA FOLIO | 123 | 204/204 | ✅ |
| | | 456 | 73/204 | 运行中 |
| | | 789 | — | 排队 |
| **cuda:2** (PID 510987, 10h14m) | Mistral PW | 42 | 600/600 | ✅ |
| | | 123 | 600/600 | ✅ **新完成** |
| | | 456 | 43/600 | 运行中 |
| | | 789 | — | 排队 |
| **cuda:3** (PID 614142, 22m) | LLaMA PW | 42 | 28/600 | 运行中 |
| | | 123 | — | 排队 |
| | | 456 | — | 排队 |

**新完成:** Mistral PW seed=123（之前 586/600），结果：SICA acc=0.375, SC acc=0.408, delta=-0.033。

**cuda:3** 刚启动 22 分钟，LLaMA PW seed=42 刚开始 (28/600)。

---
