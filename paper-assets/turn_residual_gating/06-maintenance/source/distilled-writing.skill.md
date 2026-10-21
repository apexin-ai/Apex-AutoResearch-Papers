---
name: distilled-writing
description: "Narrative structure, figure/table design, and visual rhetoric patterns for multi-turn/depth/gating LLM papers — distilled from 8 deep-read papers at ICLR/NeurIPS/ACL/COLM 2024-2025"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [bai2024mt, gromov2024unreasonable, sun2025curse, li2024measuring, qiu2025gated, peng2024yarn, xiao2024efficient, han2024lm, makkuva2025attention, ildiz2024self, chiang2024chatbot, liu2023lost, luo2025adaptive, ko2024found, zheng2023judging, sirdeshmukh2025multichallenge, fan2020reducing, schuster2022confident, wang2018skipnet, press2022train, dubois2024length, bengio2015scheduled, ranzato2016sequence, lamb2016professor, leblond2018searnn]
  last_distilled: "2026-05-22T13:00:00Z"
---

## Story Types

突破局限型 dominates (4/8): "X inadequate → diagnose → fix." 化繁为简型 secondary (3/8): "partial solutions → unify." For turn-residual gating, 突破局限型 fits. **7/8, high.**

## Hooks

1. **Concrete failure**: li2024 GPT-3.5 screenshot; xiao2024 PPL 5→5158. Visceral. (2/8, high)
2. **Provocative title**: gromov "Unreasonable Ineffectiveness"; sun "Curse of Depth." (2/8, medium)
3. **Genealogy**: peng2024 PI→NTK→YaRN evolution. (1/8, medium)

## Figure 1

**Multi-panel mandatory** (7/8). Dominant type: method_overview (5/8), often double-duty showing method + key result. Best examples: qiu2025 (3-panel: positions + bars + loss curves), sun2025 (architecture + "66% fewer params" annotation). Include quantitative result in Fig 1 — pure method diagrams without numbers are less compelling. **Support**: 7/8. **Confidence**: high.

## Result Visualization

- **Line plots for trends** (6/8): pruning fraction, context length, training steps, turns. "Flat-then-cliff" (gromov) and "diverging curves" (xiao, han) are visually powerful.
- **Heatmaps for attention/similarity** (3/8): before/after attention maps are standard proof for mechanism papers.
- **Scatter for trade-offs** (1/8): li2024's Pareto front (stability vs performance) ideal for multi-objective methods.
**Support**: 6/8. **Confidence**: high.

## Table Design

**Row organization**: by_category (5/8) — group methods by type. **Highlight**: bold_best (4/8); dramatic numerical contrast can self-highlight (xiao: 5158 vs 5.40). **Reporting**: single run for pre-training (6/8); mean±std for SFT. **Ablation style**: full_numbers dominates (6/8); include mechanism columns alongside performance (qiu2025: gate-score + M-Act + F-Attn with PPL). **Support**: 6/8. **Confidence**: high.

## Figure vs Table Division

Trends → figures (gromov: 1 table, all figures — phase transition needs curves). Point comparisons → tables. Standard: main results table + mechanism figures + hyperparameter appendix. **5/8, high.**

## Surgical Ablations

Most persuasive ablations change exactly one thing to kill one hypothesis: xiao2024's linebreak replacement (sinks are positional, not semantic), qiu2025's Switch-Heads 1-expert reduction (gating, not routing, drives gains), gromov2024's simple-vs-informed pruning (similarity analysis unnecessary after healing). Design each ablation to disprove one alternative explanation. **Support**: 3/8. **Confidence**: high.

## Intro Structure

4-6 paragraphs typical. Pattern: P1=problem + urgency, P2=existing solutions + their limits, P3=this paper's insight, P4=contributions list (3-4 items, numbered or bulleted), P5=results summary. Contributions framed as discovery+solution pairs work best (sun2025: "identify curse + propose fix"). **Support**: 7/8. **Confidence**: high.
