---
name: distilled-writing
description: "Neurosymbolic × reward hacking 领域的叙事结构、图表编排、表格设计共识（基于 8 篇深度精读）"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [linc, logic-lm, fover-pei2025, spurious-rewards, qwen-prm-lessons, energy-loss-reward-hacking, inform-reward-hacking, kim-game-formalization, thought-like-pro, deepseek-prover-v15, lightman-verify-step, math-shepherd, rubric-grpo, yue-rlvr-limits, moskovitz-constrained-rlhf, logic-rl, gao-reward-overoptimization, mellgren-prolog-grpo, satlm, karwowski-goodhart-rl, lorp, kwa-catastrophic-goodhart, rafailov-daa-scaling, huang-chi-squared, fover-kamoi2026]
  last_distilled: "2026-05-22T18:00:00Z"
---

## Story Type: 突破局限型 Dominates (6/8, High)
Limitation→diagnosis→principled fix。2/8 (LINC, Logic-LM) 用跨界迁移型。**建议**: 用突破局限型 frame 我们的论文。*Source: FoVer-Pei, Spurious-Rewards, Energy-Loss*

## Hook Modes (8/8, High)
**Capability-reliability gap** (3/8): "LLMs impress at X but fail at Y"。**Hidden system flaw** (3/8): "Standard practice X has unrecognized problem Y"。**Counterintuitive finding** (1/8): 直接抛反直觉结果。**Verification gap** (1/8)。*Source: all 8 deep-read*

## Intro: 5-6 Paragraph Funnel (7/8, High)
P1 motivation → P2 gap → P3 root cause → P4 solution → P5 scope → P6 results。变体: double-hook (LINC), counterintuitive-first (Spurious-rewards)。贡献声明: 3 条 bullets 是众数 (5/8)。*Source: LINC, Logic-LM, InfoRM*

## Figure 1 Consensus (8/8, High)
跨界迁移型 → method_overview (3/8)。突破局限型 → problem_illustration/motivation (4/8)。Teaser_result 仅用于 counterintuitive hook (1/8)。**核心技法**: side-by-side comparison (correct vs incorrect) 出现在 5/8。*Source: LINC, FoVer-Pei, Kim*

## Visualization Patterns (8/8, High)
**Line plots for dynamics** (5/8 主结果图)。**"Diverging lines"**: proposed stays flat, baselines degrade over depth/steps (LINC, Logic-LM, InfoRM)——最强 robustness 叙事。Bar charts for static comparisons (3/8)。Sankey for flow (Kim), T-SNE for latent space (InfoRM, Energy-Loss)。exe_rate × exe_accuracy 分解是 neurosymbolic 标配。*Source: LINC, Logic-LM*

## Table Design (7/8, High)
Row=methods by_category, Col=grouped_by_dataset (4/8)。Highlight: bold_best (3/8), win/tie/lose (2/8, RLHF 标配)。统计: single-run (neurosymbolic) → McNemar (FoVer) → bootstrap SD (LINC)。消融全用 full numbers (6/8)，非 checkmark grid。Baselines 3-12 (median ~6)。LINC 主文零表格——仅当条件少且 depth curves 比数字更强时可行。*Source: Logic-LM, FoVer-Pei, Qwen-PRM*

## Narrative Techniques Worth Stealing
1. **Running example** (FoVer): 同一例子贯穿 Fig1→pipeline→table
2. **Error taxonomy** (LINC, Kim): 分类+similarity metric → "A and B fail differently"
3. **Dual contribution from single theory** (InfoRM): IB → mitigation AND detection
4. **Observation-first** (Energy-Loss): 先 4 模型 empirical，再 theorem
5. **Dialectic** (Spurious-rewards): surprising finding → dismantling generality
6. **Case-study asymmetry** (Kim): 同问题两模型不同 failure modes

## Appendix: Heavy Is Normal (8/8, High)
10+ sections 标配。Main = story，appendix = reproducibility。
