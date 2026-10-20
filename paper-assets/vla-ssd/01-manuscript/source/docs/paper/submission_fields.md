# OpenReview Submission Fields — CoRL 2026

## Title

Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis

## TL;DR

Cross-architecture analysis of three VLAs reveals that VLM-to-VLA fine-tuning produces exit collapse in action-probe decodability while L1 instruction attention is inherited from pretrained backbones.

## Abstract

When vision-language models are fine-tuned for robotic action prediction, which representational changes reflect training and which are inherited from the pretrained backbone? We conduct a cross-architecture representational analysis of three VLAs---OpenVLA, TracVLA, and NORA---across four LIBERO task suites, comparing trained and reference checkpoints. Using layer-wise action probes, attention profiling, and counterfactual instruction perturbations, we find that the two tested VLM-to-VLA transitions exhibit pronounced peak-to-exit reductions in action-probe decodability, whereas the tested VLA-to-VLA transition shows only small fluctuations. An NLP finetuning control on each of the three backbone families (Delta R^2 = 0.000) is consistent with exit collapse being specific to action-oriented training rather than generic fine-tuning. Trained action-producing VLAs show medium-to-large sensitivity to instruction perturbations (d = 0.45--1.52), while L1 instruction-dominant attention largely pre-exists in the underlying pretrained backbones. These results provide a cross-architecture characterization of instruction-related representations in action-finetuned VLAs and clarify which observed patterns are training-associated versus inherited from reference models.

## Keywords

1. Vision-Language-Action models
2. Representational analysis
3. Action fine-tuning
4. Exit collapse
5. Instruction attention routing
6. Cross-architecture evaluation
7. Robotics
8. Probing methodology

## Supplementary Material Summary

The appendix (25 pages) contains:

- **Architecture details** (A.1): Summary table of OpenVLA, TracVLA, NORA backbones and reference baselines
- **OpenVLA deep dive** (A.2--A.3): Cross-instruction probes, L1 attention gradient, counterfactual perturbation, dose-response ablation, R^2 localization
- **Counterfactual sensitivity details** (A.4): Per-condition rankings for all 8 action-producing cells; metric constraints on trained-reference comparison; NORA cosine distance details
- **Metric sensitivity** (A.5--A.6): CKA vs RSA divergence analysis; linear CKA and RDM kernel CKA comparisons
- **Representation source analyses** (A.7--A.9): Branch-split (DINOv2 vs SigLIP), RSA across sources, per-layer RSA profiles
- **Training stage comparisons** (A.10): Three-condition action decoding (random / Llama-2 base / VLA-trained)
- **Ablation analyses** (A.11--A.12): Random-subset ablation; action trajectory analysis with dose-response gradients
- **Robustness analyses** (A.19): Distance metric invariance, per-DOF decomposition, permutation test, probe seed sensitivity (single-architecture 5-seed + cross-architecture 4-seed), bootstrap confidence intervals for Delta R^2 (1000-iteration MCCV + permutation test p=0.008), demonstration subsample sensitivity, statistical power analysis, Delta R^2 threshold robustness
- **Cross-suite validation** (A.18): LIBERO-Spatial replication of all analyses
- **Instruction classification** (A.21): Dense layer profiles, LOOCV validation, QA probes, cross-architecture profiles
- **Statistical controls** (A.22--A.27): L1 attention decomposition, per-dimension MAE, per-task R^2, task complexity analysis, specificity controls, paired effect sizes
- **Cross-architecture R^2 design** (A.29): 2x2 factorial (architecture x training) with TOST equivalence testing
- **Bonferroni correction** (A.30): Global multiple comparison correction across 63 tests
- **NLP finetuning controls** (A.34): Llama-2-7b-chat, Phi-3-mini-4k-instruct, Qwen2.5-3B-Instruct — all Delta R^2 = 0.000
- **Claim-evidence summary** (A.35): Evidence ladder mapping claims to supporting analyses

## Submission Checklist

- [x] Paper PDF (8-page body + references + appendix)
- [x] Abstract submitted (DDL: 5/26)
- [x] Code/data availability statement: "Code and data will be released upon acceptance"
- [ ] Supplementary PDF (same file, appendix starts p13)
- [ ] Author information (to be de-anonymized after review)
