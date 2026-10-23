**English** | [简体中文](README.zh-CN.md)

# Apex Research

**Autonomous research from question to evidence.**

Apex Research, built by Apex Intelligence, is a public showcase of 36 research projects spanning evaluation, reasoning, agents, safety, embodied AI, and model efficiency. The catalogue is organized into six numbered research areas; papers inside each area are numbered from `01` onward for quick navigation.

**36 projects** · **06 research areas** · **numbered project lists**

[Search the full catalogue](CONTENTS.md) · [Browse all numbered areas](categories/README.md) · [Open project assets](paper-assets/)

## 01–06 · Research areas

| No. | Research area | Projects | Collection |
|---:|---|---:|---|
| **01** | [Model Evaluation, Benchmarks & Data Quality](categories/model-evaluation-and-data-quality/README.md) | **11** | [Open](categories/model-evaluation-and-data-quality/README.md) |
| **02** | [Information Extraction, Causal Inference & Symbolic Reasoning](categories/information-extraction-causal-and-symbolic-reasoning/README.md) | **8** | [Open](categories/information-extraction-causal-and-symbolic-reasoning/README.md) |
| **03** | [Agents, Reinforcement Learning & Code Repair](categories/agents-reinforcement-learning-and-code-repair/README.md) | **4** | [Open](categories/agents-reinforcement-learning-and-code-repair/README.md) |
| **04** | [LLM Safety & Alignment](categories/llm-safety-and-alignment/README.md) | **5** | [Open](categories/llm-safety-and-alignment/README.md) |
| **05** | [Embodied AI & VLA](categories/embodied-ai-and-vla/README.md) | **3** | [Open](categories/embodied-ai-and-vla/README.md) |
| **06** | [Model Mechanisms, Training & Inference Efficiency](categories/model-mechanisms-training-and-inference-efficiency/README.md) | **5** | [Open](categories/model-mechanisms-training-and-inference-efficiency/README.md) |

<p align="center">
  <img src="assets/research-overview.jpg" alt="Six research areas across 36 Apex Research projects" width="560" />
</p>

## Numbered project index

Each area has its own sequence. The numbers are presentation labels and do not change project names or asset paths.

### 01 · Model Evaluation, Benchmarks & Data Quality (11)

Benchmark validity, contamination, reproducibility, model-collapse detection, and evaluation bias.

| No. | Project | Paper | Entry points |
|---:|---|---|---|
| **01** | [causal_style_decomp_judge](paper-assets/causal_style_decomp_judge/README.md) | The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation | [PDF](paper-assets/causal_style_decomp_judge/01-manuscript/the-likert-blindspot-measurement-mode-divergence-in-llm-judge-style-evaluation.pdf) · [Guide](paper-assets/causal_style_decomp_judge/README.md) |
| **02** | [contamcal-irt-calibration](paper-assets/contamcal-irt-calibration/README.md) | Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families | [PDF](paper-assets/contamcal-irt-calibration/01-manuscript/not-all-models-are-inflated-profiling-contamination-dose-response-across-model-families.pdf) · [Guide](paper-assets/contamcal-irt-calibration/README.md) |
| **03** | [distrib_canary_collapse](paper-assets/distrib_canary_collapse/README.md) | Characterizing the Detectability Landscape of Iterative Model Collapse | [PDF](paper-assets/distrib_canary_collapse/01-manuscript/characterizing-the-detectability-landscape-of-iterative-model-collapse.pdf) · [Guide](paper-assets/distrib_canary_collapse/README.md) |
| **04** | [gated_mfrm_judge_bias](paper-assets/gated_mfrm_judge_bias/README.md) | Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation | [PDF](paper-assets/gated_mfrm_judge_bias/01-manuscript/fair-scores-via-joint-calibration-a-gated-many-facet-rasch-model-for-disentangling-judge-bias-and-contamination-in-llm-evaluation.pdf) · [Guide](paper-assets/gated_mfrm_judge_bias/README.md) |
| **05** | [gen-depth-contamination](paper-assets/gen-depth-contamination/README.md) | Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary | [PDF](paper-assets/gen-depth-contamination/01-manuscript/generational-depth-estimation-of-recursive-synthetic-text-measuring-the-discrimination-boundary.pdf) · [Guide](paper-assets/gen-depth-contamination/README.md) |
| **06** | [gen-depth-fingerprint](paper-assets/gen-depth-fingerprint/README.md) | Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text | [PDF](paper-assets/gen-depth-fingerprint/01-manuscript/depth-profiling-classifying-recursive-generation-depth-in-base-model-llm-text.pdf) · [Guide](paper-assets/gen-depth-fingerprint/README.md) |
| **07** | [irt_equated_bench_regen](paper-assets/irt_equated_bench_regen/README.md) | Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models | [PDF](paper-assets/irt_equated_bench_regen/01-manuscript/temporal-score-incomparability-in-llm-benchmarks-a-large-scale-psychometric-audit-of-5227-models.pdf) · [Guide](paper-assets/irt_equated_bench_regen/README.md) |
| **08** | [irt_personfit_contam](paper-assets/irt_personfit_contam/README.md) | What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? | [PDF](paper-assets/irt_personfit_contam/01-manuscript/what-can-irt-person-fit-statistics-reveal-about-sft-stage-benchmark-contamination.pdf) · [Guide](paper-assets/irt_personfit_contam/README.md) |
| **09** | [nlp_variance_gtheory](paper-assets/nlp_variance_gtheory/README.md) | Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models | [PDF](paper-assets/nlp_variance_gtheory/01-manuscript/reproducibility-budgets-for-open-weight-llm-evaluation-a-generalizability-theory-study-of-7-9b-instruction-tuned-models.pdf) · [Guide](paper-assets/nlp_variance_gtheory/README.md) |
| **10** | [recursive_gen_depth_est](paper-assets/recursive_gen_depth_est/README.md) | How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints | [PDF](paper-assets/recursive_gen_depth_est/01-manuscript/how-deep-is-your-data-estimating-recursive-generation-depth-via-statistical-fingerprints.pdf) · [Guide](paper-assets/recursive_gen_depth_est/README.md) |
| **11** | [spectral_collapse_ews](paper-assets/spectral_collapse_ews/README.md) | Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff | [PDF](paper-assets/spectral_collapse_ews/01-manuscript/spectral-early-warning-signals-for-model-collapse-and-their-prevention-detectability-tradeoff.pdf) · [Guide](paper-assets/spectral_collapse_ews/README.md) |

### 02 · Information Extraction, Causal Inference & Symbolic Reasoning (8)

Structured extraction, causal effects with noisy annotations, evidence, self-consistency, and formal reasoning.

| No. | Project | Paper | Entry points |
|---:|---|---|---|
| **01** | [causal_annot_error_attrib](paper-assets/causal_annot_error_attrib/README.md) | Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction | [PDF](paper-assets/causal_annot_error_attrib/01-manuscript/multi-class-annotation-errors-in-causal-inference-topology-dependent-bias-sensitivity-and-correction.pdf) · [Guide](paper-assets/causal_annot_error_attrib/README.md) |
| **02** | [ec_hte_llm_annotation](paper-assets/ec_hte_llm_annotation/README.md) | When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects | [PDF](paper-assets/ec_hte_llm_annotation/01-manuscript/when-debiasing-hurts-an-exact-bias-identity-for-llm-annotated-treatment-effects.pdf) · [Guide](paper-assets/ec_hte_llm_annotation/README.md) |
| **03** | [faith-evidence-ie](paper-assets/faith-evidence-ie/README.md) | Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction | [PDF](paper-assets/faith-evidence-ie/01-manuscript/evidence-at-what-cost-decoupling-and-scaling-in-llm-based-document-relation-extraction.pdf) · [Guide](paper-assets/faith-evidence-ie/README.md) |
| **04** | [schema-dag-extraction](paper-assets/schema-dag-extraction/README.md) | How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? | [PDF](paper-assets/schema-dag-extraction/01-manuscript/how-does-schema-complexity-predict-performance-in-training-free-llm-information-extraction.pdf) · [Guide](paper-assets/schema-dag-extraction/README.md) |
| **05** | [schema_semantic_constrained_ie](paper-assets/schema_semantic_constrained_ie/README.md) | OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints | [PDF](paper-assets/schema_semantic_constrained_ie/01-manuscript/ontocodec-type-constrained-information-extraction-via-compiled-schema-constraints.pdf) · [Guide](paper-assets/schema_semantic_constrained_ie/README.md) |
| **06** | [solver-trace-ablation](paper-assets/solver-trace-ablation/README.md) | Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning | [PDF](paper-assets/solver-trace-ablation/01-manuscript/observe-but-don-t-optimize-structural-rewards-trigger-goodhart-effects-in-neurosymbolic-reasoning.pdf) · [Guide](paper-assets/solver-trace-ablation/README.md) |
| **07** | [struct_self_consist_ie](paper-assets/struct_self_consist_ie/README.md) | When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap | [PDF](paper-assets/struct_self_consist_ie/01-manuscript/when-self-consistency-fails-for-ner-degeneracy-signal-collapse-and-the-correlation-selection-gap.pdf) · [Guide](paper-assets/struct_self_consist_ie/README.md) |
| **08** | [symb_invariant_consensus](paper-assets/symb_invariant_consensus/README.md) | Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction | [PDF](paper-assets/symb_invariant_consensus/01-manuscript/beyond-self-consistency-self-extracted-constraints-reduce-to-majority-voting-under-zero-shot-extraction.pdf) · [Guide](paper-assets/symb_invariant_consensus/README.md) |

### 03 · Agents, Reinforcement Learning & Code Repair (4)

Multi-agent communication, credit assignment, routing, verification, and execution-free program repair.

| No. | Project | Paper | Entry points |
|---:|---|---|---|
| **01** | [comm_gate_mas](paper-assets/comm_gate_mas/README.md) | When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems | [PDF](paper-assets/comm_gate_mas/01-manuscript/when-the-most-disruptive-messages-are-safe-to-prune-in-aggregate-functional-analysis-of-communication-pruning-in-two-agent-llm-systems.pdf) · [Guide](paper-assets/comm_gate_mas/README.md) |
| **02** | [cost-verify-agent-rl](paper-assets/cost-verify-agent-rl/README.md) | Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction | [PDF](paper-assets/cost-verify-agent-rl/01-manuscript/sign-misattribution-in-step-independent-agent-rl-dual-mechanism-diagnosis-and-episode-level-correction.pdf) · [Guide](paper-assets/cost-verify-agent-rl/README.md) |
| **03** | [exec-sim-repair-verifier](paper-assets/exec-sim-repair-verifier/README.md) | A Systematic Comparison of Execution-Free Verification Formulations for Code Repair | [PDF](paper-assets/exec-sim-repair-verifier/01-manuscript/a-systematic-comparison-of-execution-free-verification-formulations-for-code-repair.pdf) · [Guide](paper-assets/exec-sim-repair-verifier/README.md) |
| **04** | [simgate-modular-routing](paper-assets/simgate-modular-routing/README.md) | Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld | [PDF](paper-assets/simgate-modular-routing/01-manuscript/death-avoidance-as-the-dominant-routing-signal-a-counterfactual-analysis-on-scienceworld.pdf) · [Guide](paper-assets/simgate-modular-routing/README.md) |

### 04 · LLM Safety & Alignment (5)

Sycophancy, hidden-state safety monitoring, adversarial evaluation, jailbreak detection, and policy compliance.

| No. | Project | Paper | Entry points |
|---:|---|---|---|
| **01** | [cert_manip_resist_eval](paper-assets/cert_manip_resist_eval/README.md) | The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation | [PDF](paper-assets/cert_manip_resist_eval/01-manuscript/the-weakest-link-across-panel-sizes-predictor-relevance-patterns-in-multi-judge-llm-evaluation-under-adversarial-manipulation.pdf) · [Guide](paper-assets/cert_manip_resist_eval/README.md) |
| **02** | [contrastive_entrain_calib](paper-assets/contrastive_entrain_calib/README.md) | The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration | [PDF](paper-assets/contrastive_entrain_calib/01-manuscript/the-probe-reward-trap-behavioral-death-before-distributional-collapse-in-sycophancy-calibration.pdf) · [Guide](paper-assets/contrastive_entrain_calib/README.md) |
| **03** | [contrastive_trace_safety](paper-assets/contrastive_trace_safety/README.md) | Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models | [PDF](paper-assets/contrastive_trace_safety/01-manuscript/layer-selection-sensitivity-in-hidden-state-safety-probes-for-reasoning-models.pdf) · [Guide](paper-assets/contrastive_trace_safety/README.md) |
| **04** | [persuasion_turn_jailbreak_detect](paper-assets/persuasion_turn_jailbreak_detect/README.md) | DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection | [PDF](paper-assets/persuasion_turn_jailbreak_detect/01-manuscript/disped-a-controlled-study-of-encoder-adaptation-for-multi-turn-jailbreak-detection.pdf) · [Guide](paper-assets/persuasion_turn_jailbreak_detect/README.md) |
| **05** | [policy_ambiguity_safety](paper-assets/policy_ambiguity_safety/README.md) | Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety | [PDF](paper-assets/policy_ambiguity_safety/01-manuscript/policy-ambiguity-is-nocuous-clause-level-causal-effects-on-customer-service-agent-safety.pdf) · [Guide](paper-assets/policy_ambiguity_safety/README.md) |

### 05 · Embodied AI & VLA (3)

Collision avoidance, spatial supervision, and representation changes in vision-language-action models.

| No. | Project | Paper | Entry points |
|---:|---|---|---|
| **01** | [diff_collision_sdf](paper-assets/diff_collision_sdf/README.md) | How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation | [PDF](paper-assets/diff_collision_sdf/01-manuscript/how-action-collapse-creates-illusory-safety-in-diffusion-based-vla-collision-avoidance-evaluation.pdf) · [Guide](paper-assets/diff_collision_sdf/README.md) |
| **02** | [occsafe_vla](paper-assets/occsafe_vla/README.md) | Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis | [PDF](paper-assets/occsafe_vla/01-manuscript/does-auxiliary-spatial-supervision-make-vision-language-action-models-safer-a-factorial-analysis.pdf) · [Guide](paper-assets/occsafe_vla/README.md) |
| **03** | [vla-ssd](paper-assets/vla-ssd/README.md) | Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis | [PDF](paper-assets/vla-ssd/01-manuscript/instruction-routing-in-fine-tuned-vision-language-action-models-a-cross-architecture-analysis.pdf) · [Guide](paper-assets/vla-ssd/README.md) |

### 06 · Model Mechanisms, Training & Inference Efficiency (5)

Cross-lingual mechanisms, contextual sparsity, pruning recovery, hybrid architectures, and spectral optimization.

| No. | Project | Paper | Entry points |
|---:|---|---|---|
| **01** | [clkc_mech_interp](paper-assets/clkc_mech_interp/README.md) | English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries | [PDF](paper-assets/clkc_mech_interp/01-manuscript/english-chinese-knowledge-conflict-signals-are-consistent-with-general-cross-lingual-asymmetries.pdf) · [Guide](paper-assets/clkc_mech_interp/README.md) |
| **02** | [distill_sparse_swiglu](paper-assets/distill_sparse_swiglu/README.md) | Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs | [PDF](paper-assets/distill_sparse_swiglu/01-manuscript/output-distribution-distillation-for-contextual-sparsity-prediction-in-swiglu-llms.pdf) · [Guide](paper-assets/distill_sparse_swiglu/README.md) |
| **03** | [entrainment_gated_ft](paper-assets/entrainment_gated_ft/README.md) | Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models | [PDF](paper-assets/entrainment_gated_ft/01-manuscript/aggregate-equivalence-vs-behavioral-equivalence-per-example-multiplicity-in-hybrid-linear-recurrent-models.pdf) · [Guide](paper-assets/entrainment_gated_ft/README.md) |
| **04** | [recovery_aware_struct_prune](paper-assets/recovery_aware_struct_prune/README.md) | How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM | [PDF](paper-assets/recovery_aware_struct_prune/01-manuscript/how-pruning-criteria-shape-post-rlvr-recovery-a-controlled-study-of-structured-mlp-pruning-in-a-reasoning-llm.pdf) · [Guide](paper-assets/recovery_aware_struct_prune/README.md) |
| **05** | [spectral_optim_vision_geometry](paper-assets/spectral_optim_vision_geometry/README.md) | Spectral Optimization Across Vision Architecture Families: A Controlled Empirical Study | [PDF](paper-assets/spectral_optim_vision_geometry/01-manuscript/spectral-optimization-across-vision-architecture-families-a-controlled-empirical-study.pdf) · [Guide](paper-assets/spectral_optim_vision_geometry/README.md) |

## Shared project layout

Every project keeps the same seven material directories:

| Directory | What to look for |
|---|---|
| `01-manuscript/` | Paper PDF, source, figures, and manuscript versions |
| `02-code/` | Research code, scripts, configurations, and dependencies |
| `03-experiments/` | Experiment settings, results, tables, and analysis outputs |
| `04-generation-trace/` | Readable generation records and structured sessions |
| `05-validation/` | Validation records, audits, and checks |
| `06-maintenance/` | Project notes, revisions, and maintenance material |
| `07-index/` | File manifests, paths, checksums, and availability records |

Use [CONTENTS.md](CONTENTS.md) for searchable titles and material counts. Open a project guide before browsing its files.
