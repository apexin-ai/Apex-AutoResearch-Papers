---
name: distilled-research
description: "Domain consensus for execution-simulation-based code verification: baselines, metrics, experimental design, and research gaps from 25 papers"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: ["S*: Test Time Scaling for Code Generation", "SWE-bench: Can Language Models Resolve Real-world Github Issues?", "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", "QLoRA: Efficient Finetuning of Quantized LLMs", "SWE-bench Verified", "LoRA: Low-Rank Adaptation of Large Language Models", "SQuAD: 100,000+ Questions for Machine Comprehension of Text", "BART: Denoising Sequence-to-Sequence Pre-training for NLG, Translation, and Comprehension", "Self-Execution Simulation Improves Coding Models", "CWM: An Open-Weights LLM for Research on Code Generation with World Models", "CodeMind: A Framework to Challenge Large Language Models for Code Reasoning", "Demystifying Errors in LLM Reasoning Traces: An Empirical Study of Code Execution Simulation", "SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution", "SWE-RM: Execution-free Feedback for Software Engineering Agents", "Scalable Supervising Software Agents with Patch Reasoner", "Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling", "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Parameters", "Agentless: Demystifying LLM-based Software Engineering Agents", "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications", "SWE-Bench+: Enhanced Coding Benchmark for LLMs", "SWE-Bench Pro: Can AI Agents Solve Real-World Software Engineering Tasks?", "Qwen2.5-Coder Technical Report", "Qwen2.5 Technical Report", "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", "A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability"]
  last_distilled: "2026-05-24T12:00:00Z"
---

## Standard Evaluation Setup

**Primary benchmark**: SWE-bench Verified (500 instances) — de facto standard for SE verification/repair. (10/25, 高). Source: SWE-RM, Patch Reasoner, CWM.

**Primary metric**: pass@1 / resolve_rate (15/25, 高). Cost-per-instance secondary. Source: Agentless ($0.70).

**Required baselines**: (1) test execution, (2) majority voting, (3) LLM-as-judge, (4) trajectory-level RM. (5/25, 高). Source: SWE-RM, S*.

## Methodology Trends (2024-2026)

**Rising — Execution-free verification**: SWE-RM (30B MoE), Patch Reasoner (72.2%), VG-Search. Field converging on avoiding test execution overhead. (5/25, 高)

**Rising — RL-trained verifiers**: SWE-RM and Patch Reasoner both use RL (not just SFT). Calibration for downstream RL is key. (3/25, 中)

**Rising — Test-time scaling for code**: S* (3B matches GPT-4o-mini); small+TTS beats 14x larger. Verification quality is the bottleneck. (4/25, 高)

**Established — Generation-based exec sim**: CWM (65.8%), Self-Exec Sim (SFT+RL). Limitation: error accumulation in long traces (9 error types per Demystifying Errors). (4/25, 高)

## Competitor Positioning

**SWE-RM**: Trajectory-level, 30B sparse MoE, SOTA open-source (74.6%). Gap: no per-test granularity.
**Patch Reasoner**: Reasoning-based binary verification, 72.2% accuracy, 50x faster than tests. Gap: binary only.
**CWM**: 32B world model, generation-based. Gap: requires large scale, generation errors accumulate.
**Self-Exec Sim**: Closest prior — generation formulation for execution prediction. Gap: classification may be more robust.

## Research Gaps (Cross-Paper)

1. **Per-test verification granularity**: All competitors do binary/trajectory-level. No work provides per-test-case signals. (支持度: 0/25 do this, 置信度: 高)
2. **Classification vs generation for execution sim**: CodeMind shows generation degrades with complexity; Demystifying Errors catalogs 9 failure modes. Classification formulation is unexplored. (支持度: 0/25, 置信度: 中)
3. **Small-scale verifiers (<8B)**: SWE-RM uses 30B, Patch Reasoner uses 32B. Sub-8B verification is underexplored. (支持度: 0/25, 置信度: 中)
4. **Verification + iterative repair loop**: Agentless identifies validation as weakest phase. Closing the verification→repair loop is a gap. (支持度: 2/25 mention, 置信度: 中). Source: Agentless, S*.

## Experimental Design Consensus

- Report across multiple model sizes/families for generality (4/25, 高). Source: S* (12 models).
- LoRA rank 16 + NF4 is standard efficient finetuning (3/25, 高). Source: QLoRA, LoRA.
- TOST for equivalence claims (1/25, 低 but sound). Source: TOST 1987.
