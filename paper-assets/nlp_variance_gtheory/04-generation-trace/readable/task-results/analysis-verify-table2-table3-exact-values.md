# analysis verify table2 table3 exact values

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_table2_table3_exact_values_20260522T001642_result.json`
- **Structured JSON:** [`8a53d4d65c9efa3edd64.json`](../../sessions/8a/8a53d4d65c9efa3edd64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. The paper file at `docs/paper/experiments.tex` contains Table 2 and Table 3. Here are the comparisons:

---

## Table 2: MMLU 8-model G-study

Source: `per_benchmark_gstudy_mmlu.json` vs paper Table 2 (`docs/paper/experiments.tex:28-42`)

Paper caption says G_item = 0.896. JSON: G_item = 0.896. **OK**.

| Component | JSON exact | Paper current | Diff (pp) | Action |
|-----------|-----------|---------------|-----------|--------|
| item\_id | **37.88** | 37.9 | 0.02 | OK |
| model×item | **30.21** | 33.0 | **2.79** | **FIX→30** |
| residual | **25.01** | 23.1 | **1.91** | **FIX→25** |
| model | **2.83** | 0.9 | **1.93** | **FIX→3** |
| model×prompt | **1.59** | (in "all others <0.2") | **1.39** | **FIX→add row, 2%** |
| prompt×item | **0.95** | 2.1 | **1.15** | **FIX→1** |
| temp×item | **0.56** | 0.8 | 0.24 | OK (round to 1) |
| seed×item | **0.53** | 1.5 | **0.97** | **FIX→1** |
| ordering×item | **0.31** | 0.5 | 0.19 | OK (round to <1) |

**7 of 9 rows need correction.** The paper values appear to be from an older 4-model analysis.

Key text in body that also needs updating (line 21):
- "The model main effect remains below 1%" → actually **2.83%**, should say "below 3%"
- "model×item interaction emerges as the second-largest component at up to 33%" → actually **30%**

---

## Table 3: Cross-benchmark comparison (5 benchmarks)

Sources: `per_benchmark_gstudy_mmlu.json`, `per_benchmark_gstudy_arc.json`, `per_benchmark_gstudy_hellaswag_2temp.json`, `per_benchmark_gstudy_ff.json` (GSM8K section), `math_8model_verified.json`

Paper Table 3 (`docs/paper/experiments.tex:65-78`)

### MMLU
| Component | JSON exact | Paper | Diff | Action |
|-----------|-----------|-------|------|--------|
| item | 37.88 | 38 | 0.1 | OK |
| mod.×item | 30.21 | 33 | **2.8** | **FIX→30** |
| model | 2.83 | 1 | **1.8** | **FIX→3** |
| prompt | 0.00 | <1 | 0 | OK |
| mod.×prmpt | 1.59 | <1 | **0.6+** | **FIX→2** |
| residual | 25.01 | 23 | **2.0** | **FIX→25** |

### ARC
| Component | JSON exact | Paper | Diff | Action |
|-----------|-----------|-------|------|--------|
| item | 37.88 | 38 | 0.1 | OK |
| mod.×item | 33.73 | 32 | **1.7** | **FIX→34** |
| model | 3.08 | 1 | **2.1** | **FIX→3** |
| prompt | 0.00 | <1 | 0 | OK |
| mod.×prmpt | 8.00 | <1 | **7.0** | **FIX→8** |
| residual | 15.44 | 22 | **6.6** | **FIX→15** |

### HellaSwag
| Component | JSON exact | Paper | Diff | Action |
|-----------|-----------|-------|------|--------|
| item | 34.27 | 34 | 0.3 | OK |
| mod.×item | 36.00 | 34 | **2.0** | **FIX→36** |
| model | 5.35 | 1 | **4.4** | **FIX→5** |
| prompt | 0.00 | <1 | 0 | OK |
| mod.×prmpt | 0.19 | <1 | 0 | OK |
| residual | 21.41 | 25 | **3.6** | **FIX→21** |

### GSM8K
| Component | JSON exact | Paper | Diff | Action |
|-----------|-----------|-------|------|--------|
| item | 16.86 | 17 | 0.1 | OK |
| mod.×item | 14.55 | 8 | **6.6** | **FIX→15** |
| model | 10.75 | 15 | **4.3** | **FIX→11** |
| prompt | 5.41 | 12 | **6.6** | **FIX→5** |
| mod.×prmpt | 8.53 | 9 | 0.5 | OK |
| residual | 39.89 | 30 | **9.9** | **FIX→40** |

### MATH (from `math_8model_verified.json`)
| Component | JSON exact | Paper | Diff | Action |
|-----------|-----------|-------|------|--------|
| item | 24.03 | 24 | 0.03 | OK |
| mod.×item | 17.28 | 12 | **5.3** | **FIX→17** |
| model | 8.51 | 10 | **1.5** | **FIX→9** |
| prompt | 0.83 | 8 | **7.2** | **FIX→1** |
| mod.×prmpt | 1.67 | 6 | **4.3** | **FIX→2** |
| residual | 43.88 | 32 | **11.9** | **FIX→44** |

### G_item and N (not currently in paper Table 3, but available)
| Benchmark | G_item | N |
|-----------|--------|---|
| MMLU | 0.896 | 200 |
| ARC | 0.892 | 200 |
| HellaSwag | 0.872 | 200 |
| GSM8K | 0.284 | 200 |
| MATH | 0.888 | 200 |

---

## Summary

**Table 2**: 7/9 displayed rows are wrong. The biggest errors: model×item (30→33, +2.8pp), model (2.8→0.9, -1.9pp), residual (25→23, -2pp). Additionally, model×prompt (1.59%) is incorrectly lumped into "all others <0.2".

**Table 3**: 19/30 cells need correction. The worst errors are in:
- **MATH**: residual off by 11.9pp, prompt off by 7.2pp, mod.×item off by 5.3pp
- **GSM8K**: residual off by 9.9pp, prompt off by 6.6pp, mod.×item off by 6.6pp
- **ARC**: mod.×prmpt off by 7.0pp, residual off by 6.6pp

The paper Table 3 also incorrectly states all MC benchmarks have model ≈ 1%, but JSON shows model = 2.83% (MMLU), 3.08% (ARC), 5.35% (HellaSwag). Body text at line 56 and line 73 needs updating accordingly.

---
