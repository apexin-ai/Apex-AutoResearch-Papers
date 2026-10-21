---
name: distilled-writing
description: "Writing patterns for execution-simulation/verification papers: narrative structures, figure design, table conventions from 8 deep-read papers"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: ["S*: Test Time Scaling for Code Generation", "SWE-bench: Can Language Models Resolve Real-world Github Issues?", "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", "QLoRA: Efficient Finetuning of Quantized LLMs", "SWE-bench Verified", "LoRA: Low-Rank Adaptation of Large Language Models", "SQuAD: 100,000+ Questions for Machine Comprehension of Text", "BART: Denoising Sequence-to-Sequence Pre-training for NLG, Translation, and Comprehension", "Self-Execution Simulation Improves Coding Models", "CWM: An Open-Weights LLM for Research on Code Generation with World Models", "CodeMind: A Framework to Challenge Large Language Models for Code Reasoning", "Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation", "SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution", "SWE-RM: Execution-free Feedback for Software Engineering Agents", "Scalable Supervising Software Agents with Patch Reasoner", "Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling", "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Parameters", "Agentless: Demystifying LLM-based Software Engineering Agents", "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications", "SWE-Bench+: Enhanced Coding Benchmark for LLMs", "SWE-Bench Pro: Can AI Agents Solve Real-World Software Engineering Tasks?", "Qwen2.5-Coder Technical Report", "Qwen2.5 Technical Report", "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", "A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability"]
  last_distilled: "2026-05-24T12:00:00Z"
---

## Narrative Strategy

**Dominant story**: "突破局限型" — X works for Y, fails for Z, propose solution. (3/8, 高). Source: SWE-bench, QLoRA.

**Runner-up**: "统一框架型" — unify partial solutions. (2/8, 中). Source: S*, BART.

**Hook patterns**:
- "X proven for A but underexplored for code" — positions in active wave. (2/8, 高). Source: S*.
- "Even with oracle, models barely solve N%" — urgency via negative result. (2/8, 中). Source: SWE-bench.

**Tension**: Frame seeming contradiction, resolve with reframing insight. "quantization degrades quality" (QLoRA), "execution needed but unavailable" (Patch Reasoner). (5/8, 高)

**Contributions**: 3 is modal (method + evaluation + artifact). (4/8, 高)

## Figure Design Consensus

**Figure 1**: method_overview dominates (4/8). Full system in one diagram. Source: S*, LoRA, BART, SWE-agent. (高)

**Fig 1 elements**: flow arrows + color-coded components + embedded examples. LoRA's minimal matrix diagram = gold standard. (6/8, 高)

**Result viz**: bar_chart dominant (5/8). line_plot for scaling/continuous ablation. (高)

**Figure flow**: method → main_result → ablation → qualitative (4-beat rhythm, 5/8, 高).

**Count**: median 5 figures for long papers. (8/8, 高)

## Table Design Consensus

**Main table**: rows = methods (by_category), cols = datasets × metrics. (6/8, 高)

**Highlight**: bold_best universal (7/8). Add cost/param column for efficiency claims (LoRA, Agentless). (高)

**Baselines**: 4-6 in main table; more → appendix. (6/8, 高)

**Stats**: Single run acceptable (5/8) — SWE-bench deterministic at temp=0. With sampling: mean±std, 3 seeds. (中)

**Ablation style**: full_numbers (5/8) over delta or checkmark. Readers want absolute numbers. (高)

**Split**: Tables for discrete comparisons; figures for scaling curves. Appendix: per-repo, hyperparams, full rankings. (7/8, 高)

## Intro Structure Template

4 paragraphs (modal): (1) broad context + hook, (2) current limitation/gap, (3) our approach + key insight, (4) preview results + contributions list. S* and LoRA both follow this structure. (支持度: 5/8, 置信度: 高)
