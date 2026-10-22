[English](README.md) | **简体中文**

# Apex Research

**从研究问题到可检查证据的自主科研。**

Apex Research 由 Apex Intelligence 构建。本仓库展示 36 个研究项目，分为六个编号研究方向；每个方向内的论文从 `01` 开始编号，方便读者快速浏览。

**36 个项目** · **06 个研究方向** · **分级编号目录**

[搜索完整目录](CONTENTS.md) · [浏览全部编号方向](categories/README.md) · [打开项目资产](paper-assets/)

## 01–06 · 研究方向

| 编号 | 研究方向 | 项目数 | 集合入口 |
|---:|---|---:|---|
| **01** | [模型评测、基准与数据质量](categories/model-evaluation-and-data-quality/README.md) | **11** | [进入](categories/model-evaluation-and-data-quality/README.md) |
| **02** | [信息抽取、因果推断与符号推理](categories/information-extraction-causal-and-symbolic-reasoning/README.md) | **8** | [进入](categories/information-extraction-causal-and-symbolic-reasoning/README.md) |
| **03** | [智能体、强化学习与代码修复](categories/agents-reinforcement-learning-and-code-repair/README.md) | **4** | [进入](categories/agents-reinforcement-learning-and-code-repair/README.md) |
| **04** | [LLM 安全与对齐](categories/llm-safety-and-alignment/README.md) | **5** | [进入](categories/llm-safety-and-alignment/README.md) |
| **05** | [具身智能与 VLA](categories/embodied-ai-and-vla/README.md) | **3** | [进入](categories/embodied-ai-and-vla/README.md) |
| **06** | [模型机制、训练与推理效率](categories/model-mechanisms-training-and-inference-efficiency/README.md) | **5** | [进入](categories/model-mechanisms-training-and-inference-efficiency/README.md) |

<p align="center">
  <img src="assets/research-overview.jpg" alt="36 个 Apex Research 项目的六个研究方向" width="560" />
</p>

## 编号项目目录

每个研究方向拥有独立的项目序号。编号只用于展示和导航，不改变项目名称或资产路径。

### 01 · 模型评测、基准与数据质量（11 个）

关注基准有效性、数据污染、可复现性、模型坍塌检测与评测偏差。

| 编号 | 项目 | 论文 | 入口 |
|---:|---|---|---|
| **01** | [causal_style_decomp_judge](paper-assets/causal_style_decomp_judge/README.md) | The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation | [PDF](paper-assets/causal_style_decomp_judge/01-manuscript/paper.pdf) · [项目说明](paper-assets/causal_style_decomp_judge/README.md) |
| **02** | [contamcal-irt-calibration](paper-assets/contamcal-irt-calibration/README.md) | Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families | [PDF](paper-assets/contamcal-irt-calibration/01-manuscript/paper.pdf) · [项目说明](paper-assets/contamcal-irt-calibration/README.md) |
| **03** | [distrib_canary_collapse](paper-assets/distrib_canary_collapse/README.md) | Characterizing the Detectability Landscape of Iterative Model Collapse | [PDF](paper-assets/distrib_canary_collapse/01-manuscript/paper.pdf) · [项目说明](paper-assets/distrib_canary_collapse/README.md) |
| **04** | [gated_mfrm_judge_bias](paper-assets/gated_mfrm_judge_bias/README.md) | Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation | [PDF](paper-assets/gated_mfrm_judge_bias/01-manuscript/paper.pdf) · [项目说明](paper-assets/gated_mfrm_judge_bias/README.md) |
| **05** | [gen-depth-contamination](paper-assets/gen-depth-contamination/README.md) | Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary | [PDF](paper-assets/gen-depth-contamination/01-manuscript/paper.pdf) · [项目说明](paper-assets/gen-depth-contamination/README.md) |
| **06** | [gen-depth-fingerprint](paper-assets/gen-depth-fingerprint/README.md) | Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text | [PDF](paper-assets/gen-depth-fingerprint/01-manuscript/paper.pdf) · [项目说明](paper-assets/gen-depth-fingerprint/README.md) |
| **07** | [irt_equated_bench_regen](paper-assets/irt_equated_bench_regen/README.md) | Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models | [PDF](paper-assets/irt_equated_bench_regen/01-manuscript/paper.pdf) · [项目说明](paper-assets/irt_equated_bench_regen/README.md) |
| **08** | [irt_personfit_contam](paper-assets/irt_personfit_contam/README.md) | What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? | [PDF](paper-assets/irt_personfit_contam/01-manuscript/paper.pdf) · [项目说明](paper-assets/irt_personfit_contam/README.md) |
| **09** | [nlp_variance_gtheory](paper-assets/nlp_variance_gtheory/README.md) | Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models | [PDF](paper-assets/nlp_variance_gtheory/01-manuscript/paper.pdf) · [项目说明](paper-assets/nlp_variance_gtheory/README.md) |
| **10** | [recursive_gen_depth_est](paper-assets/recursive_gen_depth_est/README.md) | How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints | [PDF](paper-assets/recursive_gen_depth_est/01-manuscript/paper.pdf) · [项目说明](paper-assets/recursive_gen_depth_est/README.md) |
| **11** | [spectral_collapse_ews](paper-assets/spectral_collapse_ews/README.md) | Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff | [PDF](paper-assets/spectral_collapse_ews/01-manuscript/paper.pdf) · [项目说明](paper-assets/spectral_collapse_ews/README.md) |

### 02 · 信息抽取、因果推断与符号推理（8 个）

关注结构化信息抽取、带噪标注下的因果效应、证据、自洽性与形式推理。

| 编号 | 项目 | 论文 | 入口 |
|---:|---|---|---|
| **01** | [causal_annot_error_attrib](paper-assets/causal_annot_error_attrib/README.md) | Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction | [PDF](paper-assets/causal_annot_error_attrib/01-manuscript/paper.pdf) · [项目说明](paper-assets/causal_annot_error_attrib/README.md) |
| **02** | [ec_hte_llm_annotation](paper-assets/ec_hte_llm_annotation/README.md) | When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects | [PDF](paper-assets/ec_hte_llm_annotation/01-manuscript/paper.pdf) · [项目说明](paper-assets/ec_hte_llm_annotation/README.md) |
| **03** | [faith-evidence-ie](paper-assets/faith-evidence-ie/README.md) | Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction | [PDF](paper-assets/faith-evidence-ie/01-manuscript/paper.pdf) · [项目说明](paper-assets/faith-evidence-ie/README.md) |
| **04** | [schema-dag-extraction](paper-assets/schema-dag-extraction/README.md) | How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? | [PDF](paper-assets/schema-dag-extraction/01-manuscript/paper.pdf) · [项目说明](paper-assets/schema-dag-extraction/README.md) |
| **05** | [schema_semantic_constrained_ie](paper-assets/schema_semantic_constrained_ie/README.md) | OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints | [PDF](paper-assets/schema_semantic_constrained_ie/01-manuscript/paper.pdf) · [项目说明](paper-assets/schema_semantic_constrained_ie/README.md) |
| **06** | [solver-trace-ablation](paper-assets/solver-trace-ablation/README.md) | Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning | [PDF](paper-assets/solver-trace-ablation/01-manuscript/paper.pdf) · [项目说明](paper-assets/solver-trace-ablation/README.md) |
| **07** | [struct_self_consist_ie](paper-assets/struct_self_consist_ie/README.md) | When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap | [PDF](paper-assets/struct_self_consist_ie/01-manuscript/paper.pdf) · [项目说明](paper-assets/struct_self_consist_ie/README.md) |
| **08** | [symb_invariant_consensus](paper-assets/symb_invariant_consensus/README.md) | Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction | [PDF](paper-assets/symb_invariant_consensus/01-manuscript/paper.pdf) · [项目说明](paper-assets/symb_invariant_consensus/README.md) |

### 03 · 智能体、强化学习与代码修复（4 个）

关注多智能体通信、信用分配、计算路由、验证与免执行代码修复。

| 编号 | 项目 | 论文 | 入口 |
|---:|---|---|---|
| **01** | [comm_gate_mas](paper-assets/comm_gate_mas/README.md) | When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems | [PDF](paper-assets/comm_gate_mas/01-manuscript/paper.pdf) · [项目说明](paper-assets/comm_gate_mas/README.md) |
| **02** | [cost-verify-agent-rl](paper-assets/cost-verify-agent-rl/README.md) | Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction | [PDF](paper-assets/cost-verify-agent-rl/01-manuscript/paper.pdf) · [项目说明](paper-assets/cost-verify-agent-rl/README.md) |
| **03** | [exec-sim-repair-verifier](paper-assets/exec-sim-repair-verifier/README.md) | A Systematic Comparison of Execution-Free Verification Formulations for Code Repair | [PDF](paper-assets/exec-sim-repair-verifier/01-manuscript/paper.pdf) · [项目说明](paper-assets/exec-sim-repair-verifier/README.md) |
| **04** | [simgate-modular-routing](paper-assets/simgate-modular-routing/README.md) | Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld | [PDF](paper-assets/simgate-modular-routing/01-manuscript/paper.pdf) · [项目说明](paper-assets/simgate-modular-routing/README.md) |

### 04 · LLM 安全与对齐（5 个）

关注谄媚、隐藏状态安全监测、对抗性评测、多轮越狱检测与策略合规。

| 编号 | 项目 | 论文 | 入口 |
|---:|---|---|---|
| **01** | [cert_manip_resist_eval](paper-assets/cert_manip_resist_eval/README.md) | The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation | [PDF](paper-assets/cert_manip_resist_eval/01-manuscript/paper.pdf) · [项目说明](paper-assets/cert_manip_resist_eval/README.md) |
| **02** | [contrastive_entrain_calib](paper-assets/contrastive_entrain_calib/README.md) | The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration | [PDF](paper-assets/contrastive_entrain_calib/01-manuscript/paper.pdf) · [项目说明](paper-assets/contrastive_entrain_calib/README.md) |
| **03** | [contrastive_trace_safety](paper-assets/contrastive_trace_safety/README.md) | Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models | [PDF](paper-assets/contrastive_trace_safety/01-manuscript/paper.pdf) · [项目说明](paper-assets/contrastive_trace_safety/README.md) |
| **04** | [persuasion_turn_jailbreak_detect](paper-assets/persuasion_turn_jailbreak_detect/README.md) | DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection | [PDF](paper-assets/persuasion_turn_jailbreak_detect/01-manuscript/paper.pdf) · [项目说明](paper-assets/persuasion_turn_jailbreak_detect/README.md) |
| **05** | [policy_ambiguity_safety](paper-assets/policy_ambiguity_safety/README.md) | Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety | [PDF](paper-assets/policy_ambiguity_safety/01-manuscript/paper.pdf) · [项目说明](paper-assets/policy_ambiguity_safety/README.md) |

### 05 · 具身智能与 VLA（3 个）

关注碰撞规避、空间监督以及视觉-语言-动作模型的表示变化。

| 编号 | 项目 | 论文 | 入口 |
|---:|---|---|---|
| **01** | [diff_collision_sdf](paper-assets/diff_collision_sdf/README.md) | How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation | [PDF](paper-assets/diff_collision_sdf/01-manuscript/paper.pdf) · [项目说明](paper-assets/diff_collision_sdf/README.md) |
| **02** | [occsafe_vla](paper-assets/occsafe_vla/README.md) | Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis | [PDF](paper-assets/occsafe_vla/01-manuscript/paper.pdf) · [项目说明](paper-assets/occsafe_vla/README.md) |
| **03** | [vla-ssd](paper-assets/vla-ssd/README.md) | Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis | [PDF](paper-assets/vla-ssd/01-manuscript/paper.pdf) · [项目说明](paper-assets/vla-ssd/README.md) |

### 06 · 模型机制、训练与推理效率（5 个）

关注跨语言机制、上下文稀疏、剪枝恢复、混合架构与谱优化。

| 编号 | 项目 | 论文 | 入口 |
|---:|---|---|---|
| **01** | [clkc_mech_interp](paper-assets/clkc_mech_interp/README.md) | English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries | [PDF](paper-assets/clkc_mech_interp/01-manuscript/paper.pdf) · [项目说明](paper-assets/clkc_mech_interp/README.md) |
| **02** | [distill_sparse_swiglu](paper-assets/distill_sparse_swiglu/README.md) | Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs | [PDF](paper-assets/distill_sparse_swiglu/01-manuscript/paper.pdf) · [项目说明](paper-assets/distill_sparse_swiglu/README.md) |
| **03** | [entrainment_gated_ft](paper-assets/entrainment_gated_ft/README.md) | Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models | [PDF](paper-assets/entrainment_gated_ft/01-manuscript/paper.pdf) · [项目说明](paper-assets/entrainment_gated_ft/README.md) |
| **04** | [recovery_aware_struct_prune](paper-assets/recovery_aware_struct_prune/README.md) | How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM | [PDF](paper-assets/recovery_aware_struct_prune/01-manuscript/paper.pdf) · [项目说明](paper-assets/recovery_aware_struct_prune/README.md) |
| **05** | [spectral_optim_vision_geometry](paper-assets/spectral_optim_vision_geometry/README.md) | Spectral Optimization Across Vision Architecture Families: A Controlled Empirical Study | [PDF](paper-assets/spectral_optim_vision_geometry/01-manuscript/paper.pdf) · [项目说明](paper-assets/spectral_optim_vision_geometry/README.md) |

## 统一项目结构

所有项目采用相同的七类材料目录：

| 目录 | 材料内容 |
|---|---|
| `01-manuscript/` | 论文 PDF、源文件、图表和版本材料 |
| `02-code/` | 研究代码、脚本、配置和依赖记录 |
| `03-experiments/` | 实验设置、结果、表格和分析输出 |
| `04-generation-trace/` | 可读生成记录和结构化会话 |
| `05-validation/` | 验证记录、审计和检查材料 |
| `06-maintenance/` | 项目说明、修订和维护材料 |
| `07-index/` | 文件清单、路径、校验和可用性记录 |

需要检索论文标题和材料数量时，请查看 [CONTENTS.md](CONTENTS.md)；需要了解项目材料范围时，先打开项目说明。
