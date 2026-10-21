---
name: distilled-research
description: "Neurosymbolic reasoning × reward hacking/RLVR 领域的实验设计共识、方法论趋势、竞品定位与研究空白"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [linc, logic-lm, fover-pei2025, spurious-rewards, qwen-prm-lessons, energy-loss-reward-hacking, inform-reward-hacking, kim-game-formalization, thought-like-pro, deepseek-prover-v15, lightman-verify-step, math-shepherd, rubric-grpo, yue-rlvr-limits, moskovitz-constrained-rlhf, logic-rl, gao-reward-overoptimization, mellgren-prolog-grpo, satlm, karwowski-goodhart-rl, lorp, kwa-catastrophic-goodhart, rafailov-daa-scaling, huang-chi-squared, fover-kamoi2026]
  last_distilled: "2026-05-22T18:00:00Z"
---

## Two Converging Streams (25/25, High)
Neurosymbolic pipelines (LLM→solver, 7/25) 和 reward signal analysis (12/25) 交汇于: solver traces 提供的是真实学习信号还是会被 game？PRM (4/25) 桥接两侧。

## Dataset Consensus (25/25, High)
Logic: FOLIO (5/25) + ProofWriter (4/25)。Math: MATH (6/25) + GSM8K (4/25)。RLHF: AlpacaFarm + Anthropic-HH。新兴: ProcessBench (step-level F1), Multi-LogiEval (depth-stratified)。*Source: Logic-LM, Qwen-PRM*

## Executability Bottleneck (5/25, High)
FoVer: GPT-4o 频繁产出不可执行 Z3。Logic-LM: AR-LSAT 仅 39.8% exec rate。Kim: compilation 跨阶段下降。仅 Logic-LM 有 self-refinement 且限于语法。**exe_rate × exe_accuracy 分解**是标准诊断。*Source: FoVer-Pei, Logic-LM*

## GRPO as RL Standard (4/25, High)
共识 recipe: lr=5e-7, 8×A100, 16 rollouts, λ=0 KL, ~24h/run。Neurosymbolic 论文全 inference-only，PRM 用 CE on scalar head。*Source: Spurious Rewards, Mellgren*

## Qwen Specificity Warning (2/25, High)
Random/incorrect rewards 的 RLVR gains 是 Qwen 特有 (+21.4% random vs OLMo/Llama 无效)。机制: GRPO 放大 pretraining latent code reasoning。Yue 佐证: RLVR 不创造超越 base 的新推理。*Source: Spurious Rewards, Yue*

## PRM vs Value Model (3/25, High)
MC estimation → value-model labels (40.2% F1), 非 PRM labels (56.5%)。Consensus filtering (MC∩LLM-judge) 保留 40% 数据达可比质量。BoN 有 3 个系统偏差，30-50% correct-answer responses 含推理错误。*Source: Qwen-PRM*

## Three Orthogonal Hacking Mitigations (8/25, High)
(1) RM-side: InfoRM, ensembles, WARM。(2) Policy-side: KL, constrained RLHF, chi-squared。(3) Internal: energy loss (EPPO)。三类可叠加。KL 单独在 heavy-tailed error 下失效。*Source: InfoRM, Energy-Loss, Kwa*

## Gaming Under Separation (1/25, Medium)
Unified generation 93-98% definite precision (倾向报告失败)。Two-stage 暴露非对称性: GPT-5 fabricates axioms (可检测), DeepSeek-R1 mistranslates (不可检测)。仅测 prompted 模型。*Source: Kim*

## Research Gaps
- Neurosymbolic + RL 交叉 (neurosymbolic 全 inference-only)
- 迭代 self-correction 超越语法修复
- RLVR 模型族多样性
- RL-trained 系统的 gaming 检测
- Neurosymbolic 跨领域迁移
