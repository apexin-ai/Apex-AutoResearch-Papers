---
name: distilled-writing
description: "LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 28
  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 叙事类型分布

**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverQA）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。

## Intro模式

**4-5段标准**（9/11，高）：(1)领域→(2)局限→(3)方案→(4)贡献→[可选(5)结构]。SymbCoT/Aristotle例外用6段（多CoT背景或root cause分析段）。

**3条贡献标配**（8/11，高）。变体：LINC 2条；Khan 9条numbered insights；SatLM "2 advantages + 3 findings"。

**贡献嵌数字**（3/11，中）：DyLoS("+27%")、SatLM("+23%")、SymbCoT("+7.88%")——Intro即有说服力。

## 可模仿技巧（按实用性排序）

1. **范式对比图**（SatLM Fig1, SymbCoT Fig1）：side-by-side对比旧方法(错误标红)vs新方法(正确标绿)。problem_illustration类Fig1最主流(3/11)。

2. **角色重构**（3/11）："LLM is translator not solver"(Logic-LM)；"declarative not imperative"(SatLM)。一句重定义格局。

3. **Parse-Plan-Execute分解**（SatLM）：展示offload步骤数(ProgLM 1/3 vs SatLM 2/3)——通用于hybrid系统。

4. **对手优势反转**（SymbCoT）：外部solver的reliability重构为"inflexibility+information loss"。

5. **Teaser result图放Intro**（Aristotle）：Fig1 bar chart量化问题，未看方法已知需求。

6. **诊断baseline**（LINC Scratchpad, SatLM CoTSolver）：中间态baseline隔离组件因果贡献。

7. **Mirror figure pair**（Khan Fig3-4）：同指标两设置相反趋势，视觉对称强化论证。

8. **Design space分解**（xiong2024）：empirical study组织为prompting×sampling×aggregation三维框架。

## Figure编排

**Fig1类型**：method_overview(7/11)最多；problem_illustration(3/11)其次；teaser_result(1/11)。

**必配图型**（高）：depth-accuracy曲线(5/11 neurosymbolic必做)；execution rate对比(3/11)。

**叙事节奏**：motivation/problem → method → main_results(bar) → depth(line) → ablation(grouped_bar) → error_analysis。5篇核心论文(LINC/Logic-LM/Aristotle/SymbCoT/SatLM)均遵循。Figure数量5-8常见；Khan极端17图1表。

## Table编排

**主结果表**（8/11，高）：row=methods(by_category分LLM-only/hybrid)，col=datasets。bold_best通用(8/11)；underline_second(3/11)。delta brackets(SymbCoT)新趋势。Baseline 3-10个。

**消融表**：full_numbers(6/11)主流；checkmark_grid(2/11,Aristotle)适合多组件on/off。SatLM增加error type分解表(planning vs execution)——值得借鉴。

**统计报告**：多数single run；SatLM bootstrap p<0.05；CREST mean across 3 seeds。要求正在收紧。

**附录**：prompt templates + extra models + error examples(8/11有)。SatLM 7表最多(含exemplar sensitivity/cross-model)。
