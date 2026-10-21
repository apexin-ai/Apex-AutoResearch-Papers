# Table 1: Ablation Results — Reward Shaping for Solver Trace Alignment

**Model**: Qwen3-4B | **Training**: GRPO, 500 steps, K=8 | **Data**: train_500_seed42.jsonl | **Eval**: proofwriter_fol_100.jsonl via eval_sta.py (full STA)

## Main Comparison Table

| Experiment | Reward Formula | Eval PR ↑ | Eval ISR ↑ | Proved-Only ISR | Components | Collapse | Mode |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Base Model (no training) | — | 0.12 | 0.064 | — | — | — | baseline |
| Exec-Only 100-step (s42) | r_exec | 0.32 | 0.206 | 0.642 | — | No | genuine |
| **Exec-Only 500-step (s42)** | **r_exec** | **0.93** | **0.123** | **0.132** | **7.08** | **No** | **genuine** |
| Exec-Only (s43) | r_exec | 0.14\* | 0.0\* | — | — | — | degraded |
| Exec-Only (s44) | r_exec | 0.98 | 0.57† | 0.582† | 2.04 | **Yes** | tautological |
| **Additive ISR β=0.1 (s42)** | **r_exec(1+0.1·ISR)** | **0.81** | **0.337** | **0.415** | **5.58** | **No** | **genuine** |
| Additive ISR β=0.3 (s42) | r_exec(1+0.3·ISR) | 0.18 | 0.026 | 0.143 | — | No | PR collapse |
| Convex ISR α=0.9 (s42) | 0.9·r_exec+0.1·STA | 0.77‡ | 0.230‡ | — | — | No | genuine (depressed) |
| Convex Random (s42) | 0.9·r_exec+0.1·rand | 1.00 | 0.535† | 0.535† | ~2 | **Yes** | tautological |
| **Additive Random β=0.1 (s42)** | **r_exec(1+0.1·rand)** | **0.79** | **0.104** | **0.131** | **8.46** | **No** | **redundant premises** |
| Additive Random β=0.3 (s42) | r_exec(1+0.3·rand) | 0.48 | 0.045 | 0.094 | 9.6 | No | complexity w/o utility |
| 1000-step Extended (s42) | r_exec (1000 steps) | 0.96 | 0.003 | 0.003 | 18.55 | No | contradiction explosion |

### Annotations

- **†** Tautological artifact — ISR inflated by trivial 2-component proofs (premise=conclusion). Not genuine structural alignment.
- **\*** Sampling eval (T=0.7), not eval_sta.py full STA. Cross-seed instability: 87% samples hit max_new_tokens limit.
- **‡** Training log metrics only (checkpoint deleted before eval_sta.py). Last-100-step window averages, not held-out eval.
- **Bold rows** = primary comparison pair (exec-only baseline vs best additive ISR).
- Components = mean number of FOL components per proof. 2.0 indicates tautological collapse.
- Collapse = tautological collapse detected (≥90% proofs with ≤2 components).

## Key Findings

### 1. Exec-Only Baseline Exhibits Reward Hacking
Exec-only s42 achieves PR=93% but ISR=12.3% — the model learns to prove theorems without structurally aligned reasoning. ISR barely exceeds the untrained base model (6.4%).

### 2. Cross-Seed Instability in Exec-Only
Three seeds produce three distinct failure modes: genuine (s42, PR=93%), degraded (s43, PR=14%), and tautological collapse (s44, PR=98% but ISR=0.57 is artifact).

### 3. Additive ISR β=0.1 is the Best Operating Point
PR=81% (-12pp vs exec-only) with ISR=33.7% (2.73× exec-only). Mean 5.58 components per proof, no tautological collapse. Acceptable PR trade-off for genuine structural alignment.

### 4. β=0.3 Causes PR Collapse
Tripling the ISR bonus weight collapses PR from 81%→18%. The ISR signal overwhelms the execution reward.

### 5. Random Reward Controls Confirm ISR Signal is Informative
- **Additive random β=0.1** (r_exec(1+0.1·rand)): PR=79% matches ISR β=0.1 (81%), but ISR=10.4% vs 33.7% — ISR reward provides 3.2× structural advantage over matched random control at same β dose.
- **Additive random β=0.3** (r_exec(1+0.3·rand)): No tautological collapse but ISR=4.5%. Model generates complex formalizations (9.6 components) that are structurally useless — "complexity without utility."
- **Convex random** (0.9·r_exec+0.1·rand): Tautological collapse — same failure mode as exec-only s44. Random noise in convex form doesn't prevent degenerate solutions.
- Both controls confirm that ISR improvements in plan002-additive-b01-s42 are driven by meaningful STA signal, not noise.

### 6. Extended Training Worsens ISR Collapse (1000 Steps)
At 1000 steps, exec-only achieves PR=96% but ISR collapses to 0.3% (vs 13.2% at 500 steps, a 97.8% drop). Component count triples to 18.55 with 94.8% of proofs having zero necessary components — contradiction explosion rather than tautological collapse. The ISR trajectory is monotonically decreasing: 0.11 (steps 101-200) → 0.04 (401-500) → 0.02 (601-700) → 0.01 (901-1000). No recovery signal.

### 7. Training Dynamics (100-step Snapshot)
At 100 steps, proved-only ISR=0.64 but PR=32%. Early training maintains high structural quality per solved problem, but solve rate is low. By 500 steps, PR rises to 93% while ISR drops to 13% — the model trades structural alignment for solve rate.

## Reward Formula Reference

| Label | Formula | Type |
|:---|:---|:---|
| Exec-Only | r = r_exec ∈ {0, 1} | Baseline |
| Additive ISR β | r = r_exec × (1 + β × ISR) | Multiplicative bonus |
| Convex ISR α | r = α × r_exec + (1−α) × STA | Linear interpolation |
| Additive Random β | r = r_exec × (1 + β × U[0,1]) | Noise control |
| Convex Random α | r = α × r_exec + (1−α) × U[0,1] | Noise control |
