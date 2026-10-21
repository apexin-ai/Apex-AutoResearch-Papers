---
name: distilled-research
description: "Multi-turn LLM depth/gating/attention research patterns — baselines, metrics, experimental design consensus, competitor landscape, and research gaps distilled from 25 papers"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [bai2024mt, gromov2024unreasonable, sun2025curse, li2024measuring, qiu2025gated, peng2024yarn, xiao2024efficient, han2024lm, makkuva2025attention, ildiz2024self, chiang2024chatbot, liu2023lost, luo2025adaptive, ko2024found, zheng2023judging, sirdeshmukh2025multichallenge, fan2020reducing, schuster2022confident, wang2018skipnet, press2022train, dubois2024length, bengio2015scheduled, ranzato2016sequence, lamb2016professor, leblond2018searnn]
  last_distilled: "2026-05-22T13:00:00Z"
---

## Baselines & Metrics

**Baselines**: Llama-2/3 family mandatory (6/8). Full-depth unpruned model as reference. Add GPT-4 for multi-turn eval. 7-8 baselines is median. **Confidence**: high.

**Metrics**: PPL is primary (6/8) but insufficient alone — gromov2024 shows PPL-accuracy decoupling. Pair with MMLU (5/8), HellaSwag (4/8), ARC (3/8), GSM8K (2/8). Reasoning tasks degrade first under depth changes. Multi-turn: instruction stability (li2024), MT-Bench-101 (bai2024). **Confidence**: high.

## Depth Ineffectiveness

Two independent confirmations: (1) gromov2024: ~50% of Llama-2-70B layers removable, sharp phase transition; (2) sun2025: Pre-LN variance grows exponentially → deep Jacobians collapse to identity; LNS (1/√l) fixes this, 66% param savings. **QA robust to pruning; reasoning (GSM8K) degrades immediately** — gating must preserve reasoning paths. **Support**: 2/8. **Confidence**: high.

## Attention Sinks

Softmax constraint dumps excess attention on initial tokens (xiao2024). Positional, not semantic (linebreak replacement proves this). qiu2025 eliminates sinks via sigmoid gate after SDPA: 46.7%→4.8% first-token attention, massive activations 1053→94. **Support**: 2/8. **Confidence**: high.

## Competitor: qiu2025gated (NeurIPS Oral)

Head-specific sigmoid gate after SDPA. Two-factor explanation: non-linearity breaks W_V·W_O low-rank bottleneck + query-dependent sparsity. PPL -0.265, MMLU +2.03, RULER 128k +27.17, <2% overhead. Trained at 15B MoE / 1.7B dense on 3.5T tokens. **Does not address turn-level dynamics** — our differentiation axis. **Support**: 1/8. **Confidence**: high.

## Research Gaps

1. **Turn × depth**: No paper studies how layer behavior changes across conversation turns. Depth work (gromov/sun) is static; turn work (li) ignores depth. **0/25 papers. High confidence.**
2. **Training-time multi-turn**: li2024 (split-softmax) and xiao2024 (StreamingLLM) are inference-only. qiu2025 is training-time but turn-agnostic. **0/25. High confidence.**
3. **Modern exposure bias**: Classical solutions (scheduled sampling, professor forcing) targeted RNNs. No multi-turn transformer equivalent exists. **4/17 abstract. Medium confidence.**

## Experimental Design

- Scale: 130M-7B for pre-training, 7B-70B for analysis. Test ≥2 scales.
- Single run acceptable for pre-training (6/8); report variance for SFT/downstream.
- Simple baselines often match complex: gromov (simple pruning ≈ informed after healing), xiao (4 sink tokens suffice). Always include simplest baseline.
- Ablation: 3-7 dimensions. Must have component ablation + hyperparameter sensitivity.
