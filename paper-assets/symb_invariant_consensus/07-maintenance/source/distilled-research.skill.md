---
name: distilled-research
description: "LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 28
  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 基线与数据集共识

**基线层级**（8/11深读，高）：Standard → CoT → SC-CoT → neurosymbolic (LINC/Logic-LM/SymbCoT)。2024+必对比至少一个neurosymbolic baseline。来源：Aristotle, DyLoS, SymbCoT。

**FOL逻辑5件套**（高）：FOLIO(8/28) naturalistic FOL、ProofWriter(8/28) synthetic深度、PrOntoQA(7/28) sanity check、AR-LSAT(4/28) constraint-heavy、LogicalDeduction(3/28)。**数学推理**：GSM8K(10/28)、MATH(5/28)。

**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11)区分external vs LLM-based；faithfulness(2/11,上升)。ECE/AUROC仅uncertainty。

## 方法范式光谱

**LLM→External Solver**（高）：LINC→Logic-LM→SatLM→DyLoS→Aristotle。趋势：单solver→多solver路由→逻辑完备pipeline。SatLM关键：声明式取代命令式，solver处理planning+execution。Aristotle端点：CNF+resolution达99.7%单步准确。

**LLM内化Symbolic**（中）：SymbCoT。100%执行率(vs Logic-LM~80%)，模型升级收益更大(+24.3% GPT3.5→4 vs Logic-LM +19.9%)。对立范式。

**Consistency/Verification**（高，8/28）：SC→USC→CISC→DSC→CREST→RC。朴素vote→confidence-weighted→difficulty-adaptive→representation-based→follow-up consistency。

**Process Reward**（中）：Math-Shepherd, V-STaR, FoVer。formal tool自动生成step-level标签是新趋势。

## 实验设计共识

**Depth analysis必做**（5/11，高）：accuracy-vs-depth曲线，neurosymbolic核心论据。LINC/Logic-LM/Aristotle/SymbCoT/SatLM均有。

**Error taxonomy**（4/11，高）：formalization/planning/execution三类。SatLM: planning error占42-72%是声明式核心论据。

**Cross-model**（7/11，高）：GPT-4 + GPT-3.5最低配；开源模型(Llama/Gemma)验证泛化；DyLoS加LoRA小模型。

**Selective prediction**（2/11，中）：SatLM利用UNSAT/AMBIG反馈abstain；SATBench揭示UNSAT系统性偏差。

## 竞品Claim与高频局限

**竞品**：DyLoS—多solver路由(+27%)；Aristotle—逻辑完备(99.7%)；SymbCoT—无外部依赖(100% exe)；SatLM—声明式消除planning error(+23%)；LogicAgent—多视角推理(+7%)。

**高频局限**（高）：FOL表达力不足(5/11)；形式化瓶颈(4/11,60-80%错误)；隐含知识盲区(3/11,Aristotle LogiQA仅31%)；LLM过度自信(xiong2024,80-100%区间聚集)；单轮无迭代(SatLM/Logic-LM)。

## 研究空白

1. **Symbolic × debate零交集**（高）：debate论文(Du/Khan)不用symbolic，反之亦然
2. **跨表示一致性检验缺失**：无人检查FOL/SAT/CSP对同一问题是否一致
3. **声明式 vs LLM-based symbolic未统一**：SatLM(外部solver)和SymbCoT(内化)互有优劣，无hybrid
4. **Uncertainty × symbolic reasoning**：xiong2024的confidence framework未被应用于symbolic pipeline步骤级验证
5. **语义级self-refinement缺失**：仅修语法不修语义(Logic-LM)；无人用solver反馈指导语义修正
