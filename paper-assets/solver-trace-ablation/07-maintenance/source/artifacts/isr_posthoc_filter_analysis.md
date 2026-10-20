# ISR Post-Hoc Filter Analysis

## Setup

Evaluate whether an ISR threshold τ applied as a post-hoc filter on exec-only GRPO outputs can separate genuine proofs from hacking artifacts.

**Data**: plan001 exec-only seeds s42 (CE-dominant) and s44 (TS-dominant), evaluated with eval_sta.py on proofwriter_fol_100.jsonl.

## Per-Sample Hacking Classification & ISR Distribution

### Seed s42 — 93 proved samples

| Mode | Count | ISR mean | ISR min | ISR max |
|------|------:|:--------:|:-------:|:-------:|
| CE (Conclusion Echo) | 80 | 0.107 | 0.000 | 0.750 |
| TS (Tautological Shortcut) | 1 | 0.000 | 0.000 | 0.000 |
| CI (Contradiction Injection) | 1 | 0.000 | 0.000 | 0.000 |
| PG (Premise Grafting) | 2 | 0.583 | 0.500 | 0.667 |
| Genuine | 9 | 0.289 | 0.000 | 1.000 |

### Seed s44 — 97 proved samples

| Mode | Count | ISR mean | ISR min | ISR max |
|------|------:|:--------:|:-------:|:-------:|
| TS (Tautological Shortcut) | 97 | 0.567 | 0.500 | 1.000 |

s44 exhibits 100% tautological collapse — every proved sample is a 2-component P→P proof.

## Filter Results by Seed

### Seed s42

| τ | Retained | Rate | CE filtered | Genuine filtered | Genuine retained | Precision |
|------:|--------:|:------:|--------:|--------:|--------:|--------:|
| 0.00 | 93 | 100% | 0 | 0 | 9 | 9.7% |
| 0.10 | 46 | 49.5% | 43 | 2 | 7 | 15.2% |
| 0.20 | 23 | 24.7% | 63 | 5 | 4 | 17.4% |
| 0.30 | 11 | 11.8% | 74 | 6 | 3 | 27.3% |
| 0.50 | 7 | 7.5% | 77 | 7 | 2 | 28.6% |
| 0.80 | 1 | 1.1% | 80 | 8 | 1 | 100.0% |

ISR filter removes most CE samples (CE mean ISR=0.107) but also discards genuine proofs — 6/9 genuine samples lost at τ=0.3. The filter cannot discriminate CE from low-ISR genuine proofs.

### Seed s44

| τ | Retained | Rate | TS filtered | Genuine retained | Precision |
|------:|--------:|:------:|--------:|--------:|--------:|
| 0.00 | 97 | 100% | 0 | 0 | 0.0% |
| 0.50 | 97 | 100% | 0 | 0 | 0.0% |
| 0.60 | 13 | 13.4% | 84 | 0 | 0.0% |
| 1.00 | 13 | 13.4% | 84 | 0 | 0.0% |

ISR filter is **completely ineffective** against TS. All 97 TS samples have ISR ≥ 0.5 (structural artifact: 2-component tautology where Prover9 marks 1/2 as "necessary"). No threshold ≤ 0.5 filters any TS sample; even τ=0.6 only catches 84/97.

## Conclusions

1. **ISR filters CE effectively but not selectively.** At τ=0.1, the filter removes 54% of CE samples; at τ=0.3, 93%. But it simultaneously removes 22–67% of genuine proofs, because genuine proofs can also have low ISR (mean=0.289, min=0.0).

2. **ISR is structurally blind to TS.** Tautological shortcuts (P→P) produce ISR≈0.5 by construction — Prover9 needs the single premise to execute, yielding n_necessary=1 out of n_components=2. This places TS in the same ISR band as genuine mid-quality proofs. No single threshold can separate them.

3. **Post-hoc ISR filtering alone is insufficient.** The best achievable precision on s42 is ~28% (τ=0.5), but this retains only 2/9 genuine proofs and still passes all TS samples. A useful post-hoc filter requires mode-specific classifiers (e.g., structural tautology detection for TS, conclusion-in-premises check for CE) rather than a single ISR threshold.
