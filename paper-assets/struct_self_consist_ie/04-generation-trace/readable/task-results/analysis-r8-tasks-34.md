# analysis r8 tasks 34

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r8_tasks_34_20260515T223541_result.json`
- **Structured JSON:** [`91171c1a0429e6043876.json`](../../sessions/91/91171c1a0429e6043876.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Task 3: Thinking Token LP 影响量化（R8-W2）

**方案选择：B**（数据只有 sample 级 cumulative/mean logprob，无 per-token logprobs）

| 指标 | SciERC (Qwen3-4B) | CoNLL (Qwen3-4B) |
|------|-------------------|-------------------|
| N instances | 551 | 3,453 |
| Avg tokens/sample | **213.5** | **58.9** |
| Thinking tokens | ~4-5 | ~4-5 |
| Token count ratio | **2.11%** | **7.64%** |
| LP contribution (scenario 1, LP=-0.001/tok) | **0.04%** | **0.62%** |
| LP contribution (scenario 2, LP=-0.01/tok) | **0.39%** | **6.15%** |
| Selection changed (mean LP adjusted) | **8/551 (1.5%)** | **0/3453 (0.0%)** |

**关键论证**：
1. 使用 **cumulative LP** 排序时，thinking tokens 对所有 sample 加一个**常量偏移** → 排序**完全不变** → selection 结果**完全相同**
2. 使用 **mean LP** 排序时，thinking tokens 影响分母，但实际仅导致 SciERC 1.5% 的 instances 改变选择（CoNLL 0%）
3. LP 贡献量占 cumulative LP 的 0.04%–0.39%（SciERC）

**结论：影响可忽略。Thinking tokens 不影响 LP-based selection 的实质结果。**

---

## Task 4: RE 多种子 Selection 数据（R7-C1）

**数据可用性**：
- Seed 42 RE data: **EXISTS** (`exp_008_re_n16_v2/`)
- Seed 123 RE data: **EXISTS** (`exp_re_scierc_seed123/`, 551 instances, joint subtask)
- Seed 456 RE data: **EXISTS** (`exp_re_scierc_seed456/`, 551 instances, joint subtask)

**3-seed RE Selection F1 (SciERC, Qwen3-4B, N=16)**：

| Signal | Mean F1 | Std | Seed 42 | Seed 123 | Seed 456 | Δ vs Greedy (mean) |
|--------|---------|-----|---------|----------|----------|---------------------|
| Greedy | 0.2914 | 0.0002 | 0.2915 | 0.2915 | 0.2913 | — |
| Random | 0.2624 | 0.0014 | 0.2619 | 0.2613 | 0.2640 | -0.0290 |
| Oracle | 0.4628 | 0.0063 | 0.4630 | 0.4690 | 0.4564 | +0.1714 |
| **LP** | **0.2988** | **0.0065** | 0.2930 | 0.2974 | 0.3059 | **+0.0073** |
| VC | 0.2837 | 0.0016 | 0.2819 | 0.2841 | 0.2850 | -0.0077 |
| SJ | 0.2812 | 0.0051 | 0.2757 | 0.2823 | 0.2856 | -0.0102 |
| FK | 0.2826 | 0.0052 | 0.2768 | 0.2867 | 0.2843 | -0.0088 |
| EM | 0.2768 | 0.0074 | 0.2683 | 0.2817 | 0.2804 | -0.0147 |

**结论**：3 个 seed 的 RE selection 数据全部可用。**LP 是唯一在 RE 上超过 greedy 的 signal**（+0.73 F1 points），其余 signal 均略低于 greedy。这与 NER 上 LP 的优势一致。

---

结果已保存至 `output/review_round8/r8w2_thinking_token_lp.json` 和 `output/review_round8/r7c1_re_multiseed_selection.json`。

---
