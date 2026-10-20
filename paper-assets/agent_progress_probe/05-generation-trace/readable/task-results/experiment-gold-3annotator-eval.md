# experiment gold 3annotator eval

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_gold-3annotator-eval_20260515T121516_result.json`
- **Structured JSON:** [`5218904a673624447051.json`](../../sessions/52/5218904a673624447051.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 results collected. Now producing the comparison tables.

---

## Step 5: Verification & Comparison Tables

### Eval ↔ Bootstrap Consistency Check

Bootstrap F1 values for GB and RF match eval results exactly across all sets:

| Model | Set A eval | Set A boot | Set B eval | Set B boot | Set C eval | Set C boot |
|-------|-----------|-----------|-----------|-----------|-----------|-----------|
| GB | 0.7210 | 0.7210 | 0.8394 | 0.8394 | 0.8381 | 0.8381 |
| RF | 0.7401 | 0.7401 | 0.8107 | 0.8107 | 0.8099 | 0.8099 |

**All within 0pp tolerance — perfect consistency.**

---

### Table 1: Per-Model Macro-F1 Across 4 Gold Sets

| Model | Old N=195 | Set A (N=52, conf≥3) | Set B (N=505, conf≥2) | Set C (N=512, all) |
|-------|----------|---------------------|----------------------|-------------------|
| **GB** | 0.764 | 0.7210 (n=50) | **0.8394** (n=491) | **0.8381** (n=498) |
| RF | 0.752 | 0.7401 (n=50) | 0.8107 (n=491) | 0.8099 (n=498) |
| MV | 0.718 | 0.7210 (n=50) | 0.7975 (n=491) | 0.7992 (n=498) |
| GRU Probe | 0.735 | 0.7619 (n=35) | 0.7895 (n=322) | 0.7936 (n=328) |
| TWV | 0.768 | 0.6766 (n=37) | 0.8478 (n=335) | 0.8508 (n=341) |
| TWV Probe | — | 0.7464 (n=35) | 0.8539 (n=322) | 0.8569 (n=328) |

---

### Table 2: Bootstrap Paired Tests (p-values, 10K iterations, seed=42)

| Comparison | Set A (N=52) | Set B (N=505) | Set C (N=512) |
|-----------|-------------|--------------|--------------|
| **GB vs MV** | p=1.000 (n=50, Δ=0.000) | **p=0.0001** (n=491, Δ=+0.042) | **p<0.0001** (n=498, Δ=+0.039) |
| **GB vs Probe** | p=0.253 (n=35, Δ=-0.053) | **p<0.0001** (n=322, Δ=+0.088) | **p<0.0001** (n=328, Δ=+0.086) |
| **RF vs GB** | p=0.366 (n=50, Δ=+0.019) | **p=0.0003** (n=491, Δ=-0.029) | **p=0.0003** (n=498, Δ=-0.028) |
| TWV Probe vs GB | p=0.289 (n=35, Δ=+0.038) | p=0.056 (n=322, Δ=-0.023) | p=0.061 (n=328, Δ=-0.023) |
| TWV Probe vs Probe | p=0.417 (n=35, Δ=-0.016) | **p=0.0002** (n=322, Δ=+0.064) | **p=0.0002** (n=328, Δ=+0.063) |

---

### Key Findings

1. **Set A (N=52, strict 3-annotator)**: Too small for significance — all p>0.25. GB=MV=0.721, wide CIs.
2. **Set B & C are highly consistent**: B and C differ by only 7 windows, and all F1 values agree within 0.3pp. Significance patterns are identical.
3. **GB dominates on conf≥2**: GB significantly beats MV (+4.2pp, p=0.0001), GRU Probe (+8.8pp, p<0.0001), and RF (+2.9pp, p=0.0003).
4. **TWV Probe vs GB**: Borderline non-significant (p=0.056/0.061) — GB has 2.3pp edge, TWV Probe can't close the gap.
5. **TWV Probe vs GRU Probe**: Strongly significant (+6.3pp, p=0.0002) — trajectory-weighted embeddings dominate standard embeddings.

---
