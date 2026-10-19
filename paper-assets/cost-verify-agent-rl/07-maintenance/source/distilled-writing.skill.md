---
name: distilled-writing
description: "Agentic RL paper writing patterns: intro structure, narrative techniques, figure/table design consensus from 8 deep-read top-venue papers (2024-2026)"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [tie2025correctbench, verifiagent2025, feng2025gigpo, spear2025, wei2025webagent-r1, digiRL2024, t2po2026, gvpo2026, agent-omit2026, du2025thinkless, kim2025reflact, selfbudgeter2026, tu2025autothink, wan2025derailer-rerailer, xiang2024retrospex, cfgm2025, istar2025, archer2024, agentic-rl-survey-2025, ava2026, xi2025agentprm, kamoi2024self-correction-survey, self-verification-dilemma-2026, zhang2025incentivize-self-verify, mar2025]
  last_distilled: "2026-05-23T00:00:00Z"
---

## Story Type & Intro

7/8 use **突破局限型**. Default for this field. (高)

**Intro 4-5 paragraphs**: P1 context+promise → P2 problem → P3 existing fixes fail → P4 our solution (explicit research question per GiGPO, or labeled "OUR KEY INSIGHT" per T2PO) → P5 contributions (3-5 bullets). (高, 8/8)

**Intro comparison table**: 3/8 (VerifiAgent, GVPO, WebAgent-R1) embed checkmark-grid Table 1 in intro: "we're the only method with all properties." Highly effective. (高)

## Hook & Argumentation

- **Promise-vs-reality gap** (4/8): "VLMs promise but fail at 8%" (DigiRL). Most common hook. (高)
- **Name the failure mode** (2/8): "hesitation" (T2PO), "entropy collapse" (SPEAR). (中)
- **Show-failure-then-fix** (3/8): SPEAR embeds entropy collapse figures IN method section before presenting fix. DigiRL decomposes failure modes to explain WHY RL helps. (高)
- **Near-zero cost preemption**: GiGPO: "<0.002% overhead" preempts "must be expensive" objection. (中)
- **Negative result as validation**: WebAgent-R1 R1-Zero ablation (5.7%) validates SFT→RL pipeline. (中)

## Figure Consensus

**Fig 1**: method_overview 5/8, teaser_result 2/8, motivation 1/8. Default: left-to-right pipeline with color-coded stages. GiGPO uses 3-column (problem→naive→ours). (高)

**Training dynamics**: 5/8 include success-rate-over-iterations line plots with multi-seed overlay. T2PO: orange collapse regions. WebAgent-R1: dashed phase annotations. (高)

**Composite figures**: T2PO/SPEAR combine 3+ subplots (perf+diagnostic+efficiency) in one figure. (中)

## Table Consensus

**Main result table**: Rows = methods by category (prompting→SFT→RL), cols = datasets. 8-13 baselines. (高, 8/8)

**Highlight**: bold_best 5/8; bold_best+underline_second 2/8 (GVPO/T2PO). (高)

**Variance**: mean±std across 3 seeds (GiGPO/T2PO/DigiRL). 3/8 report no std — reviewer risk. (高)

**Ablation**: Component removal dominates (T2PO: w/o RFT, w/o TTI, w/o TDS). Hyperparameter sensitivity in appendix. (中)

## Figure-Table Division

Main results→table; training dynamics→line plots (5/8); ablation→bar chart or table; failure/behavior analysis→bar chart (DigiRL/GVPO); hyperparameter sensitivity→appendix; qualitative examples→appendix figures. (高)
