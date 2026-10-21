# eval_sta.py Full STA Evaluation Comparison
Date: 2026-05-14
Eval data: proofwriter_fol_100.jsonl (100 samples)
Solver: Prover9Solver

## Summary Table

| Experiment | Reward Type | Seed | Prove Rate | Mean ISR | ISR Std | Proved-only ISR | Median ISR | Time/sample |
|---|---|---|---|---|---|---|---|---|
| plan001-s42-r2 | exec-only | 42 | **93.0%** | 0.1232 | 0.1887 | 0.1324 | 0.000 | 2.4s |
| plan013-s42-r4 | random reward | 42 | 100.0%† | 0.5350† | 0.1282 | 0.5350† | 0.500 | 0.9s |
| plan001-s43-r4 | exec-only | 43 | 13.0%‡ | 0.0000 | 0.0000 | 0.0000 | 0.000 | 11.0s |

† **DEGENERATE**: plan013 generates trivial 2-component proofs (1 premise = conclusion assertion + conclusion). ISR=0.500 is a fixed artifact, not meaningful quality.
‡ **SEVERELY DEGRADED**: 87% of samples hit max_new_tokens. Training PR (last100)=0.883 but eval PR=0.13.

## By Answer Type

### plan001-s42-r2 (exec-only, seed=42)
| Type | Count | Proved | Prove Rate | Mean ISR |
|---|---|---|---|---|
| false | 25 | 23 | 92.0% | 0.0817 |
| unknown | 41 | 39 | 95.1% | 0.1550 |
| true | 34 | 31 | 91.2% | 0.1153 |

### plan013-s42-r4 (random reward)
| Type | Count | Proved | Prove Rate | Mean ISR |
|---|---|---|---|---|
| false | 25 | 25 | 100% | 0.5600 |
| unknown | 41 | 41 | 100% | 0.5366 |
| true | 34 | 34 | 100% | 0.5147 |

### plan001-s43-r4 (exec-only, seed=43)
| Type | Count | Proved | Prove Rate | Mean ISR |
|---|---|---|---|---|
| false | 25 | 5 | 20.0% | 0.0000 |
| unknown | 41 | 4 | 9.8% | 0.0000 |
| true | 34 | 4 | 11.8% | 0.0000 |

## Key Findings

### 1. plan013 (random reward) = Reward Hacking
The random reward model collapses to a degenerate proof strategy:
- Every proof has exactly 2 components: `premise=conclusion_fact` + `conclusion=conclusion_fact`
- This trivially passes the solver (conclusion appears in premises)
- ISR = 1/2 = 0.500 is a fixed artifact of this pattern
- Generation is extremely fast (0.9s/sample) because outputs are very short
- PR=100% because every proof is trivially valid

**Implication**: Without meaningful ISR signal, the model learns to "hack" the execution reward by generating the shortest possible valid proof — just assert the conclusion as a premise.

### 2. plan001-s42 (exec-only, seed=42) = Best Real Model
- High prove rate (93%) with genuine multi-premise formalizations
- ISR=0.1232 reflects real (but noisy) formalizations with many unnecessary premises
- Average 7+ components per proof, 1-2 necessary
- Generation time 2.4s reflects real FOL generation

### 3. plan001-s43 (exec-only, seed=43) = Training Instability
- Severe eval degradation: training PR=88.3% but eval PR=13%
- All ISR=0.000 — model generates unparseable/long outputs hitting max_new_tokens
- 11.5s generation (= max_new_tokens reached) on 87% of samples
- This suggests significant seed sensitivity or training instability for exec-only

### 4. Cross-Seed Stability: POOR
plan001-s42 (93% PR) vs plan001-s43 (13% PR) shows extreme variance across seeds.
This is a critical finding: the exec-only reward landscape may have high-variance optima.

## Reference: plan003 (100-step checkpoint, prior eval)
- prove_rate=0.32, mean_isr=0.2055, proved_only_isr=0.6423
- Higher proved_only_ISR (0.64 vs 0.13) at 100 steps suggests ISR degrades as model overfits to execution reward
