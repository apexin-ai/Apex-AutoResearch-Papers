---
name: xling-calib-direction-writing
description: Writing and visual presentation patterns from 8 papers on cross-lingual calibration and representations
type: skill
---

# Cross-Lingual Calibration — Writing Patterns (8 papers)

## Narrative

**Story type**: "突破局限型" (7/8). Blind spot → reveal → fill. High conf.

**Intro**: 4 paragraphs (5/8). P1 motivation → P2 prior work → P3 gap+approach → P4 three contributions [(1) discovery, (2) method, (3) generalization]. High conf.

**Hooks** (pick one):
- English-centric gap: "Prior work focuses on English, leaving X unexplored" (xiao, zhou). 2/8.
- Name the meta-problem: "Square One Bias" (zhou) — forces acknowledgment.
- Cognitive dissonance: "LLMs are surprisingly well-calibrated" (joshi) — contradicts expectation.
- Pain narrowing: "most dangerous hallucination — confident wrong answers" (ji).

**Tension**: Show standard practice actively fails, not just untried. "Fine-tuning doesn't change alignment" (liu). "Final layer overwrites multilingual signals" (zhou). "Aggregate correlation masks instance-level failure" (ravisankar). 3/8. High conf.

## Insight Delivery

**Layer-wise revelation** (3/8): Probe all layers → phase transition → motivates method. Signature move of this subfield.

**Negative-as-evidence** (2/8): "X doesn't work" proves your design. SAE failure → distributed signal → justifies probe (miao2026coral). SFT doesn't align → explicit alignment needed (liu).

**"Finding the knob"** (ji): Abstract concept → manipulable direction. Provides understanding + intervention.

## Figures

**Figure 1**: 50/50 motivation (analytical) vs method overview (method papers). High conf.

**Layer analysis → line plots** (universal). Overlay conditions on same axes. Never tables for continuous layer data. High conf.

**Xling transfer → heatmaps**. Side-by-side at contrasting layers (xiao: layer 3 vs 19). 3/8.

**Gain highlighting**: Dashed baseline line (miao2026coral), before/after panels (xiao), curve gaps (ji). 4/8.

**Progression**: motivation → method → finding → ablation → surprise. 14+ figures: front-load key results, appendix for per-language. 6/8.

## Tables

**Main result**: rows=methods, cols=datasets×metrics, grouped by dataset. Bold best. 3-4 baselines main, full in appendix. 5/8. High conf.

**Ablations**: full numbers (8/8). No checkmark grids. Delta-from-base rare. High conf.

**Division**: Continuous → figures. Discrete comparisons → tables. Per-language → appendix. Mechanistic = figure-heavy; benchmarking = table-heavy. High conf.

**Appendix**: Main 1-2 models + key langs. Appendix exhaustive. zhou: 15 main, 122 appendix. 6/8.
