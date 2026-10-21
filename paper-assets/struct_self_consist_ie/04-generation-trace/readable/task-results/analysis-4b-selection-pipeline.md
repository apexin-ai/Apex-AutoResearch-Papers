# analysis 4b selection pipeline

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4b_selection_pipeline_20260515T200110_result.json`
- **Structured JSON:** [`21dbf9b40726bd1a131f.json`](../../sessions/21/21dbf9b40726bd1a131f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据齐了。以下是完整结果：

---

## Qwen3-4B Selection F1 Results

### CoNLL NER (n=2756, N=8)

| Method | Sel F1 | Δ Greedy | p-value |
|--------|--------|----------|---------|
| Greedy | 0.9213 | — | — |
| Random | 0.9183 | -0.0029 | — |
| **VC** | **0.9233** | **+0.0020** | 0.076 |
| SJ | 0.9220 | +0.0007 | 0.256 |
| FK | 0.9215 | +0.0003 | 0.411 |
| EM | 0.9220 | +0.0007 | 0.255 |
| LP | 0.9221 | +0.0009 | 0.093 |
| Oracle | 0.9382 | +0.0170 | — |

**Selection gaps**: SJ-FK=+0.0005, SJ-VC=-0.0013, SJ-LP=-0.0002

### SciERC NER (n=529, N=8)

| Method | Sel F1 | Δ Greedy | p-value |
|--------|--------|----------|---------|
| Greedy | 0.6622 | — | — |
| Random | 0.5991 | -0.0631 | — |
| VC | 0.6282 | -0.0340 | 1.000 |
| **SJ** | **0.6473** | **-0.0149** | 0.975 |
| FK | 0.6466 | -0.0156 | 0.980 |
| EM | 0.6436 | -0.0187 | 0.992 |
| LP | 0.6399 | -0.0223 | 0.998 |
| Oracle | 0.7925 | +0.1302 | — |

**Selection gaps**: SJ-FK=+0.0007, SJ-VC=+0.0191, SJ-LP=+0.0074

### SciERC RE (n=397, N=8)

| Method | Sel F1 | Δ Greedy | p-value |
|--------|--------|----------|---------|
| Greedy | 0.4076 | — | — |
| Random | 0.3350 | -0.0726 | — |
| VC | 0.4002 | -0.0074 | 0.713 |
| **SJ** | **0.4073** | **-0.0002** | 0.511 |
| FK | 0.3925 | -0.0151 | 0.912 |
| EM | 0.3804 | -0.0272 | 0.995 |
| LP | 0.3941 | -0.0135 | 0.852 |
| Oracle | 0.5970 | +0.1894 | — |

**Selection gaps**: SJ-FK=+0.0149, SJ-VC=+0.0071, SJ-LP=+0.0132

---

## 4B vs 8B Comparison (N=8)

### CoNLL NER

| Metric | 8B | 4B |
|--------|----|----|
| Greedy | 0.9079 | 0.9213 |
| Oracle | 0.9483 | 0.9382 |
| Headroom | +0.0404 | +0.0170 |
| SJ sel | 0.8990 | 0.9220 |
| FK sel | 0.8988 | 0.9215 |
| SJ-FK sel gap | +0.0002 | +0.0005 |
| SJ ρ | 0.4357 | 0.4324 |
| FK ρ | 0.3998 | 0.4244 |
| SJ-FK ρ gap | +0.0359 | +0.0080 |

### SciERC NER (8B = 3-seed mean N=8)

| Metric | 8B | 4B |
|--------|----|----|
| Greedy | 0.6458 | 0.6622 |
| Oracle | 0.7764 | 0.7925 |
| SJ sel | 0.6413 | 0.6473 |
| FK sel | 0.6413 | 0.6466 |
| SJ-FK sel gap | +0.0001 | +0.0007 |
| SJ ρ | ~0.42 | 0.4221 |
| FK ρ | ~0.33 | 0.3258 |
| SJ-FK ρ gap | ~+0.09 | +0.0963 |

---

## Key Finding for Correlation-Selection Gap Claim

**SciERC NER 4B** demonstrates the pattern clearly:
- **Correlation gap** (SJ-FK ρ): **+0.096** — SJ correlates much better with quality
- **Selection gap** (SJ-FK sel F1): **+0.0007** — but selects virtually identically

**SciERC RE 4B** shows the largest selection gap:
- SJ-FK sel: **+0.0149** (SJ definitively better at selection for RE)
- SJ-LP sel: **+0.0132**

**CoNLL 4B** has compressed headroom (only 1.7pp greedy-oracle gap), so all signals are packed together with negligible selection gaps.

Results saved to `/root/autodl-tmp/struct_self_consist_ie/output/selection_f1_4b_results.json`.

---
