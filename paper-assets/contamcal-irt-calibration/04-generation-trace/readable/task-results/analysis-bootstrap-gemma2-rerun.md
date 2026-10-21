# analysis bootstrap gemma2 rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-gemma2-rerun_20260521T070853_result.json`
- **Structured JSON:** [`ebb6d55adeb1d63be23e.json`](../../sessions/eb/ebb6d55adeb1d63be23e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 benchmark 的 bootstrap 都完成了。以下是汇总。

---

## Updated Bootstrap CI Results (2026-05-21)

### MMLU

| Family | n | Baseline | Mean Δ(d100) | 95% CI | Method | Significant? |
|--------|---|----------|-------------|--------|--------|-------------|
| Phi-4 | 3 | 76.40% | +0.72pp | [-0.17, +1.39] | boot | No (marginal) |
| Qwen2.5-14B | 2* | 68.98% | -11.05pp | [-32.41, +10.30] | t | No |
| Qwen2.5-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37] | t | No |
| **Gemma-2-9B** | **3** | **64.20%** | **+2.38pp** | **[+1.49, +3.14]** | **boot** | **Yes** |
| OLMo-2-7B | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | boot | No (marginal) |

### ARC-Challenge

| Family | n | Baseline | Mean Δ(d100) | 95% CI | Method | Significant? |
|--------|---|----------|-------------|--------|--------|-------------|
| Phi-4 | 3 | 91.92% | +0.65pp | [+0.51, +0.77] | boot | Yes |
| **Qwen2.5-14B** | **3*** | **90.64%** | **-5.03pp** | **[-9.39, -2.76]** | **boot** | **Yes** |
| Qwen2.5-7B | 2 | 87.50% | -2.65pp | [-5.90, +0.61] | t | No |
| **Gemma-2-9B** | **3** | **85.89%** | **-0.14pp** | **[-1.96, +1.42]** | **boot** | **No (p=0.371)** |
| OLMo-2-7B | 3 | 76.28% | +3.44pp | [+2.90, +3.78] | boot | Yes |

---

### Key changes from previous run

**Gemma-2-9B:**
- **MMLU**: n=2→3. CI collapsed from [-11.81, +17.06](t) to **[+1.49, +3.14](boot)** — now statistically significant positive effect (+2.38pp). s0 pattern = V-recovery (differs from s42=Benefit-sat, s123=Benefit).
- **ARC**: n=1→3. Went from point estimate +2.73pp (Benefit) to **[-1.96, +1.42](boot), not significant** (p=0.371, mean -0.14pp). Two of 3 seeds show V-recovery pattern. Cross-seed ρ = -0.167 (very low stability).

**Qwen2.5-14B (also changed):**
- **MMLU**: s0 added 3/5 dosages (d000,d005,d025). d000-d025 now use bootstrap (n=3); d050/d100 still t (n=2). Baseline shifted slightly 69.05%→68.98%.
- **ARC**: s0 added 4/5 dosages (missing d050). Δ(d100) went from -2.86pp CI[-6.65,+0.94](t) to **-5.03pp CI[-9.39,-2.76](boot) — now statistically significant harm**.

**Qwen2.5-7B**: unchanged (n=2 for both, no s0 data found).

---
