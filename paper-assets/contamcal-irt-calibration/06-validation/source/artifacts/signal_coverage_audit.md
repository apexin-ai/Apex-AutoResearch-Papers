# Signal Coverage Audit for IRT Pooling

**Date**: 2026-05-16  
**Target**: N >= 16 respondents per benchmark for IRT pooling  
**Signal types**: s1_embedding, s2_minkpp, s3_constat, s4_selfcritique  
**Benchmarks**: mmlu, gsm8k, arc_challenge  

---

## Coverage Matrix

### 0.5B — seed 42 (all alpha=32, valid)

| checkpoint | s1_emb | s2_mink | s3_con | s4_self | mmlu | gsm8k | arc |
|------------|--------|---------|--------|---------|------|-------|-----|
| d000_s42   | ✅✅✅  | ✅✅✅   | ❌❌❌  | ✅✅✅   | 3/4  | 3/4   | 3/4 |
| d005_s42   | ✅✅✅  | ✅✅✅   | ❌❌❌  | ✅✅✅   | 3/4  | 3/4   | 3/4 |
| d025_s42   | ✅✅✅  | ✅✅✅   | ❌❌❌  | ✅✅✅   | 3/4  | 3/4   | 3/4 |
| d100_s42   | ✅✅✅  | ✅✅✅   | ❌❌❌  | ✅✅✅   | 3/4  | 3/4   | 3/4 |

> s1/s2/s4 complete for all 3 benchmarks. **s3_constat missing for all 0.5B checkpoints.**

### 0.5B — seed 123

| checkpoint | s1_emb | s2_mink | s3_con | s4_self | Status |
|------------|--------|---------|--------|---------|--------|
| d000_s123  | ❌     | ❌      | ❌     | ❌      | No signal dir |
| d005_s123  | ❌     | ❌      | ❌     | ❌      | No signal dir |
| d025_s123  | ❌     | ❌      | ❌     | ❌      | No signal dir |
| d100_s123  | ❌     | ❌      | ❌     | ❌      | No signal dir |

> **No 0.5B s123 signals computed at all.** SFT checkpoints exist (confirmed in registry).

---

### 1.5B — seed 42 (all alpha=32, valid)

| checkpoint | s1_emb | s2_mink | s3_con | s4_self | mmlu | gsm8k | arc |
|------------|--------|---------|--------|---------|------|-------|-----|
| d000_s42   | ✅✅✅  | ✅✅✅   | ❌❌❌  | ✅✅✅   | 3/4  | 3/4   | 3/4 |
| d005_s42   | ✅✅✅  | ✅✅✅   | ❌❌❌  | ✅✅✅   | 3/4  | 3/4   | 3/4 |
| d025_s42   | ✅✅✅  | ✅✅✅   | ❌❌❌  | ✅✅✅   | 3/4  | 3/4   | 3/4 |
| d100_s42   | ✅✅✅  | ✅✅✅   | ❌❌❌  | ✅✅✅   | 3/4  | 3/4   | 3/4 |

> Same pattern as 0.5B. **s3_constat missing for all 1.5B checkpoints.**

### 1.5B — seed 123

| checkpoint | s1_emb | s2_mink | s3_con | s4_self | Status |
|------------|--------|---------|--------|---------|--------|
| d000_s123  | ❌     | ❌      | ❌     | ❌      | No signal dir |
| d005_s123  | ❌     | ❌      | ❌     | ❌      | No signal dir |
| d025_s123  | ❌     | ❌      | ❌     | ❌      | No signal dir |
| d100_s123  | ❌     | ❌      | ❌     | ❌      | No signal dir |

> **No 1.5B s123 signals computed at all.** SFT checkpoints exist (confirmed in registry).

---

### 3B — seed 42

| checkpoint | signal | mmlu | gsm8k | arc | Notes |
|------------|--------|------|-------|-----|-------|
| d000_v2_s42 (alpha=32) | s1_emb | ✅ | ✅ | ✅ | Valid |
| | s2_mink | ✅ | ✅ | ✅ | Valid |
| | s3_con  | ✅ | ✅ | ✅ | Valid |
| | s4_self | ❌ | ❌ | ❌ | v6 batch died before s4 |
| d005_s42 | s1_emb | ⚠️ | ⚠️ | ⚠️ | SFT running (exp_001_sft_3B_d005_s42_a32); existing signals from old checkpoint |
| | s2_mink | ⚠️ | ⚠️ | ⚠️ | Same — pending SFT completion |
| | s3_con  | ❌ | ❌ | ❌ | Never computed |
| | s4_self | ❌ | ❌ | ⚠️ | Same — pending SFT |
| d025_v3_s42 (alpha=32) | s1_emb | ✅ | ✅ | ✅ | Valid |
| | s2_mink | ✅ | ✅ | ✅ | Valid |
| | s3_con  | ❌ | ❌ | ❌ | Never computed |
| | s4_self | ⏳ | ❌ | ❌ | mmlu 26% running (~1.5hr ETA) |
| d100_s42 | s1_emb | ✅ | ✅ | ✅ | Valid (from v6 batch) |
| | s2_mink | ✅ | ✅ | ✅ | Valid |
| | s3_con  | ❌ | ❌ | ❌ | Never computed |
| | s4_self | ❌ | ✅ | ✅ | mmlu missing; gsm8k+arc from v6 batch |

> - d005_s42 blocked on SFT training (exp_001_sft_3B_d005_s42_a32 RUNNING)
> - d100_s42 SFT v3 also running (exp_001_sft_3B_d100_s42_a32_v3) — existing signals may need revalidation
> - d025_v3_s42 s4_selfcritique_mmlu actively computing (exp_002_signals_3B_d025_v3_s42)

### 3B — seed 123

| checkpoint | signal | mmlu | gsm8k | arc | Notes |
|------------|--------|------|-------|-----|-------|
| d000_s123  | all    | ❌   | ❌    | ❌  | **No signal dir exists** |
| d005_s123  | s1_emb | ✅   | ❌    | ❌  | Only mmlu computed |
| | s2_mink | ✅  | ❌    | ❌  | Only mmlu computed |
| | s3_con  | ❌   | ❌    | ❌  | Never computed |
| | s4_self | ❌   | ❌    | ❌  | Never computed |
| d025_s123  | s1_emb | ✅   | ✅    | ✅  | Complete |
| | s2_mink | ✅  | ✅    | ✅  | Complete |
| | s3_con  | ❌   | ❌    | ❌  | Never computed |
| | s4_self | ⏳   | ✅    | ✅  | mmlu partial (_s4_chunks_mmlu) |
| d100_a32_s123 | s1_emb | ✅ | ❌ | ❌ | Only mmlu computed |
| | s2_mink | ✅ | ❌    | ❌  | Only mmlu computed |
| | s3_con  | ❌  | ❌    | ❌  | Never computed |
| | s4_self | ❌  | ❌    | ❌  | Never computed |

---

## Running Experiments

| Registry ID | What | GPU Status |
|---|---|---|
| exp_002_signals_3B_d025_v3_s42 | s4_selfcritique mmlu (26%, ~1.5hr ETA) | Active |
| exp_002_signals_3B_v7 | Unknown scope (no log found) | Active |
| exp_001_sft_3B_d005_s42_a32 | d005 SFT training | Active |
| exp_001_sft_3B_d100_s42_a32_v3 | d100 SFT re-training | Active |
| exp_001_eval_3B_d025_v3_s42_batch | Eval batch | Active |
| exp_001_eval_3B_d100_s123_a32_batch | Eval batch | Active |

---

## IRT Pooling N-count (valid respondents per benchmark)

Counting checkpoints with at least s1+s2 complete (minimum for IRT feature vector):

| Benchmark | 0.5B s42 | 0.5B s123 | 1.5B s42 | 1.5B s123 | 3B s42 | 3B s123 | **Total** |
|-----------|----------|-----------|----------|-----------|--------|---------|-----------|
| **mmlu**  | 4        | 0         | 4        | 0         | 3*     | 3       | **14**    |
| **gsm8k** | 4        | 0         | 4        | 0         | 3*     | 1       | **12**    |
| **arc**   | 4        | 0         | 4        | 0         | 3*     | 1       | **12**    |

*3B s42: d000_v2, d025_v3, d100 (d005 blocked on SFT)

Counting checkpoints with s1+s2+s4 all complete (full non-constat signal set):

| Benchmark | 0.5B s42 | 1.5B s42 | 3B s42 | 3B s123 | **Total** |
|-----------|----------|----------|--------|---------|-----------|
| **mmlu**  | 4        | 4        | 0      | 0       | **8**     |
| **gsm8k** | 4        | 4        | 1 (d100) | 1 (d025) | **10** |
| **arc**   | 4        | 4        | 1 (d100) | 1 (d025) | **10** |

> **None of the benchmarks reach N >= 16 with full signal sets.** The critical bottlenecks are:
> 1. All s123 signals for 0.5B and 1.5B (0 out of 8 checkpoints)
> 2. s3_constat missing for ALL 0.5B and 1.5B checkpoints (never computed)
> 3. s4_selfcritique missing or incomplete for most 3B checkpoints

---

## Missing Items — Priority Ranking

### P0 — Blocking IRT pooling (massive N gap)

1. **0.5B s123 signals (×4 checkpoints × 3 benchmarks × 3-4 signals)** — 0/4 done, SFT checkpoints exist
2. **1.5B s123 signals (×4 checkpoints × 3 benchmarks × 3-4 signals)** — 0/4 done, SFT checkpoints exist
3. **3B d000_s123 signals** — No signal dir, SFT checkpoint exists (exp_001_sft_3B_d000_s123)

### P1 — Incomplete 3B signals (blocking individual checkpoints)

4. **3B d000_v2_s42: s4_selfcritique** (all 3 benchmarks) — v6 batch died before completing
5. **3B d025_v3_s42: s4_selfcritique** — mmlu ⏳ running, gsm8k+arc missing
6. **3B d100_s42: s4_selfcritique mmlu** — gsm8k+arc done, only mmlu missing
7. **3B d005_s123: gsm8k + arc signals** — only mmlu s1+s2 done
8. **3B d100_a32_s123: gsm8k + arc signals** — only mmlu s1+s2 done
9. **3B d025_s123: s4_selfcritique mmlu** — partial (_s4_chunks), gsm8k+arc done

### P2 — Blocked on upstream SFT

10. **3B d005_s42: all signals** — SFT still training (exp_001_sft_3B_d005_s42_a32)
11. **3B d100_s42: revalidation** — SFT v3 running; existing signals may need recomputation

### P3 — s3_constat gap (systemic)

12. **s3_constat for ALL 0.5B checkpoints** (8 checkpoints × 3 benchmarks = 24 cells)
13. **s3_constat for ALL 1.5B checkpoints** (8 checkpoints × 3 benchmarks = 24 cells)
14. **s3_constat for ALL 3B checkpoints except d000_v2_s42** (7+ checkpoints × 3 benchmarks)

> s3_constat has only ever been computed for 3B_d000_v2_s42. This is a systemic gap.
> **Decision needed**: Is s3 required for IRT pooling, or can we proceed with s1+s2+s4?

---

## Summary

- **Current max N (s1+s2 only)**: mmlu=14, gsm8k=12, arc=12
- **Current max N (s1+s2+s4)**: mmlu=8, gsm8k=10, arc=10
- **Target N**: >= 16
- **Biggest gap**: 0.5B+1.5B s123 signals (16 checkpoint × 3 benchmark combinations, zero computed)
- **Quick win**: Computing 0.5B+1.5B s123 signals would add 8 respondents per benchmark, pushing mmlu to 22 and gsm8k/arc to 20 (with s1+s2)
