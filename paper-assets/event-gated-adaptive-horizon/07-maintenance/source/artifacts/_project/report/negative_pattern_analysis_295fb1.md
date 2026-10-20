# Negative Experiment Pattern Analysis

**Date**: 2026-05-28 | **Scope**: 43 negative out of 208 total experiments (21%)

## 1. By Intervention Type (failure rates)

| Intervention | Total | Negative | Rate | Key Pattern |
|---|---|---|---|---|
| TCN (noise on dt_emb) | 12 | 10 | **83%** | Binary outcome: full suppress or runaway. Fails on Cheetah at all σ (0.2/0.5/1.0) |
| RAVE (value cap) | 2 | 2 | **100%** | EMA anchor tracks biased values; structurally unfit for CIVO |
| SGS (gradient stop) | 15 | 5 | 33% | Full-SGS: 0/3 Cheetah elimination (exp_021 NVE=9.94×); obs-SGS: 1/6 prevention |
| Dual/wide critic | 11 | 4 | 36% | Fails cross-env: Cheetah NVE=1.8-3.6 (exp_034/037); Walker s2 non-CIVO collapse |
| Event-gated design | 3 | 3 | 100% | Hard Gumbel gate structurally unstable (exp_003-005) |
| dt=1 imag mitigation | 6 | 4 | 67% | exp_008e_v3_s3 NVE=4.02 (unexpected CIVO despite dt=1 imag); exp_070 eval=148 stagnation |

## 2. By Environment

| Environment | Neg/Total | Rate | Pattern |
|---|---|---|---|
| Walker Walk | 28/112 | 25% | Primary testbed; most intervention failures here |
| Cheetah Run | 4/33 | 12% | Lower count but higher severity: NVE 8-108×; all TCN/SGS interventions fail |
| Cartpole | 1/2 | 50% | No CIVO triggered (expected); "negative" = degradation from subsample+H=8 config itself |
| Hopper | 2/10 | 20% | Extension runs: frozen/trained both degrade at 150K |

## 3. Systematic Failure Patterns

**P1: Cross-environment transfer failure.** Interventions tuned on Walker fail on Cheetah. TCN σ=0.2 works on 2/4 Walker seeds but 0/1 Cheetah. Dual-critic prevents CIVO on Walker (7/11 success) but fails on Cheetah (exp_034 NVE=1.8, exp_037 NVE=3.6). CIVO severity scales ~2-20× higher on Cheetah, overwhelming interventions calibrated for Walker's milder form.

**P2: Gradient pathway redundancy.** SGS blocking any single pathway (reward: exp_016e; obs: exp_025/026) or all pathways (exp_018) achieves at best partial mitigation. Full-SGS: seed 1 NVE=1.66 (partial), seed 2 collapsed. On Cheetah, full-SGS NVE=9.94× (exp_021). CIVO co-adapts through whichever gradient channel remains open. This is a method-level limitation, not a tuning issue.

**P3: Seed sensitivity of forward-pass interventions.** TCN σ=0.2 on Walker: 2/4 seeds full suppression (NVE<1.0×), 2/4 seeds runaway (NVE 2.8-3.0×, exp_029b/029d). No intermediate outcomes. The binary on/off behavior suggests TCN gates a bifurcation rather than smoothly attenuating CIVO.

**P4: Non-CIVO collapse mode.** exp_038 (dual-critic Walker s2): eval 354→121, NVE=0.3× (no value overestimation). exp_070 (008e_v3 s0): eval=148, NVE=0.8×. These are performance failures unrelated to CIVO, revealing that the base config (subsample+H=8) causes independent degradation in some seeds.

## 4. Configuration Correlations

- **dt_embed_dim=32 (trained)**: 9/16 CIVO-positive in multi-joint locomotion. The trained embedding is the dominant CIVO trigger.
- **Subsample ON + H=8**: Even without CIVO, this config underperforms baseline by 40-70% (exp_008f mean=302 vs baseline 916). The short horizon itself is harmful.
- **Frozen dt_emb**: 0/16 CIVO across all environments. Eliminates CIVO but doesn't recover performance (exp_015b eval=204, exp_047 eval=144).

## 5. Re-run Candidates

| Candidate | Rationale | Priority |
|---|---|---|
| Dual-critic + frozen dt_emb (Cheetah) | Dual-critic works on Walker; frozen eliminates CIVO. Combining may address Cheetah transfer gap. | Low (already well-characterized) |
| TCN σ=0.3 (Walker) | σ=0.2 has 50% success, σ=0.5 overdoses. Intermediate dose untested. | Low (binary outcome suggests no sweet spot) |
| None recommended for SGS/RAVE | Fundamentally limited by gradient redundancy / EMA tracking bias | Not viable |

## 6. Key Takeaway

Negative results reveal that CIVO is not a single-pathway defect amenable to targeted blocking. It is an emergent property of trained temporal embeddings co-adapting with the world model under multi-rate data, operating through redundant gradient channels. Interventions that work on Walker (moderate CIVO, NVE 2-5×) fail on Cheetah (severe CIVO, NVE 8-108×) because they suppress symptoms rather than the root cause. The only reliable elimination is removing the trained embedding (frozen or dt_embed_dim=0), which eliminates the phenomenon entirely but also removes the temporal conditioning capability.
