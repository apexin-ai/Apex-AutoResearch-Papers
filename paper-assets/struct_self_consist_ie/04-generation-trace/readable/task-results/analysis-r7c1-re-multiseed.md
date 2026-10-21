# analysis r7c1 re multiseed

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r7c1_re_multiseed_20260515T224037_result.json`
- **Structured JSON:** [`6df90c643fae84446bad.json`](../../sessions/6d/6df90c643fae84446bad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Task A: RE Multi-seed Selection (R7-C1) — **数据完整，3-seed 全有**

数据来源：`multiseed_selection_f1.json` (qwen_scierc_re_n16) + `r7c1_re_multiseed_selection.json`

**过滤后 (n=397, 仅含 RE 标注的实例):**

| Signal | Seed 42 | Seed 123 | Seed 456 | Mean±σ |
|--------|---------|----------|----------|--------|
| Greedy | 0.4046 | 0.4046 | 0.4042 | 0.4045±0.0002 |
| **SJ** | 0.3827 | 0.3918 | 0.3964 | 0.3903±0.0070 |
| **FK** | 0.3842 | 0.3979 | 0.3946 | 0.3922±0.0072 |
| **LP** | 0.4066 | 0.4128 | 0.4245 | **0.4146±0.0091** |
| Oracle | 0.6426 | 0.6509 | 0.6335 | 0.6423±0.0087 |

LP 是唯一 delta_vs_greedy > 0 的信号 (+0.0102)，Fisher combined p=0.053（边际显著）。

**全实例 (n=551):**

| Signal | Seed 42 | Seed 123 | Seed 456 | Mean±σ |
|--------|---------|----------|----------|--------|
| Greedy | 0.2915 | 0.2915 | 0.2913 | 0.2914±0.0002 |
| **SJ** | 0.2757 | 0.2823 | 0.2856 | 0.2812±0.0051 |
| **FK** | 0.2768 | 0.2867 | 0.2843 | 0.2826±0.0052 |
| **LP** | 0.2930 | 0.2974 | 0.3059 | **0.2988±0.0065** |
| Oracle | 0.4630 | 0.4690 | 0.4564 | 0.4628±0.0063 |

### Task B: N=8 Multi-seed QE (R8-W5) — **不完整**

- Seed 42: 有 (4 configs × 5 signals)
- Seed 123: 有 (3 configs: llama_conll, llama_scierc, qwen_scierc)
- **Seed 456: 没有** — N=8 inference 从未对 seed=456 运行过

结论：`"N=8 QE data: only seed=42 and seed=123 available. Seed=456 N=8 inference was never run. Paper Agent has already written a design rationale footnote."`

两个输出已保存到 `output/review_round8/r7c1_re_multiseed.json` 和 `output/review_round8/r8w5_n8_multiseed.json`。

---
