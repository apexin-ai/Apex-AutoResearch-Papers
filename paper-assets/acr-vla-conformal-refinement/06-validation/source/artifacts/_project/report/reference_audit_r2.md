# Method Attribution Audit — ACR-VLA Paper (R2)

**Date**: 2026-05-15
**Scope**: All citations across Introduction, Method, Experiments, Related Work, Discussion sections
**Method**: Web search verification of each citation's method description against actual paper content

---

## Summary

- **Total citations audited**: 30 unique references
- **Critical errors found & fixed**: 2 (ReconVLA attribution in intro + related work)
- **Bib title error found & fixed**: 1 (ACP+CBF)
- **Minor issues flagged**: 2 (SC-VLA classification, LIBERO-Plus specific numbers)
- **All other attributions**: ✅ Verified correct

---

## FIXED: ReconVLA (chen2026reconvla) — CRITICAL

### Error
**Intro**: "operates as an uncertainty quantification framework rather than an action improvement method"
**Related Work**: "providing a principled uncertainty quantification framework that operates without retraining but does not modify the VLA's actions"

### Reality
ReconVLA uses CQR-based uncertainty estimation to **guide action selection** under generative variability and performs OOD/failure detection. It DOES influence action selection, contradicting "does not modify the VLA's actions."

### Fix Applied
**Intro**: → "applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals."
**Related Work**: → "applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining."

### D034 Alignment
Now correctly positions ReconVLA as a **UQ-guided approach** (same domain, different route) rather than a direct competitor or a passive UQ tool. The gap statement ("no existing inference-time method combines multi-sample conformal selection with bounded residual correction") remains valid since ReconVLA does UQ-guided selection but not learned residual correction.

---

## FIXED: ACP+CBF Bib Title (zhou2025acp_cbf)

### Error
Bib entry title: "Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning"
Actual paper title: "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction"

### Fix Applied
Updated bib entry title to match actual paper.

---

## FLAGGED (not changed): SC-VLA "residual RL" Classification

### Current Text
"SC-VLA performs online action refinement through sparse world imagination combined with residual RL"

### Observation
SC-VLA uses an Online Action Refinement (OAR) module with progress-dependent dense rewards and residual adjustments. The term "residual RL" is defensible (it does use RL with residual adjustments) but could be confused with the RPL framework (Silver et al.). More precise would be "RL-based action refinement with progress-dependent rewards."

### Recommendation
Minor issue — acceptable as-is. Consider "online RL" instead of "residual RL" if a future revision refines the taxonomy.

---

## FLAGGED (not changed): LIBERO-Plus Specific Numbers

### Current Text (Intro)
"π₀ drops from 94.2% to 6.6% under robot initial-state perturbation, and UniVLA from 95.2% to 4.3% under camera viewpoint changes"

### Observation
- LIBERO-Plus tests π0, π0-fast, UniVLA, OpenVLA-OFT among others
- Web search confirms UniVLA achieves ~95.5% baseline (close to cited 95.2%)
- General trend (dramatic drops under perturbation) is confirmed
- Exact numbers (94.2%, 6.6%, 95.2%, 4.3%) could not be precisely verified via web search alone

### Recommendation
Verify exact numbers against LIBERO-Plus Table 1 before submission. The general claim is sound.

---

## Verified Correct: All Other Citations

### Training-time VLA Robustness
| Citation | Attribution | Verdict |
|----------|-----------|---------|
| `robustvla2025` | RL post-training + Jacobian regularization + smoothness regularization | ✅ Confirmed |
| `srpo2025` | Self-referential RL fine-tuning, own successful rollouts as references, latent world model | ✅ Confirmed |
| `digflow2025` | Distributional discrepancy as gating signal to rebalance representation-level control | ✅ Confirmed |
| `liu2026ttvla` | Test-time RL with step-by-step progress rewards | ✅ Confirmed |

### Inference-time VLA Methods
| Citation | Attribution | Verdict |
|----------|-----------|---------|
| `a2c2_2025` | Lightweight per-step correction head for action chunks, no selection stage | ✅ Confirmed |
| `li2025vlapilot` | Evolutionary diffusion optimization + MLLM verifier, 2.41s/step | ✅ Confirmed |
| `liu2026scvla` | Online action refinement via sparse world imagination + RL | ✅ (see flag above) |

### Conformal Prediction in Robotics
| Citation | Attribution | Verdict |
|----------|-----------|---------|
| `angelopoulos2023gentle` | Distribution-free coverage guarantees under exchangeability | ✅ Confirmed |
| `braun2025cgs` | CGS: Mahalanobis-based nonconformity scores for multivariate CP | ✅ Confirmed |
| `zhao2024conformalized` | CP for high-DOF action mappings in shared autonomy teleoperation | ✅ Confirmed |
| `wang2025cploop` | CP regions as feedback constraints in trajectory optimization | ✅ Confirmed |
| `zhou2025acp_cbf` | Adaptive CP + control barrier functions for safe RL | ✅ Confirmed |

### Residual Policy Learning
| Citation | Attribution | Verdict |
|----------|-----------|---------|
| `silver2018residual` | Introduced RPL framework for classical controllers, zero-initialization | ✅ Confirmed |
| `jiang2024transic` | Gated residual policy for sim-to-real transfer | ✅ Confirmed |
| `xiao2026pld` | Frozen VLA + lightweight residual actors + off-policy RL + distillation | ✅ Confirmed |
| `pan2025drc` | Decaying relative correction for online imitation learning via teleoperation | ✅ Confirmed |

### Uncertainty Quantification for VLAs
| Citation | Attribution | Verdict |
|----------|-----------|---------|
| `xing2026diu` | Closed-form posterior covariance via velocity field divergence (single-pass) | ✅ Confirmed |
| `gu2025safe` | Multitask failure detector on VLA features + functional CP calibration | ✅ Confirmed |
| `zollo2025vla_calibration` | First systematic VLA calibration study, prompt ensembles + Platt scaling | ✅ Confirmed |

### Foundation / Infrastructure
| Citation | Attribution | Verdict |
|----------|-----------|---------|
| `black2024pi0` | π₀: flow-matching VLA | ✅ |
| `shukor2025smolvla` | SmolVLA: 450M flow-matching VLA | ✅ |
| `lipman2023flow` | Flow matching for generative modeling | ✅ |
| `liu2023libero` | LIBERO benchmark | ✅ |
| `fei2025liberoplus` | LIBERO-Plus robustness analysis | ✅ (numbers flagged) |
| `ledoit2004well` | Ledoit-Wolf shrinkage covariance estimation | ✅ |
| `ross2011dagger` | DAgger / compounding error in imitation learning | ✅ |

---

## Pre-Submission Checklist
- [x] ReconVLA attribution fixed (intro + related work)
- [x] ACP+CBF bib title corrected
- [ ] Verify LIBERO-Plus exact numbers (94.2%, 6.6%, 95.2%, 4.3%) against Table 1
- [ ] Consider refining SC-VLA "residual RL" → "online RL" (optional)
