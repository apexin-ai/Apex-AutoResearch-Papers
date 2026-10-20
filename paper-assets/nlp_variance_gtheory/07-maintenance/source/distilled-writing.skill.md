---
name: LLM Evaluation Variance — Writing Patterns
description: Narrative strategies, figure/table conventions from LLM evaluation variance papers (16 deep-read, 2018-2026)
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [sclar2024formatting, zhou2026irt, saleva2025beyond, pezeshkpour2024ordering, polo2024tinybenchmarks, magnusson2023reproducibility, shanmugavelu2024floating, lalor2019irt, rodriguez2021leaderboards, henderson2018deep, madaan2024quantifying, song2025exploring, zhang2025tbik, li2025atlas, biderman2024lessons, hua2025flaw, mesting2026hidden, brittlebench2026, yuan2025layercast, kunievsky2025intent, thinkingmachines2025batch, messina2026background, generalizit2024, bui2025seeds, sameprompt2026]
  last_distilled: "2026-05-22T00:00:00Z"
---

## Story Types

**Revealing Hidden Problem** (8/16, HIGH): "X assumed negligible → massive." Sclar (76pp), Shanmugavelu (unique models), Pezeshkpour (85%), Yuan (9%), ThinkingMachines, Brittlebench. Dominant—the subfield's claim IS that ignored variance is large.

**Unifying Framework** (3/16, MEDIUM): Zhou (PSN-IRT), Saleva (variance decomposition), Mesting (TEE). Structure: fragmented observations → unified formalism → multi-domain validation.

**Simplification** (3/16, MEDIUM): Polo (14K→100 examples), Hua (sensitivity is artifact), Magnusson (checklist analysis).

**Cross-domain Transfer** (2/16, LOW but strategic): Lalor (psychometrics→NLP), Mesting (G-theory→ML). Our paper fits here.

## Hook: Shocking Number First (7/16, HIGH)

"76pp" (Sclar), "13-85%" (Pezeshkpour), "80/1000 unique at T=0" (ThinkingMachines), "CIs→79% coverage" (Mesting), "$10K+" (Polo), "ρ 0.30→0.95" (Hua). **Pattern**: concrete number violating expectations in paragraph 1. Never "X is important."

## Tension: 3-4 Level Escalation (HIGH)

Sclar: formatting noise → cross-model invalidity → methodology crisis. Shanmugavelu: sums → kernels → unique runs → certification blocked. Zhou: inconsistent rankings → difficulty ceiling → saturation → failure. **Template**: assumption → contradiction → escalate scope → systemic impact.

## Intro: 4-5 Para + 3 Contributions (8/16)

P1: Context. P2: Existing approaches + limitation. P3: Gap/surprise. P4: 3 contributions (framework + finding + tool). Saleva's intro subsections mirror method structure—effective for framework papers.

## Figure 1: Problem Illustration (9/16, HIGH)

Show problem before solution. Sclar: format examples + accuracy. Zhou: real leaderboard screenshots. Shanmugavelu: variability PDFs. Exception—Polo: teaser scatter (simplification story). **Consensus**: real data not diagrams, key numbers annotated, no method architecture.

## Result Presentation

**Table-driven** (10/16, HIGH): Variance papers use columns=variance components, not metrics (Saleva, Mesting). Rows=models, 4-8 baselines. Bold best (Zhou), asterisks for non-significant (Saleva).

**Figures for trends** (6/16): Line plots for efficiency (Polo), heatmaps for 2D sensitivity (Shanmugavelu), stacked bars for decomposition (Mesting, Brittlebench—subfield signature).

**Stats**: Variance components and correlations over mean±std (only 3/16 use traditional reporting). Decomposed variances, effect sizes, coverage probabilities are the norm.

**Flow**: 4-6 figures. Problem → method → results → decomposition/ablation.

## Our Paper Blueprint

Open with shocking quantified finding → "everyone's CIs are wrong" tension → G-theory as borrowed lens → 2-3 domain demonstrations → stacked-bar variance decomposition as signature visual → D-study projections for practical value → position against IRT alternatives (dominant competitor framework).
