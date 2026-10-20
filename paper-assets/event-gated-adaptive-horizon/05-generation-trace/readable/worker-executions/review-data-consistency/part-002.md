# review data consistency — Part 2 of 2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../review-data-consistency.md) · [Structured JSON](../../../sessions/d5/d5df406346b781b9504d.json)

## Round 2

### Tool result

_source line 134 · 2026-05-24T02:18:42.297Z_

<details><summary>↩ Tool result · `toolu_015tp1CEMzPpFQ1WtejthEt9`</summary>

```text
Here is the comprehensive audit of every quantitative claim, organized by file.

---

## main.tex

**Line 27:** `\sgseval{448.3}` — SGS eval value = 448.3
**Line 28:** `\sgsnve{1.66}` — SGS NVE value = 1.66
**Line 29:** `\sgsclaim{...}` — "0/3 across environments" (CIVO elimination rate)

---

## abstract_body.tex

**Line 1:**
- `14--30\%` — degradation range of all variable-rate configs relative to baseline
- `26/29` — NVE classifier accuracy (any CIVO across all configs)
- `AUROC = 0.953` — NVE classifier AUC (in-sample)
- `2.78\times` — RSSM reward prediction gap at dt>1
- `\rho > 0.999` — dual critic correlation in pure imagination
- `100\%` sensitivity for NVE detector

---

## introduction.tex

**Line 6:**
- `14--19\%` of baseline — performance degradation range (note: abstract says 14--30%; introduction says 14--19%)
- `2.78\times` — RSSM reward prediction gap at dt>1 vs dt=2
- `26/29` — NVE classification accuracy
- `n=29` — sample size for NVE evaluation
- `AUROC = 0.953` — in-sample
- `LOEO cross-validated` — mean AUROC = 0.981 (reference to Appendix Table)
- `38--49\%` — reward head gradient share of ∇θ e_dt
- `16--22\%` — observation decoder gradient share

**Line 12 (Contributions):**
- `6/6 seeds` — CIVO from trained dt-embedding + multi-rate exposure
- `two locomotion environments`
- `AUROC = 0.953` in-sample, LOEO cross-validated
- Three manipulation tasks with frozen-embedding controls

**Line 14:**
- `38--49\%` — reward head gradient share; reward-only stopping fails
- `\rho > 0.999` — dual critics converge

**Line 15:**
- `100\%` sensitivity
- `5/5` — NVE detector sensitivity
- `2/5` — predictive warning cases

---

## methodology.tex

**Line 7:**
- `32 categories × 32 classes` — RSSM discrete latent states
- `H=15` — default imagination horizon
- `dt=1` — standard temporal resolution

**Lines 16-21:**
- `d=32` — temporal embedding dimensionality (trained, frozen modes)

**Line 27:**
- `H=15` (default) and `H=8` — tested horizons
- `H=8 at dt=2` covers `16` physical time steps vs. `15` for default

**Line 32:**
- `12 conditions` in factorial design
- `4 seeds` per key configuration

**Line 38:**
- `35K+` window for NVE computation
- `505K steps` — baseline reference (exp_001, seed 1)
- `26/29` accuracy
- `AUROC = 0.953` in-sample
- LOEO mean `AUROC = 0.981`

**Line 48:**
- TCN noise: `σ ∈ {0.5, 0.2}`, three environments
- RAVE clips: `c ∈ {2.0, 1.5}`

**Line 53:**
- Narrow critic: `~1.2M` parameters
- Wide critic: `~2.4M` parameters

**Line 58:**
- Baseline runs: `500K steps`, peak return `970.4`
- Treatments run: `105K steps`
- `d=32` temporal embedding
- `~80 GPU-hours` total on single NVIDIA RTX PRO 6000

---

## results.tex

**Line 4:** Treatments run to `105K` steps; baseline to `505K` steps; eval = mean over `10 episodes`

**Table 1 (tab:main_results, lines 20-35):**

| Exp | Config | dt_emb | Sub | H | Eval@final | NVE |
|-----|--------|--------|-----|---|-----------|-----|
| 001 | Baseline | --- | --- | 15 | 915.7 @105K | 1.00× |
| 008d | Factorial s1 | trn | ON | 8 | 82.8 @55K | 4.12× |
| 008f | No dt_emb s1 | --- | ON | 8 | 503.0 @105K | 0.97× |
| 008a | Unexposed emb | exp | OFF | 15 | 777.7 @105K | 0.93× |
| 015b | Frozen emb | frz | ON | 8 | 204.2 @105K | 1.45× |
| 022b | Frozen emb+Gumbel | frz | ON | 8 | 300.7 @105K | 0.63× |
| 010b | Cheetah Run | trn | ON | 8 | 51.7 @105K | 8.27× |
| 019b | PickCube-v1 | trn | ON | 8 | 26.64 @200K | 3.78× (^c) |
| 049 | StackCube-v1 | trn | ON | 8 | 34.9 @212K | 5.05× (^d) |
| 050 | PegInsertionSide-v1 | trn | ON | 8 | 20.86 @212K | 10.05× (^e) |
| 046 | Cheetah Run frz | frz | ON | 8 | --- | 1.35× |

**Footnote ^d (line 45):** frozen control (exp_051) exhibits peak `4.30×` at `42.5K`, self-correcting by `82.5K`

**Footnote ^e (lines 46):**
- Seed 0 trained peaks at `10.05×` (`82.5K`) with delayed self-correction
- Seed 1 trained (exp_055) peaks at `3.08×` (`92.5K`), final `0.50×`
- Seed 1 frozen (exp_056) peaks at `11.32×` (`82.5K`), final `1.19×`

**F1 (line 56):**
- Baseline reaches `915.7` at 105K
- Fixed dt=2 (006): peaks at `485.3` before collapsing to `132.9` (`14%` of baseline)
- Fixed dt=4 (007): never exceeds `176.9` (`19%`)
- Learned gate (005): collapses to `98.8` (`11%`)

**F2 (line 72):**
- 008d: NVE = `4.12×` (eval 82.8) vs. 008f: NVE ≤ `0.97×` (eval 503.0)
- `26/29` across two environments, `AUROC = 0.953`

**Line 77 (figure caption):** Walker Walk, `n=3` seeds plotted; seed 4 data in Table

**Line 81:**
- Peak NVEs: `4.62×`, `4.12×`, `1.62×`, `1.53×` (4 Walker Walk seeds)
- All below `30%` of baseline
- IQM `175.2`, mean `170.6`, `n=4`
- One self-corrects to `29.3%` of baseline
- `n=6` seeds total across two environments; `5/6` progressing toward collapse

**F3-F5 (line 90):**
- 008a (3 seeds): peak NVE `0.83--0.93×`
- 008f (3 seeds): peak NVE ≤ `1.41×`
- Frozen NVE range: `0.19--1.71×` vs. trained `1.53--4.62×`
- 3/4 seeds below threshold, 1/4 transient self-correcting
- Partial gradient blocking (exp_044): peak NVE `4.45×`, final eval `538`, `59%` baseline
- Degradation: `-47%` at dt=2, `-81%` at dt=4

**ManiSkill manipulation (line 93):**
- StackCube trained (049/052): NVE `5.05×/4.67×`, frozen (051): `4.30×`, all self-correcting by `82.5K`
- PegInsertionSide: high-amplitude `4--11×`; seed 0 trained `10.05×` vs. frozen `1.82×`; seed 1 reverses: frozen `11.32×` vs. trained `3.08×`
- PickCube frozen control (exp_054): peak `8.81×` at `62.5K`, self-correcting

**F6 (line 103):**
- Exp_008e_v3: 2/4 seeds collapse (`50%`)
- Pathway A (CIVO): NVE = `4.02×`
- Pathway B (entropy increase): NVE = `3.78×`; 2 seeds only

**F7 (line 106):**
- Full-SGS (exp_018): seed 1 eval `448.3`, NVE `1.66×`; seed 2 collapsed (0/2 elimination)
- Cheetah (010b): NVE `8.27--108.52×`; full-SGS: 0/3 elimination
- Removing embedding on Cheetah (024b): NVE `<0.2×`

**Obs-decoder-only SGS (line 109):** `1/6` CIVO prevention (`1/4` Walker, `0/2` Cheetah)

**Table: Intervention hierarchy (lines 121-148):**

| Level | Intervention | Seeds | Prev. | Rate |
|-------|-------------|-------|-------|------|
| --- | Untreated | 6 | 0/6 | 0% |
| Gradient | Reward-only SGS | 2 | 0/2 | 0% |
| Gradient | Full-pathway SGS | 3 | 0/3 | 0% |
| Gradient | Obs-decoder SGS | 6 | 1/6 | 17% |
| Output | RAVE (c=1.5,2.0) | 2 | 0/2 | 0% |
| Repr. | TCN (σ=0.1) | 1 | 1/1†† | 100% |
| Repr. | TCN (σ=0.2) | 6† | 2/6 | 33% |
| Repr. | TCN (σ=0.5) | 3 | 0/3 | 0% |
| Repr. | TCN (σ=1.0) | 1 | 1/1§ | 100% |
| Arch. | Wide single | 2 | 0/2 | 0% |
| Arch. | Narrow dual (min) | 2 | 0/2 | 0% |
| Arch. | Wide dual (min) | 4 | 3/4‖ | 75% |
| --- | Embedding frozen | 7 | 5/7# | 71% |
| --- | Embedding removed | 5 | 5/5 | 100% |

Footnotes:
- †Walker 2/4 (s2 NVE `2.11×`; s3 late-onset NVE `3.04×` at 105K); Cheetah 0/1, PickCube 0/1
- ††Borderline (NVE = `1.02×`, eval `55%`)
- §CIVO prevented but progressive policy erosion (peak `116%`, final `15%` baseline)
- ‖Walker 3/3 (NVE ≤ `1.4×`; `1/3` non-CIVO eval collapse), Cheetah 0/1
- #Walker 5 + Cheetah 2; Exp_047 (NVE `1.71×`) and Exp_057 (NVE `1.88×`): both transient, self-correcting within `20K` steps; remaining 5 seeds: NVE `0.19--1.45×`

**Forward-pass interventions (line 157):**
- TCN at σ=0.2: 2/4 Walker seeds suppressed, NVE `<1.0×`, eval `45--91%`

**Architecture-level (line 167):**
- `n=7` dual-critic configs: `ρ > 0.999`, pessimism at `3--4%` of independent-critic bound

**Recovery ratios (line 170):**
- Narrow dual: `~16--19×` recovery ratio
- Wide dual: NVE ≤ `1.4×`, `3/3` prevention, `1/3` non-CIVO collapse

**Online CIVO Detection (line 179):**
- 14 runs across 3 environments
- TPR = `5/5`, FPR = `2/9`
- Predictive alerts in `2/5` cases

---

## analysis.tex

**Line 5:**
- `2.78×` reward prediction gap (Table ref)
- Reward head: `38--49%` of ∇θ e_dt; fails when blocked alone
- Observation decoder: `16--22%`
- Full-pathway SGS: `0/3`

**Line 8 (Practitioner guidelines):**
- NVE diagnostic: ≥ `1.5×`, AUROC = `0.953`
- Frozen converts sustained CIVO (`4/4` trained, NVE `1.53--108×`) to transient spikes (`2/3` frozen Walker, `1.71--1.88×`)
- Self-correct within `20K` steps
- Extreme CIVO: `70.6×` causes irrecoverable damage

**Line 11:**
- Manipulation peaks: `4--11×`, but frozen controls show comparable/higher peaks

---

## appendix.tex — Complete Results (tab:complete_results, lines 17-91)

All 42 experiments (key additional values beyond the main table):

| Exp | Config | NVE | Eval | Step |
|-----|--------|-----|------|------|
| 001 s2 | Baseline s2 | --- | 443.5 | @105K |
| 006 | Fixed dt=2 | 4.83× | 132.9 | @65K |
| 007 | Fixed dt=4 | --- | 152.5 | @55K |
| 005 | Learned gate | --- | 98.8 | @145K |
| 009b | Factorial s2 | 1.62× | 267.9 | @105K |
| 008d_s3 | Factorial s3 | 1.53× | 268◇ | @105K |
| 008d_s4 | Factorial s4 | 4.62× | 63.6 | @105K |
| 008f s4 | No dt_emb s4 | 1.41× | 306.5 | @105K |
| 009c s3 | No dt_emb s3 | 1.04× | 311.9 | @105K |
| 008a_s1 | Unexposed emb | 0.83× | 630.9 | @105K |
| 008a_s2 | Unexposed emb | 0.89× | 899.4 | @105K |
| 042 | Frozen emb (dedicated) | 0.19× | 612.0 | @105K |
| 057 | Frozen emb s2 | 1.88× | --- | |
| 018 s1 | Full-SGS | 1.66× | 448.3 | @105K |
| 018 s2 | Full-SGS | --- | 40.8 | @105K |
| 008e_v3 s1 | Mitigation | 0.94× | 869.9 | @105K |
| 008e_v3 s2† | Mitigation | 3.78× | 137.0 | @105K |
| 008e_v3 s3 | Mitigation | 4.02× | 92.7 | @105K |
| 008e_v3 s4 | Mitigation | 0.99× | 899.3 | @105K |
| 010b_s0 | Cheetah Run | 108.52× | 0.83 | @105K |
| 021 | Cheetah Run SGS | 9.94× | 221.5 | @105K |
| 024b s0 | Cheetah no emb | <0.20× | 96.5 | @105K |
| 024b s1 | Cheetah no emb | 0.10× | 77.3 | @105K |
| 008a_ch s0 | Cheetah unexposed | 1.08× | 532.4 | @105K |
| 008a_ch s1 | Cheetah unexposed | 1.29× | 504.4 | @105K |
| 054 | PickCube frz | 8.81×^h | --- | |
| 052 | StackCube trn | 4.67× | --- | |
| 051 | StackCube frz | 4.30× | 30.7 | @155K |
| 053 | PegInsertion frz | 8.10× | 5.89 | |
| 055 | PegInsertion trn | 3.08× | 11.44 | @212K |
| 056 | PegInsertion frz | 11.32× | 4.37 | @212K |
| 058 | Cheetah frz | 0.23× | 80.46 | @215K |

Footnote ^h: PickCube frozen control peak `8.81×` at `62.5K`, self-correcting to `0.55×` at `72.5K`
Footnote ^d: Peak NVE `9.94×` at `45K`, transient, self-correcting to `<1×` by `55K`
Footnote ^g: Seed 0 trained peaks at `10.05×` (`82.5K`); seed 1 trained peaks at `3.08×` (`92.5K`), final `0.50×` at `212.5K`; seed 1 frozen peaks at `11.32×` (`82.5K`), final `1.19×` at `212.5K`

**Cross-domain table (tab:cross_domain, lines 103-108):**
| Domain | Environment | Trained | Frz ctrl | dt-emb-dep. CIVO |
|--------|-------------|---------|----------|-----------------|
| Locomotion | Walker Walk | 4/4 | 0/3 | Yes (NVE 1.53--4.62×) |
| Locomotion | Cheetah Run | 2/2 | 0/2 | Yes (NVE 8.27--108.5×) |
| Manipulation | StackCube-v1 | 0/2 | 0/1 | No |
| Manipulation | PegInsertionSide | 0/2 | 0/2 | No |
| Manipulation | PickCube-v1 | 0/1 | 0/1 | No |

**NVE Sensitivity Tables (lines 148-210):**

Task B1 (n_pos=3, n_neg=7, n=10, AUROC=1.000):
| Threshold | TP | FP | FN | TN | Accuracy | Precision | Recall | F1 |
|-----------|----|----|----|----|----------|-----------|--------|-----|
| ≥1.0× | 3 | 3 | 0 | 4 | 70.0% [34.8,93.3] | 50.0% | 100% | 66.7% |
| ≥1.2× | 3 | 2 | 0 | 5 | 80.0% [44.4,97.5] | 60.0% | 100% | 75.0% |
| ≥1.5× | 3 | 2 | 0 | 5 | 80.0% [44.4,97.5] | 60.0% | 100% | 75.0% |
| ≥1.7× | 3 | 1 | 0 | 6 | 90.0% [55.5,99.7] | 75.0% | 100% | 85.7% |
| ≥2.0× | 3 | 1 | 0 | 6 | 90.0% [55.5,99.7] | 75.0% | 100% | 85.7% |
| ≥3.9× | 3 | 0 | 0 | 7 | 100% [69.2,100] | 100% | 100% | 100% |

Task B2 (n_pos=4, n_neg=6, n=10, AUROC=0.958):
| Threshold | TP | FP | FN | TN | Accuracy | Precision | Recall | F1 |
|-----------|----|----|----|----|----------|-----------|--------|-----|
| ≥1.0× | 4 | 2 | 0 | 4 | 80.0% [44.4,97.5] | 66.7% | 100% | 80.0% |
| ≥1.2× | 4 | 1 | 0 | 5 | 90.0% [55.5,99.7] | 80.0% | 100% | 88.9% |
| ≥1.5× | 4 | 1 | 0 | 5 | 90.0% [55.5,99.7] | 80.0% | 100% | 88.9% |
| ≥1.7× | 3 | 1 | 1 | 5 | 80.0% [44.4,97.5] | 75.0% | 75.0% | 75.0% |
| ≥2.0× | 3 | 1 | 1 | 5 | 80.0% [44.4,97.5] | 75.0% | 75.0% | 75.0% |
| ≥3.9× | 3 | 0 | 1 | 6 | 90.0% [55.5,99.7] | 100% | 75.0% | 85.7% |

Task B2 full (n_pos=8, n_neg=8, n=16, AUROC=0.969):
| ≥1.0× | 8 | 2 | 0 | 6 | 87.5% [61.7,98.4] | 80.0% | 100% | 88.9% |
| ≥1.2× | 8 | 1 | 0 | 7 | 93.8% [69.8,99.8] | 88.9% | 100% | 94.1% |
| ≥1.5× | 8 | 1 | 0 | 7 | 93.8% [69.8,99.8] | 88.9% | 100% | 94.1% |
| ≥1.7× | 6 | 1 | 2 | 7 | 81.3% [54.4,96.0] | 85.7% | 75.0% | 80.0% |
| ≥2.0× | 6 | 1 | 2 | 7 | 81.3% [54.4,96.0] | 85.7% | 75.0% | 80.0% |
| ≥3.9× | 6 | 0 | 2 | 8 | 87.5% [61.7,98.4] | 100% | 75.0% | 85.7% |

**NVE Raw Values Table (tab:nve_raw, lines 130-141):**
- 006: NVE = `4.83`
- 008d: NVE = `4.13`
- 008e_v3_s3: NVE = `4.02`
- 008e_v3_s2: NVE = `3.78`
- 009b: NVE = `1.62`
- 001: NVE = `1.00`
- 008e_v3_s4: NVE = `0.99`
- 008f: NVE = `0.97`
- 008e_v3_s1: NVE = `0.94`
- 008a: NVE = `0.93`

**LOEO cross-validation (tab:nve_loeo, lines 286-292):**
| Held-out | N_train | N_test | θ_opt range | Test Accuracy | Test AUROC |
|----------|---------|--------|-------------|--------------|-----------|
| PickCube | 18 | 2 | (1.45, 1.53] | 2/2 (1.000) | 1.000 |
| Cheetah | 15 | 5 | (1.45, 1.53] | 5/5 (1.000) | 1.000 |
| Walker | 7 | 13 | (1.00, 3.78) | 12/13 (0.923) | 0.944 |
| **Mean** | — | — | — | **0.974** | **0.981** |

**Baseline seeds table (tab:baseline_seeds, lines 253-259):**
| Seed | Eval@105K | Eval@505K | ve@65K | ve@105K |
|------|-----------|-----------|--------|---------|
| s1 | 915.7 | 970.4 | 0.563 | 0.656 |
| s2 | 443.5 | 945.7 | 0.898 | 0.742 |
| s3 | 869.0 | 947.7 | --- | 0.664 |
| s4 | 922.8 | 938.9 | --- | 0.624 |

**NVE normalization robustness (line 264):**
- Single-seed (s1): AUROC = `0.933`, accuracy `7/8` (`87.5%`)
- Four-seed mean: AUROC = `0.867`, accuracy `6/8` (`75.0%`)
- Boundary case 009b: NVE flips from `1.62×` (s1) to `1.23×` (4-seed mean) at peak at `45K`
- s1 v/e ratio at 45K: `0.331`; 4-seed mean: `0.436`
- 006 NVE: `4.84× → 4.52×`; 008d NVE: `4.13× → 3.54×`

**Normalization conventions (line 266):**
- Walker: 4-seed mean baseline (seeds 1--4, each to `505K+` steps)
- Cheetah: 5-seed mean baseline (seeds 0--4, each to `~210K` steps)

**Factorial Appendix (line 319 — tab:three_way_emb):**
| Condition | Grad flow | Exp(s) | NVE peak | Eval | CIVO |
|-----------|-----------|--------|----------|------|------|
| Trained | all | 008d | 1.53--4.62× | 64--268 | 4/4 |
| Reward detach | obs+KL only | 044 | 4.45× | 44→538† | 1/1 |
| Full SGS | KL only | 018 | 1.66× | 448 | 1/1* |
| Frozen | none | 042,015b,047,057 | 0.19--1.88×‡ | 204--612 | 2/4 |
| Removed | N/A | 008f | 0.97--1.41× | 307--503 | 0/3 |

†Self-corrected at ~175K (eval 44→538, 59% baseline; 224K run)
‡Exp_047 (NVE 1.71×) and Exp_057 (NVE 1.88×): transient, self-correcting within 20K steps

**F3 Evidence A (line 382):**
- 008a: NVE `0.83--0.93×`, eval `777.7` at 105K (`85%` of baseline)
- 006 NVE accelerates from `1.61×` at 45K to `2.31×` at 55K before collapse to `132.9` at 65K

**F3 Evidence B (line 385):**
- 015b NVE trajectory: `0.81 → 1.26 → 1.45 → 0.65 → 1.05 → 0.47 → 0.39 → 0.42`
- Peaks at `1.45×` at 55K, retreats to `0.65×` by 65K, settles at `0.42×` by 105K, final eval `204.2`

- 008d trajectory: `1.78 → 1.71 → 2.09 → 4.12×`, eval `82.8`

**Cross-environment (line 391):**
- Cheetah exp_010b: `2 seeds`, NVE `8.27--108.52×`, collapse to `51.7/0.83`
- exp_024b: `2 seeds`, NVE `<0.2×`, eval `96.5/77.3`
- Freezing on Cheetah (exp_046): NVE `1.35×` vs. trained `70.64×` — `52×` reduction

**F4 (line 426):**
- dt=1 (baseline): `915.7` at 105K
- Fixed dt=2 (006): peak `485.3` (`-47%`)
- Fixed dt=4 (007): peak `176.9` (`-81%`)

**F5 (line 431):**
- 008a: `777.7` vs. 008c: `240.9` — `3.2×` performance gap (horizon effect, healthy NVE ≤ `0.93×`)
- 008f: `503.0` vs. 009c: `148.3` — cross-seed variance

**RSSM Fidelity Table (tab:rssm_fidelity, lines 463-468):**
| Config | obs_MSE dt=1 | obs_MSE dt=2 | Gap | reward_MAE dt=1 | reward_MAE dt=2 | Gap |
|--------|-------------|-------------|-----|----------------|----------------|-----|
| Baseline | 13.49 | 27.50 | 2.04× | 0.0102 | 0.0159 | 1.56× |
| 008d (trained) | 41.31 | 53.67 | 1.30× | 0.0568 | 0.1579 | 2.78× |
| 008f (no emb) | 8.01 | 22.04 | 2.75× | 0.7469 | 0.7526 | 1.01× |

**CIVO mechanism (line 475):**
- Random policy: dt=2 imagination produces `1.68×` higher mean reward than dt=1 (Stage 1)
- Trained actor amplifies to `2.90×` (Stage 2)
- No-embedding control: random policy ratio `1.11×`, trained-actor ratio `0.98×`
- Stage 1 contributes `~36%`, Stage 2 `~64%` of total effect

**Signed reward error table (tab:signed_error, lines 492-499):**
| Config | dt | Mean SE | Std | %Over | Actual | Pred |
|--------|-----|---------|-----|-------|--------|------|
| Baseline | 1 | +0.001 | 0.023 | 39.6% | 1.893 | 1.894 |
| 008d | 1 | +0.018 | 0.072 | 61.8% | 0.361 | 0.379 |
| 008d | 2 | **-0.599** | 0.722 | 8.0% | 0.721 | 0.121 |
| 008f | 1 | -0.710 | 0.704 | 14.0% | 0.921 | 0.211 |
| 008f | 2 | -1.645 | 1.485 | 5.0% | 1.840 | 0.195 |

**Gradient decomposition table (tab:gradient_decomposition, lines 532-536):**
| Loss component | @55K share | @112K share |
|----------------|-----------|------------|
| Reward head | 49.0% | 38.1% |
| KL dynamics | 34.7% | 40.4% |
| Observation decoders | 16.3% | 21.5% |

**Exp_016e (line 517):**
- Peak eval `326.7` at 75K steps, decline to `31.7` at 95K, NVE `10.42×`

**Entropy (line 572):** all configs start at `~8 nats`, converge to `~-4.5 to -5`

**016e vs 008d timing (line 579):**
- Collapse onset: `75K` (016e) vs. `25K` (008d)
- Peak eval: `326.7` (016e) vs. `167.2` (008d)

**Post-CIVO outcomes table (tab:post_civo, lines 594-601):**
| Env | Seed | Peak | Final | Eval | Outcome |
|-----|------|------|-------|------|---------|
| Walker | s1 (008d) | 4.12× | 4.12× | 82.8 | Full collapse |
| Walker | s2 (009b) | 1.62× | 0.38× | 267.9 | Transient CIVO |
| Walker | s3 (008d_s3) | 1.53× | 1.53× | 268◇ | Late-onset collapse |
| Walker | s4 (008d_s4) | 4.62× | 4.62× | 63.6 | Full collapse |
| Cheetah | s1 (010b) | 8.27× | 8.27× | 51.7 | Full collapse |
| Cheetah | s0 (010b_s0) | 108.52× | 108.52× | 0.83 | Full collapse |

Full collapse majority: `5/6` seeds; one self-correction (Walker s2) at `29.3%` of baseline

**Obs-decoder SGS seed 3 (line 610):**
- Healthy through `105K` (NVE `<1.0×`, eval `818.6`)
- CIVO onset at `135K` (NVE `5.47×`, eval `67.0`)
- Evaluation recovery: `590.2` at `215K`, `64%` of baseline
- Persistent value collapse: NVE `0.14×`, value mean `80.6`
- Seed 4 same terminal value collapse: NVE `0.14×` at `215K`, eval `242`

**Embedding dilemma (line 645):**
- Removing embedding (008f): `13×` cost to reward prediction quality (`0.7469` vs. `0.0568` MAE)

**TCN full table (tab:tcn_full, lines 679-699):**
| Env | σ | Seed | NVE_max | Prevented? | Eval % |
|-----|---|------|---------|-----------|--------|
| Walker | 0.1 | s0 | 1.02 | ✓* | 55% |
| Walker | 0.2 | s0 | 0.91 | ✓ | 91% |
| Walker | 0.2 | s1 | 0.64 | ✓ | 45% |
| Walker | 0.2 | s2 | 2.11† | ✗ | ~5% |
| Walker | 0.2 | s3 | 3.04¶ | ✗ | 11% |
| Walker | 0.5 | s0 | 3.97 | ✗ | 27% |
| Walker | 0.5 | s1 | 1.64 | ✗ | 41% |
| Cheetah | 0.2 | s0 | 1.90 | ✗ | crashed |
| Cheetah | 0.5 | s0 | 10.67 | ✗ | 26% |
| Cheetah | 1.0 | s0 | ≤0.30 | ✓§ | 15% |
| PickCube | 0.2 | s0 | 3.71 | ✗ | failing |

¶Late-onset CIVO: NVE declined to `0.67×` at 95K before spike to `3.04×` at 105K; eval `349.6` at 95K → `71.8` at 105K → `104.5` at 215K

**Cheetah σ=0.5 (line 703):** transient CIVO spike NVE = `10.67×` at `55K`, NVE recovery `<0.3×` by `95K`, permanent eval damage `26%`

**Cheetah σ=0.2 (line 706):** NVE = `1.9×` at `55K`

**PickCube σ=0.2 (line 709):** NVE = `3.71×` at `52.5K`

**Exp_030c (line 715):** at σ=1.0: CIVO eliminated (NVE ≤ `0.30`), peak eval `372` at `35K` (`116%` of baseline), eval declines to `47` by `215K` (`15%`); value_mean = `12.4`, NVE = `0.26` at 215K

**DreamerV3 Hyperparameters (tab:hyperparams, lines 733-770):**
- RSSM discrete states: `32 classes × 32 categories`
- RSSM stochastic dim: `32`
- RSSM deterministic dim: `512`
- MLP hidden size: `512`
- MLP layers: `2`
- Batch size: `16 sequences × 64 steps`
- Learning rate: `3×10^-4` (Adam, ε=`10^-8`)
- Sequence length: `64`
- Training ratio: `512`
- Free nats: `1.0`
- KL balance (α): `0.8`
- Discount (γ): `0.997`
- λ-return: `0.95`
- Actor entropy scale: `3×10^-4`
- Action repeat: `2` (Walker Walk, Cheetah Run)
- Total environment steps: `105K`
- Evaluation frequency: every `10K` steps
- Evaluation episodes: `10`

**Detector algorithm (line 785):**
- τ_mag = `0.49`, τ_vel = `0.1`, ε = `10^-6`
- Acceleration condition: last `3` checkpoints, ≥ `2` declining

**Detector sensitivity (line 805):**
- τ_mag = `0.49` maximizes Youden's J = `0.714`
- Raising to `0.50` loses seed 3 (triggers at r_t = `0.497`)
- τ_vel = `0.1` stable across `[0.05, 0.18]`

**Detector validation table (tab:detector-validation, lines 819-842):**
| Exp | Verdict | Trigger | Type | Peak Eval | r_ve |
|-----|---------|---------|------|-----------|------|
| 008d s0 | TP | 45K | predictive | 167 | 0.69 |
| 010b Cheetah | TP | 65K | reactive | 322 | 3.18 |
| 008d s3 | TP | 45K | predictive | 452 | 0.50 |
| 008d s4 | TP | 105K | reactive | 383 | 3.03 |
| 010b_s0 Cheetah | TP | 95K | reactive | 248 | 6.34 |
| 008f s3 | TN | -- | -- | 594 | -- |
| 009b s2 | TN | -- | -- | 279 | -- |
| baseline s1 | TN | -- | -- | 970 | -- |
| 009d s0 | TN | -- | -- | 951 | -- |
| 009d s1 | TN | -- | -- | 920 | -- |
| 019b PickCube | TN | -- | -- | 26.6 | -- |
| 009c s2 | FP | 105K | reactive | 359 | 0.75 |
| 009a s2 | FP | 85K | predictive | 967 | 0.73 |
| 009c s3 | TN | -- | -- | 457 | -- |
| **TPR = 5/5 (1.00), FPR = 2/9 (0.22)** | | | | | |

**PickCube cross-simulator (line 846):**
- Oscillatory V/E ratio, spikes to r_t = `5.66` at `52.5K`, deflates to `1.38` by `72.5K`
- 14 checkpoints through `132.5K`
- Frozen PickCube (exp_054): peak `8.81×` at `62.5K`, resolves to `0.55×` at `72.5K`

**Dual critic table (tab:dual_critic_full, lines 869-884):**
| Exp | Config | Params | NVE | Eval | Outcome |
|-----|--------|--------|-----|------|---------|
| 008d | Single narrow | 1.2M | 4.12× | 82.8 | Collapse |
| 033 | Wide single | 2.4M | 4.75× | 407.9 | CIVO → self-repair |
| 035 s0 | Narrow dual (min) | 1.2M | 2.75× | 697.8 | CIVO → recovery |
| 039 s1 | Narrow dual (min) | 1.2M | 2.19× | 592.7 | CIVO → recovery |
| 032 s0 | Wide dual (min) | 2.4M | ≤1.1× | 739.7 | CIVO prevented |
| 032b s1 | Wide dual (min) | 2.4M | 1.4× | 551.8 | CIVO prevented |
| 038 s2 | Wide dual (min) | 2.4M | ≤0.3× | 120.9* | Non-CIVO collapse |
| 034 | Cheetah dual | 2.4M | 1.75× | 97.5 | Partial recovery (31%) |
| 037 | Cheetah wide single | 2.4M | 3.60× | 146.1 | CIVO → self-repair |
| 036 | PickCube dual | 2.4M | 2.3× | 27.7 | Transient CIVO |

*038 s2: eval peaked at `354` (`155K`), then declined to `120.9` (`224K`); actor entropy from `-3.59` to `-0.45`

**Recovery mechanism (line 897):**
- 035 (s0): NVE `2.75×`, eval `33.8 → 697.8`, recovery ratio `20.6×`
- 039 (s1): NVE `2.19×`, eval `35.9 → 592.7`, recovery ratio `16.5×`
- Both outperform wide single (033, 2.4M params, eval 407.9)
- Min reduces peak CIVO: `2.19--2.75×` vs. `4.75×`

**Cheetah dual (line 901):**
- Wide dual reduces Cheetah NVE from `8.27×` to `1.75×` (≥ `4×` reduction)
- Recovery: `31%` of pre-CIVO peak

---

## nve_sensitivity_table.tex (paper/tables/ version)

- Task B2 (main): threshold `≥1.5×`, n_pos/n_neg = `4/6`, AUROC = `0.958`, accuracy `90.0%`, CI `[55.5,99.7]`, F1 `88.9%`, 1 FP (IRD)
- Task B1 (app): threshold `≥3.9×`, n_pos/n_neg = `3/7`, AUROC = `1.000`, accuracy `100%`, CI `[69.2,100]`, F1 `100%`

---

## nve_sensitivity_table.tex (artifacts/_project/paper/ and _37b680 versions — identical)

- Task B2 (main): threshold `≥1.5×`, n = `8`, pos/neg = `3/5`, AUROC = `0.933`, accuracy `87.5%`, CI `[0.474,0.997]`, margin `-2.16`, 1 FP
- Task B1 (sens.): threshold `≥1.7×`, n = `8`, pos/neg = `2/6`, AUROC = `1.000`, accuracy `100%`, CI `[0.631,1.000]`, margin `+0.35`, n_pos = 2

---

## artifacts/analysis/detector_table.tex

- TPR = `3/3 (1.00)`, FPR = `2/7 (0.286)` — **different values from the appendix table which reports TPR=5/5, FPR=2/9**
- Same TP rows (008d s0 @ 45K, 010b Cheetah @ 65K, 008d s3 @ 45K) but missing the two additional TP entries (008d s4, 010b s0) present in the appendix table
- FP: 009c s2 @ 105K (r_ve 0.75), 009a s2 @ 85K (r_ve 0.73)

---

## Key Discrepancies / Inconsistencies Flagged

1. **Abstract vs. Introduction degradation range**: Abstract says `14--30%` of baseline; Introduction says `14--19%`. The results section confirms: fixed dt=2 → 14%, dt=4 → 19%, learned gate → 11%. The 30% figure in the abstract appears unsupported by the primary data.

2. **detector_table.tex vs. appendix detector table**: `artifacts/analysis/detector_table.tex` shows TPR = `3/3`, FPR = `2/7` (older version, 10 runs); appendix Table shows TPR = `5/5`, FPR = `2/9` (final, 14 runs). The main text cites the 14-run version (5/5), but the artifact file is the stale 10-run version.

3. **nve_sensitivity_table.tex inconsistency**: The `paper/tables/` version reports AUROC = `0.958` and n_pos/n_neg = `4/6`; the `artifacts/_project/paper/` version reports AUROC = `0.933`, n = `8`, pos/neg = `3/5`, threshold B1 = `≥1.7×`. The current appendix (in the actual paper) uses B1 threshold = `≥3.9×`, n_pos = `3`, AUROC = `1.000`. The artifact files are stale intermediate versions.

4. **"trained s1 peak = 3.08"**: This value appears in the PegInsertionSide footnote as exp_055 (seed 1 trained) peak NVE = `3.08×` at `92.5K`. In the complete results table (line 71), it appears as `3.08×` for exp_055. The same `3.08×` value is also used in the Cheetah Walker context separately.

5. **Walker frozen "2/4 CIVO"**: The cross-domain table says `0/3` for Walker frozen, but tab:three_way_emb says `2/4` — this is consistent because there are 4 frozen seeds total (042, 015b, 047, 057) with 2 showing transient exceedances (047 at `1.71×`, 057 at `1.88×`), but the cross-domain table counts only the 3 seeds that are definitively non-CIVO.

6. **Walker frozen NVE range**: The Cheetah freeze (exp_046) is stated as NVE `1.35×` in the main table, but line 391 refers to `70.64×` as the trained Cheetah NVE for that comparison (citing the extreme seed 010b_s0). The line uses `trained 70.64×` as the comparator — this is the peak across both Cheetah trained seeds combined (`max(8.27, 108.52)` is not `70.64`; this appears to be the mean or a specific checkpoint value not matching the table peak of `108.52×`).

agentId: a00056aa23f532ed4 (use SendMessage with to: 'a00056aa23f532ed4' to continue this agent)
&lt;usage>total_tokens: 74565
tool_uses: 18
duration_ms: 266415&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "415cd407-1937-49ae-8408-a1524cdb0ba2",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read all the LaTeX paper files in /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/ and extract every quantitative claim (numbers, ratios like \"6/6\", percentages, NVE values, seed counts, step counts, etc.).\n\nThe files to read are:\n- docs/paper/main.tex\n- docs/paper/sections/abstract_body.tex\n- docs/paper/sections/introduction.tex\n- docs/paper/sections/methodology.tex\n- docs/paper/sections/results.tex\n- docs/paper/sections/analysis.tex\n- docs/paper/sections/related_work.tex\n- docs/paper/sections/conclusion.tex\n- docs/paper/sections/appendix.tex\n\nAlso check:\n- paper/tables/nve_sensitivity_table.tex\n- artifacts/_project/paper/nve_sensitivity_table.tex\n- artifacts/_project/paper/nve_sensitivity_table_37b680.tex\n- artifacts/analysis/detector_table.tex\n\nFor each quantitative claim, report:\n1. File name and line number\n2. The exact text/context around the number\n3. The specific value claimed\n\nFocus especially on:\n- Cross-domain statistics like \"X/Y locomotion\", \"X/Y manipulation\", \"X/Y frozen\"\n- NVE values (especially Walker frozen and Cheetah frozen)\n- Seed counts (n=2, n=3, etc.)\n- Step counts (132.5K, 142.5K, etc.)\n- Any baseline comparison values (like \"trained s1 peak = 3.08\")\n- Table data in tabular environments\n\nReturn a comprehensive list organized by file. Be thorough - every number matters for this audit.",
    "agentId": "a00056aa23f532ed4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the comprehensive audit of every quantitative claim, organized by file.\n\n---\n\n## main.tex\n\n**Line 27:** `\\sgseval{448.3}` — SGS eval value = 448.3\n**Line 28:** `\\sgsnve{1.66}` — SGS NVE value = 1.66\n**Line 29:** `\\sgsclaim{...}` — \"0/3 across environments\" (CIVO elimination rate)\n\n---\n\n## abstract_body.tex\n\n**Line 1:**\n- `14--30\\%` — degradation range of all variable-rate configs relative to baseline\n- `26/29` — NVE classifier accuracy (any CIVO across all configs)\n- `AUROC = 0.953` — NVE classifier AUC (in-sample)\n- `2.78\\times` — RSSM reward prediction gap at dt>1\n- `\\rho > 0.999` — dual critic correlation in pure imagination\n- `100\\%` sensitivity for NVE detector\n\n---\n\n## introduction.tex\n\n**Line 6:**\n- `14--19\\%` of baseline — performance degradation range (note: abstract says 14--30%; introduction says 14--19%)\n- `2.78\\times` — RSSM reward prediction gap at dt>1 vs dt=2\n- `26/29` — NVE classification accuracy\n- `n=29` — sample size for NVE evaluation\n- `AUROC = 0.953` — in-sample\n- `LOEO cross-validated` — mean AUROC = 0.981 (reference to Appendix Table)\n- `38--49\\%` — reward head gradient share of ∇θ e_dt\n- `16--22\\%` — observation decoder gradient share\n\n**Line 12 (Contributions):**\n- `6/6 seeds` — CIVO from trained dt-embedding + multi-rate exposure\n- `two locomotion environments`\n- `AUROC = 0.953` in-sample, LOEO cross-validated\n- Three manipulation tasks with frozen-embedding controls\n\n**Line 14:**\n- `38--49\\%` — reward head gradient share; reward-only stopping fails\n- `\\rho > 0.999` — dual critics converge\n\n**Line 15:**\n- `100\\%` sensitivity\n- `5/5` — NVE detector sensitivity\n- `2/5` — predictive warning cases\n\n---\n\n## methodology.tex\n\n**Line 7:**\n- `32 categories × 32 classes` — RSSM discrete latent states\n- `H=15` — default imagination horizon\n- `dt=1` — standard temporal resolution\n\n**Lines 16-21:**\n- `d=32` — temporal embedding dimensionality (trained, frozen modes)\n\n**Line 27:**\n- `H=15` (default) and `H=8` — tested horizons\n- `H=8 at dt=2` covers `16` physical time steps vs. `15` for default\n\n**Line 32:**\n- `12 conditions` in factorial design\n- `4 seeds` per key configuration\n\n**Line 38:**\n- `35K+` window for NVE computation\n- `505K steps` — baseline reference (exp_001, seed 1)\n- `26/29` accuracy\n- `AUROC = 0.953` in-sample\n- LOEO mean `AUROC = 0.981`\n\n**Line 48:**\n- TCN noise: `σ ∈ {0.5, 0.2}`, three environments\n- RAVE clips: `c ∈ {2.0, 1.5}`\n\n**Line 53:**\n- Narrow critic: `~1.2M` parameters\n- Wide critic: `~2.4M` parameters\n\n**Line 58:**\n- Baseline runs: `500K steps`, peak return `970.4`\n- Treatments run: `105K steps`\n- `d=32` temporal embedding\n- `~80 GPU-hours` total on single NVIDIA RTX PRO 6000\n\n---\n\n## results.tex\n\n**Line 4:** Treatments run to `105K` steps; baseline to `505K` steps; eval = mean over `10 episodes`\n\n**Table 1 (tab:main_results, lines 20-35):**\n\n| Exp | Config | dt_emb | Sub | H | Eval@final | NVE |\n|-----|--------|--------|-----|---|-----------|-----|\n| 001 | Baseline | --- | --- | 15 | 915.7 @105K | 1.00× |\n| 008d | Factorial s1 | trn | ON | 8 | 82.8 @55K | 4.12× |\n| 008f | No dt_emb s1 | --- | ON | 8 | 503.0 @105K | 0.97× |\n| 008a | Unexposed emb | exp | OFF | 15 | 777.7 @105K | 0.93× |\n| 015b | Frozen emb | frz | ON | 8 | 204.2 @105K | 1.45× |\n| 022b | Frozen emb+Gumbel | frz | ON | 8 | 300.7 @105K | 0.63× |\n| 010b | Cheetah Run | trn | ON | 8 | 51.7 @105K | 8.27× |\n| 019b | PickCube-v1 | trn | ON | 8 | 26.64 @200K | 3.78× (^c) |\n| 049 | StackCube-v1 | trn | ON | 8 | 34.9 @212K | 5.05× (^d) |\n| 050 | PegInsertionSide-v1 | trn | ON | 8 | 20.86 @212K | 10.05× (^e) |\n| 046 | Cheetah Run frz | frz | ON | 8 | --- | 1.35× |\n\n**Footnote ^d (line 45):** frozen control (exp_051) exhibits peak `4.30×` at `42.5K`, self-correcting by `82.5K`\n\n**Footnote ^e (lines 46):**\n- Seed 0 trained peaks at `10.05×` (`82.5K`) with delayed self-correction\n- Seed 1 trained (exp_055) peaks at `3.08×` (`92.5K`), final `0.50×`\n- Seed 1 frozen (exp_056) peaks at `11.32×` (`82.5K`), final `1.19×`\n\n**F1 (line 56):**\n- Baseline reaches `915.7` at 105K\n- Fixed dt=2 (006): peaks at `485.3` before collapsing to `132.9` (`14%` of baseline)\n- Fixed dt=4 (007): never exceeds `176.9` (`19%`)\n- Learned gate (005): collapses to `98.8` (`11%`)\n\n**F2 (line 72):**\n- 008d: NVE = `4.12×` (eval 82.8) vs. 008f: NVE ≤ `0.97×` (eval 503.0)\n- `26/29` across two environments, `AUROC = 0.953`\n\n**Line 77 (figure caption):** Walker Walk, `n=3` seeds plotted; seed 4 data in Table\n\n**Line 81:**\n- Peak NVEs: `4.62×`, `4.12×`, `1.62×`, `1.53×` (4 Walker Walk seeds)\n- All below `30%` of baseline\n- IQM `175.2`, mean `170.6`, `n=4`\n- One self-corrects to `29.3%` of baseline\n- `n=6` seeds total across two environments; `5/6` progressing toward collapse\n\n**F3-F5 (line 90):**\n- 008a (3 seeds): peak NVE `0.83--0.93×`\n- 008f (3 seeds): peak NVE ≤ `1.41×`\n- Frozen NVE range: `0.19--1.71×` vs. trained `1.53--4.62×`\n- 3/4 seeds below threshold, 1/4 transient self-correcting\n- Partial gradient blocking (exp_044): peak NVE `4.45×`, final eval `538`, `59%` baseline\n- Degradation: `-47%` at dt=2, `-81%` at dt=4\n\n**ManiSkill manipulation (line 93):**\n- StackCube trained (049/052): NVE `5.05×/4.67×`, frozen (051): `4.30×`, all self-correcting by `82.5K`\n- PegInsertionSide: high-amplitude `4--11×`; seed 0 trained `10.05×` vs. frozen `1.82×`; seed 1 reverses: frozen `11.32×` vs. trained `3.08×`\n- PickCube frozen control (exp_054): peak `8.81×` at `62.5K`, self-correcting\n\n**F6 (line 103):**\n- Exp_008e_v3: 2/4 seeds collapse (`50%`)\n- Pathway A (CIVO): NVE = `4.02×`\n- Pathway B (entropy increase): NVE = `3.78×`; 2 seeds only\n\n**F7 (line 106):**\n- Full-SGS (exp_018): seed 1 eval `448.3`, NVE `1.66×`; seed 2 collapsed (0/2 elimination)\n- Cheetah (010b): NVE `8.27--108.52×`; full-SGS: 0/3 elimination\n- Removing embedding on Cheetah (024b): NVE `<0.2×`\n\n**Obs-decoder-only SGS (line 109):** `1/6` CIVO prevention (`1/4` Walker, `0/2` Cheetah)\n\n**Table: Intervention hierarchy (lines 121-148):**\n\n| Level | Intervention | Seeds | Prev. | Rate |\n|-------|-------------|-------|-------|------|\n| --- | Untreated | 6 | 0/6 | 0% |\n| Gradient | Reward-only SGS | 2 | 0/2 | 0% |\n| Gradient | Full-pathway SGS | 3 | 0/3 | 0% |\n| Gradient | Obs-decoder SGS | 6 | 1/6 | 17% |\n| Output | RAVE (c=1.5,2.0) | 2 | 0/2 | 0% |\n| Repr. | TCN (σ=0.1) | 1 | 1/1†† | 100% |\n| Repr. | TCN (σ=0.2) | 6† | 2/6 | 33% |\n| Repr. | TCN (σ=0.5) | 3 | 0/3 | 0% |\n| Repr. | TCN (σ=1.0) | 1 | 1/1§ | 100% |\n| Arch. | Wide single | 2 | 0/2 | 0% |\n| Arch. | Narrow dual (min) | 2 | 0/2 | 0% |\n| Arch. | Wide dual (min) | 4 | 3/4‖ | 75% |\n| --- | Embedding frozen | 7 | 5/7# | 71% |\n| --- | Embedding removed | 5 | 5/5 | 100% |\n\nFootnotes:\n- †Walker 2/4 (s2 NVE `2.11×`; s3 late-onset NVE `3.04×` at 105K); Cheetah 0/1, PickCube 0/1\n- ††Borderline (NVE = `1.02×`, eval `55%`)\n- §CIVO prevented but progressive policy erosion (peak `116%`, final `15%` baseline)\n- ‖Walker 3/3 (NVE ≤ `1.4×`; `1/3` non-CIVO eval collapse), Cheetah 0/1\n- #Walker 5 + Cheetah 2; Exp_047 (NVE `1.71×`) and Exp_057 (NVE `1.88×`): both transient, self-correcting within `20K` steps; remaining 5 seeds: NVE `0.19--1.45×`\n\n**Forward-pass interventions (line 157):**\n- TCN at σ=0.2: 2/4 Walker seeds suppressed, NVE `<1.0×`, eval `45--91%`\n\n**Architecture-level (line 167):**\n- `n=7` dual-critic configs: `ρ > 0.999`, pessimism at `3--4%` of independent-critic bound\n\n**Recovery ratios (line 170):**\n- Narrow dual: `~16--19×` recovery ratio\n- Wide dual: NVE ≤ `1.4×`, `3/3` prevention, `1/3` non-CIVO collapse\n\n**Online CIVO Detection (line 179):**\n- 14 runs across 3 environments\n- TPR = `5/5`, FPR = `2/9`\n- Predictive alerts in `2/5` cases\n\n---\n\n## analysis.tex\n\n**Line 5:**\n- `2.78×` reward prediction gap (Table ref)\n- Reward head: `38--49%` of ∇θ e_dt; fails when blocked alone\n- Observation decoder: `16--22%`\n- Full-pathway SGS: `0/3`\n\n**Line 8 (Practitioner guidelines):**\n- NVE diagnostic: ≥ `1.5×`, AUROC = `0.953`\n- Frozen converts sustained CIVO (`4/4` trained, NVE `1.53--108×`) to transient spikes (`2/3` frozen Walker, `1.71--1.88×`)\n- Self-correct within `20K` steps\n- Extreme CIVO: `70.6×` causes irrecoverable damage\n\n**Line 11:**\n- Manipulation peaks: `4--11×`, but frozen controls show comparable/higher peaks\n\n---\n\n## appendix.tex — Complete Results (tab:complete_results, lines 17-91)\n\nAll 42 experiments (key additional values beyond the main table):\n\n| Exp | Config | NVE | Eval | Step |\n|-----|--------|-----|------|------|\n| 001 s2 | Baseline s2 | --- | 443.5 | @105K |\n| 006 | Fixed dt=2 | 4.83× | 132.9 | @65K |\n| 007 | Fixed dt=4 | --- | 152.5 | @55K |\n| 005 | Learned gate | --- | 98.8 | @145K |\n| 009b | Factorial s2 | 1.62× | 267.9 | @105K |\n| 008d_s3 | Factorial s3 | 1.53× | 268◇ | @105K |\n| 008d_s4 | Factorial s4 | 4.62× | 63.6 | @105K |\n| 008f s4 | No dt_emb s4 | 1.41× | 306.5 | @105K |\n| 009c s3 | No dt_emb s3 | 1.04× | 311.9 | @105K |\n| 008a_s1 | Unexposed emb | 0.83× | 630.9 | @105K |\n| 008a_s2 | Unexposed emb | 0.89× | 899.4 | @105K |\n| 042 | Frozen emb (dedicated) | 0.19× | 612.0 | @105K |\n| 057 | Frozen emb s2 | 1.88× | --- | |\n| 018 s1 | Full-SGS | 1.66× | 448.3 | @105K |\n| 018 s2 | Full-SGS | --- | 40.8 | @105K |\n| 008e_v3 s1 | Mitigation | 0.94× | 869.9 | @105K |\n| 008e_v3 s2† | Mitigation | 3.78× | 137.0 | @105K |\n| 008e_v3 s3 | Mitigation | 4.02× | 92.7 | @105K |\n| 008e_v3 s4 | Mitigation | 0.99× | 899.3 | @105K |\n| 010b_s0 | Cheetah Run | 108.52× | 0.83 | @105K |\n| 021 | Cheetah Run SGS | 9.94× | 221.5 | @105K |\n| 024b s0 | Cheetah no emb | <0.20× | 96.5 | @105K |\n| 024b s1 | Cheetah no emb | 0.10× | 77.3 | @105K |\n| 008a_ch s0 | Cheetah unexposed | 1.08× | 532.4 | @105K |\n| 008a_ch s1 | Cheetah unexposed | 1.29× | 504.4 | @105K |\n| 054 | PickCube frz | 8.81×^h | --- | |\n| 052 | StackCube trn | 4.67× | --- | |\n| 051 | StackCube frz | 4.30× | 30.7 | @155K |\n| 053 | PegInsertion frz | 8.10× | 5.89 | |\n| 055 | PegInsertion trn | 3.08× | 11.44 | @212K |\n| 056 | PegInsertion frz | 11.32× | 4.37 | @212K |\n| 058 | Cheetah frz | 0.23× | 80.46 | @215K |\n\nFootnote ^h: PickCube frozen control peak `8.81×` at `62.5K`, self-correcting to `0.55×` at `72.5K`\nFootnote ^d: Peak NVE `9.94×` at `45K`, transient, self-correcting to `<1×` by `55K`\nFootnote ^g: Seed 0 trained peaks at `10.05×` (`82.5K`); seed 1 trained peaks at `3.08×` (`92.5K`), final `0.50×` at `212.5K`; seed 1 frozen peaks at `11.32×` (`82.5K`), final `1.19×` at `212.5K`\n\n**Cross-domain table (tab:cross_domain, lines 103-108):**\n| Domain | Environment | Trained | Frz ctrl | dt-emb-dep. CIVO |\n|--------|-------------|---------|----------|-----------------|\n| Locomotion | Walker Walk | 4/4 | 0/3 | Yes (NVE 1.53--4.62×) |\n| Locomotion | Cheetah Run | 2/2 | 0/2 | Yes (NVE 8.27--108.5×) |\n| Manipulation | StackCube-v1 | 0/2 | 0/1 | No |\n| Manipulation | PegInsertionSide | 0/2 | 0/2 | No |\n| Manipulation | PickCube-v1 | 0/1 | 0/1 | No |\n\n**NVE Sensitivity Tables (lines 148-210):**\n\nTask B1 (n_pos=3, n_neg=7, n=10, AUROC=1.000):\n| Threshold | TP | FP | FN | TN | Accuracy | Precision | Recall | F1 |\n|-----------|----|----|----|----|----------|-----------|--------|-----|\n| ≥1.0× | 3 | 3 | 0 | 4 | 70.0% [34.8,93.3] | 50.0% | 100% | 66.7% |\n| ≥1.2× | 3 | 2 | 0 | 5 | 80.0% [44.4,97.5] | 60.0% | 100% | 75.0% |\n| ≥1.5× | 3 | 2 | 0 | 5 | 80.0% [44.4,97.5] | 60.0% | 100% | 75.0% |\n| ≥1.7× | 3 | 1 | 0 | 6 | 90.0% [55.5,99.7] | 75.0% | 100% | 85.7% |\n| ≥2.0× | 3 | 1 | 0 | 6 | 90.0% [55.5,99.7] | 75.0% | 100% | 85.7% |\n| ≥3.9× | 3 | 0 | 0 | 7 | 100% [69.2,100] | 100% | 100% | 100% |\n\nTask B2 (n_pos=4, n_neg=6, n=10, AUROC=0.958):\n| Threshold | TP | FP | FN | TN | Accuracy | Precision | Recall | F1 |\n|-----------|----|----|----|----|----------|-----------|--------|-----|\n| ≥1.0× | 4 | 2 | 0 | 4 | 80.0% [44.4,97.5] | 66.7% | 100% | 80.0% |\n| ≥1.2× | 4 | 1 | 0 | 5 | 90.0% [55.5,99.7] | 80.0% | 100% | 88.9% |\n| ≥1.5× | 4 | 1 | 0 | 5 | 90.0% [55.5,99.7] | 80.0% | 100% | 88.9% |\n| ≥1.7× | 3 | 1 | 1 | 5 | 80.0% [44.4,97.5] | 75.0% | 75.0% | 75.0% |\n| ≥2.0× | 3 | 1 | 1 | 5 | 80.0% [44.4,97.5] | 75.0% | 75.0% | 75.0% |\n| ≥3.9× | 3 | 0 | 1 | 6 | 90.0% [55.5,99.7] | 100% | 75.0% | 85.7% |\n\nTask B2 full (n_pos=8, n_neg=8, n=16, AUROC=0.969):\n| ≥1.0× | 8 | 2 | 0 | 6 | 87.5% [61.7,98.4] | 80.0% | 100% | 88.9% |\n| ≥1.2× | 8 | 1 | 0 | 7 | 93.8% [69.8,99.8] | 88.9% | 100% | 94.1% |\n| ≥1.5× | 8 | 1 | 0 | 7 | 93.8% [69.8,99.8] | 88.9% | 100% | 94.1% |\n| ≥1.7× | 6 | 1 | 2 | 7 | 81.3% [54.4,96.0] | 85.7% | 75.0% | 80.0% |\n| ≥2.0× | 6 | 1 | 2 | 7 | 81.3% [54.4,96.0] | 85.7% | 75.0% | 80.0% |\n| ≥3.9× | 6 | 0 | 2 | 8 | 87.5% [61.7,98.4] | 100% | 75.0% | 85.7% |\n\n**NVE Raw Values Table (tab:nve_raw, lines 130-141):**\n- 006: NVE = `4.83`\n- 008d: NVE = `4.13`\n- 008e_v3_s3: NVE = `4.02`\n- 008e_v3_s2: NVE = `3.78`\n- 009b: NVE = `1.62`\n- 001: NVE = `1.00`\n- 008e_v3_s4: NVE = `0.99`\n- 008f: NVE = `0.97`\n- 008e_v3_s1: NVE = `0.94`\n- 008a: NVE = `0.93`\n\n**LOEO cross-validation (tab:nve_loeo, lines 286-292):**\n| Held-out | N_train | N_test | θ_opt range | Test Accuracy | Test AUROC |\n|----------|---------|--------|-------------|--------------|-----------|\n| PickCube | 18 | 2 | (1.45, 1.53] | 2/2 (1.000) | 1.000 |\n| Cheetah | 15 | 5 | (1.45, 1.53] | 5/5 (1.000) | 1.000 |\n| Walker | 7 | 13 | (1.00, 3.78) | 12/13 (0.923) | 0.944 |\n| **Mean** | — | — | — | **0.974** | **0.981** |\n\n**Baseline seeds table (tab:baseline_seeds, lines 253-259):**\n| Seed | Eval@105K | Eval@505K | ve@65K | ve@105K |\n|------|-----------|-----------|--------|---------|\n| s1 | 915.7 | 970.4 | 0.563 | 0.656 |\n| s2 | 443.5 | 945.7 | 0.898 | 0.742 |\n| s3 | 869.0 | 947.7 | --- | 0.664 |\n| s4 | 922.8 | 938.9 | --- | 0.624 |\n\n**NVE normalization robustness (line 264):**\n- Single-seed (s1): AUROC = `0.933`, accuracy `7/8` (`87.5%`)\n- Four-seed mean: AUROC = `0.867`, accuracy `6/8` (`75.0%`)\n- Boundary case 009b: NVE flips from `1.62×` (s1) to `1.23×` (4-seed mean) at peak at `45K`\n- s1 v/e ratio at 45K: `0.331`; 4-seed mean: `0.436`\n- 006 NVE: `4.84× → 4.52×`; 008d NVE: `4.13× → 3.54×`\n\n**Normalization conventions (line 266):**\n- Walker: 4-seed mean baseline (seeds 1--4, each to `505K+` steps)\n- Cheetah: 5-seed mean baseline (seeds 0--4, each to `~210K` steps)\n\n**Factorial Appendix (line 319 — tab:three_way_emb):**\n| Condition | Grad flow | Exp(s) | NVE peak | Eval | CIVO |\n|-----------|-----------|--------|----------|------|------|\n| Trained | all | 008d | 1.53--4.62× | 64--268 | 4/4 |\n| Reward detach | obs+KL only | 044 | 4.45× | 44→538† | 1/1 |\n| Full SGS | KL only | 018 | 1.66× | 448 | 1/1* |\n| Frozen | none | 042,015b,047,057 | 0.19--1.88×‡ | 204--612 | 2/4 |\n| Removed | N/A | 008f | 0.97--1.41× | 307--503 | 0/3 |\n\n†Self-corrected at ~175K (eval 44→538, 59% baseline; 224K run)\n‡Exp_047 (NVE 1.71×) and Exp_057 (NVE 1.88×): transient, self-correcting within 20K steps\n\n**F3 Evidence A (line 382):**\n- 008a: NVE `0.83--0.93×`, eval `777.7` at 105K (`85%` of baseline)\n- 006 NVE accelerates from `1.61×` at 45K to `2.31×` at 55K before collapse to `132.9` at 65K\n\n**F3 Evidence B (line 385):**\n- 015b NVE trajectory: `0.81 → 1.26 → 1.45 → 0.65 → 1.05 → 0.47 → 0.39 → 0.42`\n- Peaks at `1.45×` at 55K, retreats to `0.65×` by 65K, settles at `0.42×` by 105K, final eval `204.2`\n\n- 008d trajectory: `1.78 → 1.71 → 2.09 → 4.12×`, eval `82.8`\n\n**Cross-environment (line 391):**\n- Cheetah exp_010b: `2 seeds`, NVE `8.27--108.52×`, collapse to `51.7/0.83`\n- exp_024b: `2 seeds`, NVE `<0.2×`, eval `96.5/77.3`\n- Freezing on Cheetah (exp_046): NVE `1.35×` vs. trained `70.64×` — `52×` reduction\n\n**F4 (line 426):**\n- dt=1 (baseline): `915.7` at 105K\n- Fixed dt=2 (006): peak `485.3` (`-47%`)\n- Fixed dt=4 (007): peak `176.9` (`-81%`)\n\n**F5 (line 431):**\n- 008a: `777.7` vs. 008c: `240.9` — `3.2×` performance gap (horizon effect, healthy NVE ≤ `0.93×`)\n- 008f: `503.0` vs. 009c: `148.3` — cross-seed variance\n\n**RSSM Fidelity Table (tab:rssm_fidelity, lines 463-468):**\n| Config | obs_MSE dt=1 | obs_MSE dt=2 | Gap | reward_MAE dt=1 | reward_MAE dt=2 | Gap |\n|--------|-------------|-------------|-----|----------------|----------------|-----|\n| Baseline | 13.49 | 27.50 | 2.04× | 0.0102 | 0.0159 | 1.56× |\n| 008d (trained) | 41.31 | 53.67 | 1.30× | 0.0568 | 0.1579 | 2.78× |\n| 008f (no emb) | 8.01 | 22.04 | 2.75× | 0.7469 | 0.7526 | 1.01× |\n\n**CIVO mechanism (line 475):**\n- Random policy: dt=2 imagination produces `1.68×` higher mean reward than dt=1 (Stage 1)\n- Trained actor amplifies to `2.90×` (Stage 2)\n- No-embedding control: random policy ratio `1.11×`, trained-actor ratio `0.98×`\n- Stage 1 contributes `~36%`, Stage 2 `~64%` of total effect\n\n**Signed reward error table (tab:signed_error, lines 492-499):**\n| Config | dt | Mean SE | Std | %Over | Actual | Pred |\n|--------|-----|---------|-----|-------|--------|------|\n| Baseline | 1 | +0.001 | 0.023 | 39.6% | 1.893 | 1.894 |\n| 008d | 1 | +0.018 | 0.072 | 61.8% | 0.361 | 0.379 |\n| 008d | 2 | **-0.599** | 0.722 | 8.0% | 0.721 | 0.121 |\n| 008f | 1 | -0.710 | 0.704 | 14.0% | 0.921 | 0.211 |\n| 008f | 2 | -1.645 | 1.485 | 5.0% | 1.840 | 0.195 |\n\n**Gradient decomposition table (tab:gradient_decomposition, lines 532-536):**\n| Loss component | @55K share | @112K share |\n|----------------|-----------|------------|\n| Reward head | 49.0% | 38.1% |\n| KL dynamics | 34.7% | 40.4% |\n| Observation decoders | 16.3% | 21.5% |\n\n**Exp_016e (line 517):**\n- Peak eval `326.7` at 75K steps, decline to `31.7` at 95K, NVE `10.42×`\n\n**Entropy (line 572):** all configs start at `~8 nats`, converge to `~-4.5 to -5`\n\n**016e vs 008d timing (line 579):**\n- Collapse onset: `75K` (016e) vs. `25K` (008d)\n- Peak eval: `326.7` (016e) vs. `167.2` (008d)\n\n**Post-CIVO outcomes table (tab:post_civo, lines 594-601):**\n| Env | Seed | Peak | Final | Eval | Outcome |\n|-----|------|------|-------|------|---------|\n| Walker | s1 (008d) | 4.12× | 4.12× | 82.8 | Full collapse |\n| Walker | s2 (009b) | 1.62× | 0.38× | 267.9 | Transient CIVO |\n| Walker | s3 (008d_s3) | 1.53× | 1.53× | 268◇ | Late-onset collapse |\n| Walker | s4 (008d_s4) | 4.62× | 4.62× | 63.6 | Full collapse |\n| Cheetah | s1 (010b) | 8.27× | 8.27× | 51.7 | Full collapse |\n| Cheetah | s0 (010b_s0) | 108.52× | 108.52× | 0.83 | Full collapse |\n\nFull collapse majority: `5/6` seeds; one self-correction (Walker s2) at `29.3%` of baseline\n\n**Obs-decoder SGS seed 3 (line 610):**\n- Healthy through `105K` (NVE `<1.0×`, eval `818.6`)\n- CIVO onset at `135K` (NVE `5.47×`, eval `67.0`)\n- Evaluation recovery: `590.2` at `215K`, `64%` of baseline\n- Persistent value collapse: NVE `0.14×`, value mean `80.6`\n- Seed 4 same terminal value collapse: NVE `0.14×` at `215K`, eval `242`\n\n**Embedding dilemma (line 645):**\n- Removing embedding (008f): `13×` cost to reward prediction quality (`0.7469` vs. `0.0568` MAE)\n\n**TCN full table (tab:tcn_full, lines 679-699):**\n| Env | σ | Seed | NVE_max | Prevented? | Eval % |\n|-----|---|------|---------|-----------|--------|\n| Walker | 0.1 | s0 | 1.02 | ✓* | 55% |\n| Walker | 0.2 | s0 | 0.91 | ✓ | 91% |\n| Walker | 0.2 | s1 | 0.64 | ✓ | 45% |\n| Walker | 0.2 | s2 | 2.11† | ✗ | ~5% |\n| Walker | 0.2 | s3 | 3.04¶ | ✗ | 11% |\n| Walker | 0.5 | s0 | 3.97 | ✗ | 27% |\n| Walker | 0.5 | s1 | 1.64 | ✗ | 41% |\n| Cheetah | 0.2 | s0 | 1.90 | ✗ | crashed |\n| Cheetah | 0.5 | s0 | 10.67 | ✗ | 26% |\n| Cheetah | 1.0 | s0 | ≤0.30 | ✓§ | 15% |\n| PickCube | 0.2 | s0 | 3.71 | ✗ | failing |\n\n¶Late-onset CIVO: NVE declined to `0.67×` at 95K before spike to `3.04×` at 105K; eval `349.6` at 95K → `71.8` at 105K → `104.5` at 215K\n\n**Cheetah σ=0.5 (line 703):** transient CIVO spike NVE = `10.67×` at `55K`, NVE recovery `<0.3×` by `95K`, permanent eval damage `26%`\n\n**Cheetah σ=0.2 (line 706):** NVE = `1.9×` at `55K`\n\n**PickCube σ=0.2 (line 709):** NVE = `3.71×` at `52.5K`\n\n**Exp_030c (line 715):** at σ=1.0: CIVO eliminated (NVE ≤ `0.30`), peak eval `372` at `35K` (`116%` of baseline), eval declines to `47` by `215K` (`15%`); value_mean = `12.4`, NVE = `0.26` at 215K\n\n**DreamerV3 Hyperparameters (tab:hyperparams, lines 733-770):**\n- RSSM discrete states: `32 classes × 32 categories`\n- RSSM stochastic dim: `32`\n- RSSM deterministic dim: `512`\n- MLP hidden size: `512`\n- MLP layers: `2`\n- Batch size: `16 sequences × 64 steps`\n- Learning rate: `3×10^-4` (Adam, ε=`10^-8`)\n- Sequence length: `64`\n- Training ratio: `512`\n- Free nats: `1.0`\n- KL balance (α): `0.8`\n- Discount (γ): `0.997`\n- λ-return: `0.95`\n- Actor entropy scale: `3×10^-4`\n- Action repeat: `2` (Walker Walk, Cheetah Run)\n- Total environment steps: `105K`\n- Evaluation frequency: every `10K` steps\n- Evaluation episodes: `10`\n\n**Detector algorithm (line 785):**\n- τ_mag = `0.49`, τ_vel = `0.1`, ε = `10^-6`\n- Acceleration condition: last `3` checkpoints, ≥ `2` declining\n\n**Detector sensitivity (line 805):**\n- τ_mag = `0.49` maximizes Youden's J = `0.714`\n- Raising to `0.50` loses seed 3 (triggers at r_t = `0.497`)\n- τ_vel = `0.1` stable across `[0.05, 0.18]`\n\n**Detector validation table (tab:detector-validation, lines 819-842):**\n| Exp | Verdict | Trigger | Type | Peak Eval | r_ve |\n|-----|---------|---------|------|-----------|------|\n| 008d s0 | TP | 45K | predictive | 167 | 0.69 |\n| 010b Cheetah | TP | 65K | reactive | 322 | 3.18 |\n| 008d s3 | TP | 45K | predictive | 452 | 0.50 |\n| 008d s4 | TP | 105K | reactive | 383 | 3.03 |\n| 010b_s0 Cheetah | TP | 95K | reactive | 248 | 6.34 |\n| 008f s3 | TN | -- | -- | 594 | -- |\n| 009b s2 | TN | -- | -- | 279 | -- |\n| baseline s1 | TN | -- | -- | 970 | -- |\n| 009d s0 | TN | -- | -- | 951 | -- |\n| 009d s1 | TN | -- | -- | 920 | -- |\n| 019b PickCube | TN | -- | -- | 26.6 | -- |\n| 009c s2 | FP | 105K | reactive | 359 | 0.75 |\n| 009a s2 | FP | 85K | predictive | 967 | 0.73 |\n| 009c s3 | TN | -- | -- | 457 | -- |\n| **TPR = 5/5 (1.00), FPR = 2/9 (0.22)** | | | | | |\n\n**PickCube cross-simulator (line 846):**\n- Oscillatory V/E ratio, spikes to r_t = `5.66` at `52.5K`, deflates to `1.38` by `72.5K`\n- 14 checkpoints through `132.5K`\n- Frozen PickCube (exp_054): peak `8.81×` at `62.5K`, resolves to `0.55×` at `72.5K`\n\n**Dual critic table (tab:dual_critic_full, lines 869-884):**\n| Exp | Config | Params | NVE | Eval | Outcome |\n|-----|--------|--------|-----|------|---------|\n| 008d | Single narrow | 1.2M | 4.12× | 82.8 | Collapse |\n| 033 | Wide single | 2.4M | 4.75× | 407.9 | CIVO → self-repair |\n| 035 s0 | Narrow dual (min) | 1.2M | 2.75× | 697.8 | CIVO → recovery |\n| 039 s1 | Narrow dual (min) | 1.2M | 2.19× | 592.7 | CIVO → recovery |\n| 032 s0 | Wide dual (min) | 2.4M | ≤1.1× | 739.7 | CIVO prevented |\n| 032b s1 | Wide dual (min) | 2.4M | 1.4× | 551.8 | CIVO prevented |\n| 038 s2 | Wide dual (min) | 2.4M | ≤0.3× | 120.9* | Non-CIVO collapse |\n| 034 | Cheetah dual | 2.4M | 1.75× | 97.5 | Partial recovery (31%) |\n| 037 | Cheetah wide single | 2.4M | 3.60× | 146.1 | CIVO → self-repair |\n| 036 | PickCube dual | 2.4M | 2.3× | 27.7 | Transient CIVO |\n\n*038 s2: eval peaked at `354` (`155K`), then declined to `120.9` (`224K`); actor entropy from `-3.59` to `-0.45`\n\n**Recovery mechanism (line 897):**\n- 035 (s0): NVE `2.75×`, eval `33.8 → 697.8`, recovery ratio `20.6×`\n- 039 (s1): NVE `2.19×`, eval `35.9 → 592.7`, recovery ratio `16.5×`\n- Both outperform wide single (033, 2.4M params, eval 407.9)\n- Min reduces peak CIVO: `2.19--2.75×` vs. `4.75×`\n\n**Cheetah dual (line 901):**\n- Wide dual reduces Cheetah NVE from `8.27×` to `1.75×` (≥ `4×` reduction)\n- Recovery: `31%` of pre-CIVO peak\n\n---\n\n## nve_sensitivity_table.tex (paper/tables/ version)\n\n- Task B2 (main): threshold `≥1.5×`, n_pos/n_neg = `4/6`, AUROC = `0.958`, accuracy `90.0%`, CI `[55.5,99.7]`, F1 `88.9%`, 1 FP (IRD)\n- Task B1 (app): threshold `≥3.9×`, n_pos/n_neg = `3/7`, AUROC = `1.000`, accuracy `100%`, CI `[69.2,100]`, F1 `100%`\n\n---\n\n## nve_sensitivity_table.tex (artifacts/_project/paper/ and _37b680 versions — identical)\n\n- Task B2 (main): threshold `≥1.5×`, n = `8`, pos/neg = `3/5`, AUROC = `0.933`, accuracy `87.5%`, CI `[0.474,0.997]`, margin `-2.16`, 1 FP\n- Task B1 (sens.): threshold `≥1.7×`, n = `8`, pos/neg = `2/6`, AUROC = `1.000`, accuracy `100%`, CI `[0.631,1.000]`, margin `+0.35`, n_pos = 2\n\n---\n\n## artifacts/analysis/detector_table.tex\n\n- TPR = `3/3 (1.00)`, FPR = `2/7 (0.286)` — **different values from the appendix table which reports TPR=5/5, FPR=2/9**\n- Same TP rows (008d s0 @ 45K, 010b Cheetah @ 65K, 008d s3 @ 45K) but missing the two additional TP entries (008d s4, 010b s0) present in the appendix table\n- FP: 009c s2 @ 105K (r_ve 0.75), 009a s2 @ 85K (r_ve 0.73)\n\n---\n\n## Key Discrepancies / Inconsistencies Flagged\n\n1. **Abstract vs. Introduction degradation range**: Abstract says `14--30%` of baseline; Introduction says `14--19%`. The results section confirms: fixed dt=2 → 14%, dt=4 → 19%, learned gate → 11%. The 30% figure in the abstract appears unsupported by the primary data.\n\n2. **detector_table.tex vs. appendix detector table**: `artifacts/analysis/detector_table.tex` shows TPR = `3/3`, FPR = `2/7` (older version, 10 runs); appendix Table shows TPR = `5/5`, FPR = `2/9` (final, 14 runs). The main text cites the 14-run version (5/5), but the artifact file is the stale 10-run version.\n\n3. **nve_sensitivity_table.tex inconsistency**: The `paper/tables/` version reports AUROC = `0.958` and n_pos/n_neg = `4/6`; the `artifacts/_project/paper/` version reports AUROC = `0.933`, n = `8`, pos/neg = `3/5`, threshold B1 = `≥1.7×`. The current appendix (in the actual paper) uses B1 threshold = `≥3.9×`, n_pos = `3`, AUROC = `1.000`. The artifact files are stale intermediate versions.\n\n4. **\"trained s1 peak = 3.08\"**: This value appears in the PegInsertionSide footnote as exp_055 (seed 1 trained) peak NVE = `3.08×` at `92.5K`. In the complete results table (line 71), it appears as `3.08×` for exp_055. The same `3.08×` value is also used in the Cheetah Walker context separately.\n\n5. **Walker frozen \"2/4 CIVO\"**: The cross-domain table says `0/3` for Walker frozen, but tab:three_way_emb says `2/4` — this is consistent because there are 4 frozen seeds total (042, 015b, 047, 057) with 2 showing transient exceedances (047 at `1.71×`, 057 at `1.88×`), but the cross-domain table counts only the 3 seeds that are definitively non-CIVO.\n\n6. **Walker frozen NVE range**: The Cheetah freeze (exp_046) is stated as NVE `1.35×` in the main table, but line 391 refers to `70.64×` as the trained Cheetah NVE for that comparison (citing the extreme seed 010b_s0). The line uses `trained 70.64×` as the comparator — this is the peak across both Cheetah trained seeds combined (`max(8.27, 108.52)` is not `70.64`; this appears to be the mean or a specific checkpoint value not matching the table peak of `108.52×`)."
      }
    ],
    "totalDurationMs": 266415,
    "totalTokens": 74565,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1558,
      "cache_read_input_tokens": 60090,
      "output_tokens": 12916,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1558
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12916,
          "cache_read_input_tokens": 60090,
          "cache_creation_input_tokens": 1558,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1558,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 16,
      "searchCount": 2,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### Assistant

_source line 135_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data from both the paper tex files and the registry. Let me cross-reference them systematically to find inconsistencies.

Let me organize the key claims and check each one:

### 1. Cross-domain statistics

**Paper claims:**
- Cross-domain table (appendix): Walker Walk trained 4/4, frozen 0/3; Cheetah Run trained 2/2, frozen 0/2; StackCube 0/2, 0/1; PegInsertion 0/2, 0/2; PickCube 0/1, 0/1
- "6/6 locomotion" — let me check: Walker 4/4 + Cheetah 2/2 = 6/6 trained locomotion CIVO triggers. 

The locomotion numbers check out, and the manipulation tasks all show zero CIVO triggers as claimed. But I'm noticing a discrepancy with the frozen Walker count—the table reports 0/3, yet I'm seeing four frozen Walker seeds in the registry, which would suggest the denominator might be off. Looking at the specific seed IDs and their NVE values, I'm trying to reconcile why the cross-domain table shows "0/3" for Walker frozen when there appear to be 4 seeds listed. The task note mentions Walker frozen transitioning from n=2 to n=3 after exp_057 was added, so I need to figure out which seeds are actually being counted in that "0/3" figure. I'm realizing the frozen control seeds actually include exp_022b as well, so that's five Walker seeds total: 042, 015b, 047, 057, and 022b. But now the cross-domain table is showing 0/3 for frozen controls, which doesn't align with the intervention table's count of 7 frozen seeds with a 5/7 prevention rate—I need to figure out if these tables are using different subsets of the data. prevented CIVO. 2 were transient. But the cross-domain table says 0/3 for Walker frozen. That's contradictory...

Actually no. Let me re-read the cross-domain table more carefully. The "Frz ctrl" column showing 0/3 means none of the three frozen seeds demonstrated dt-emb-dependent CIVO. Now I need to verify whether n=3 is actually correct for the Walker frozen experiments by checking the registry — I'm seeing four experiment IDs listed (042, 015b, 047, 057), but 015b and 042 might be duplicates since they're both labeled as s0. Looking at their metrics though, they have very different evaluation scores and NVE values, so they must be distinct experiments. The footnote clarifies that experiments 047 and 057 show transient effects, but there's a real discrepancy across tables: the cross-domain table reports 0/3 Walker frozen cases, while the three-way embedding table lists 4 frozen seeds (042, 015b, 047, 057) with 2/4 showing the effect. The intervention hierarchy table adds another count—5 Walker frozen seeds with 5/7 prevention across embedding conditions. I need to figure out why these numbers don't align, likely because 015b uses different settings or the cross-domain analysis excludes certain experiments.

Now checking the NVE values from the registry against what the paper claims for the three frozen Walker seeds.

Looking at the Cheetah frozen results, the paper shows exp_046 with NVE=1.35, which matches the registry. But exp_058 is showing NVE=0.23 in the appendix table, not the 0.78 that was mentioned in the task notes—there's a discrepancy I need to resolve. I need to figure out what NVE actually represents here. The registry shows nve_peak of 0.78 at 45K with a ve_ratio_peak of 0.231, which means the baseline ve_ratio must be around 0.296 if NVE is calculated as the ratio between them. So the paper's 0.23× might be referring to something different—possibly the final ve_ratio rather than the normalized NVE metric. So the paper's table is reporting the raw ve_ratio value of 0.23× at the final step (215K), not the NVE peak at 45K—these are measurements from different points in training. I need to check whether the paper is consistently using final values or peak values across all experiments to understand if this is just a reporting difference or an actual inconsistency. I'm noticing a discrepancy—the paper's appendix shows exp_058 with 0.23×, but that appears to be the ve_ratio_peak rather than the actual NVE value. Looking at the cross-domain and intervention tables, there's conflicting information about whether exp_058 even appears in Table 1, and I need to trace through the agent's extraction more carefully to resolve what the paper actually reports for this experiment. Looking at the baseline comparison in analysis.tex line 11, it mentions manipulation peaks of 4-11× with frozen controls showing comparable or higher values. The footnotes confirm that the trained s1 baseline for PegInsertion (exp_055) peaks at 3.08×, which matches the registry data.

For the PegInsertion interim data question, the footnotes show exp_045 reached a peak NVE of 4.91 at 132K steps, then self-corrected by 142K steps, and I'm cross-referencing this against the registry values to verify the final measurements.

Now I'm checking the Walker frozen seed counts across the different tables—the cross-domain table shows 0/3 frozen Walker seeds, while the three-way embedding table lists 4 frozen Walker seeds (exp_042, 015b, 047, 057) with 2/4 CIVO seeds. The intervention hierarchy shows 7 total seeds (5 Walker + 2 Cheetah) with 5/7 showing prevention effects, but there's a discrepancy in the Walker frozen counts that I need to resolve.

The cross-domain table might be using a stricter definition specific to "dt-emb-dependent CIVO" and could be excluding 015b from the count, while the intervention hierarchy's Walker count of 5 includes 022b which uses Gumbel. Let me verify the paper's claims about locomotion and manipulation performance by checking the registry data for the trained seeds.

For locomotion, I'm seeing Walker contributed 4 trained seeds and Cheetah contributed 2, matching the claimed 6/6. For manipulation tasks, all five seeds across StackCube, PegInsertion, and PickCube show self-correcting or transient behavior rather than dt-emb-dependent CIVO, which explains the 0/5 count. Now I need to reconcile the abstract's "14--30%" degradation range with what the introduction states.

Looking at the actual numbers: fixed dt=2 gives 14.5% of baseline, dt=4 gives 19.3%, and the learned gate gives 10.8%. These all fall within 11--19%, so I'm trying to figure out where that 30% figure in the abstract comes from—it might be referencing a different configuration or there's a discrepancy I need to track down. not consistent with the data showing much worse degradation (to 14% of baseline).

I think both the abstract and introduction are stating the performance as a percentage of baseline. The inconsistency is 14-30% vs 14-19%.

Actually, maybe the 30% includes other variable-rate configs beyond the three mentioned. But looking at the data, all the variable-rate configs (dt=2, dt=4, learned gate) give less than 20% of baseline.

Wait, maybe I'm confusing things. Let me look again: Walker s2 (009b) under the CIVO trigger condition gets 267.9 = 29.3% of baseline. So maybe the "30%" comes from the best-performing CIVO run that partially self-corrects. So the range is 11-30% across all variable-rate configs? Hmm, but that's different experiments.

Actually, looking more carefully, the abstract might be talking about something different entirely.

The abstract could be summarizing results across all configurations including some reaching up to 30%, while the introduction focuses specifically on the fixed-dt configs that stay in the 14-19% range. It's a minor inconsistency but worth noting.

Now I'm checking the NVE value cited in the paper at line 391, which claims a 52× reduction by comparing a frozen model's NVE of 1.35× against a trained seed's 70.64×. But that 70.64 value is from just one specific seed (s0), while another trained seed shows 8.27, so the paper appears to be cherry-picking the worst-performing seed for comparison rather than using an average.

Let me verify the NVE values in the appendix table against the registry to see if they match up correctly.

For exp_008d_s4, the paper lists NVE=4.62, but the registry entry doesn't have an explicit nve_peak field—instead it shows ve_ratio_105K=3.03 along with other metrics like delta_ve_105K and peak_eval_return. I need to check if NVE can be computed from the available registry data by dividing ve_ratio by the baseline ve_ratio at 105K.

Now looking at exp_009b_walker_s2, the paper reports NVE=1.62 but the registry shows nve_peak=2.05 at 25K, which is a discrepancy I need to resolve. The difference might stem from different baseline windows or normalization methods used in the computation. The registry shows the peak at 25K steps while the paper reports it at 45K, so these are measuring different checkpoints—the NVE peak might shift depending on which baseline normalization is used. Let me step back and identify the clearest discrepancies: the exp_058 NVE value is genuinely inconsistent (paper shows 0.23× but registry has 0.78), the abstract and introduction report different degradation ranges (14-30% versus 14-19%), and the Walker frozen counts vary across tables with inconsistent counting criteria. I should focus on these concrete issues rather than getting lost in the normalization details.

The artifact files are also outdated—detector_table.tex shows 3/3 TPR while the paper reports 5/5, and the NVE sensitivity table artifacts don't match current results, though these don't affect the published paper itself. For exp_015b, the paper's Table 1 reports 1.45× as the peak NVE, which matches the trajectory shown in the appendix at 55K steps, but the registry only stores the final checkpoint values (0.42 at 105K), so there's a mismatch between what the paper highlights as the peak and what's recorded in the registry.

Now looking at exp_022b, the paper Table 1 lists 0.63× but the registry shows nve_peak=1.22—a significant discrepancy. The registry entry is labeled "exp_022b_no_curriculum" which suggests this might be a different experimental variant than what's in the main table. don't match up between the paper and registry. The exp_018/018v2 naming is just a simplification in the paper, but the NVE values for exp_022b are genuinely inconsistent—0.63× versus 1.22—and I need to verify this against the actual source files to understand what's going on.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "25bc9a3e-cc91-45cf-87a7-d7d8a31e9eb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zDiKvj8erNcuML6PoUEbw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7051,
      "cache_creation_input_tokens": 14268,
      "cache_read_input_tokens": 31575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14268
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 136_

Now I have both the paper claims and registry data. Let me verify the key discrepancies by reading the actual tex files directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "a2e11425-b857-4674-860e-4dab77e8507d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zDiKvj8erNcuML6PoUEbw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7051,
      "cache_creation_input_tokens": 14268,
      "cache_read_input_tokens": 31575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14268
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 137_

<details open><summary>🔧 Tool call — Read · `toolu_01DEJ72HezUk3NcGtaz2we4v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "71fbc514-e5c8-425a-a897-aefdb476efb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zDiKvj8erNcuML6PoUEbw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7051,
      "cache_creation_input_tokens": 14268,
      "cache_read_input_tokens": 31575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14268
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 138 · 2026-05-24T02:21:28.145Z_

<details><summary>↩ Tool result · reported error · `toolu_01DEJ72HezUk3NcGtaz2we4v`</summary>

```text
File content (27892 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "7d21eeea-031e-413a-8f2f-26e10e190cdf",
  "tool_use_result": "Error: File content (27892 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### Tool call

_source line 139_

<details open><summary>🔧 Tool call — Grep · `toolu_01REN8ahduPtyxT51MjHm2M1`</summary>

```json
{
  "pattern": "058|exp.058|Cheetah.*frz|cheetah.*frozen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "3de05bc8-b00a-4d48-9497-de2729806d08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p55VgJmFX1b51qH5TuZ1K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14934,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14934
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 140 · 2026-05-24T02:21:32.859Z_

<details><summary>↩ Tool result · `toolu_01REN8ahduPtyxT51MjHm2M1`</summary>

```text
71-053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\times$$^g$ & Env.\ dynamics (ctrl) \\
72-055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\times$$^g$ & Env.\ dynamics \\
73-056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\times$$^g$ & Env.\ dynamics (ctrl) \\
74:046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\times$ & No CIVO \\
75:058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.23$\times$ & No CIVO \\
76-\bottomrule
77-\end{tabular}
78-\vspace{1pt}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "01d411ff-ce7c-4152-afbc-29d1f749cc85",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "71-053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n72-055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n73-056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n74:046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n75:058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.23$\\times$ & No CIVO \\\\\n76-\\bottomrule\n77-\\end{tabular}\n78-\\vspace{1pt}",
    "numLines": 8
  }
}
```

</details>

---


### Tool call

_source line 141_

<details open><summary>🔧 Tool call — Grep · `toolu_01P9xmwKyKQZAXVXY3JgC7hH`</summary>

```json
{
  "pattern": "022b|no.curriculum|Gumbel|0\\.63",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "e8357c2b-4a87-479d-9710-870edba47294",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p55VgJmFX1b51qH5TuZ1K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14934,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14934
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-24T02:21:34.437Z_

<details><summary>↩ Tool result · `toolu_01P9xmwKyKQZAXVXY3JgC7hH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-37-008a\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\times$ & Healthy \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-38-008a\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\times$ & Healthy \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-39-015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
docs/paper/sections/appendix.tex:40:022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-41-042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\times$ & Healthy \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-42-057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\times$ & Transient (self-corr.) \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-43-\midrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-24-008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-25-008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-26-015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
docs/paper/sections/results.tex:27:022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-28-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-29-\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-30-\rowcolor{gray!15}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "0935afa8-2d57-4201-9236-677272fad851",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-37-008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-38-008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-39-015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\ndocs/paper/sections/appendix.tex:40:022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-41-042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-42-057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex-43-\\midrule\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-24-008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-25-008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-26-015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\ndocs/paper/sections/results.tex:27:022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-28-\\midrule\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-29-\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex-30-\\rowcolor{gray!15}",
    "numLines": 15
  }
}
```

</details>

---


### Tool call

_source line 143_

<details open><summary>🔧 Tool call — Grep · `toolu_01JbSfsQam9G1YiPh6mCacgr`</summary>

```json
{
  "pattern": "14.*30|30.*14|14--30|degradation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex",
  "output_mode": "content",
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "3e3f0c75-ea20-4c32-b149-964ade34bf36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p55VgJmFX1b51qH5TuZ1K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14934,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14934
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-24T02:21:35.722Z_

<details><summary>↩ Tool result · `toolu_01JbSfsQam9G1YiPh6mCacgr`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "5337dde6-0a98-46aa-8a40-f297b391cd69",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---


### Tool call

_source line 145_

<details open><summary>🔧 Tool call — Grep · `toolu_01GHBb9oAjNLHR4p56Ynwvx7`</summary>

```json
{
  "pattern": "14.*19|19.*14|14--19|degradation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "output_mode": "content",
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "802de66e-314f-4b7d-a45a-8bc901ed72ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p55VgJmFX1b51qH5TuZ1K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14934,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14934
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-24T02:21:36.857Z_

<details><summary>↩ Tool result · `toolu_01GHBb9oAjNLHR4p56Ynwvx7`</summary>

```text
4-[Omitted long context line]
5-
6:[Omitted long matching line]
7-
8-[Omitted long context line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "39a14eb5-8f9c-4257-b80c-fde3c52f4e2f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "4-[Omitted long context line]\n5-\n6:[Omitted long matching line]\n7-\n8-[Omitted long context line]",
    "numLines": 5
  }
}
```

</details>

---


### Assistant

_source line 147_

<details><summary>Logged reasoning block</summary>

```text
Let me read the abstract and introduction more carefully to check the degradation range.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "b99680f8-b4ea-462c-8144-d70963a9bfed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHUtPKFC45PNgkbBjgKVtx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2113,
      "cache_read_input_tokens": 60777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2113
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 148_

<details open><summary>🔧 Tool call — Read · `toolu_0171NjAseH9TEnkdSAT6cwes`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "f73f1680-c232-4382-bdf1-e0a23cedd8bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHUtPKFC45PNgkbBjgKVtx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2113,
      "cache_read_input_tokens": 60777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2113
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-24T02:21:40.234Z_

<details><summary>↩ Tool result · `toolu_0171NjAseH9TEnkdSAT6cwes`</summary>

```text
1	World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--30\% of baseline. Factorial diagnostics on two continuous-control tasks isolate trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\emph{conditioning-induced value overestimation} (CIVO; 26/29, AUROC${=}0.953$, LOEO cross-validated). The RSSM develops a $2.78\times$ reward prediction gap at $\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as the structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination ($\rho > 0.999$), rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery. A lightweight NVE detector achieves 100\% sensitivity.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "e7330baa-d749-45f1-9342-9323170406c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract_body.tex",
      "content": "World-model reinforcement learning is increasingly deployed for robot control, where temporal abstraction enables planning across heterogeneous time scales. We find that $\\Delta t$-conditioning, effective in model-predictive control (MPC), cannot transfer to imagination-based actor-critic training: every variable-rate DreamerV3 configuration degrades to 14--30\\% of baseline. Factorial diagnostics on two continuous-control tasks isolate trained temporal embedding with multi-rate data exposure as the strongest predictor of this failure---\\emph{conditioning-induced value overestimation} (CIVO; 26/29, AUROC${=}0.953$, LOEO cross-validated). The RSSM develops a $2.78\\times$ reward prediction gap at $\\Delta t{>}1$ that the critic internalizes as optimistic values; the contrast with MPC identifies feedback architecture as the structural factor. No tested intervention across four levels (gradient, output, representation, architecture) reliably eliminates CIVO: dual critics converge in pure imagination ($\\rho > 0.999$), rendering Double Q pessimism ineffective, though min $+$ increased capacity enables recovery. A lightweight NVE detector achieves 100\\% sensitivity.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---


### Tool call

_source line 150_

<details open><summary>🔧 Tool call — Read · `toolu_01TcHoB2rsous6ndPaHo9Mxy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "59b15615-9b24-428e-936e-53435fbd2949",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHUtPKFC45PNgkbBjgKVtx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2113,
      "cache_read_input_tokens": 60777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2113
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-24T02:21:40.699Z_

<details><summary>↩ Tool result · `toolu_01TcHoB2rsous6ndPaHo9Mxy`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	World-model reinforcement learning enables sample-efficient learning directly on physical hardware \citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\dt$ mismatches between simulation and hardware. TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\% of baseline). Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\geq 1.5\times$ achieves 26/29 classification ($n{=}29$, two environments, AUROC${=}0.953$, in-sample; LOEO cross-validated, Appendix~Table~\ref{tab:nve_loeo}).
7	
8	Gradient decomposition reveals that gradient magnitude does not predict causal importance: the reward head contributes 38--49\% of $\nabla_\theta e_{\dt}$ yet reward-only stopping fails, while the observation decoder (16--22\%) carries the critical signal. A four-level intervention hierarchy (gradient, output, representation, architecture) shows that no tested intervention reliably eliminates CIVO across environments. In pure-imagination training, dual critics converge to identical value functions ($\rho > 0.999$), rendering Double Q pessimism ineffective; the min operation nonetheless enables CIVO recovery, while prevention requires min $+$ increased capacity. These findings are directly relevant to robotics: as world-model RL moves toward real systems with variable-rate sensing and multi-timescale control, understanding when temporal conditioning fails, and why standard countermeasures cannot fix it, is essential for safe deployment.
9	
10	\paragraph{Contributions.}
11	\begin{enumerate}[nosep,leftmargin=*]
12	    \item \textbf{Failure mode identification.} We identify CIVO as specific to imagination-based actor-critic with temporal conditioning and isolate trained $\dt$-embedding $+$ multi-rate exposure as jointly sufficient in tested configurations (6/6 seeds, two locomotion environments, AUROC${=}0.953$, in-sample; LOEO cross-validated). Cross-environment validation spanning locomotion and manipulation (ManiSkill) establishes that CIVO is locomotion-specific; frozen-embedding controls on three manipulation tasks identify value-ratio transients as environment-driven, demonstrating the diagnostic's specificity on non-CIVO dynamics.
13	    \item \textbf{Architectural boundary.} $\dt$-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping, where model errors compound into biased value targets with no real-data anchor.
14	    \item \textbf{Four-level intervention hierarchy.} Across gradient, output, representation, and architecture levels, no intervention reliably eliminates CIVO across environments. Gradient magnitude does not predict causal importance (reward head: 38--49\%, reward-only stopping fails). In pure-imagination training, dual critics converge ($\rho > 0.999$), eliminating Double Q pessimism, though the min operation enables recovery through a different mechanism.
15	    \item \textbf{Online detection.} A lightweight NVE-based detector achieves 100\% sensitivity (5/5) with predictive warning in 2/5 cases.
16	\end{enumerate}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "dc7975ad-b93c-49f5-929d-580a73068c0e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWorld-model reinforcement learning enables sample-efficient learning directly on physical hardware \\citep{wu2023daydreamer, hansen2024tdmpc2}. Real robotic tasks demand temporal abstraction: manipulation requires fast reactive grasping alongside slow approach planning, locomotion involves gait phases at different frequencies, and sim-to-real transfer must handle $\\dt$ mismatches between simulation and hardware. TAWM \\citep{nhu2025tawm} shows that conditioning a world model on step size $\\dt$ yields consistent gains within TD-MPC2's MPC framework \\citep{hansen2024tdmpc2}. Can the same $\\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \\citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?\n\nWe find that it cannot. Every variable-rate configuration degrades performance catastrophically (14--19\\% of baseline). Through a factorial analysis on Walker Walk \\citep{tassa2018dmcontrol}, we isolate the combination of a \\emph{trained} $\\dt$-embedding and multi-rate data exposure as the strongest predictor. This combination enables the RSSM reward head to develop a $2.78\\times$ prediction gap between $\\dt{=}1$ and $\\dt{=}2$, which the critic internalizes as optimistic value estimates, a failure mode we term \\emph{conditioning-induced value overestimation} (CIVO), analogous to delusional bias \\citep{lu2018nondelusional} but model-induced rather than policy-class-induced. A normalized value-to-eval (NVE) threshold of $\\geq 1.5\\times$ achieves 26/29 classification ($n{=}29$, two environments, AUROC${=}0.953$, in-sample; LOEO cross-validated, Appendix~Table~\\ref{tab:nve_loeo}).\n\nGradient decomposition reveals that gradient magnitude does not predict causal importance: the reward head contributes 38--49\\% of $\\nabla_\\theta e_{\\dt}$ yet reward-only stopping fails, while the observation decoder (16--22\\%) carries the critical signal. A four-level intervention hierarchy (gradient, output, representation, architecture) shows that no tested intervention reliably eliminates CIVO across environments. In pure-imagination training, dual critics converge to identical value functions ($\\rho > 0.999$), rendering Double Q pessimism ineffective; the min operation nonetheless enables CIVO recovery, while prevention requires min $+$ increased capacity. These findings are directly relevant to robotics: as world-model RL moves toward real systems with variable-rate sensing and multi-timescale control, understanding when temporal conditioning fails, and why standard countermeasures cannot fix it, is essential for safe deployment.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Failure mode identification.} We identify CIVO as specific to imagination-based actor-critic with temporal conditioning and isolate trained $\\dt$-embedding $+$ multi-rate exposure as jointly sufficient in tested configurations (6/6 seeds, two locomotion environments, AUROC${=}0.953$, in-sample; LOEO cross-validated). Cross-environment validation spanning locomotion and manipulation (ManiSkill) establishes that CIVO is locomotion-specific; frozen-embedding controls on three manipulation tasks identify value-ratio transients as environment-driven, demonstrating the diagnostic's specificity on non-CIVO dynamics.\n    \\item \\textbf{Architectural boundary.} $\\dt$-conditioning succeeds in TD-MPC2's MPC re-planning but fails under imagination-based bootstrapping, where model errors compound into biased value targets with no real-data anchor.\n    \\item \\textbf{Four-level intervention hierarchy.} Across gradient, output, representation, and architecture levels, no intervention reliably eliminates CIVO across environments. Gradient magnitude does not predict causal importance (reward head: 38--49\\%, reward-only stopping fails). In pure-imagination training, dual critics converge ($\\rho > 0.999$), eliminating Double Q pessimism, though the min operation enables recovery through a different mechanism.\n    \\item \\textbf{Online detection.} A lightweight NVE-based detector achieves 100\\% sensitivity (5/5) with predictive warning in 2/5 cases.\n\\end{enumerate}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  }
}
```

</details>

---


### Assistant

_source line 152_

<details><summary>Logged reasoning block</summary>

```text
Now I can see:
- Abstract: "14--30\% of baseline" 
- Introduction: "14--19\% of baseline"

These are different. The abstract says 14-30%, introduction says 14-19%. The actual data:
- Fixed dt=2: 132.9 / 915.7 = 14.5%
- Fixed dt=4: 176.9 / 915.7 = 19.3%
- Learned gate: 98.8 / 915.7 = 10.8%

If we include 009b (self-correcting, 267.9 / 915.7 = 29.3%), that's close to 30%. 

But 009b is a CIVO trigger, not a variable-rate configuration, so the 30% upper bound in the abstract might be coming from a different configuration or a different interpretation of the results. Looking at the results section more carefully, the CIVO-triggered runs are all below 30% of baseline, and the mean across those runs is around 19%, but individual runs vary widely—some as low as 9% and others reaching 29.3%.

The variable-rate configurations mentioned in the introduction (fixed dt=2, fixed dt=4, and learned gate) actually degrade to 14-19%, which is narrower than the 14-30% range stated in the abstract. The 30% upper bound seems to come from 009b specifically, which hits 29.3% of baseline, but that's a CIVO-triggered run rather than one of the core variable-rate configurations being discussed.

Now I need to verify the NVE calculation for exp_058. The paper reports 0.23× on line 75 of the appendix, but the registry shows nve_peak=0.78, which suggests they might be using different normalizations. Let me check how the NVE is computed for Cheetah—it's normalized against the 5-seed mean baseline, and for exp_046 (Cheetah frozen s0), the NVE of 1.35× appears consistently in both the paper and registry with ve_ratio_peak=0.4.

For exp_058 (Cheetah frozen s1), the registry shows nve_peak=0.78 at 45K with ve_ratio_peak=0.231, which gives NVE = 0.231/0.296 = 0.78, matching the registry. But the paper's 0.23× looks like it might be reporting the ve_ratio directly instead of the normalized NVE—that would be a discrepancy. Alternatively, the paper could be reporting a different checkpoint's NVE, perhaps at the final 215K step where ve_ratio_final=0.107, so I need to check what the baseline_ve would be at that point.

Looking at the other experiments in the appendix table, they all seem to report peak NVE values from the registry, not final values. Let me verify this pattern across the experiments to see if exp_058 is an outlier or if I'm misinterpreting which checkpoint the paper is using. is 0.78, not 0.23—there's a clear discrepancy between what the paper reports and what the registry shows. Let me also check the exp_022b numbers more carefully, since the registry indicates nve_peak=1.22 but the paper lists 0.63×, and I should verify whether the agent's extraction of the registry data is accurate. I need to look more closely at the cross-domain results and the frozen condition counts to understand what's happening across these experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "2e8b4ac7-fb71-4ada-9b51-9bb89e394b84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXENJHrawYYYLJJvHvfWt4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1766,
      "cache_read_input_tokens": 62890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1766
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 153_

<details open><summary>🔧 Tool call — Grep · `toolu_0139eqJxrwVL6DKN6RbEMvqU`</summary>

```json
{
  "pattern": "cross.domain|tab:cross|locomotion.*manipulation|Trained.*Frz|6/6|0/5|0/3",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-C": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "36ca93ae-79a7-4ebe-adfb-e6e6f1ff4697",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXENJHrawYYYLJJvHvfWt4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1766,
      "cache_read_input_tokens": 62890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1766
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-24T02:22:22.734Z_

<details><summary>↩ Tool result · `toolu_0139eqJxrwVL6DKN6RbEMvqU`</summary>

```text
93-\end{table*}
94-
95-\begin{table}[h]
96-\centering
97-\caption{Cross-domain CIVO reproducibility. ``$\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}
98:\label{tab:cross_domain}
99-\footnotesize
100-\begin{tabular}{llccc}
101-\toprule
102:\textbf{Domain} & \textbf{Environment} & \textbf{Trained} & \textbf{Frz ctrl} & \textbf{$\dt$-emb-dep.\ CIVO} \\
103-\midrule
104:Locomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\times$) \\
105-Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\times$) \\
106-Manipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\approx$trained) \\
107-Manipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\ ordering) \\
108-Manipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\
109-\bottomrule
--
316-\midrule
317-Trained & all & 008d & $1.53$--$4.62\times$ & 64--268 & 4/4 \\
318-Reward detach & obs+KL only & 044 & $4.45\times$ & 44$\to$538$^\dagger$ & 1/1 \\
319-Full SGS & KL only & 018 & $1.66\times$ & 448 & 1/1$^*$ \\
320-Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\times$$^\ddagger$ & 204--612 & 2/4 \\
321:Removed & N/A & 008f & $0.97$--$1.41\times$ & 307--503 & 0/3 \\
322-\bottomrule
323-\end{tabular}
324-\vspace{1pt}
325-{\raggedright\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\times$); seed~2 collapsed. $^\dagger$Self-corrected at ${\sim}175$K (eval 44$\to$538, 59\% baseline; 224K run). $^\ddagger$Exp\_047 (NVE $1.71\times$) and Exp\_057 (NVE $1.88\times$): both transient, self-correcting within 20K steps.\par}
326-\end{table}
--
557-[Omitted long context line]
558-\label{fig:civo_decomposition}
559-\end{figure}
560-\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}
561-
562:[Omitted long matching line]
563-
564-[Omitted long context line]
565-
566-\subsubsection{Entropy Dynamics Across Configurations}
567-\label{sec:entropy_dynamics}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "bbbbfe11-6fe7-4676-aa91-823fdad891a7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "93-\\end{table*}\n94-\n95-\\begin{table}[h]\n96-\\centering\n97-\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n98:\\label{tab:cross_domain}\n99-\\footnotesize\n100-\\begin{tabular}{llccc}\n101-\\toprule\n102:\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n103-\\midrule\n104:Locomotion & Walker Walk & 4/4 & 0/3 & Yes (NVE $1.53$--$4.62\\times$) \\\\\n105-Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\n106-Manipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\n107-Manipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\n108-Manipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n109-\\bottomrule\n--\n316-\\midrule\n317-Trained & all & 008d & $1.53$--$4.62\\times$ & 64--268 & 4/4 \\\\\n318-Reward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\n319-Full SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\n320-Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\n321:Removed & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n322-\\bottomrule\n323-\\end{tabular}\n324-\\vspace{1pt}\n325-{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n326-\\end{table}\n--\n557-[Omitted long context line]\n558-\\label{fig:civo_decomposition}\n559-\\end{figure}\n560-\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n561-\n562:[Omitted long matching line]\n563-\n564-[Omitted long context line]\n565-\n566-\\subsubsection{Entropy Dynamics Across Configurations}\n567-\\label{sec:entropy_dynamics}",
    "numLines": 41
  }
}
```

</details>

---


### Tool call

_source line 155_

<details open><summary>🔧 Tool call — Grep · `toolu_01HTRaMpMKwdmk37C8chZWpM`</summary>

```json
{
  "pattern": "NVE.*peak|peak.*NVE|NVE$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-C": 2,
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "36395296-cc29-499f-a1f3-7936339d1aa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXENJHrawYYYLJJvHvfWt4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1766,
      "cache_read_input_tokens": 62890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1766
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-24T02:22:24.181Z_

<details><summary>↩ Tool result · `toolu_01HTRaMpMKwdmk37C8chZWpM`</summary>

```text
8-\begin{table*}[t]
9-\centering
10:\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
11-\label{tab:complete_results}
12-\scriptsize
--
83-frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
84---- = removed ($d{=}0$).\\
85:$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
86-$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\
87-$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
--
261-\end{table}
262-
263:[Omitted long matching line]
264-
265:[Omitted long matching line]
266-
267-\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).
--
313-\begin{tabular}{lccccl}
314-\toprule
315:Condition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\
316-\midrule
317-Trained & all & 008d & $1.53$--$4.62\times$ & 64--268 & 4/4 \\
--
384-
385-\paragraph{Evidence B: trainability is necessary (exp\_015b).}
386:[Omitted long matching line]
387-

[Showing results with pagination = limit: 30]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "fbcf72cf-0ca6-4a34-bf1f-e6cb55928d22",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "8-\\begin{table*}[t]\n9-\\centering\n10:\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n11-\\label{tab:complete_results}\n12-\\scriptsize\n--\n83-frz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n84---- = removed ($d{=}0$).\\\\\n85:$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n86-$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n87-$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n--\n261-\\end{table}\n262-\n263:[Omitted long matching line]\n264-\n265:[Omitted long matching line]\n266-\n267-\\paragraph{Normalization conventions.} Walker NVE is normalized against the 4-seed mean baseline (seeds~1--4, each run to 505K+ steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n--\n313-\\begin{tabular}{lccccl}\n314-\\toprule\n315:Condition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n316-\\midrule\n317-Trained & all & 008d & $1.53$--$4.62\\times$ & 64--268 & 4/4 \\\\\n--\n384-\n385-\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\n386:[Omitted long matching line]\n387-",
    "numLines": 30,
    "appliedLimit": 30
  }
}
```

</details>

---


### Tool call

_source line 157_

<details open><summary>🔧 Tool call — Bash · `toolu_01DdXBX7sfcyBb1ecbjuaWib`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/7ea0cafa-bccd-4a6a-979a-adad0a282f84/tool-results/mcp-agent-ml-research-read_registry-1779588804851.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Check exp_022b\nfor eid, exp in exps.items():\n    if '022b' in eid:\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n        print(f'  description: {exp.get(\\\"description\\\", \\\"\\\")[:200]}')\n        print(f'  metrics: {json.dumps(exp.get(\\\"metrics\\\", {}), indent=2)[:500]}')\n        print()\n\n# Check exp_058\nfor eid, exp in exps.items():\n    if '058' in eid:\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n        print(f'  description: {exp.get(\\\"description\\\", \\\"\\\")[:200]}')\n        print(f'  metrics: {json.dumps(exp.get(\\\"metrics\\\", {}), indent=2)[:500]}')\n        print()\n\" 2>&1",
  "description": "Check registry exp_022b and exp_058 full details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "f42e3b09-c3ad-4aa6-8fd5-d2f5ff52c299",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXENJHrawYYYLJJvHvfWt4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1766,
      "cache_read_input_tokens": 62890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1766
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 158 · 2026-05-24T02:22:31.810Z_

<details><summary>↩ Tool result · `toolu_01DdXBX7sfcyBb1ecbjuaWib`</summary>

```text
=== exp_022b_no_curriculum ===
  status: DONE
  conclusion: success
  description: 
  metrics: {
  "civo_alert_max": 0,
  "eval_return_105K": 300.7,
  "gate_dt_1_frac_105K": 0.145,
  "gate_dt_mean_105K": 3.41,
  "gate_entropy_ratio_105K": 0.912,
  "gate_near_uniform": true,
  "nve_peak": 1.22,
  "ve_ratio_105K": 0.075,
  "ve_ratio_peak": 0.218
}

=== exp_058_frozen_dt_emb_cheetah_s1 ===
  status: DONE
  conclusion: success
  description: 
  metrics: {
  "total_steps": 224000,
  "ve_ratio_peak": 0.231,
  "ve_ratio_peak_step": 45000,
  "ve_ratio_final": 0.107,
  "ve_ratio_final_step": 215000,
  "eval_return_final": 80.46,
  "eval_return_final_step": 215000,
  "eval_return_peak": 191.74,
  "eval_return_peak_step": 25000,
  "nve_peak": 0.78,
  "nve_peak_step": 45000,
  "nve_classification": "no_civo",
  "note": "Cheetah frozen s1. NVE=0.78\u00d7 (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 \u2014 both clean, f
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "8431c70b-d1b7-4787-af6f-bc7ff32ecef4",
  "tool_use_result": {
    "stdout": "=== exp_022b_no_curriculum ===\n  status: DONE\n  conclusion: success\n  description: \n  metrics: {\n  \"civo_alert_max\": 0,\n  \"eval_return_105K\": 300.7,\n  \"gate_dt_1_frac_105K\": 0.145,\n  \"gate_dt_mean_105K\": 3.41,\n  \"gate_entropy_ratio_105K\": 0.912,\n  \"gate_near_uniform\": true,\n  \"nve_peak\": 1.22,\n  \"ve_ratio_105K\": 0.075,\n  \"ve_ratio_peak\": 0.218\n}\n\n=== exp_058_frozen_dt_emb_cheetah_s1 ===\n  status: DONE\n  conclusion: success\n  description: \n  metrics: {\n  \"total_steps\": 224000,\n  \"ve_ratio_peak\": 0.231,\n  \"ve_ratio_peak_step\": 45000,\n  \"ve_ratio_final\": 0.107,\n  \"ve_ratio_final_step\": 215000,\n  \"eval_return_final\": 80.46,\n  \"eval_return_final_step\": 215000,\n  \"eval_return_peak\": 191.74,\n  \"eval_return_peak_step\": 25000,\n  \"nve_peak\": 0.78,\n  \"nve_peak_step\": 45000,\n  \"nve_classification\": \"no_civo\",\n  \"note\": \"Cheetah frozen s1. NVE=0.78\\u00d7 (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 \\u2014 both clean, f",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 159_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key data. Let me compile the inconsistencies:

1. **exp_058 NVE**: Paper appendix line 75 says `0.23×`, but registry says nve_peak=0.78. The registry note says "NVE=0.78× (raw 0.231 / baseline 0.296 @45K)". So 0.23× is the raw ve_ratio, not the NVE. The paper is reporting the raw ve_ratio instead of the NVE. This is WRONG.


2. **exp_022b NVE**: Paper says 0.63×, registry says nve_peak=1.22. I need to figure out if these are using different normalizations. The registry shows ve_ratio_peak=0.218 and ve_ratio_105K=0.075, while the paper reports peak NVE in the 35K+ window. I'm trying to work backwards from the ve_ratio_peak to see what baseline was used at that step.

If the baseline VE is around 0.18, then dividing 0.218 by that gives roughly 1.22, but if it's closer to 0.346, I get 0.63 instead. So the discrepancy likely comes down to whether the registry used a single-seed baseline versus the paper's 4-seed mean baseline. Looking at the Walker baseline data, I see ve values of 0.563 at 65K and 0.656 at 105K, which should help me figure out which baseline was actually used for each calculation. the registry's NVE computation is using a different normalization than the paper, which is a systemic issue. Let me cross-check with other experiments to see if this is widespread—exp_008d and exp_042 match between paper and registry, but exp_022b doesn't, suggesting the registry might not have been updated consistently when the normalization was standardized to the 4-seed mean baseline.

Looking at exp_022b specifically, the registry shows nve_peak of 1.22, which was likely computed with an older single-seed normalization, while the paper's value of 0.63 uses the stated 4-seed mean baseline. Since the paper explicitly defines its normalization convention, I can verify which is correct by checking the 4-seed mean baseline ve at the peak step. For now, I'll flag this as a discrepancy that needs verification rather than diving deeper into the computation.

Now examining the Abstract versus Introduction claims about variable-rate degradation. The Abstract states 14-30% of baseline while the Introduction claims 14-19%, but looking at the actual fixed-rate configs, dt=2 is 14.5%, dt=4 is 19.3%, and the learned gate is only 10.8%. The Introduction's range covers the first two but excludes the learned gate, while the Abstract's range is even broader. I need to check whether the CIVO trigger runs should be included in this comparison.

When I add those variable-rate CIVO runs, I see performance ranging from 6.9% to 29.3%, with the best runs hitting around 30%. This suggests the Abstract might be pulling from all variable-rate configurations including factorial treatments, whereas the Introduction focuses narrowly on fixed-dt configs. The inconsistency in how "variable-rate" is defined across these sections needs clarification.

For the Walker frozen count discrepancy, the cross-domain table shows 0/3 frozen seeds, but the three-way breakdown lists 4 frozen Walker seeds. Looking closer, the cross-domain table specifically counts seeds where trained peaks consistently exceed frozen at matched timepoints. The count might exclude 015b since it's an early exploration run with different settings than the dedicated frozen controls (042, 047, 057), or the table is only counting those three dedicated runs rather than all four seeds in the Walker frozen group. The discrepancy hinges on how "dt-emb-dependent CIVO" is defined—it requires trained peaks to consistently exceed frozen at matched timepoints across seeds, which is a stricter criterion than just showing elevated NVE values like 047 and 057 do.  The cross-domain table's "0/3" counts only sustained CIVO in frozen controls, while the three-way table's "2/4" captures any transient exceedances above the threshold, so these are measuring different things. I should flag this distinction more clearly.

Now I'm noticing that exp_047 appears in the three-way comparison table with an NVE of 1.71, but it's completely absent from the complete results table in the appendix—only 042, 015b, and 057 are listed there.

Looking at the intervention hierarchy footnote, it breaks down the Walker experiments: 042 at 0.19×, 015b at 1.45×, 047 at 1.71×, 057 at 1.88×, and 022b at 0.63×. So 047 should definitely be in that complete results table, but it's missing. The range holds up regardless of which NVE value I use for seed 058—whether it's 0.78 or 0.23, both fall within the 0.19–1.45 span, so the footnote is accurate. Now I'm checking the three-way table's CIVO column more carefully, looking at the frozen seeds to see which ones actually show CIVO effects. There's a discrepancy with 008d's NVE value—the main table shows 4.12× while the raw values table lists 4.13, likely due to rounding from an underlying value around 4.125. Now I need to check exp_047 in the complete results table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "23fffb29-f1cb-4365-94f5-bdb601a27e68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKGyBbHEjWE2xqnxSt1X7j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4466,
      "cache_read_input_tokens": 64656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4466
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 160_

<details open><summary>🔧 Tool call — Grep · `toolu_01Su5JqEbv5BTCxAZzzbcDjm`</summary>

```json
{
  "pattern": "047",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-C": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "3169d129-bff9-48e7-a1e1-88250000de3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKGyBbHEjWE2xqnxSt1X7j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4466,
      "cache_read_input_tokens": 64656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4466
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-24T02:23:54.766Z_

<details><summary>↩ Tool result · `toolu_01Su5JqEbv5BTCxAZzzbcDjm`</summary>

```text
319-Full SGS & KL only & 018 & $1.66\times$ & 448 & 1/1$^*$ \\
320:Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\times$$^\ddagger$ & 204--612 & 2/4 \\
321-Removed & N/A & 008f & $0.97$--$1.41\times$ & 307--503 & 0/3 \\
--
324-\vspace{1pt}
325:{\raggedright\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\times$); seed~2 collapsed. $^\dagger$Self-corrected at ${\sim}175$K (eval 44$\to$538, 59\% baseline; 224K run). $^\ddagger$Exp\_047 (NVE $1.71\times$) and Exp\_057 (NVE $1.88\times$): both transient, self-correcting within 20K steps.\par}
326-\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "058a7627-4d5e-4969-b3cf-c54446cc6e63",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "319-Full SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\n320:Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\n321-Removed & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n--\n324-\\vspace{1pt}\n325:{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n326-\\end{table}",
    "numLines": 7
  }
}
```

</details>

---


### Tool call

_source line 162_

<details open><summary>🔧 Tool call — Read · `toolu_01NYS68fQDDrnJ5AWPWtEP5w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 14,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "192829bc-cf8e-46cf-8211-c78b8ceb012e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKGyBbHEjWE2xqnxSt1X7j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4466,
      "cache_read_input_tokens": 64656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4466
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-24T02:23:55.763Z_

<details><summary>↩ Tool result · `toolu_01NYS68fQDDrnJ5AWPWtEP5w`</summary>

```text
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	001 s2 & Baseline ($\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\
20	\rowcolor{gray!15}
21	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
22	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
23	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
24	\midrule
25	\rowcolor{gray!15}
26	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
27	\rowcolor{gray!15}
28	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
29	\rowcolor{gray!15}
30	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
31	\rowcolor{gray!15}
32	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
33	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
34	008f s4 & No dt\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\times$ & Healthy \\
35	009c s3 & No dt\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\times$ & Healthy \\
36	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
37	008a\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\times$ & Healthy \\
38	008a\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\times$ & Healthy \\
39	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
40	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
41	042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\times$ & Healthy \\
42	057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\times$ & Transient (self-corr.) \\
43	\midrule
44	018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & Partial mitig.\ (CIVO+) \\
45	\rowcolor{gray!15}
46	018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
47	008e\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\times$ & Healthy \\
48	008e\_v3 s2$^\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\times$ & Non-CIVO collapse \\
49	\rowcolor{gray!15}
50	008e\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\times$ & CIVO collapse \\
51	008e\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\times$ & Healthy \\
52	\midrule
53	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
54	\rowcolor{gray!15}
55	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
56	\rowcolor{gray!15}
57	010b\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\times$ & Full collapse \\
58	\rowcolor{gray!15}
59	021 & Cheetah Run & trn$^\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\times$$^d$ & Transient CIVO (self-corr.) \\
60	024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\times$ & Healthy \\
61	024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\times$ & Healthy \\
62	008a\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\times$ & Healthy \\
63	008a\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\times$ & Healthy \\
64	\rowcolor{gray!15}
65	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
66	054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\times$$^h$ & Env.\ transient (ctrl) \\
67	049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\times$$^f$ & Env.\ transient \\
68	052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\times$$^f$ & Env.\ transient \\
69	051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\times$$^f$ & Env.\ transient (ctrl) \\
70	050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\times$$^g$ & Env.\ dynamics \\
71	053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\times$$^g$ & Env.\ dynamics (ctrl) \\
72	055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\times$$^g$ & Env.\ dynamics \\
73	056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\times$$^g$ & Env.\ dynamics (ctrl) \\
74	046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\times$ & No CIVO \\
75	058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.23$\times$ & No CIVO \\
76	\bottomrule
77	\end{tabular}
78	\vspace{1pt}
79	{\raggedright\footnotesize
80	trn = trained ($d{=}32$, subsample ON);
81	trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
82	exp$^a$ = trained, subsample OFF;
83	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
84	--- = removed ($d{=}0$).\\
85	$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
86	$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\
87	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
88	$^d$ Peak NVE $9.94\times$ at 45K (transient, self-correcting to $<$1$\times$ by 55K); final eval 221.5.\\
89	$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\
90	$^f$ StackCube transient: frozen control (exp\_051, peak $4.30\times$ at 42.5K) matches trained (exp\_049/052), self-correcting by 82.5K; environment-specific, not $\dt$-embedding-driven.\\
91	$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\times$ (82.5K); seed~1 trained (exp\_055) peaks at $3.08\times$ (92.5K), final $0.50\times$ at 212.5K; seed~1 frozen (exp\_056) peaks at $11.32\times$ (82.5K), final $1.19\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\dt$-embedding causation.\\
92	$^h$ PickCube environment transient: frozen control peak $8.81\times$ at 62.5K, self-correcting to $0.55\times$ at 72.5K; matches trained (exp\_019b) trajectory.\par}
93	\end{table*}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "87a46b5b-5c6d-461a-bc0d-694a8c1a15e2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.23$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\par}\n\\end{table*}",
      "numLines": 80,
      "startLine": 14,
      "totalLines": 902
    }
  }
}
```

</details>

---


### Tool call

_source line 164_

<details open><summary>🔧 Tool call — Read · `toolu_01HQviQ911BW3WtraoJS1QoT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": 120,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "d2ff28eb-15c5-4c0b-8d4a-7dda617867aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKGyBbHEjWE2xqnxSt1X7j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4466,
      "cache_read_input_tokens": 64656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4466
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-24T02:23:56.514Z_

<details><summary>↩ Tool result · `toolu_01HQviQ911BW3WtraoJS1QoT`</summary>

```text
120	\midrule
121	--- & Untreated & 6 & 0/6 & 0\% \\
122	\midrule
123	Gradient & Reward-only SGS & 2 & 0/2 & 0\% \\
124	Gradient & Full-pathway SGS & 3 & 0/3 & 0\% \\
125	Gradient & Obs-decoder SGS & 6 & 1/6 & 17\% \\
126	\midrule
127	Output & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\% \\
128	\midrule
129	Repr. & TCN ($\sigma{=}0.1$) & 1 & 1/1$^\ddagger$ & 100\% \\
130	Repr. & TCN ($\sigma{=}0.2$) & 6$^\dagger$ & 2/6 & 33\% \\
131	Repr. & TCN ($\sigma{=}0.5$) & 3 & 0/3 & 0\% \\
132	Repr. & TCN ($\sigma{=}1.0$) & 1 & 1/1$^\S$ & 100\% \\
133	\midrule
134	Arch. & Wide single & 2 & 0/2 & 0\% \\
135	Arch. & Narrow dual (min) & 2 & 0/2 & 0\% \\
136	Arch. & Wide dual (min) & 4 & 3/4$^\|$ & 75\% \\
137	\midrule
138	--- & Embedding frozen & 7 & 5/7$^\#$ & 71\% \\
139	--- & Embedding removed & 5 & 5/5 & 100\% \\
140	\bottomrule
141	\end{tabular}
142	\vspace{1pt}
143	{\raggedright\footnotesize $^\dagger$Walker 2/4 (s2 NVE $2.11\times$; s3 late-onset CIVO, NVE $3.04\times$ at 105K); Cheetah 0/1, PickCube 0/1.
144	$^\ddagger$Borderline (NVE${=}1.02\times$, eval 55\%).
145	$^\S$CIVO prevented but progressive policy erosion (peak 116\%, final 15\% baseline).
146	$^\|$Walker 3/3 ($\nve \leq 1.4\times$; 1/3 non-CIVO eval collapse), Cheetah 0/1.\\
147	$^\#$Walker 5 + Cheetah 2. Exp\_047 (NVE $1.71\times$) and Exp\_057 (NVE $1.88\times$): both transient, self-correcting within 20K steps; remaining 5 seeds: NVE $0.19$--$1.45\times$.\par}
148	\end{table}
149	
150	%% ============================================================
151	%% Forward-pass interventions
152	%% ============================================================
153	
154	\subsection{Forward-Pass Interventions}
155	\label{sec:forward_results}
156	
157	We test two forward-pass alternatives (Table~\ref{tab:intervention_hierarchy}). \textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\sigma{=}0.2$ (NVE $< 1.0\times$, eval 45--91\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\sigma{=}1.0$) causes policy erosion to 15\% baseline; PickCube 0/1 (Appendix~\ref{sec:tcn_cross_env}). TCN is a \emph{diagnostic probe}, not a deployable mitigation.
158	
159	%% ============================================================
160	%% Architecture-Level Ablation
161	%% ============================================================
162	
163	\subsection{Architecture-Level Ablation}
164	\label{sec:arch_results}
165	
166	\paragraph{Critic convergence in pure imagination.}
167	Across all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\rho > 0.999$), with pessimism at 3--4\% of the independent-critic bound (\S\ref{sec:dual_critic_method}).
168	
169	\paragraph{$2{\times}2$ factorial: recovery vs.\ prevention.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "0d404b04-0509-4bdc-916a-ded45d778793",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
      "content": "\\midrule\n--- & Untreated & 6 & 0/6 & 0\\% \\\\\n\\midrule\nGradient & Reward-only SGS & 2 & 0/2 & 0\\% \\\\\nGradient & Full-pathway SGS & 3 & 0/3 & 0\\% \\\\\nGradient & Obs-decoder SGS & 6 & 1/6 & 17\\% \\\\\n\\midrule\nOutput & RAVE ($c{=}1.5{,}2.0$) & 2 & 0/2 & 0\\% \\\\\n\\midrule\nRepr. & TCN ($\\sigma{=}0.1$) & 1 & 1/1$^\\ddagger$ & 100\\% \\\\\nRepr. & TCN ($\\sigma{=}0.2$) & 6$^\\dagger$ & 2/6 & 33\\% \\\\\nRepr. & TCN ($\\sigma{=}0.5$) & 3 & 0/3 & 0\\% \\\\\nRepr. & TCN ($\\sigma{=}1.0$) & 1 & 1/1$^\\S$ & 100\\% \\\\\n\\midrule\nArch. & Wide single & 2 & 0/2 & 0\\% \\\\\nArch. & Narrow dual (min) & 2 & 0/2 & 0\\% \\\\\nArch. & Wide dual (min) & 4 & 3/4$^\\|$ & 75\\% \\\\\n\\midrule\n--- & Embedding frozen & 7 & 5/7$^\\#$ & 71\\% \\\\\n--- & Embedding removed & 5 & 5/5 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\dagger$Walker 2/4 (s2 NVE $2.11\\times$; s3 late-onset CIVO, NVE $3.04\\times$ at 105K); Cheetah 0/1, PickCube 0/1.\n$^\\ddagger$Borderline (NVE${=}1.02\\times$, eval 55\\%).\n$^\\S$CIVO prevented but progressive policy erosion (peak 116\\%, final 15\\% baseline).\n$^\\|$Walker 3/3 ($\\nve \\leq 1.4\\times$; 1/3 non-CIVO eval collapse), Cheetah 0/1.\\\\\n$^\\#$Walker 5 + Cheetah 2. Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps; remaining 5 seeds: NVE $0.19$--$1.45\\times$.\\par}\n\\end{table}\n\n%% ============================================================\n%% Forward-pass interventions\n%% ============================================================\n\n\\subsection{Forward-Pass Interventions}\n\\label{sec:forward_results}\n\nWe test two forward-pass alternatives (Table~\\ref{tab:intervention_hierarchy}). \\textbf{RAVE} (value-level capping) fails: the EMA anchor tracks biased values during CIVO onset. \\textbf{TCN} (representation-level noise) suppresses CIVO in 2 of 4 Walker seeds at $\\sigma{=}0.2$ (NVE $< 1.0\\times$, eval 45--91\\%), but remaining seeds show runaway escalation, suggesting TCN gates rather than attenuates CIVO. Cross-environment transfer fails: Cheetah effective dose ($\\sigma{=}1.0$) causes policy erosion to 15\\% baseline; PickCube 0/1 (Appendix~\\ref{sec:tcn_cross_env}). TCN is a \\emph{diagnostic probe}, not a deployable mitigation.\n\n%% ============================================================\n%% Architecture-Level Ablation\n%% ============================================================\n\n\\subsection{Architecture-Level Ablation}\n\\label{sec:arch_results}\n\n\\paragraph{Critic convergence in pure imagination.}\nAcross all dual-critic configurations ($n{=}7$), critics trained on shared RSSM features converge ($\\rho > 0.999$), with pessimism at 3--4\\% of the independent-critic bound (\\S\\ref{sec:dual_critic_method}).\n\n\\paragraph{$2{\\times}2$ factorial: recovery vs.\\ prevention.}",
      "numLines": 50,
      "startLine": 120,
      "totalLines": 180
    }
  }
}
```

</details>

---


### Assistant

_source line 166_

<details><summary>Logged reasoning block</summary>

```text
Now I have a much clearer picture. Let me also verify the analysis.tex line 11 reference and check for the "trained s1 peak = 3.08" baseline comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "8d775c39-341b-4964-b84f-d52d871dc807",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01289DCyEjeXGUVJwQCuecqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8658,
      "cache_read_input_tokens": 69122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8658
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 167_

Let me check the analysis.tex for the key claims and verify one more potential issue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "e45b2c36-b78b-446f-a13c-e0f4883a447c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01289DCyEjeXGUVJwQCuecqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8658,
      "cache_read_input_tokens": 69122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8658
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 168_

<details open><summary>🔧 Tool call — Read · `toolu_019QyR1ucDaj58Evn8poMwRc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "295ef514-ef15-4219-977b-6a226807c9e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01289DCyEjeXGUVJwQCuecqw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8658,
      "cache_read_input_tokens": 69122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8658
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-24T02:24:02.528Z_

<details><summary>↩ Tool result · `toolu_019QyR1ucDaj58Evn8poMwRc`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{CIVO mechanism.}
5	The RSSM develops a $2.78\times$ reward prediction gap under trained conditioning (Table~\ref{tab:rssm_fidelity}), analogous to delusional bias \citep{lu2018nondelusional}. Gradient magnitude $\neq$ causal importance: the reward head (38--49\% of $\nabla_\theta e_{\dt}$) fails when blocked alone; the observation decoder (16--22\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\S\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\ref{sec:mpc_immune}).
6	
7	\paragraph{Practitioner guidelines.}
8	Monitor via NVE diagnostic ($\geq 1.5\times$, AUROC${=}0.953$; Table~\ref{tab:nve_loeo}). Freezing the $\dt$-embedding converts sustained CIVO (4/4 trained, NVE $1.53$--$108\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\times$) causes irrecoverable damage (Appendix~\ref{sec:appendix_analysis}).
9	
10	\paragraph{Implications for robot learning.}
11	No $\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\times$), but frozen controls show comparable or higher peaks (Table~\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\dt$-embedding bias, while manipulation rewards are sparse and contact-gated.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "9e9b979a-40f2-4890-96cd-8c3abae5f443",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{CIVO mechanism.}\nThe RSSM develops a $2.78\\times$ reward prediction gap under trained conditioning (Table~\\ref{tab:rssm_fidelity}), analogous to delusional bias \\citep{lu2018nondelusional}. Gradient magnitude $\\neq$ causal importance: the reward head (38--49\\% of $\\nabla_\\theta e_{\\dt}$) fails when blocked alone; the observation decoder (16--22\\%) carries the critical signal; full-pathway SGS (0/3) confirms forward-pass conditioning as the irreducible vulnerability. CIVO is upstream of estimation error---dual critics converge (\\S\\ref{sec:arch_results})---so standard corrections are inapplicable; MPC re-planning prevents accumulation (Appendix~\\ref{sec:mpc_immune}).\n\n\\paragraph{Practitioner guidelines.}\nMonitor via NVE diagnostic ($\\geq 1.5\\times$, AUROC${=}0.953$; Table~\\ref{tab:nve_loeo}). Freezing the $\\dt$-embedding converts sustained CIVO (4/4 trained, NVE $1.53$--$108\\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\\times$) causes irrecoverable damage (Appendix~\\ref{sec:appendix_analysis}).\n\n\\paragraph{Implications for robot learning.}\nNo $\\dt$-embedding-dependent CIVO was observed in manipulation: all three ManiSkill environments exhibit ve-ratio transients (peaks $4$--$11\\times$), but frozen controls show comparable or higher peaks (Table~\\ref{tab:cross_domain}), establishing environment-specific origin. A possible mediator is reward density: locomotion provides continuous rewards accumulating coherent $\\dt$-embedding bias, while manipulation rewards are sparse and contact-gated.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---


### Assistant

_source line 170_

<details><summary>Logged reasoning block</summary>

```text
Now let me look at analysis.tex line 8 more carefully:

"Freezing the $\dt$-embedding converts sustained CIVO (4/4 trained, NVE $1.53$--$108\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\times$; 0/2 frozen Cheetah)"

- "4/4 trained, NVE 1.53--108×": This means 4 out of 4 trained Walker seeds show CIVO with NVE range 1.53-108×. 

Wait, I need to reconsider this. The Walker trained range is actually 1.53-4.62, while Cheetah goes up to 108.52. So that full span of 1.53-108× includes both environments, but the "4/4 trained" specifically refers to the 4 Walker seeds. The 108× value is coming from Cheetah results, which makes the range notation a bit ambiguous about what's being measured where. also be split between Walker and Cheetah to match the frozen section's format. So either "4/4 trained Walker, NVE 1.53--4.62×" or "6/6 trained (4/4 Walker + 2/2 Cheetah), NVE 1.53--108×" would be clearer than the current phrasing.

Now checking the frozen Walker numbers: if 047 and 057 showed transient spikes out of three seeds, that's 2/3, which matches the analysis section. But the cross-domain table reports "0/3" for Walker frozen, which is measuring something different—whether those runs had dt-embedding-dependent CIVO, not whether they showed transient spikes.

The issue is that the three-way table says "2/4 CIVO" for frozen, using n=4, while the analysis uses n=3. This suggests the three-way table is including 015b, which the analysis and cross-domain table exclude—I need to figure out why that seed is being counted differently across these tables.

Looking at the seed counts more carefully, I'm seeing inconsistencies: the cross-domain table has 3 frozen Walker seeds (042, 047, 057), the three-way embedding table has 4 (adding 015b), and the intervention hierarchy has 5 (also including 022b). The analysis matches the cross-domain count of 3. These different scopes might be justified—015b appears to be gradient starvation rather than pure frozen control, and 022b has a Gumbel gate—but it's creating potential confusion.

Now checking the "0/2 frozen Cheetah" claim: the registry shows 046 (NVE=1.35) and 058 (NVE=0.78), both below the CIVO threshold or transient, so "0/2" correctly indicates neither showed transient spikes.

I'm starting to compile all the inconsistencies I've found so far, beginning with the NVE value for exp_058 in the appendix table. be narrowed to Walker-only "1.53--4.62×". For exp_022b, there's a discrepancy where the paper reports 0.63× but the registry shows nve_peak = 1.22, likely due to different normalization approaches—single-seed versus the paper's 4-seed mean. Finally, exp_047 is missing from the complete results table despite being referenced elsewhere in the document, while other frozen seed experiments are properly included.

Beyond these definite issues, I'm noticing some inconsistencies that might warrant attention: the Walker frozen seed count differs across tables (3 seeds in the cross-domain table, 4 in the three-way embedding table, and 5 in the intervention hierarchy), which could create confusion. There's also a minor rounding discrepancy with 008d showing 4.12× versus 4.13 in different tables, and some artifact files appear outdated with old detector metrics that don't match what's in the paper.

Let me double-check item #5 against the full results table to make sure I'm not missing anything.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "1f19e12e-faa6-43de-b1a4-81d9ab1b7c0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R83x4pc6cfQM2Xtoom7kyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 77780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 715
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 171_

Now I need to verify one final thing — whether exp_047 appears in the complete results table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "bec37d0d-f6c1-4935-834f-f4cc389b0448",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R83x4pc6cfQM2Xtoom7kyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 77780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 715
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 172_

<details open><summary>🔧 Tool call — Grep · `toolu_01QJTK3yegEnxkygwUmdmYfx`</summary>

```json
{
  "pattern": "047",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "d05fab53-ecf2-4a1a-9592-d7bb8f22163f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R83x4pc6cfQM2Xtoom7kyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 77780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 715
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-24T02:24:54.042Z_

<details><summary>↩ Tool result · `toolu_01QJTK3yegEnxkygwUmdmYfx`</summary>

```text
320:Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\times$$^\ddagger$ & 204--612 & 2/4 \\
325:{\raggedright\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\times$); seed~2 collapsed. $^\dagger$Self-corrected at ${\sim}175$K (eval 44$\to$538, 59\% baseline; 224K run). $^\ddagger$Exp\_047 (NVE $1.71\times$) and Exp\_057 (NVE $1.88\times$): both transient, self-correcting within 20K steps.\par}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "66c24edb-3fe6-4f66-b3ee-1bd709036f41",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "320:Frozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\n325:{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}",
    "numLines": 2
  }
}
```

</details>

---


### Tool call

_source line 174_

<details open><summary>🔧 Tool call — Grep · `toolu_01VBQ9KqfvAJ3hkaq8Gtf3cw`</summary>

```json
{
  "pattern": "4\\.12|4\\.13",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "2039ce6d-f603-4a43-911f-20bdb3c90018",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R83x4pc6cfQM2Xtoom7kyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 77780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 715
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-24T02:24:54.852Z_

<details><summary>↩ Tool result · `toolu_01VBQ9KqfvAJ3hkaq8Gtf3cw`</summary>

```text
docs/paper/sections/related_work.tex:8:[Omitted long matching line]
docs/paper/sections/appendix.tex:26:008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
docs/paper/sections/appendix.tex:132:008d         & 4.13 & sustained CIVO & $+$ & $+$ \\
docs/paper/sections/appendix.tex:265:[Omitted long matching line]
docs/paper/sections/appendix.tex:388:[Omitted long matching line]
docs/paper/sections/appendix.tex:404: & NVE 4.12$\times$, collapse & NVE 0.93$\times$ \\
docs/paper/sections/appendix.tex:432:Neither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\nve < 0.93\times$ (\S\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\nve = 4.12\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\ 009c: 148.3) but neither exhibits $\nve > 1.5\times$; low evaluation alone does not indicate CIVO.
docs/paper/sections/appendix.tex:543:[Omitted long matching line]
docs/paper/sections/appendix.tex:594:Walker & s1 (008d) & 4.12$\times$ & 4.12$\times$ & 82.8 & Full collapse \\
docs/paper/sections/appendix.tex:869:008d & Single narrow & 1.2M & 4.12$\times$ & 82.8 & Collapse \\
docs/paper/sections/results.tex:23:008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
docs/paper/sections/results.tex:72:[Omitted long matching line]
docs/paper/sections/results.tex:81:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "ca8d335d-989f-487e-abcb-94acff7415fa",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:8:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:26:008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\ndocs/paper/sections/appendix.tex:132:008d         & 4.13 & sustained CIVO & $+$ & $+$ \\\\\ndocs/paper/sections/appendix.tex:265:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:388:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:404: & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\ndocs/paper/sections/appendix.tex:432:Neither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$; low evaluation alone does not indicate CIVO.\ndocs/paper/sections/appendix.tex:543:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:594:Walker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\ndocs/paper/sections/appendix.tex:869:008d & Single narrow & 1.2M & 4.12$\\times$ & 82.8 & Collapse \\\\\ndocs/paper/sections/results.tex:23:008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K & 4.12$\\times$ & Full collapse \\\\\ndocs/paper/sections/results.tex:72:[Omitted long matching line]\ndocs/paper/sections/results.tex:81:[Omitted long matching line]",
    "numLines": 13
  }
}
```

</details>

---


### Assistant

_source line 176_

<details><summary>Logged reasoning block</summary>

```text
Key findings:

1. **exp_047 is missing from the complete results table** (tab:complete_results, appendix lines 14-93). It only appears in the three-way table (line 320) and its footnote (line 325). This is an omission.

2. **008d NVE inconsistency**: 
   - Complete results table (line 26): 4.12×
   - NVE raw values table (line 132): 4.13
   - All other mentions: 4.12×
   - The NVE raw values table has a rounding discrepancy.

3. **exp_058 NVE = 0.23×** in the complete results table (line 75), but registry says 0.78. This is confirmed as an error.

4. **Abstract 14-30% vs Introduction 14-19%**: Confirmed.

5. **Analysis.tex line 8**: "4/4 trained" with NVE range 1.53-108× (mixing Walker count with cross-environment NVE range).

Now I need to check whether exp_053 and exp_054 have any NVE data listed in the paper.

Looking at the registry, both exp_053 and exp_054 show empty metrics, yet the paper reports NVE values of 8.10× and 8.81× respectively—these can't be cross-checked against the registry data. I'm also verifying the intervention hierarchy footnote that mentions "remaining 5 seeds: NVE 0.19--1.45×" to see if the individual seed values align with that range.

Checking the five seeds against the claimed range: 042 gives 0.19, 015b gives 1.45, 022b gives 0.63, 046 gives 1.35, and 058 shows conflicting values between paper (0.23) and registry (0.78)—but either way, all values fit within the 0.19--1.45 range, so the footnote's claim holds up. Now I need to double-check the PickCube data as well. The 200K final value of 26.64 aligns with what the paper reports, while the peak of 26.9 at 132.5K represents an intermediate checkpoint. The 14 checkpoints through 132.5K mentioned in the appendix are specifically for the detector analysis, separate from the full eval run that extends to 200K. Now I need to verify the Cheetah frozen count—the cross-domain table shows "0/2" but the registry lists two Cheetah frozen seeds with different performance values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "d2a49e7b-06cb-49cd-80b2-0e70d971d527",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UJvT1RtcffNHp2VcUR4py",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3490,
      "cache_read_input_tokens": 78495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3490
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 177_

审计完成。以下是全部发现：

---

## 不一致报告

### [不一致 #1] exp\_058 NVE 值错误
```
文件: docs/paper/sections/appendix.tex 行 75
论文中的值: 0.23×
Registry/实际值: nve_peak = 0.78 @ 45K
```
Registry note 明确记录 "NVE=0.78× (raw 0.231 / baseline 0.296 @45K)"。论文误用了原始 ve_ratio (0.231) 而非 NVE (0.78)。
**修正建议**: 将 `0.23$\times$` 改为 `0.78$\times$`

---

### [不一致 #2] Abstract vs Introduction 退化范围不一致
```
文件: docs/paper/sections/abstract_body.tex 行 1
论文中的值: "14--30\% of baseline"

文件: docs/paper/sections/introduction.tex 行 6
论文中的值: "14--19\% of baseline"
```
实际数据：fixed dt=2 → 14.5%, fixed dt=4 → 19.3%, learned gate → 10.8%。Introduction 的 14-19% 覆盖 dt=2 和 dt=4。Abstract 的 30% 可能来自 CIVO factorial 中 self-correcting seed (009b: 267.9/915.7 = 29.3%)，但这不属于"variable-rate configuration"的同一范畴。
**修正建议**: 统一为 `11--19\%`（含 learned gate）或 `14--19\%`（仅 fixed-dt），并在 abstract 修正

---

### [不一致 #3] analysis.tex 行 8 种子数与 NVE 范围不匹配
```
文件: docs/paper/sections/analysis.tex 行 8
论文中的值: "sustained CIVO (4/4 trained, NVE 1.53--108×)"
```
"4/4" 是 Walker 种子数，但 NVE 范围 1.53--108× 跨越了 Walker (1.53--4.62×) 和 Cheetah (8.27--108.52×)。
**修正建议**: 改为 `(6/6 trained locomotion, NVE $1.53$--$108\times$)` 或保持 4/4 但缩窄范围为 `NVE $1.53$--$4.62\times$`

---

### [不一致 #4] exp\_047 缺失于 Complete Results 表
```
文件: docs/paper/sections/appendix.tex tab:complete_results (行 14-93)
论文中的值: exp_047 未出现
Registry/实际值: exp_047_frozen_dt_emb_walker_s1, NVE=1.71×, eval_peak=408.79@125K, eval_final=144.22@215K
```
exp\_047 在 three-way table (行 320) 和脚注 (行 325) 中被引用，但在 complete results 表中缺失。其他 frozen Walker 种子 (042, 015b, 057) 都有列出。
**修正建议**: 在 042 和 057 之间添加一行：`047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\times$ & Transient (self-corr.)`

---

### [不一致 #5] NVE 原始值表中 008d 四舍五入不一致
```
文件: docs/paper/sections/appendix.tex 行 132
论文中的值: 4.13 (NVE raw values table)

文件: docs/paper/sections/appendix.tex 行 26 (及全文其他位置)
论文中的值: 4.12×
```
Complete results 表、main Table 1、post-CIVO 表、dual critic 表全部使用 4.12×，唯独 NVE raw values 表写成 4.13。
**修正建议**: 统一为 `4.12`

---

### [不一致 #6] exp\_022b NVE — Registry 值陈旧
```
文件: docs/paper/sections/appendix.tex 行 40
论文中的值: 0.63×
Registry 值: nve_peak = 1.22
```
Registry 记录的 ve\_ratio\_peak=0.218，ve\_ratio\_105K=0.075。论文使用 4-seed mean baseline 归一化得到 0.63×，而 registry 似乎使用单种子 baseline 得到 1.22。论文的归一化规范 (4-seed mean) 是明确声明的 (appendix 行 267)，论文值 0.63 可能正确。
**修正建议**: 更新 registry 中 exp\_022b 的 nve\_peak 为与论文一致的 0.63（使用 4-seed 归一化）

---

## 一致性确认

以下检查点全部一致：

| 检查项 | 论文 | Registry | 状态 |
|--------|------|----------|------|
| 6/6 locomotion CIVO | Walker 4/4 + Cheetah 2/2 | ✓ | 一致 |
| 0/5 manipulation dt-emb-dep CIVO | Stack 0/2 + Peg 0/2 + Pick 0/1 | ✓ | 一致 |
| Walker frozen s0 NVE | 0.19× | 0.194 | 一致 |
| Walker frozen s1 NVE | 1.71× | 1.71 | 一致 |
| Walker frozen s2 NVE | 1.88× | 1.88 | 一致 |
| Cheetah frozen s0 NVE | 1.35× | 1.35 | 一致 |
| PegInsertion s1 trained peak | 3.08× | ve_ratio_peak=3.08 | 一致 |
| PegInsertion s1 frozen peak | 11.32× | ve_ratio_peak=11.321 | 一致 |
| Detector TPR/FPR | 5/5, 2/9 | N/A (14 runs) | 论文内一致 |
| Baseline s1 eval@105K | 915.7 | N/A | 一致 |
| Baseline s1 eval@505K | 970.4 | N/A | 一致 |
| LOEO mean AUROC | 0.981 | N/A | 论文内一致 |
| 022b eval@105K | 300.7 | 300.7 | 一致 |
| 058 eval@215K | 80.46 | 80.46 | 一致 |
| Frozen intervention 5/7 prevention | 7 seeds (W5+C2) | ✓ | 一致 |
| PickCube frozen peak | 8.81× @ 62.5K | exp\_054 (metrics empty but paper cites) | 无法验证 |

---

## 附注：陈旧 Artifact 文件（不影响论文）

- `artifacts/analysis/detector_table.tex`: TPR=3/3, FPR=2/7（旧版 10-run），论文已更新为 5/5, 2/9（14-run）
- `artifacts/_project/paper/nve_sensitivity_table*.tex`: AUROC=0.933（旧版），论文已更新为 0.958
- exp\_053, exp\_054 registry metrics 为空，无法从 registry 交叉验证

**总结**: 6 个不一致（#1 exp\_058 NVE 最严重，直接影响数值准确性），14+ 个检查点一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "uuid": "c82936f2-e236-47bb-9a31-b29c48add8b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UJvT1RtcffNHp2VcUR4py",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3490,
      "cache_read_input_tokens": 78495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3490
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 178_

审计完成。以下是全部发现：

---

## 不一致报告

### [不一致 #1] exp\_058 NVE 值错误
```
文件: docs/paper/sections/appendix.tex 行 75
论文中的值: 0.23×
Registry/实际值: nve_peak = 0.78 @ 45K
```
Registry note 明确记录 "NVE=0.78× (raw 0.231 / baseline 0.296 @45K)"。论文误用了原始 ve_ratio (0.231) 而非 NVE (0.78)。
**修正建议**: 将 `0.23$\times$` 改为 `0.78$\times$`

---

### [不一致 #2] Abstract vs Introduction 退化范围不一致
```
文件: docs/paper/sections/abstract_body.tex 行 1
论文中的值: "14--30\% of baseline"

文件: docs/paper/sections/introduction.tex 行 6
论文中的值: "14--19\% of baseline"
```
实际数据：fixed dt=2 → 14.5%, fixed dt=4 → 19.3%, learned gate → 10.8%。Introduction 的 14-19% 覆盖 dt=2 和 dt=4。Abstract 的 30% 可能来自 CIVO factorial 中 self-correcting seed (009b: 267.9/915.7 = 29.3%)，但这不属于"variable-rate configuration"的同一范畴。
**修正建议**: 统一为 `11--19\%`（含 learned gate）或 `14--19\%`（仅 fixed-dt），并在 abstract 修正

---

### [不一致 #3] analysis.tex 行 8 种子数与 NVE 范围不匹配
```
文件: docs/paper/sections/analysis.tex 行 8
论文中的值: "sustained CIVO (4/4 trained, NVE 1.53--108×)"
```
"4/4" 是 Walker 种子数，但 NVE 范围 1.53--108× 跨越了 Walker (1.53--4.62×) 和 Cheetah (8.27--108.52×)。
**修正建议**: 改为 `(6/6 trained locomotion, NVE $1.53$--$108\times$)` 或保持 4/4 但缩窄范围为 `NVE $1.53$--$4.62\times$`

---

### [不一致 #4] exp\_047 缺失于 Complete Results 表
```
文件: docs/paper/sections/appendix.tex tab:complete_results (行 14-93)
论文中的值: exp_047 未出现
Registry/实际值: exp_047_frozen_dt_emb_walker_s1, NVE=1.71×, eval_peak=408.79@125K, eval_final=144.22@215K
```
exp\_047 在 three-way table (行 320) 和脚注 (行 325) 中被引用，但在 complete results 表中缺失。其他 frozen Walker 种子 (042, 015b, 057) 都有列出。
**修正建议**: 在 042 和 057 之间添加一行：`047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\times$ & Transient (self-corr.)`

---

### [不一致 #5] NVE 原始值表中 008d 四舍五入不一致
```
文件: docs/paper/sections/appendix.tex 行 132
论文中的值: 4.13 (NVE raw values table)

文件: docs/paper/sections/appendix.tex 行 26 (及全文其他位置)
论文中的值: 4.12×
```
Complete results 表、main Table 1、post-CIVO 表、dual critic 表全部使用 4.12×，唯独 NVE raw values 表写成 4.13。
**修正建议**: 统一为 `4.12`

---

### [不一致 #6] exp\_022b NVE — Registry 值陈旧
```
文件: docs/paper/sections/appendix.tex 行 40
论文中的值: 0.63×
Registry 值: nve_peak = 1.22
```
Registry 记录的 ve\_ratio\_peak=0.218，ve\_ratio\_105K=0.075。论文使用 4-seed mean baseline 归一化得到 0.63×，而 registry 似乎使用单种子 baseline 得到 1.22。论文的归一化规范 (4-seed mean) 是明确声明的 (appendix 行 267)，论文值 0.63 可能正确。
**修正建议**: 更新 registry 中 exp\_022b 的 nve\_peak 为与论文一致的 0.63（使用 4-seed 归一化）

---

## 一致性确认

以下检查点全部一致：

| 检查项 | 论文 | Registry | 状态 |
|--------|------|----------|------|
| 6/6 locomotion CIVO | Walker 4/4 + Cheetah 2/2 | ✓ | 一致 |
| 0/5 manipulation dt-emb-dep CIVO | Stack 0/2 + Peg 0/2 + Pick 0/1 | ✓ | 一致 |
| Walker frozen s0 NVE | 0.19× | 0.194 | 一致 |
| Walker frozen s1 NVE | 1.71× | 1.71 | 一致 |
| Walker frozen s2 NVE | 1.88× | 1.88 | 一致 |
| Cheetah frozen s0 NVE | 1.35× | 1.35 | 一致 |
| PegInsertion s1 trained peak | 3.08× | ve_ratio_peak=3.08 | 一致 |
| PegInsertion s1 frozen peak | 11.32× | ve_ratio_peak=11.321 | 一致 |
| Detector TPR/FPR | 5/5, 2/9 | N/A (14 runs) | 论文内一致 |
| Baseline s1 eval@105K | 915.7 | N/A | 一致 |
| Baseline s1 eval@505K | 970.4 | N/A | 一致 |
| LOEO mean AUROC | 0.981 | N/A | 论文内一致 |
| 022b eval@105K | 300.7 | 300.7 | 一致 |
| 058 eval@215K | 80.46 | 80.46 | 一致 |
| Frozen intervention 5/7 prevention | 7 seeds (W5+C2) | ✓ | 一致 |
| PickCube frozen peak | 8.81× @ 62.5K | exp\_054 (metrics empty but paper cites) | 无法验证 |

---

## 附注：陈旧 Artifact 文件（不影响论文）

- `artifacts/analysis/detector_table.tex`: TPR=3/3, FPR=2/7（旧版 10-run），论文已更新为 5/5, 2/9（14-run）
- `artifacts/_project/paper/nve_sensitivity_table*.tex`: AUROC=0.933（旧版），论文已更新为 0.958
- exp\_053, exp\_054 registry metrics 为空，无法从 registry 交叉验证

**总结**: 6 个不一致（#1 exp\_058 NVE 最严重，直接影响数值准确性），14+ 个检查点一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 782933,
  "duration_api_ms": 967435,
  "num_turns": 30,
  "stop_reason": "end_turn",
  "session_id": "7ea0cafa-bccd-4a6a-979a-adad0a282f84",
  "total_cost_usd": 2.65054115,
  "usage": {
    "input_tokens": 7068,
    "cache_creation_input_tokens": 70538,
    "cache_read_input_tokens": 631034,
    "output_tokens": 24886,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 70538,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3464,
        "cache_read_input_tokens": 78495,
        "cache_creation_input_tokens": 3490,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3490
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1712,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001792,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7068,
      "outputTokens": 24886,
      "cacheReadInputTokens": 631034,
      "cacheCreationInputTokens": 70538,
      "webSearchRequests": 0,
      "costUSD": 1.4138694999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-sonnet-4-6": {
      "inputTokens": 29,
      "outputTokens": 25102,
      "cacheReadInputTokens": 991863,
      "cacheCreationInputTokens": 149521,
      "webSearchRequests": 0,
      "costUSD": 1.2348796499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9a7d6a31-99af-4e83-9f96-99eaf7cf2cbd"
}
```

</details>

---
