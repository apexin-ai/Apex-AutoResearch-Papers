# analysis gpt2m v4 table7

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2m_v4_table7_20260518T113128_result.json`
- **Structured JSON:** [`f3247eec1d80a7246169.json`](../../sessions/f3/f3247eec1d80a7246169.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPT-2m v4 Table 7 (n_perm=5000, 8 canonical pairs)

| Pair | Naive_p | Diff_p | Thresh | TY_p | PG_fwd_p | PG_rev_p | K(fwd) |
|------|---------|--------|--------|------|----------|----------|--------|
| ent→d1 | 0.0000 | 0.0000 | 2 (Y) | 0.1160 | 0.0006 | 0.0964 | 4/5 |
| ent→d2 | 0.0000 | 0.0000 | 2 (Y) | 0.0017 | 0.0020 | 0.1052 | 5/5 |
| ent→d3 | 0.0000 | 0.0000 | 2 (Y) | 0.0000 | 0.0024 | 0.1062 | 5/5 |
| ent→ppl | 0.0114 | 0.0022 | 7 (Y) | 0.9998 | 0.4989 | 0.1820 | 3/5 |
| ece→d1 | 0.0000 | 0.0005 | 1 (Y) | 0.0000 | 0.0006 | 0.0032 | 5/5 |
| ece→d2 | 0.0000 | 0.0000 | 1 (Y) | 0.0000 | 0.0010 | 0.0160 | 5/5 |
| ece→d3 | 0.0000 | 0.0000 | 1 (Y) | 0.0000 | 0.0010 | 0.0084 | 5/5 |
| ece→ppl | 0.0034 | 0.0029 | 6 (Y) | 0.2254 | 0.8796 | 0.6107 | 3/5 |

**Summary:** Naive=8/8, Diff=8/8, Thresh=8/8, TY=5/8, PG_fwd=6/8, PG_rev=3/8, K≥4=6/8

**Final gen_10 metrics:**
- ppl=16520.55, entropy=0.4794, ece=0.5216
- eff_rank=25.00, mauve=0.033925
- d1=0.0918, d2=0.4717, d3=0.7394, self_bleu=0.011851

**Key observations:**
- Entropy/ECE→distinct pairs show very strong signals (6/8 with K≥4)
- Both canary→ppl pairs are weaker (K=3/5, TY and PG_fwd both fail)
- PG_rev is significant only for ECE→distinct pairs (3/8), confirming directional asymmetry for entropy pairs but bidirectional coupling for ECE→distinct
- ECE is a slightly stronger canary than entropy on GPT-2m (5/5 K≥4 on distinct pairs vs 4-5/5)

**Intervention training:** `intervention_predictive_s42` was **already running** on cuda:0 (PID 351362, started ~19:50). `intervention_reactive_s42` running on cuda:1 (PID 340969, started ~18:26). No action needed.

---
