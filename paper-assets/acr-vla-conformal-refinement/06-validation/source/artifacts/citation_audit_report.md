# Citation & Method Attribution Audit Report

**Date**: 2026-05-15
**Scope**: All .tex files in `artifacts/_project/paper/`, `artifacts/_project/paper/sections/`, `docs/paper/`; `references.bib`
**Verdict**: **2 issues require fix before submission. See below.**

---

## 1. Citation Key Completeness

### All 29 cited keys exist in references.bib

| # | Key | Sections Used | Status |
|---|-----|---------------|--------|
| 1 | a2c2_2025 | intro, related, method | ✅ |
| 2 | angelopoulos2023gentle | related | ✅ |
| 3 | black2024pi0 | intro | ✅ |
| 4 | braun2025cgs | intro, related, method | ✅ |
| 5 | chen2026reconvla | intro, related, method | ✅ |
| 6 | digflow2025 | intro, related | ✅ |
| 7 | fei2025liberoplus | intro | ✅ |
| 8 | gibbs2021aci | intro, method | ✅ |
| 9 | gu2025safe | intro (old), related | ✅ |
| 10 | jiang2024transic | related, method | ✅ |
| 11 | ledoit2004well | method, experiments | ✅ |
| 12 | li2025vlapilot | intro (new), related | ✅ |
| 13 | lipman2023flow | intro (new), method | ✅ |
| 14 | liu2023libero | intro, method, experiments | ✅ |
| 15 | liu2026scvla | related | ✅ |
| 16 | liu2026ttvla | intro (new), related | ✅ |
| 17 | pan2025drc | related | ✅ |
| 18 | ross2011dagger | related, method, experiments | ✅ |
| 19 | robustvla2025 | intro, related | ✅ |
| 20 | silver2018residual | related, method | ✅ |
| 21 | shukor2025smolvla | intro, method, experiments | ✅ |
| 22 | srpo2025 | intro, related | ✅ |
| 23 | wang2025cploop | intro (old), related | ✅ |
| 24 | xiao2026pld | related, method | ✅ |
| 25 | xing2026diu | related | ✅ |
| 26 | yuan2026ups | intro (old) | ✅ |
| 27 | zhao2024conformalized | related | ✅ |
| 28 | zhou2025acp_cbf | related | ✅ |
| 29 | zollo2025vla_calibration | related | ✅ |

**No missing bib entries. No dangling \cite{} keys.**

### 14 bib entries not cited (unused)

barber2023conformal, brohan2023rt2, chi2023diffusion_policy, cosmos_policy_2026, gal2016dropout, ghosh2024octo, kim2024openvla, lakshminarayanan2017ensembles, luan2026snapflow, romano2019cqr, shafer2008tutorial, tang2026shifting, vla_gse_2026, zhong2026acotvla

These don't cause compilation errors but should be cleaned before submission if unused in the final draft.

---

## 2. Method Attribution Audit

### ⚠️ ISSUE 1: chen2026reconvla — cross-section inconsistency (partially fixed)

The old `introduction.tex` had a confirmed error (D034):

> "ReconVLA draws multiple action samples and selects the one closest to the sample mean, using scalar Euclidean distance as an uncertainty proxy."

This was fixed in `sections/introduction.tex` to:

> "ReconVLA applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states, but operates as an uncertainty quantification framework rather than an action improvement method."

**However, related_work.tex and method.tex have NOT been updated to match the D034 repositioning:**

- `related_work.tex` line 15: "uses conformal prediction over multiple VLA samples for **action selection** and failure detection" — still describes ReconVLA as doing "action selection," contradicting the new introduction's framing as "UQ framework, not action improvement."
- `method.tex` line 42: "inspired by the **conformal selection frontend** of ReconVLA" — still attributes a "selection frontend" to ReconVLA.

**Fix needed**: Align related_work.tex and method.tex with the D034 decision. Related work should describe ReconVLA's UQ/failure-detection capabilities without implying it does sample selection in ACR-VLA's sense. Method should rephrase the argmin selection as inspired by conformal scoring methodology (braun2025cgs) rather than by a ReconVLA "selection frontend."

### ⚠️ ISSUE 2: braun2025cgs — potential CGS naming misattribution

`related_work.tex` line 30: "Braun et al. develop Conformalized Gaussian Scoring (CGS)"

The bib entry for braun2025cgs is titled **"Multivariate Standardized Residuals for Conformal Prediction"** — NOT "Conformalized Gaussian Scoring." The term "CGS" appears to be coined by this paper (ACR-VLA), not by braun2025cgs.

**Fix needed**: Either (a) verify that braun2025cgs actually uses the term "CGS" (in which case no fix needed), or (b) rephrase to "we build upon the Mahalanobis-based nonconformity scoring of Braun et al." and introduce "CGS" as our own naming.

### ✅ Verified attributions (22 citations, all accurate based on paper titles)

| Citation | Attributed Method/Concept | Title Match |
|----------|--------------------------|-------------|
| srpo2025 | Self-referential policy optimization | ✅ Title: "SRPO: Self-Referential Policy Optimization..." |
| robustvla2025 | RL post-training + robustness regularization | ✅ Title: "RobustVLA: Robustness-Aware Reinforcement Post-Training..." |
| digflow2025 | Discrepancy-guided flow matching | ✅ Title: "DiG-Flow: Discrepancy-Guided Flow Matching..." |
| liu2026ttvla | Test-time RL adaptation | ✅ Title: "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning" |
| a2c2_2025 | Per-step correction for action chunks | ✅ Title: "Leave No Observation Behind: Real-time Correction for VLA Action Chunks" |
| liu2026scvla | Online refinement via sparse world imagination | ✅ Title: "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination" |
| li2025vlapilot | Evolutionary diffusion for VLA steering | ✅ Title: "...Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion" |
| gu2025safe | Multitask failure detection | ✅ Title: "SAFE: Multitask Failure Detection..." |
| silver2018residual | Residual policy learning framework | ✅ Title: "Residual Policy Learning" |
| jiang2024transic | Sim-to-real with binary gating | ✅ Title: "TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction" |
| xiao2026pld | Residual RL with bounded corrections | ✅ Title: "Self-Improving VLA Models with Data Generation via Residual RL" |
| pan2025drc | Decaying relative correction | ✅ Title: "DRC: Decaying Relative Correction for Policy Refinement" |
| xing2026diu | Closed-form posterior covariance for flow matching | ✅ Title: "Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching" |
| zollo2025vla_calibration | VLA confidence calibration | ✅ Title: "Confidence Calibration in Vision-Language-Action Models" |
| zhao2024conformalized | CP for teleoperation uncertainty | ✅ Title: "Conformalized Teleoperation: Confidently Mapping Human Inputs..." |
| zhou2025acp_cbf | Adaptive CP + control barrier functions | ✅ Title: "Adaptive Conformal Prediction with Control Barrier Functions..." |
| wang2025cploop | CP as feedback in trajectory optimization | ✅ Title: "Conformal Prediction in The Loop..." |
| yuan2026ups | Uncertainty-aware policy steering | ✅ Title: "When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering" |
| angelopoulos2023gentle | CP tutorial / distribution-free UQ | ✅ Title: "A Gentle Introduction to Conformal Prediction..." |
| ledoit2004well | Shrinkage covariance estimation | ✅ Title: "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices" |
| lipman2023flow | Flow matching for generative modeling | ✅ Title: "Flow Matching for Generative Modeling" |
| gibbs2021aci | Adaptive conformal inference under shift | ✅ Title: "Adaptive Conformal Inference Under Distribution Shift" |

### ✅ Other attributions verified

- fei2025liberoplus: LIBERO-Plus robustness benchmark ✅
- liu2023libero: LIBERO benchmark ✅
- shukor2025smolvla: SmolVLA 450M VLA ✅
- black2024pi0: pi0 flow-matching VLA ✅
- ross2011dagger: Compounding error / DAgger ✅
- lakshminarayanan2017ensembles (unused, in bib only) ✅
- gal2016dropout (unused, in bib only) ✅

---

## 3. File Version Status

| File | Location | Status |
|------|----------|--------|
| introduction.tex | artifacts/_project/paper/ | OLD — contains confirmed chen2026reconvla error |
| introduction.tex | artifacts/_project/paper/sections/ | NEWER — chen2026reconvla fixed per D034, but related_work/method not aligned |
| related_work.tex | both locations | Needs update for D034 alignment + CGS naming check |
| method.tex | both locations | Needs update for D034 alignment (ReconVLA "selection frontend" phrasing) |
| experiments.tex | both locations | No attribution issues |
| abstract.tex | artifacts/_project/paper/ | No citations, no issues |
| references.bib | artifacts/_project/paper/ | Complete, no missing entries |

---

## 4. Verdict

**Audit NOT passed. 2 blocking issues remain:**

1. **chen2026reconvla D034 alignment**: related_work.tex and method.tex still describe ReconVLA as doing "action selection," contradicting the new introduction's UQ-framework positioning. All sections must be consistent.

2. **braun2025cgs CGS naming**: Verify whether braun2025cgs uses the term "CGS." If not, rephrase attribution to avoid misattributing our coined terminology.

**Once these 2 issues are resolved, the audit can be marked as passed and the ROADMAP blocking item cleared.**
