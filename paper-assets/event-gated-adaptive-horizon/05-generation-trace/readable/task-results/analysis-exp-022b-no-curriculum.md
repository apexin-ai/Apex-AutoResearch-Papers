# analysis exp 022b no curriculum

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_022b_no_curriculum_20260517T135746_result.json`
- **Structured JSON:** [`a09e955f070fa55627cb.json`](../../sessions/a0/a09e955f070fa55627cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the analysis:

---

## exp_022b_no_curriculum — Analysis Report

### 1. Training Status

- **Completed normally** (EXIT_CODE=0)
- Ran to **112K env steps**, last eval checkpoint at **105K**
- No errors or anomalies
- Checkpoint: `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022b_no_curriculum/latest.pt`
- Log: `~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log`
- W&B: not integrated (no wandb logging detected in this run)

### 2. Key Metrics Over Training

**Eval Return:**

| Step | eval_return |
|-----:|------------:|
|   5K |        37.4 |
|  15K |       167.3 |
|  25K |       169.5 |
|  35K |       140.4 |
|  45K |       164.3 |
|  55K |       156.2 |
|  65K |       142.5 |
|  75K |       142.3 |
|  85K |       164.0 |
|  95K |       247.5 |
| 105K |     **300.7** |

**CIVO & Gate Metrics:**

| Step | ve_ratio | alert | dt_mean | dt1_frac | gate_entropy | ent_ratio |
|-----:|---------:|------:|--------:|---------:|-------------:|----------:|
|  15K |    0.014 |     0 |    4.56 |    0.052 |        1.973 |     0.949 |
|  25K |    0.072 |     0 |    3.81 |    0.096 |        1.932 |     0.929 |
|  35K |    0.152 |     0 |    3.48 |    0.124 |        1.885 |     0.906 |
|  45K |    0.188 |     0 |    3.98 |    0.084 |        1.961 |     0.943 |
|  55K |    0.218 |     0 |    4.10 |    0.076 |        1.972 |     0.948 |
|  65K |    0.192 |     0 |    4.04 |    0.073 |        1.947 |     0.936 |
|  75K |    0.169 |     0 |    3.76 |    0.102 |        1.940 |     0.933 |
|  85K |    0.151 |     0 |    3.55 |    0.123 |        1.911 |     0.919 |
|  95K |    0.094 |     0 |    3.50 |    0.135 |        1.918 |     0.922 |
| 105K |    0.075 |     0 |    3.41 |    0.145 |        1.896 |     0.912 |

**Final gate distribution (105K):** dt1=14.5%, dt2=21.0%, dt3=20.9%, dt4=17.4%, dt5=12.6%, dt6=7.8%, dt7=4.0%, dt8=1.7%

### 3. Baseline Comparison

| Metric | exp_022b (105K) | Baseline exp_001 (~100K) | Ratio |
|--------|----------------:|-------------------------:|------:|
| eval_return | 300.7 | ~389 | **77.3%** |

Return was flat at 140–170 for 65K steps (15K–85K), then surged in the last 20K (247→301). The model may still be improving but remains significantly below baseline.

### 4. Hypothesis Verdict: **NEGATIVE** (with partial confirmation)

**Prediction 1 — Frozen dt_emb prevents CIVO (NVE < 1.5×): ✅ CONFIRMED**
- Peak ve_ratio = 0.218 (step 55K) → NVE ≈ 1.22×, well below 1.5× threshold
- civo/alert = 0 throughout entire training
- ve_ratio actually *decreased* in the second half (0.218 → 0.075)

**Prediction 2 — Gate learns meaningful temporal abstraction (dt_1_frac < 1.0): ⚠️ Technically met, but NOT meaningful**
- gate_dt_1_frac = 0.145 (not collapsed) — literal criterion met
- BUT gate_entropy_ratio = 0.912 → distribution is 91% of maximum entropy, i.e. near-uniform
- dt_mean drifted from 4.56→3.41 (mild preference for shorter horizons), but no strong structure
- gate_dt_autocorr ≈ 0 → no temporal coherence in gate decisions
- The gate is "not collapsed" but also "not structured" — it's outputting a mildly skewed near-random distribution

**Overall: NEGATIVE**

The frozen random dt_emb successfully prevents CIVO, confirming that learned dt_emb is the source of value explosion. However, the random embeddings carry no temporal semantics, so the gate has no meaningful signal to condition on — it converges to a near-uniform distribution with a mild lower-dt bias. The 77% baseline performance and the lack of gate structure indicate that this configuration does not achieve useful temporal abstraction. The late return surge (95K–105K) is interesting but likely reflects actor/critic improvement independent of gate quality, not emergent temporal reasoning.

**Key takeaway:** Frozen dt_emb is a sufficient CIVO fix but an insufficient basis for temporal abstraction. A middle path is needed — dt_emb that carries temporal information but doesn't cause value explosion (e.g., pretrained-then-frozen, or gradient-clipped).

---
