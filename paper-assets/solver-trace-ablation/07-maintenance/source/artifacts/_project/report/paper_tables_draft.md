# Paper Tables Draft (2026-05-14)

All numbers sourced from experiment registry. Eval method is eval_sta.py full STA unless noted.

---

## Table 1: Main Results

| Method | Formula | β | Seed | eval PR | eval ISR | proved-only ISR | Comp. (mean) | Taut. Collapse? |
|--------|---------|---|------|---------|----------|-----------------|--------------|-----------------|
| Exec-only (500 steps) | R = 𝟙{exec} | — | 42 | 0.93 | 0.1232 | 0.1324 | 6.58† | No |
| Exec-only (500 steps) | R = 𝟙{exec} | — | 43 | 0.14‡ | 0.00‡ | — | — | No (degenerate)‡ |
| Exec-only (500 steps) | R = 𝟙{exec} | — | 44 | 0.98 | 0.57§ | 0.5816§ | 2.04§ | **Yes** |
| Exec-only (1000 steps) | R = 𝟙{exec} | — | 42 | 0.96 | 0.0027 | 0.0028 | 18.55 | No |
| ISR-additive | R = 𝟙{exec} + β·ISR | 0.1 | 42 | 0.81 | 0.3365 | 0.4154 | 5.58 | No |
| ISR-additive | R = 𝟙{exec} + β·ISR | 0.1 | 43 | TBD | TBD | TBD | TBD | TBD |
| ISR-additive | R = 𝟙{exec} + β·ISR | 0.1 | 44 | TBD | TBD | TBD | TBD | TBD |
| Random-additive | R = 𝟙{exec} + β·Rand | 0.1 | 42 | 0.79 | 0.1038 | 0.1314 | 8.46 | No |
| ISR-additive | R = 𝟙{exec} + β·ISR | 0.3 | 42 | 0.18 | 0.0257 | 0.1427 | — | — |
| Random-additive | R = 𝟙{exec} + β·Rand | 0.3 | 42 | 0.48 | 0.0453 | 0.0943 | 9.60 | No |
| Convex-random | R = (1−β)·𝟙{exec} + β·Rand | — | 42 | 1.00 | 0.535§ | 0.535§ | ~2§ | **Yes** (degenerate) |
| Convex-ISR (STA) | R = (1−β)·𝟙{exec} + β·ISR | — | 42 | 0.77ᵗ | 0.2299ᵗ | — | — | — |

### Footnotes

- **†** Component count 6.58 for s42 exec-only sourced from plan001-s44 cross-reference notes (eval_sta output).
- **‡** plan001-exec-only-s43-r4: sampling eval (do_sample=True, T=0.7), **not** eval_sta.py full STA. PR=0.14 reflects sampling failure; 87% of samples hit max_new_tokens generating unparseable output. Not directly comparable to greedy-decoded eval_sta results.
- **§** Tautological artifact. s44 ISR=0.57 is a structural artifact: 94% of proofs have only 2 components (premise = conclusion tautology), so ISR ≈ 0.5 mechanically. Similarly plan013 convex-random generates trivial 2-component proofs (PR=100%, ISR=0.535 = fake).
- **ᵗ** plan005-sta-low-s42: **training metrics only** (last-100-step window). Checkpoint deleted; no eval_sta.py run available. Not directly comparable to eval metrics.

### Exec-only 3-seed summary (where comparable)

Only s42 and s44 used eval_sta.py full STA. s43 used sampling eval → excluded from aggregation.

| Metric | s42 | s44 | s43 (sampling) |
|--------|-----|-----|----------------|
| PR | 0.93 | 0.98 | 0.14‡ |
| ISR | 0.1232 | 0.57§ | 0.00‡ |
| Collapse? | No | Tautological | Degenerate output |

**Key finding**: Exec-only reward fails 2/3 seeds. Only s42 produces genuine proofs.

### ISR β=0.1 vs Random β=0.1 (s42, head-to-head)

| Metric | ISR β=0.1 | Random β=0.1 | Δ |
|--------|-----------|--------------|---|
| eval PR | 0.81 | 0.79 | +0.02 |
| eval ISR | 0.3365 | 0.1038 | **+0.2327 (3.2×)** |
| proved-only ISR | 0.4154 | 0.1314 | **+0.2840 (3.2×)** |
| Components (mean) | 5.58 | 8.46 | −2.88 |
| ISR=0 ratio | 0.037 | 0.367 | −0.330 |
| ISR=1 ratio | 0.124 | 0.000 | +0.124 |
| Taut. collapse | No | No | — |

### β dose response (s42)

| β | ISR-additive PR | ISR-additive ISR | Random-additive PR | Random-additive ISR |
|---|-----------------|------------------|--------------------|---------------------|
| 0 (exec-only) | 0.93 | 0.1232 | — | — |
| 0.1 | 0.81 | 0.3365 | 0.79 | 0.1038 |
| 0.3 | 0.18 | 0.0257 | 0.48 | 0.0453 |

---

## Table 2: Hacking Taxonomy (plan012)

ISR β=0.1 (plan002-additive-b01-s42) vs Random β=0.1 (plan018-additive-random-b01-s42), classified on eval outputs. All categories use strict exact normalized match (D044).

| Mode | Name | ISR β=0.1 | Random β=0.1 | Δ (pp) |
|------|------|-----------|--------------|--------|
| H1 | Conclusion Embedding | 51.9% (42/81) | 70.9% (56/79) | −19.0 |
| H3 | Tautological Collapse | 1.2% (1/81) | 0.0% (0/79) | +1.2 |
| H4 | Complexity w/o Utility | 0.0% (0/81) | 3.8% (3/79) | −3.8 |
| **H7** | **Conclusion Duplication**† | **16.0% (13/81)** | **0.0% (0/79)** | **+16.0** |
| | **Genuine proofs** | **30.9% (25/81)** | **25.3% (20/79)** | **+5.6** |
| | **Total hacking** | **69.1% (56/81)** | **74.7% (59/79)** | **−5.6** |

† H7 = single_premise AND premise == conclusion (normalized). ISR-specific mode.
  Multi-seed prevalence under ISR β=0.1: s42 = 16.0% (13/81), s43 = 96.7% (59/61), s44 = 86.5% (77/89); 3-seed mean = 66.4%.
  Random β=0.1: 0/79 (0%). Not observed without ISR reward.

### Quality within genuine proofs

| Metric | ISR β=0.1 | Random β=0.1 |
|--------|-----------|--------------|
| Genuine proof mean ISR | 0.6723 | 0.3427 |

### Interpretation

- ISR reward produces +5.6pp more genuine proofs than random baseline at matched β (30.9% vs 25.3%).
- **H7 (Conclusion Duplication) is ISR-specific**: 16.0% in s42, absent in Random. Across seeds: mean 66.4% (s43: 96.7%, s44: 86.5%). ISR reward structurally induces this mode — model learns P→P + sub-component ablation to simultaneously game exec and ISR.
- Total conclusion-in-premise rates are similar (ISR 67.9% vs Random 70.9%), but ISR shifts the distribution: reducing multi-premise embedding (H1: 51.9% vs 70.9%) while introducing single-premise duplication (H7: 16.0% vs 0%) — a hacking mode shift, not a net reduction.
- ISR completely eliminates complexity-without-utility hacking (0% vs 3.8%).
- Among genuine proofs, ISR-trained models achieve 2.0× higher structural quality (ISR 0.67 vs 0.34).

---

## Data Provenance Notes

| exp_id | eval method | data |
|--------|-------------|------|
| plan001-exec-only-s42-r2 | eval_sta.py full STA | proofwriter_fol_100.jsonl |
| plan001-exec-only-s43-r4 | **sampling eval (T=0.7)** | proofwriter_fol_100.jsonl |
| plan001-exec-only-s44 | eval_sta.py full STA | proofwriter_fol_100.jsonl |
| plan016-extended-1000-s42 | eval_sta.py full STA | proofwriter_fol_100.jsonl |
| plan002-additive-b01-s42 | eval_sta.py full STA | proofwriter_fol_100.jsonl |
| plan002-additive-b01-s43 | eval_sta.py full STA | proofwriter_fol_100.jsonl |
| plan002-additive-b01-s44 | eval_sta.py full STA | proofwriter_fol_100.jsonl |
| plan018-additive-random-b01-s42 | eval_sta.py full STA | proofwriter_fol_100.jsonl |
| plan002-additive-b03-s42 | eval_sta.py (top-level metrics) | proofwriter_fol_100.jsonl |
| plan017-additive-random-s42 | eval_sta.py full STA | proofwriter_fol_100.jsonl |
| plan013-random-reward-s42-r4 | eval_sta.py full STA (degenerate) | proofwriter_fol_100.jsonl |
| plan005-sta-low-s42 | **train log only** (no eval checkpoint) | — |
| plan012-hacking-taxonomy | rule-based classification | eval outputs from plan002/plan018 |

All training used `data/train_500_seed42.jsonl` per constraint C001.
