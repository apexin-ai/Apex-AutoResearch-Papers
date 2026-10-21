# Full Results Harvest — 2026-05-22

## Part 1: nvidia-smi

**autodl-5090** (4× RTX 5090, 32GB each): ALL IDLE (0% util, 2 MiB each)

**autodl-5090-c** (4× RTX 5090, 32GB each):
- GPU 0: 85% util, 30115/32607 MiB
- GPU 1: 85% util, 30079/32607 MiB
- GPU 2: 0% util, 0/32607 MiB (idle)
- GPU 3: 76% util, 29785/32607 MiB

---

## Part 2: Finetuned N-scaling (seed=42, unified baseline)

All values: micro-F1 (%), gold-nonempty instances, 4-tuple entity match.
MV threshold: strict (>N/2). LP Δ unified baseline = samples[0] F1 from N=8.

### SciERC (529 gold-nonempty instances)

| N | Greedy F1 | MV strict F1 | MV Δ(pp) | LP-best F1 | LP Δ(pp) | Degen% | Oracle F1 |
|---|-----------|-------------|----------|------------|----------|--------|-----------|
| 8 | 66.83 | 65.58 | −1.24 | 66.51 | +3.03 | 13.4 | 78.40 |
| 16 | 66.51 | 66.22 | −0.29 | 66.35 | +2.87 | 7.6 | 81.79 |
| 32 | 66.29 | 67.06 | +0.78 | 67.08 | +3.60 | 3.6 | 83.99 |
| 64 | 66.73 | 67.35 | +0.63 | 67.12 | +3.64 | 2.1 | 86.26 |

LP Δ unified baseline = 63.48% (SciERC N=8 samples[0] F1).

### CoNLL (2756 gold-nonempty instances)

| N | Greedy F1 | MV strict F1 | MV Δ(pp) | LP-best F1 | LP Δ(pp) | Degen% | Oracle F1 |
|---|-----------|-------------|----------|------------|----------|--------|-----------|
| 8 | 91.23 | 91.01 | −0.22 | 89.81 | +1.18 | 60.1 | 95.38 |
| 16 | 91.28 | 91.48 | +0.19 | 89.18 | +0.55 | 49.7 | 96.36 |
| 32 | 91.20 | 91.66 | +0.46 | 89.23 | +0.60 | 40.5 | 96.90 |
| 64 | 91.20 | 91.84 | +0.64 | 88.89 | +0.26 | 30.6 | 97.51 |

LP Δ unified baseline = 88.63% (CoNLL N=8 samples[0] F1).

**Key observations:**
- SciERC: MV turns positive at N=32 (+0.78pp), LP-best stable around +3pp. Degen drops from 13.4%→2.1%.
- CoNLL: MV turns positive at N=16 (+0.19pp), scales to +0.64pp at N=64. LP-best modest (+0.26–1.18pp). Very high degen (60%→31%).

---

## Part 3: Finetuned N=32 multi-seed

### SciERC N=32

| Seed | Greedy F1 | MV strict F1 | MV Δ(pp) | Degen% |
|------|-----------|-------------|----------|--------|
| 42 | 66.29 | 67.06 | +0.78 | 3.6 |
| 123 | 66.63 | 66.75 | +0.12 | 5.1 |
| 456 | 66.61 | 66.44 | −0.17 | 4.0 |

Mean MV Δ: +0.24pp (unstable across seeds)

### CoNLL N=32

| Seed | Greedy F1 | MV strict F1 | MV Δ(pp) | Degen% |
|------|-----------|-------------|----------|--------|
| 42 | 91.20 | 91.66 | +0.46 | 40.5 |
| 123 | 91.23 | 91.77 | +0.55 | 37.9 |
| 456 | — | — | — | — |

Note: CoNLL N=32 seed 456 not available.

---

## Part 4: Pretrained N-scaling (seed=42)

### SciERC pretrained

| N | Greedy F1 | MV strict F1 | MV Δ(pp) | Degen% | Oracle F1 |
|---|-----------|-------------|----------|--------|-----------|
| 8 | 24.75 | 26.18 | +1.43 | 0.9 | 39.51 |
| 16 | 24.86 | 26.28 | +1.42 | 0.8 | 43.23 |
| 32 | 24.46 | 26.43 | +1.97 | 0.2 | 47.29 |
| 64 | — | — | — | — | — |

### CoNLL pretrained

| N | Greedy F1 | MV strict F1 | MV Δ(pp) | Degen% | Oracle F1 |
|---|-----------|-------------|----------|--------|-----------|
| 8 | 60.07 | 63.08 | +3.01 | 36.4 | 70.26 |
| 32 | 59.75 | 62.96 | +3.21 | 18.8 | 74.93 |
| 64 | — | — | — | — | — |

Note: Pretrained N=64 experiments (scierc/conll) not completed (empty output dirs). CoNLL pretrained N=16 not available.

**Key observations:**
- Pretrained MV gains are much larger than finetuned: SciERC +1.4–2.0pp, CoNLL +3.0–3.2pp.
- Pretrained degen is very low (SciERC <1%, CoNLL 19–36%) compared to finetuned.
- Oracle headroom is massive in pretrained (SciERC: ~20pp, CoNLL: ~10–15pp).

---

## Missing experiments

| Experiment | Status |
|-----------|--------|
| scierc_pretrained_n64_seed42 | Empty dir (5090) |
| conll_pretrained_n16_seed42 | Empty dir (5090) |
| conll_pretrained_n64_seed42 | Empty dir (5090) |
| conll_n32_seed456 | Not found |
| fewnerd_pretrained_n16/n32_seed42 | Empty dirs (5090-c) |

---

## Data provenance

| Experiment | Server | Output dir |
|-----------|--------|-----------|
| SciERC ft N=8 s42 | 5090 | scierc_mf4v2_seed42 |
| SciERC ft N=16 s42 | 5090 | exp_001_seed42_v2 |
| SciERC ft N=32 s42 | 5090 | scierc_n32_s42 |
| SciERC ft N=32 s123 | 5090 | scierc_n32_seed123 |
| SciERC ft N=32 s456 | 5090-c | scierc_n32_seed456 |
| SciERC ft N=64 s42 | 5090 | scierc_n64_seed42 |
| CoNLL ft N=8 s42 | 5090-c | conll_mf4v2_seed42 |
| CoNLL ft N=16 s42 | 5090-c | conll_n16_s42 |
| CoNLL ft N=32 s42 | 5090 | conll_n32_s42 |
| CoNLL ft N=32 s123 | 5090 | conll_n32_seed123 |
| CoNLL ft N=64 s42 | 5090 | conll_n64_seed42 |
| SciERC pre N=8 s42 | 5090-c | e2_pretrained_scierc_s42_v2 |
| SciERC pre N=16 s42 | 5090-c | scierc_pretrained_n16_seed42 |
| SciERC pre N=32 s42 | 5090-c | scierc_pretrained_n32_seed42 |
| CoNLL pre N=8 | 5090 | e2_pretrained_conll |
| CoNLL pre N=32 s42 | 5090-c | conll_pretrained_n32_seed42 |
