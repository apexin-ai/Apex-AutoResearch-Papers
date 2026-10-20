---
name: gen-depth-contamination writing patterns
description: Narrative structures, figure/table conventions, and presentation strategies from 12 deep-read model-collapse and contamination-detection papers (2024-2026).
---

## Narrative Types

**化繁为简型 dominates (5/12):** Kazdan, Zawalski, Zhang, Amin, DSIR. Move: "field conflated X with Y; separate them." (高)

**突破局限型 second (4/12):** Drayson, Schaeffer, Shi, Dohmatob fill blind spots or provide formalization. (高)

## Hooks & Tension

**Hooks:** Internet contamination alarm (4/12), scaling paradigm threat (Dohmatob), data scarcity (Amin), definitional confusion (Schaeffer).

**Tension:** Reconciling conflicting literature dominates (Kazdan: "both camps right"). Secondary: methods are crude/ungrounded (Zawalski, Zhang). Theory: "no formal characterization" (Dohmatob).

## Contribution Framing

Three contributions is the mode (6/12), numbered list at intro end. Template: (1) observation, (2) mechanism, (3) validation. Theory papers list more. (高)

## Figure 1

**Problem/motivation first (7/12)**, not solution. Side-by-side comparison dominates. Front-loading empirical evidence with problem setup is strongest: Zhang ROC, Zawalski log-prob contrast, Shi degradation strips. (高)

## Result Visualization

**Line plots dominate (8/12)** with generation/steps as x-axis, diverging trajectories. Scatter for correlation anchors (Shi r=0.91, DSIR r=0.82). Theory papers overlay analytical curves on empirical points (Dohmatob). (高)

**Gain highlighting:** Oracle comparison flip (Drayson: beats oracle), contrastive scatter (Shi), clean cluster separation (Zawalski: red/blue), component-addition (Zhang: +9.3%/+7.0%/+16.8%). (6/12)

## Table Design

Row=methods, Col=datasets×metrics (6/12). Bold best. 2-6 baselines. (高)

**Ablation:** Component-addition clearest (Zhang); no checkmark grids in this field. Delta-from-base preferred.

**Reporting:** mean±std 3-5 seeds (4/12) vs single run (4/12). Theory/detection=single; empirical ML=seeds. Theory papers skip tables entirely (Dohmatob: 0 tables). (中)

## Figure Narrative Flow

Consensus (8/12): Fig1 (problem) → Fig2 (method) → Figs3-4 (results as lines) → rest (ablation). Collapse papers escalate: toy → benchmark → practical. Detection papers: models×datasets grid. (高)

## Techniques Worth Imitating

1. **Oracle comparison flip** (Drayson): imperfect beats oracle; reframes error as feature (高)
2. **Meta-analysis as evidence** (Schaeffer): annotating 28 papers = empirical finding (高)
3. **Single-number anchor** (Shi r=0.91, DSIR r=0.82): one coefficient front-loaded pre-empts skepticism (高)
4. **Intuition-externalizing Fig1** (Zhang): same prob, different context; makes z-score obvious (高)
5. **Skill disappearance** (Dohmatob): GCD skills vanish = scaling theory made visceral (中)
6. **Dual inversion framing** (Amin): memorable conceptual handle for reviewers (中)
