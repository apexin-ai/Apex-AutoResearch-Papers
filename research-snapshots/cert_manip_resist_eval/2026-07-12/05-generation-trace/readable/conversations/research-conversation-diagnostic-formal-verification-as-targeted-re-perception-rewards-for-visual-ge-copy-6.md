# Research conversation: Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning ## Core Problem How can 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/273c115b-c627-458d-8f13-0cbe4eaa144a.jsonl`
- **Structured JSON:** [`a26cc816892a0419119f.json`](../../sessions/a2/a26cc816892a0419119f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:53:11.427Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:53:11.427Z",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "content": "# Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning\n\n## Core Problem\n\nHow can we provide formally verifiable, diagnostic reward signals for the visual perception stage of multimodal geometric reasoning — signals that pinpoint which specific geometric fact is wrong, explain why it contradicts known geometric constraints, and enable targeted correction at test time?\n\n## Research Opportunity\n\nCurrent RL approaches for visual math perception produce opaque reward signals that cannot diagnose specific perception errors:\n- **GeoDPO** (arXiv:2602.22703): Learned NL-to-DSL translator computes DSL-level rewards; translator can hallucinate scores.\n- **Perception-R1** (arXiv:2506.07218): Judge LLM provides visual perception rewards; lacks formal grounding.\n- **\"Bad Seeing or Bad Thinking?\"** (arXiv:2605.14054): Perception Verification (PV) via blindfolded reasoning proxy independently rewards perception fidelity — but remains a neural proxy that reports \"perception unreliable\" without diagnosing which fact conflicts with which constraint.\n- **\"From Seeing to Thinking\"** (arXiv:2605.20177): Shows perception improves more via RL than caption-based SFT, but uses only generic rewards.\n- **PDCR** (arXiv:2605.13467): Decomposes confidence rewards by perception/reasoning clusters — but still scalar confidence, no structural diagnosis.\n- **SymHPR** (arXiv:2512.03126): Hierarchical per-primitive rewards (point-on-line, line-on-shape F1/L2), closest to structured perception feedback — but rule-based metrics without formal deduction. Cannot detect semantic contradictions (e.g., angle inconsistent with circle theorem), and F1 can be noisy when primitive extraction itself errs.\n- **ViCrit** (arXiv:2506.10128, NeurIPS 2025): Verifiable RL proxy task via synthetic hallucination injection with binary exact-match reward — validates verifiable perception rewards but uses domain-agnostic hallucination detection, not domain-specific formal geometric verification.\n\nFormal verification for reasoning-stage rewards has proven effective — SGVR (arXiv:2601.05073, +9.7%), Safe (arXiv:2506.04592), FoVer (ACL 2026 Findings, arXiv:2505.15960), InternGeometry (arXiv:2512.10534) — but none applies formal verification to the perception stage. TrustGeoGen (arXiv:2504.15780) uses formal verification for geometric data generation (GeoTrust-200K), demonstrating formal tools' maturity in the geometric domain, but targets data quality rather than perception reward signals. FormalGeo (Symmetry 2024, arXiv:2310.18021) and AlphaGeometry2's DDAR engine (JMLR 2025, C++ implementation 300x faster) now make symbolic constraint checking at scale feasible. The ACL 2026 geometry survey (arXiv:2507.11936) identifies formal language representations and automated verification as critical open challenges.\n\n**The key gap all existing perception reward methods share:** they produce scalar/per-step scoring signals. None generates structured diagnostic output identifying which specific fact contradicts which geometric constraint, with formal correctness guarantees. This diagnostic capability enables a qualitatively new mechanism — targeted re-perception — that no scoring-based approach can support.\n\n## Proposed Approach\n\nWe propose FormalPerceptReward (FPR), the first framework using formal geometric constraint propagation to generate diagnostic reward signals for perception-stage RL training, enabling targeted re-perception at test time.\n\n**Core contribution chain** (each enabling the next):\n1. **Formally guaranteed reward precision** (foundation): When VLM-produced CDL is syntactically valid, FormalGeo's constraint propagation detects contradictions that are logically provable — zero false positives. This guarantee does not hold for neural judges (which hallucinate), rule-based F1 (which produces noisy scores from imperfect primitive extraction), or neural proxies (which can misjudge).\n2. **Actionable diagnostic output** (core novelty): Beyond scoring, FPR produces per-fact structured diagnostics: \"∠ABC=90° contradicts A on circle with diameter BC by the inscribed angle theorem.\" This is a qualitative shift from scoring to diagnosing — no existing perception reward method provides this.\n3. **Targeted re-perception at test time** (enabled application): Diagnostic output supports selective re-examination of specific erroneous facts rather than full-diagram re-processing.\n\n**Why training-time formal reward, not just test-time formal filtering?** One might ask whether best-of-N sampling + formal verification re-ranking suffices. Training-time formal rewards internalize geometric constraint awareness into the model, improving single-pass perception quality. Test-time filtering cannot teach the model what constitutes formally consistent perception; it only selects among existing outputs. Moreover, best-of-N compute scales linearly with N, while trained models deliver better base quality at fixed inference cost.\n\n**Pipeline.** Qwen3-VL-8B outputs structured geometric facts in FormalGeo's Conditional Declaration Language (CDL). FormalGeo's symbolic solver performs constraint propagation, producing per-fact diagnostic rewards. These replace learned neural judges in GRPO training on FormalGeo7K (~7K annotated problems).\n\n**Translator feasibility.** Converting visual perception to syntactically valid CDL is non-trivial. FGeo-Parser (Symmetry 2025) achieves 91.5% sentence-level match accuracy but only 56.5% perfect full-expression accuracy on FormalGeo data. Mitigation:\n- SFT warm-start: Fine-tune Qwen3-VL-8B on FormalGeo7K ground-truth CDL before GRPO\n- Graceful degradation: Syntactically invalid CDL receives fixed low reward + rule-based F1 fallback\n- Reward curriculum: Phase 1 (rule-based F1 dominant, CDL quality low) → Phase 2 (mixed, formal weight rises with FVUR-syntax) → Phase 3 (formal dominant). Transition governed by FVUR-syntax monitoring.\n\n**Formally detectable error types.** Geometric problems typically feature over-determined constraint systems where a single incorrect fact (e.g., a misread angle) propagates into detectable contradictions. However, missing-primitive errors (e.g., failing to detect a point entirely) may not produce contradictions — only information insufficiency. The M1 pilot study (below) will quantify the proportion of each error type and calibrate expectations for formal verification coverage.\n\n**Formal verification engine.** FormalGeo's symbolic solver is the primary engine (native CDL). AlphaGeometry2's C++ DDAR (300x faster, JMLR 2025) provides optional deeper deduction for multi-step theorem applications, with CDL-to-DDAR predicate conversion validated for accuracy (concordance >90% required; if not met, DDAR is dropped). DDAR's incremental value tested via ablation.\n\n**Targeted re-perception protocol (test time):**\n1. VLM extracts facts → FormalGeo solver identifies contradictions with constraint explanations\n2. Contradictions ranked by severity; top-k (k=1–2) flagged per round\n3. Re-prompt VLM: \"∠ABC was extracted as 90° but contradicts [constraint] — re-examine ∠ABC\"\n4. Re-run constraint checking on updated facts\n5. Terminate: no new contradictions OR facts unchanged OR max 3 rounds\n\n## Research Landscape\n\nThe perception bottleneck is well-documented: GPT-4o exhibits 70% error rate on geometric primitive grounding (SVE-Math, arXiv:2501.06430). CogFlow (ICLR 2026, arXiv:2601.01874) bridges perception and reasoning through knowledge internalization. EVPV (arXiv:2603.16253) separates grounding errors from reasoning errors via constraint matching and reliability-gating. GeoSketch (arXiv:2509.22460) implements diagram auto-correction via MLLM but \"does not assess the correctness or validity of intermediate steps.\" TangramSR (arXiv:2602.05570) achieves test-time self-refinement via geometric consistency feedback (IoU 0.63→0.932 on Tangram spatial assembly), but uses heuristic IoU on continuous spatial tasks rather than formal theorem-level verification on symbolic Euclidean geometry, and is training-free. Sketch2Feedback (arXiv:2602.18520) demonstrates a perception→symbolic→constraint→feedback pipeline for STEM diagrams, validating the architecture for educational feedback.\n\n**Closest works — key differentiations:**\n\n| Method | Reward Type | Formal Guarantee | Diagnostic Output | Stage |\n|--------|-----------|-----------------|-------------------|-------|\n| SymHPR (arXiv:2512.03126) | Per-primitive F1/L2 | No (rule-based, noisy) | No | Perception |\n| \"Bad Seeing or Bad Thinking?\" (arXiv:2605.14054) | Per-step binary PV | No (neural proxy) | No | Perception |\n| PDCR (arXiv:2605.13467) | Decomposed confidence | No (scalar) | No | Perception |\n| ViCrit (arXiv:2506.10128) | Binary hallucination | No (proxy task) | No | Perception |\n| SGVR (arXiv:2601.05073) | Sub-goal verification | Yes | Partial | Reasoning |\n| FoVer (ACL 2026, arXiv:2505.15960) | Step-level PRM data | Yes | Partial | Reasoning |\n| InternGeometry (arXiv:2512.10534) | DDAR-based | Yes | No | Reasoning |\n| TrustGeoGen (arXiv:2504.15780) | N/A (data generation) | Yes | N/A | Data |\n| **FPR (ours)** | **Per-fact diagnostic** | **Yes (zero FP on valid CDL)** | **Yes (contradiction + theorem)** | **Perception** |\n\n## Experimental Design\n\n**Base model:** Qwen3-VL-8B.\n\n**Training data:** FormalGeo7K (~7K problems with ground-truth CDL). Geometry3K for OOD evaluation only (lacks CDL). If 7K proves insufficient (A5 scaling curve unsaturated), FormalGeo7K augmentation to 133K+ is available as expansion.\n\n**Training-time baselines:**\n1. **Accuracy-only GRPO**: Binary final-answer reward\n2. **SymHPR** (arXiv:2512.03126): Rule-based per-primitive F1/L2 — most critical (formal vs. rule-based)\n3. **Perception-R1** (arXiv:2506.07218): Neural judge reward\n4. **GeoDPO** (arXiv:2602.22703): Learned translator reward\n5. **SGVR** (arXiv:2601.05073): Formal verification for reasoning only\n6. **PDCR** (arXiv:2605.13467): Decomposed confidence reward (open-source)\n7. **\"Bad Seeing or Bad Thinking?\" PV** (arXiv:2605.14054): Blindfolded reasoning proxy — conditional baseline (if code available or reproducible from method description)\n\n**Test-time baselines:**\n- Self-consistency@N (N=3, 5)\n- Best-of-N + formal verification re-ranking (N=3, 5)\n- Full-diagram re-processing\n- No re-perception (single-pass)\n- **Oracle re-perception**: Ground-truth contradiction info guides re-perception → upper bound\n\n**Ablations:**\n- A1: Formal constraint propagation reward vs. rule-based F1 (SymHPR-style) — core\n- A2: FormalGeo solver only vs. FormalGeo + DDAR — deeper deduction value\n- A3: Dense per-fact diagnostic reward vs. holistic binary reward — granularity\n- A4: Targeted re-perception vs. all test-time baselines — mechanism evaluation\n- A5: Training data scale (1K / 3K / 7K) — sample efficiency\n- A6: Reward curriculum (phased rule-based→formal) vs. formal-only vs. rule-based-only — curriculum value\n- A7: CDL quality sensitivity — oracle CDL (ground-truth) vs. learned CDL at SFT epochs 0/2/5 — quantifies translator bottleneck\n\n**Evaluation benchmarks:**\n- **GeoPerceive** (from GeoDPO): Perception-isolated — primary perception metric\n- **GePBench** (arXiv:2412.21036): Perception-specific, independently defined\n- **GeoQA, Geometry3K, PGPS9K**: Standard comprehensive benchmarks\n- **MathVerse**: Cross-paper comparison (SymHPR reports +3%)\n\n**Key metrics:**\n- Per-fact precision/recall/F1 on geometric fact extraction\n- FVUR-syntax: Proportion of rollouts with syntactically valid CDL entering solver\n- DYR (Diagnostic Yield Rate): Proportion of valid-CDL rollouts where solver produces ≥1 per-fact diagnostic — the true measure of FPR's effective coverage\n- FVUR-syntax and DYR tracked over training steps (curve)\n- DYR-conditioned performance: Stratified by DYR>80% vs. DYR<50%\n- Translator CDL accuracy (sentence-level + full-expression) on held-out set\n- Re-perception success rate, average rounds, per-fact accuracy delta\n- Oracle re-perception gap analysis: decompose into diagnostic quality gap vs. VLM re-perception capability gap\n- Per-step reward computation latency for each mechanism\n- Performance vs. wall-clock scaling curves; compute-matched control (baselines given equal wall-clock via more rollouts)\n\n**Statistical rigor:** FPR + SymHPR + accuracy-only GRPO: 3 seeds (mean ± std). Other baselines: 2 seeds (range).\n\n**Pre-experiment validation (M1):**\n1. Pilot study (500 problems): Extract CDL with baseline VLM, run rule-based F1 and FormalGeo solver, measure formal-unique error proportion and error type distribution (numeric/relational vs. missing-primitive)\n2. Profiling: Per-problem latency for constraint propagation + diagnostic output (FormalGeo only; FormalGeo + DDAR)\n3. CDL-to-DDAR converter concordance rate on FormalGeo7K ground-truth (>90% required)\n4. Translator CDL accuracy baseline (pre-SFT and post-SFT)\n\n## Key References\n\n- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026, 2602.22703)\n- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025, 2506.07218)\n- Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning (arXiv 2026, 2605.14054)\n- From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models (arXiv 2026, 2605.20177)\n- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026, 2605.13467)\n- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward [SGVR] (arXiv 2026, 2601.05073)\n- Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs [SVE-Math] (arXiv 2025, 2501.06430)\n- Solving Olympiad Geometry without Human Demonstrations [AlphaGeometry] (Nature 2024)\n- Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2 (JMLR 2025)\n- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (Symmetry 2024, arXiv 2310.18021)\n- FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems (Symmetry 2025)\n- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025, 2504.15780)\n- ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs (arXiv 2025, 2506.10128)\n- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026, arXiv 2601.01874)\n- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025, 2512.03126)\n- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026, 2603.16253)\n- Efficient PRM Training Data Synthesis via Formal Verification [FoVer] (ACL 2026 Findings, arXiv 2505.15960)\n- GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning (arXiv 2025, 2509.22460)\n- TangramSR: Can Vision-Language Models Reason in Continuous Geometric Space? (arXiv 2026, 2602.05570)\n- Sketch2Feedback: Grammar-in-the-Loop Framework for Rubric-Aligned Feedback on Student STEM Diagrams (arXiv 2026, 2602.18520)\n- GePBench: Evaluating Fundamental Geometric Perception for Multimodal Large Language Models (arXiv 2024, 2412.21036)\n- A Survey of Deep Learning for Geometry Problem Solving (ACL 2026 Main, arXiv 2507.11936)\n- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (arXiv 2025, 2506.04592)\n- InternGeometry: Olympiad-Level Geometry via Complexity-Boosted RL (arXiv 2025, 2512.10534)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 3000–3500 (16x A800-80G: GRPO runs + 7 ablations + 3-seed main + 2-seed baselines + evaluation), timeline: 5 months (M1: SFT warm-start + FormalGeo/DDAR integration + pilot study + profiling + converter validation + translator accuracy baseline; M2–3: GRPO training + reward curriculum + baseline reproduction; M4: evaluation + ablations + multi-seed + oracle analysis; M5: paper writing), estimated_gpu_cost: $6,000–7,000\n- **human_in_loop**: gpu_hours: 2500–3000, timeline: 3.5–4 months, claude_api_cost: $300–500, estimated_gpu_cost: $5,000–6,000\n- **auto_research**: gpu_hours: 3500–4500, timeline: 2.5–3 months, claude_api_cost: $1,200–2,000, estimated_gpu_cost: $7,000–9,000, speed_bottleneck: RL training wall-clock (~16–20h per GRPO run on 16x A800); formal verification throughput to be profiled in M1"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:53:11.432Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:53:11.432Z",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-27T08:53:11.490Z_

# Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning

## Core Problem

How can we provide formally verifiable, diagnostic reward signals for the visual perception stage of multimodal geometric reasoning — signals that pinpoint which specific geometric fact is wrong, explain why it contradicts known geometric constraints, and enable targeted correction at test time?

## Research Opportunity

Current RL approaches for visual math perception produce opaque reward signals that cannot diagnose specific perception errors:
- **GeoDPO** (arXiv:2602.22703): Learned NL-to-DSL translator computes DSL-level rewards; translator can hallucinate scores.
- **Perception-R1** (arXiv:2506.07218): Judge LLM provides visual perception rewards; lacks formal grounding.
- **"Bad Seeing or Bad Thinking?"** (arXiv:2605.14054): Perception Verification (PV) via blindfolded reasoning proxy independently rewards perception fidelity — but remains a neural proxy that reports "perception unreliable" without diagnosing which fact conflicts with which constraint.
- **"From Seeing to Thinking"** (arXiv:2605.20177): Shows perception improves more via RL than caption-based SFT, but uses only generic rewards.
- **PDCR** (arXiv:2605.13467): Decomposes confidence rewards by perception/reasoning clusters — but still scalar confidence, no structural diagnosis.
- **SymHPR** (arXiv:2512.03126): Hierarchical per-primitive rewards (point-on-line, line-on-shape F1/L2), closest to structured perception feedback — but rule-based metrics without formal deduction. Cannot detect semantic contradictions (e.g., angle inconsistent with circle theorem), and F1 can be noisy when primitive extraction itself errs.
- **ViCrit** (arXiv:2506.10128, NeurIPS 2025): Verifiable RL proxy task via synthetic hallucination injection with binary exact-match reward — validates verifiable perception rewards but uses domain-agnostic hallucination detection, not domain-specific formal geometric verification.

Formal verification for reasoning-stage rewards has proven effective — SGVR (arXiv:2601.05073, +9.7%), Safe (arXiv:2506.04592), FoVer (ACL 2026 Findings, arXiv:2505.15960), InternGeometry (arXiv:2512.10534) — but none applies formal verification to the perception stage. TrustGeoGen (arXiv:2504.15780) uses formal verification for geometric data generation (GeoTrust-200K), demonstrating formal tools' maturity in the geometric domain, but targets data quality rather than perception reward signals. FormalGeo (Symmetry 2024, arXiv:2310.18021) and AlphaGeometry2's DDAR engine (JMLR 2025, C++ implementation 300x faster) now make symbolic constraint checking at scale feasible. The ACL 2026 geometry survey (arXiv:2507.11936) identifies formal language representations and automated verification as critical open challenges.

**The key gap all existing perception reward methods share:** they produce scalar/per-step scoring signals. None generates structured diagnostic output identifying which specific fact contradicts which geometric constraint, with formal correctness guarantees. This diagnostic capability enables a qualitatively new mechanism — targeted re-perception — that no scoring-based approach can support.

## Proposed Approach

We propose FormalPerceptReward (FPR), the first framework using formal geometric constraint propagation to generate diagnostic reward signals for perception-stage RL training, enabling targeted re-perception at test time.

**Core contribution chain** (each enabling the next):
1. **Formally guaranteed reward precision** (foundation): When VLM-produced CDL is syntactically valid, FormalGeo's constraint propagation detects contradictions that are logically provable — zero false positives. This guarantee does not hold for neural judges (which hallucinate), rule-based F1 (which produces noisy scores from imperfect primitive extraction), or neural proxies (which can misjudge).
2. **Actionable diagnostic output** (core novelty): Beyond scoring, FPR produces per-fact structured diagnostics: "∠ABC=90° contradicts A on circle with diameter BC by the inscribed angle theorem." This is a qualitative shift from scoring to diagnosing — no existing perception reward method provides this.
3. **Targeted re-perception at test time** (enabled application): Diagnostic output supports selective re-examination of specific erroneous facts rather than full-diagram re-processing.

**Why training-time formal reward, not just test-time formal filtering?** One might ask whether best-of-N sampling + formal verification re-ranking suffices. Training-time formal rewards internalize geometric constraint awareness into the model, improving single-pass perception quality. Test-time filtering cannot teach the model what constitutes formally consistent perception; it only selects among existing outputs. Moreover, best-of-N compute scales linearly with N, while trained models deliver better base quality at fixed inference cost.

**Pipeline.** Qwen3-VL-8B outputs structured geometric facts in FormalGeo's Conditional Declaration Language (CDL). FormalGeo's symbolic solver performs constraint propagation, producing per-fact diagnostic rewards. These replace learned neural judges in GRPO training on FormalGeo7K (~7K annotated problems).

**Translator feasibility.** Converting visual perception to syntactically valid CDL is non-trivial. FGeo-Parser (Symmetry 2025) achieves 91.5% sentence-level match accuracy but only 56.5% perfect full-expression accuracy on FormalGeo data. Mitigation:
- SFT warm-start: Fine-tune Qwen3-VL-8B on FormalGeo7K ground-truth CDL before GRPO
- Graceful degradation: Syntactically invalid CDL receives fixed low reward + rule-based F1 fallback
- Reward curriculum: Phase 1 (rule-based F1 dominant, CDL quality low) → Phase 2 (mixed, formal weight rises with FVUR-syntax) → Phase 3 (formal dominant). Transition governed by FVUR-syntax monitoring.

**Formally detectable error types.** Geometric problems typically feature over-determined constraint systems where a single incorrect fact (e.g., a misread angle) propagates into detectable contradictions. However, missing-primitive errors (e.g., failing to detect a point entirely) may not produce contradictions — only information insufficiency. The M1 pilot study (below) will quantify the proportion of each error type and calibrate expectations for formal verification coverage.

**Formal verification engine.** FormalGeo's symbolic solver is the primary engine (native CDL). AlphaGeometry2's C++ DDAR (300x faster, JMLR 2025) provides optional deeper deduction for multi-step theorem applications, with CDL-to-DDAR predicate conversion validated for accuracy (concordance >90% required; if not met, DDAR is dropped). DDAR's incremental value tested via ablation.

**Targeted re-perception protocol (test time):**
1. VLM extracts facts → FormalGeo solver identifies contradictions with constraint explanations
2. Contradictions ranked by severity; top-k (k=1–2) flagged per round
3. Re-prompt VLM: "∠ABC was extracted as 90° but contradicts [constraint] — re-examine ∠ABC"
4. Re-run constraint checking on updated facts
5. Terminate: no new contradictions OR facts unchanged OR max 3 rounds

## Research Landscape

The perception bottleneck is well-documented: GPT-4o exhibits 70% error rate on geometric primitive grounding (SVE-Math, arXiv:2501.06430). CogFlow (ICLR 2026, arXiv:2601.01874) bridges perception and reasoning through knowledge internalization. EVPV (arXiv:2603.16253) separates grounding errors from reasoning errors via constraint matching and reliability-gating. GeoSketch (arXiv:2509.22460) implements diagram auto-correction via MLLM but "does not assess the correctness or validity of intermediate steps." TangramSR (arXiv:2602.05570) achieves test-time self-refinement via geometric consistency feedback (IoU 0.63→0.932 on Tangram spatial assembly), but uses heuristic IoU on continuous spatial tasks rather than formal theorem-level verification on symbolic Euclidean geometry, and is training-free. Sketch2Feedback (arXiv:2602.18520) demonstrates a perception→symbolic→constraint→feedback pipeline for STEM diagrams, validating the architecture for educational feedback.

**Closest works — key differentiations:**

| Method | Reward Type | Formal Guarantee | Diagnostic Output | Stage |
|--------|-----------|-----------------|-------------------|-------|
| SymHPR (arXiv:2512.03126) | Per-primitive F1/L2 | No (rule-based, noisy) | No | Perception |
| "Bad Seeing or Bad Thinking?" (arXiv:2605.14054) | Per-step binary PV | No (neural proxy) | No | Perception |
| PDCR (arXiv:2605.13467) | Decomposed confidence | No (scalar) | No | Perception |
| ViCrit (arXiv:2506.10128) | Binary hallucination | No (proxy task) | No | Perception |
| SGVR (arXiv:2601.05073) | Sub-goal verification | Yes | Partial | Reasoning |
| FoVer (ACL 2026, arXiv:2505.15960) | Step-level PRM data | Yes | Partial | Reasoning |
| InternGeometry (arXiv:2512.10534) | DDAR-based | Yes | No | Reasoning |
| TrustGeoGen (arXiv:2504.15780) | N/A (data generation) | Yes | N/A | Data |
| **FPR (ours)** | **Per-fact diagnostic** | **Yes (zero FP on valid CDL)** | **Yes (contradiction + theorem)** | **Perception** |

## Experimental Design

**Base model:** Qwen3-VL-8B.

**Training data:** FormalGeo7K (~7K problems with ground-truth CDL). Geometry3K for OOD evaluation only (lacks CDL). If 7K proves insufficient (A5 scaling curve unsaturated), FormalGeo7K augmentation to 133K+ is available as expansion.

**Training-time baselines:**
1. **Accuracy-only GRPO**: Binary final-answer reward
2. **SymHPR** (arXiv:2512.03126): Rule-based per-primitive F1/L2 — most critical (formal vs. rule-based)
3. **Perception-R1** (arXiv:2506.07218): Neural judge reward
4. **GeoDPO** (arXiv:2602.22703): Learned translator reward
5. **SGVR** (arXiv:2601.05073): Formal verification for reasoning only
6. **PDCR** (arXiv:2605.13467): Decomposed confidence reward (open-source)
7. **"Bad Seeing or Bad Thinking?" PV** (arXiv:2605.14054): Blindfolded reasoning proxy — conditional baseline (if code available or reproducible from method description)

**Test-time baselines:**
- Self-consistency@N (N=3, 5)
- Best-of-N + formal verification re-ranking (N=3, 5)
- Full-diagram re-processing
- No re-perception (single-pass)
- **Oracle re-perception**: Ground-truth contradiction info guides re-perception → upper bound

**Ablations:**
- A1: Formal constraint propagation reward vs. rule-based F1 (SymHPR-style) — core
- A2: FormalGeo solver only vs. FormalGeo + DDAR — deeper deduction value
- A3: Dense per-fact diagnostic reward vs. holistic binary reward — granularity
- A4: Targeted re-perception vs. all test-time baselines — mechanism evaluation
- A5: Training data scale (1K / 3K / 7K) — sample efficiency
- A6: Reward curriculum (phased rule-based→formal) vs. formal-only vs. rule-based-only — curriculum value
- A7: CDL quality sensitivity — oracle CDL (ground-truth) vs. learned CDL at SFT epochs 0/2/5 — quantifies translator bottleneck

**Evaluation benchmarks:**
- **GeoPerceive** (from GeoDPO): Perception-isolated — primary perception metric
- **GePBench** (arXiv:2412.21036): Perception-specific, independently defined
- **GeoQA, Geometry3K, PGPS9K**: Standard comprehensive benchmarks
- **MathVerse**: Cross-paper comparison (SymHPR reports +3%)

**Key metrics:**
- Per-fact precision/recall/F1 on geometric fact extraction
- FVUR-syntax: Proportion of rollouts with syntactically valid CDL entering solver
- DYR (Diagnostic Yield Rate): Proportion of valid-CDL rollouts where solver produces ≥1 per-fact diagnostic — the true measure of FPR's effective coverage
- FVUR-syntax and DYR tracked over training steps (curve)
- DYR-conditioned performance: Stratified by DYR>80% vs. DYR<50%
- Translator CDL accuracy (sentence-level + full-expression) on held-out set
- Re-perception success rate, average rounds, per-fact accuracy delta
- Oracle re-perception gap analysis: decompose into diagnostic quality gap vs. VLM re-perception capability gap
- Per-step reward computation latency for each mechanism
- Performance vs. wall-clock scaling curves; compute-matched control (baselines given equal wall-clock via more rollouts)

**Statistical rigor:** FPR + SymHPR + accuracy-only GRPO: 3 seeds (mean ± std). Other baselines: 2 seeds (range).

**Pre-experiment validation (M1):**
1. Pilot study (500 problems): Extract CDL with baseline VLM, run rule-based F1 and FormalGeo solver, measure formal-unique error proportion and error type distribution (numeric/relational vs. missing-primitive)
2. Profiling: Per-problem latency for constraint propagation + diagnostic output (FormalGeo only; FormalGeo + DDAR)
3. CDL-to-DDAR converter concordance rate on FormalGeo7K ground-truth (>90% required)
4. Translator CDL accuracy baseline (pre-SFT and post-SFT)

## Key References

- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026, 2602.22703)
- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025, 2506.07218)
- Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning (arXiv 2026, 2605.14054)
- From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models (arXiv 2026, 2605.20177)
- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026, 2605.13467)
- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward [SGVR] (arXiv 2026, 2601.05073)
- Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs [SVE-Math] (arXiv 2025, 2501.06430)
- Solving Olympiad Geometry without Human Demonstrations [AlphaGeometry] (Nature 2024)
- Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2 (JMLR 2025)
- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (Symmetry 2024, arXiv 2310.18021)
- FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems (Symmetry 2025)
- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025, 2504.15780)
- ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs (arXiv 2025, 2506.10128)
- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026, arXiv 2601.01874)
- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025, 2512.03126)
- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026, 2603.16253)
- Efficient PRM Training Data Synthesis via Formal Verification [FoVer] (ACL 2026 Findings, arXiv 2505.15960)
- GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning (arXiv 2025, 2509.22460)
- TangramSR: Can Vision-Language Models Reason in Continuous Geometric Space? (arXiv 2026, 2602.05570)
- Sketch2Feedback: Grammar-in-the-Loop Framework for Rubric-Aligned Feedback on Student STEM Diagrams (arXiv 2026, 2602.18520)
- GePBench: Evaluating Fundamental Geometric Perception for Multimodal Large Language Models (arXiv 2024, 2412.21036)
- A Survey of Deep Learning for Geometry Problem Solving (ACL 2026 Main, arXiv 2507.11936)
- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (arXiv 2025, 2506.04592)
- InternGeometry: Olympiad-Level Geometry via Complexity-Boosted RL (arXiv 2025, 2512.10534)

## Resource Estimate

- **manual**: gpu_hours: 3000–3500 (16x A800-80G: GRPO runs + 7 ablations + 3-seed main + 2-seed baselines + evaluation), timeline: 5 months (M1: SFT warm-start + FormalGeo/DDAR integration + pilot study + profiling + converter validation + translator accuracy baseline; M2–3: GRPO training + reward curriculum + baseline reproduction; M4: evaluation + ablations + multi-seed + oracle analysis; M5: paper writing), estimated_gpu_cost: $6,000–7,000
- **human_in_loop**: gpu_hours: 2500–3000, timeline: 3.5–4 months, claude_api_cost: $300–500, estimated_gpu_cost: $5,000–6,000
- **auto_research**: gpu_hours: 3500–4500, timeline: 2.5–3 months, claude_api_cost: $1,200–2,000, estimated_gpu_cost: $7,000–9,000, speed_bottleneck: RL training wall-clock (~16–20h per GRPO run on 16x A800); formal verification throughput to be profiled in M1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "6b057f1a-607d-48d0-890d-8ac20ee0730d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:53:11.489Z_

```json
{
  "parentUuid": "6b057f1a-607d-48d0-890d-8ac20ee0730d",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "a0df243d-0201-421f-8768-90ea09a594d7",
  "timestamp": "2026-05-27T08:53:11.489Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:53:11.489Z_

```json
{
  "parentUuid": "a0df243d-0201-421f-8768-90ea09a594d7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e3ff3f20-336d-451a-9b2e-03f55bc86646",
  "timestamp": "2026-05-27T08:53:11.489Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning  ## Core Problem  How can we provide formally verifiable, diagnostic reward signals for the visual per…",
  "leafUuid": "e3ff3f20-336d-451a-9b2e-03f55bc86646",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal geometric perception rewards for vision-language reasoning",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:53:16.457Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal for the "发掘 agent" role. I need to:

1. First do thorough literature research via WebSearch
2. Then assess novelty, significance, and related work differentiation
3. Provide concrete suggestions for strengthening the idea's ceiling

Let me start by searching for the most relevant recent works and the current state of this research area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3ff3f20-336d-451a-9b2e-03f55bc86646",
  "isSidechain": false,
  "requestId": "req_011CbSnp5TXFP4A3nwZvBCsc",
  "type": "assistant",
  "uuid": "dc1b1673-7797-4f3a-a8f3-541054ba29ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6h2yXJPYALwqjJaxczgYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6186,
      "cache_read_input_tokens": 14184,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 6186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6186
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-27T08:53:17.034Z_

I need to do thorough literature research before making any assessments. Let me start with targeted searches on the key aspects of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc1b1673-7797-4f3a-a8f3-541054ba29ec",
  "isSidechain": false,
  "requestId": "req_011CbSnp5TXFP4A3nwZvBCsc",
  "type": "assistant",
  "uuid": "ba46ed48-0c23-4fb8-984b-981d00a8d1ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6h2yXJPYALwqjJaxczgYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6186,
      "cache_read_input_tokens": 14184,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 6186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6186
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-27T08:53:17.391Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JQ34c7JqS6r3MpmYefoapz`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba46ed48-0c23-4fb8-984b-981d00a8d1ba",
  "isSidechain": false,
  "requestId": "req_011CbSnp5TXFP4A3nwZvBCsc",
  "type": "assistant",
  "uuid": "33934517-4ea2-47c6-87a8-7218344799f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6h2yXJPYALwqjJaxczgYw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6186,
      "cache_read_input_tokens": 14184,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 6186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6186
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-27T08:53:17.399Z_

<details><summary>↩ Tool result · `toolu_01JQ34c7JqS6r3MpmYefoapz`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33934517-4ea2-47c6-87a8-7218344799f6",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "7b1732a0-5632-4a34-a566-acc84567d428",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "33934517-4ea2-47c6-87a8-7218344799f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T08:53:19.885Z_

Now let me conduct the prerequisite literature research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b1732a0-5632-4a34-a566-acc84567d428",
  "isSidechain": false,
  "requestId": "req_011CbSnpWjZ4Nv8F8tHYmxRL",
  "type": "assistant",
  "uuid": "c9ceceb0-4090-414b-a623-27f693395d2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdwKGAWnKvgHWy1Tbo5DqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 20370,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 81,
          "cache_read_input_tokens": 20370,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 731
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T08:53:20.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016MZYQRFWyeDb5VyiwKypr6`</summary>

```json
{
  "query": "formal verification geometric perception reward VLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9ceceb0-4090-414b-a623-27f693395d2a",
  "isSidechain": false,
  "requestId": "req_011CbSnpWjZ4Nv8F8tHYmxRL",
  "type": "assistant",
  "uuid": "2f97aea7-6356-4baf-978b-e7665d8db65b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdwKGAWnKvgHWy1Tbo5DqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 20370,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 81,
          "cache_read_input_tokens": 20370,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 731
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T08:53:28.092Z_

<details><summary>↩ Tool result · `toolu_016MZYQRFWyeDb5VyiwKypr6`</summary>

```text
Web search results for query: "formal verification geometric perception reward VLM 2025 2026"

Links: [{"title":"GitHub - InternRobotics/G2VLM: [CVPR 2026] G2VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning · GitHub","url":"https://github.com/InternRobotics/G2VLM"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models","url":"https://arxiv.org/html/2603.16253"},{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/pdf/2602.22703"},{"title":"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward","url":"https://arxiv.org/pdf/2601.05073"},{"title":"Smooth Operator: Smooth Verifiable Reward Activates Spatial Reasoning Ability of Vision-Language Model","url":"https://arxiv.org/pdf/2601.07695"},{"title":"Unveiling the Compositional Ability Gap in Vision-Language Reasoning Model","url":"https://openreview.net/pdf?id=J76cCYTJub"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2509.25787v4"}]

Based on the search results, here are the key findings for your query about formal verification, geometric perception, reward mechanisms, and VLMs in 2025-2026:

## Key Research Areas

**Geometric Perception & VLMs:**
Geometry problem solving remains particularly challenging for VLMs, with difficulty stemming from the need for accurate geometric perception—models must correctly identify and ground geometric primitives such as points, lines, and circles and their spatial relations within diagrams.

**Verifiable Rewards for Geometric Reasoning:**
The Sub-Goal Verifiable Reward (SGVR) framework facilitates Reinforcement Learning with Verifiable Rewards by replacing sparse outcome rewards with dense, subgoal-oriented signals, using Group Relative Policy Optimization to maximize the Skeleton Rate.

**Spatial Reasoning & Verification:**
Verifiable numerical signals grounded in physical laws offer a promising pathway for bridging the gap between 2D perception and 3D understanding.

**Recent Models & Publications:**
G2VLM is a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for multimodal understanding and spatial reasoning tasks. Additionally, Explicit Visual Premise Verification (EVPV) is a lightweight mechanism that makes a Process Reward Model qualified to judge reasoning steps.

These research directions reflect growing focus on formally verifiable approaches to improve geometric understanding in vision-language models during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f97aea7-6356-4baf-978b-e7665d8db65b",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "edd87084-534b-4f70-8bb6-ba37d4283f6c",
  "toolUseResult": {
    "query": "formal verification geometric perception reward VLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LhkfcXYinTWFA7hj4nquMi",
        "content": [
          {
            "title": "GitHub - InternRobotics/G2VLM: [CVPR 2026] G2VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning · GitHub",
            "url": "https://github.com/InternRobotics/G2VLM"
          },
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models",
            "url": "https://arxiv.org/html/2603.16253"
          },
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.22703"
          },
          {
            "title": "Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward",
            "url": "https://arxiv.org/pdf/2601.05073"
          },
          {
            "title": "Smooth Operator: Smooth Verifiable Reward Activates Spatial Reasoning Ability of Vision-Language Model",
            "url": "https://arxiv.org/pdf/2601.07695"
          },
          {
            "title": "Unveiling the Compositional Ability Gap in Vision-Language Reasoning Model",
            "url": "https://openreview.net/pdf?id=J76cCYTJub"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2509.25787v4"
          }
        ]
      },
      "Based on the search results, here are the key findings for your query about formal verification, geometric perception, reward mechanisms, and VLMs in 2025-2026:\n\n## Key Research Areas\n\n**Geometric Perception & VLMs:**\nGeometry problem solving remains particularly challenging for VLMs, with difficulty stemming from the need for accurate geometric perception—models must correctly identify and ground geometric primitives such as points, lines, and circles and their spatial relations within diagrams.\n\n**Verifiable Rewards for Geometric Reasoning:**\nThe Sub-Goal Verifiable Reward (SGVR) framework facilitates Reinforcement Learning with Verifiable Rewards by replacing sparse outcome rewards with dense, subgoal-oriented signals, using Group Relative Policy Optimization to maximize the Skeleton Rate.\n\n**Spatial Reasoning & Verification:**\nVerifiable numerical signals grounded in physical laws offer a promising pathway for bridging the gap between 2D perception and 3D understanding.\n\n**Recent Models & Publications:**\nG2VLM is a unified model that integrates both a geometric perception expert for 3D reconstruction and a semantic perception expert for multimodal understanding and spatial reasoning tasks. Additionally, Explicit Visual Premise Verification (EVPV) is a lightweight mechanism that makes a Process Reward Model qualified to judge reasoning steps.\n\nThese research directions reflect growing focus on formally verifiable approaches to improve geometric understanding in vision-language models during 2025-2026."
    ],
    "durationSeconds": 7.596310307000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2f97aea7-6356-4baf-978b-e7665d8db65b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T08:53:30.652Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HTX9RMuv9ic5GPXkZg8Mgg`</summary>

```json
{
  "query": "SymHPR hierarchical process reward symbolic vision perception 2025 arXiv 2512.03126"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edd87084-534b-4f70-8bb6-ba37d4283f6c",
  "isSidechain": false,
  "requestId": "req_011CbSnqJ9HuZJXz2nd4cutY",
  "type": "assistant",
  "uuid": "5f98ad55-b2d5-4413-bbe1-97eb5504a2be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ekf9UtwQkoP6DDWYfvpBaZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 21101,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 21101,
          "cache_creation_input_tokens": 798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 798
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T08:53:36.313Z_

<details><summary>↩ Tool result · `toolu_01HTX9RMuv9ic5GPXkZg8Mgg`</summary>

```text
Web search results for query: "SymHPR hierarchical process reward symbolic vision perception 2025 arXiv 2512.03126"

Links: [{"title":"[2512.03126] Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/abs/2512.03126"},{"title":"Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/html/2512.03126"},{"title":"Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/pdf/2512.03126"},{"title":"[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models","url":"https://arxiv.org/abs/2604.24583"},{"title":"Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned","url":"https://arxiv.org/pdf/2509.23250"}]

I found the paper for you! Here's what I discovered:

**Title:** Hierarchical Process Reward Models are Symbolic Vision Learners

**Overview:** The paper focuses on symbolic computer vision, which represents diagrams through explicit logical rules and structured representations, enabling interpretable understanding in machine vision.

**Key Contribution - SymHPR:** The core contribution is SymHPR (Symbolic Hierarchical Process Reward Modeling), which applies hierarchical step-level parsing rewards to enforce point-on-line, line-on-shape, and shape-on-relation consistency.

**Approach:** The authors propose a novel self-supervised symbolic auto-encoder that encodes diagrams into structured primitives and their interrelationships within the latent space, and decodes them through an executable engine to reconstruct the input diagrams.

**Results:** The evaluations demonstrate effectiveness across reconstruction, perception, and reasoning tasks: achieving a 98.2% reduction in MSE for geometric diagram reconstruction, surpassing GPT-4o by 0.6% with a 7B model on chart reconstruction.

The paper was published on December 2, 2025 on arXiv and develops a neuro-symbolic system that integrates the reasoning capabilities of neural networks with the interpretability of symbolic models through reasoning-grounded visual rewards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f98ad55-b2d5-4413-bbe1-97eb5504a2be",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "73ed786e-2f3e-457e-8970-827b21e02932",
  "toolUseResult": {
    "query": "SymHPR hierarchical process reward symbolic vision perception 2025 arXiv 2512.03126",
    "results": [
      {
        "tool_use_id": "srvtoolu_019f41AcZMqrUk34bwG42ebj",
        "content": [
          {
            "title": "[2512.03126] Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/abs/2512.03126"
          },
          {
            "title": "Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/html/2512.03126"
          },
          {
            "title": "Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/pdf/2512.03126"
          },
          {
            "title": "[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models",
            "url": "https://arxiv.org/abs/2604.24583"
          },
          {
            "title": "Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned",
            "url": "https://arxiv.org/pdf/2509.23250"
          }
        ]
      },
      "I found the paper for you! Here's what I discovered:\n\n**Title:** Hierarchical Process Reward Models are Symbolic Vision Learners\n\n**Overview:** The paper focuses on symbolic computer vision, which represents diagrams through explicit logical rules and structured representations, enabling interpretable understanding in machine vision.\n\n**Key Contribution - SymHPR:** The core contribution is SymHPR (Symbolic Hierarchical Process Reward Modeling), which applies hierarchical step-level parsing rewards to enforce point-on-line, line-on-shape, and shape-on-relation consistency.\n\n**Approach:** The authors propose a novel self-supervised symbolic auto-encoder that encodes diagrams into structured primitives and their interrelationships within the latent space, and decodes them through an executable engine to reconstruct the input diagrams.\n\n**Results:** The evaluations demonstrate effectiveness across reconstruction, perception, and reasoning tasks: achieving a 98.2% reduction in MSE for geometric diagram reconstruction, surpassing GPT-4o by 0.6% with a 7B model on chart reconstruction.\n\nThe paper was published on December 2, 2025 on arXiv and develops a neuro-symbolic system that integrates the reasoning capabilities of neural networks with the interpretability of symbolic models through reasoning-grounded visual rewards."
    ],
    "durationSeconds": 5.656907895000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5f98ad55-b2d5-4413-bbe1-97eb5504a2be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T08:53:50.975Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012XoR9waiAwFhRP8z8ws9pC`</summary>

```json
{
  "query": "FormalGeo constraint propagation CDL geometric problem solving perception error detection 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73ed786e-2f3e-457e-8970-827b21e02932",
  "isSidechain": false,
  "requestId": "req_011CbSnqvSrCn73pMebAShLr",
  "type": "assistant",
  "uuid": "f1b09e9c-5f22-4e37-a394-0129594f32e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEYXKq943C42VdmydoUnf5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 644,
      "cache_read_input_tokens": 21899,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 644,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 21899,
          "cache_creation_input_tokens": 644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 644
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T08:53:58.765Z_

<details><summary>↩ Tool result · `toolu_012XoR9waiAwFhRP8z8ws9pC`</summary>

```text
Web search results for query: "FormalGeo constraint propagation CDL geometric problem solving perception error detection 2024 2025"

Links: [{"title":"FormalGeo: An Extensible Formalized Framework For Olympiad Geometric Problem Solving","url":"https://arxiv.org/html/2310.18021v6"},{"title":"FormalGeo: The First Step Toward Human-like IMO-level Geometric Automated Reasoning","url":"https://arxiv.org/html/2310.18021v5"},{"title":"FormalGeo: An Extensible Formalized Framework For Olympiad Geometric Problem","url":"https://arxiv.org/pdf/2310.18021"},{"title":"FGeo-HyperGNet: Geometric Problem Solving Integrating FormalGeo Symbolic System and Hypergraph Neural Network","url":"https://arxiv.org/pdf/2402.11461"},{"title":"FormalGeo: Formal representation and solving for Euclidean plane geometry problems","url":"https://formalgeo.github.io/"},{"title":"Citation: Zhang, X.; Zhu, N.; He, Y.; Zou, J.; Qin, C.; Li, Y.; Leng, T.","url":"https://formalgeo.github.io/papers/zhang2024fgeosss.pdf"},{"title":"FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep   Reinforcement Learning","url":"https://arxiv.org/pdf/2402.09051"},{"title":"Concise Geometric Description as a Bridge: Unleashing the Potential of LLM for Plane Geometry Problem Solving","url":"https://arxiv.org/html/2601.21164"},{"title":"System and method of perception error evaluation and correction by solving optimization problems under the probabilistic signal temporal logic based constraints","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11334767"}]

Based on the search results, here's what I found about FormalGeo, constraint propagation, CDL, and geometric problem solving:

## FormalGeo Framework

FormalGeo is a consistent formal plane geometry system designed for automated geometric problem solving. Formal languages in FormalGeo are categorized into geometry definition language (GDL) and conditional declaration language (CDL), where the former is used to define entities, attributes, theorems, and other elements of a geometry formal system, while the latter is employed for declaring known conditions and problem-solving objectives in geometric problems.

## CDL Structure

CDL consists of three main parts: construction statements, condition statements, and goal statements.

## Recent Developments (2024-2025)

The most recent work includes CDL Solver, where an MLLM Interpreter converts geometric inputs into CDL upon which the LLM Solver performs reasoning and derives the final answer. This represents work from January 2026.

## Geometric Problem Solving Performance

Experiments on the formalgeo7k dataset have achieved a problem-solving success rate of 86.40% using the FGeo-DRL approach. The framework enables readable, traceable, and verifiable solutions for geometric problems.

The search results focus primarily on the FormalGeo system for problem solving and CDL representation. For more specific information about constraint propagation techniques or perception error detection in the 2024-2025 timeframe, additional searches may be needed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1b09e9c-5f22-4e37-a394-0129594f32e9",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "78bff53b-36f2-4b2a-88c0-cf8245a08d1c",
  "toolUseResult": {
    "query": "FormalGeo constraint propagation CDL geometric problem solving perception error detection 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ACTjPXCe7NFQ4kno64nteQ",
        "content": [
          {
            "title": "FormalGeo: An Extensible Formalized Framework For Olympiad Geometric Problem Solving",
            "url": "https://arxiv.org/html/2310.18021v6"
          },
          {
            "title": "FormalGeo: The First Step Toward Human-like IMO-level Geometric Automated Reasoning",
            "url": "https://arxiv.org/html/2310.18021v5"
          },
          {
            "title": "FormalGeo: An Extensible Formalized Framework For Olympiad Geometric Problem",
            "url": "https://arxiv.org/pdf/2310.18021"
          },
          {
            "title": "FGeo-HyperGNet: Geometric Problem Solving Integrating FormalGeo Symbolic System and Hypergraph Neural Network",
            "url": "https://arxiv.org/pdf/2402.11461"
          },
          {
            "title": "FormalGeo: Formal representation and solving for Euclidean plane geometry problems",
            "url": "https://formalgeo.github.io/"
          },
          {
            "title": "Citation: Zhang, X.; Zhu, N.; He, Y.; Zou, J.; Qin, C.; Li, Y.; Leng, T.",
            "url": "https://formalgeo.github.io/papers/zhang2024fgeosss.pdf"
          },
          {
            "title": "FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep   Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2402.09051"
          },
          {
            "title": "Concise Geometric Description as a Bridge: Unleashing the Potential of LLM for Plane Geometry Problem Solving",
            "url": "https://arxiv.org/html/2601.21164"
          },
          {
            "title": "System and method of perception error evaluation and correction by solving optimization problems under the probabilistic signal temporal logic based constraints",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11334767"
          }
        ]
      },
      "Based on the search results, here's what I found about FormalGeo, constraint propagation, CDL, and geometric problem solving:\n\n## FormalGeo Framework\n\nFormalGeo is a consistent formal plane geometry system designed for automated geometric problem solving. Formal languages in FormalGeo are categorized into geometry definition language (GDL) and conditional declaration language (CDL), where the former is used to define entities, attributes, theorems, and other elements of a geometry formal system, while the latter is employed for declaring known conditions and problem-solving objectives in geometric problems.\n\n## CDL Structure\n\nCDL consists of three main parts: construction statements, condition statements, and goal statements.\n\n## Recent Developments (2024-2025)\n\nThe most recent work includes CDL Solver, where an MLLM Interpreter converts geometric inputs into CDL upon which the LLM Solver performs reasoning and derives the final answer. This represents work from January 2026.\n\n## Geometric Problem Solving Performance\n\nExperiments on the formalgeo7k dataset have achieved a problem-solving success rate of 86.40% using the FGeo-DRL approach. The framework enables readable, traceable, and verifiable solutions for geometric problems.\n\nThe search results focus primarily on the FormalGeo system for problem solving and CDL representation. For more specific information about constraint propagation techniques or perception error detection in the 2024-2025 timeframe, additional searches may be needed."
    ],
    "durationSeconds": 7.784785542999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f1b09e9c-5f22-4e37-a394-0129594f32e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T08:54:01.335Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016iqpihHm24EjgrfM5yE41A`</summary>

```json
{
  "query": "perception reward reinforcement learning visual math reasoning targeted correction test-time 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78bff53b-36f2-4b2a-88c0-cf8245a08d1c",
  "isSidechain": false,
  "requestId": "req_011CbSnsZJRFE8mGop3vVtFw",
  "type": "assistant",
  "uuid": "30f83512-4e5d-4bb9-80b1-c044670fc5a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yvNcvDjQXdEhLZ5gkoEJL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 22543,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 22543,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 894
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T08:54:10.626Z_

<details><summary>↩ Tool result · `toolu_016iqpihHm24EjgrfM5yE41A`</summary>

```text
Web search results for query: "perception reward reinforcement learning visual math reasoning targeted correction test-time 2026"

Links: [{"title":"Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned","url":"https://arxiv.org/html/2509.23250v3"},{"title":"Perception Before Reasoning: Two-Stage Reinforcement Learning for Visual Reasoning in Vision-Language Models","url":"https://arxiv.org/html/2509.13031v1"},{"title":"CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving","url":"https://arxiv.org/pdf/2601.01874"},{"title":"Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned","url":"https://arxiv.org/pdf/2509.23250"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"One RL to See Them All: Visual Triple Unified Reinforcement Learning","url":"https://arxiv.org/pdf/2505.18129"}]

Based on the search results, I found several relevant recent papers (2025-2026) on this topic:

## Key Research Papers

**1. Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning**

This research proposes perception-focused supervision, enabling Process Reward Models (PRMs) to explicitly detect errors at the visual grounding stage of reasoning. The study covers five multimodal benchmarks (MMMU, PuzzleVQA, AlgoPuzzleVQA, MathVista, and MathVision) and reveals that perception-level supervision leads to significant gains in test-time scaling.

**2. Perception Before Reasoning: Two-Stage Reinforcement Learning**

This work separates training into two distinct phases, enabling targeted learning for each capability, unlike single-stage approaches that jointly train both perception and reasoning abilities. The research uses the MathVista benchmark for evaluation.

**3. CogFlow: Bridging Perception and Reasoning**

CogFlow integrates perception enhancement into a unified reinforcement learning framework through Synergistic Visual Rewards (SynVRs), enabling dynamic perception-reasoning interaction and improving generalization.

**4. V-Triune (Visual Triple Unified Reinforcement Learning)**

V-Triune is the first unified RL system for post-training vision-language models on both visual reasoning and perception tasks.

These papers collectively demonstrate the growing focus on combining perception-level rewards with reinforcement learning for improved visual mathematical reasoning, particularly in test-time scaling scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30f83512-4e5d-4bb9-80b1-c044670fc5a9",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "fff0f5b2-334b-4bc4-9b45-941d463a50eb",
  "toolUseResult": {
    "query": "perception reward reinforcement learning visual math reasoning targeted correction test-time 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FjrnJ1ei9ybwjPgvuciwJp",
        "content": [
          {
            "title": "Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned",
            "url": "https://arxiv.org/html/2509.23250v3"
          },
          {
            "title": "Perception Before Reasoning: Two-Stage Reinforcement Learning for Visual Reasoning in Vision-Language Models",
            "url": "https://arxiv.org/html/2509.13031v1"
          },
          {
            "title": "CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving",
            "url": "https://arxiv.org/pdf/2601.01874"
          },
          {
            "title": "Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned",
            "url": "https://arxiv.org/pdf/2509.23250"
          },
          {
            "title": "GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-RLVR"
          },
          {
            "title": "One RL to See Them All: Visual Triple Unified Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2505.18129"
          }
        ]
      },
      "Based on the search results, I found several relevant recent papers (2025-2026) on this topic:\n\n## Key Research Papers\n\n**1. Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning**\n\nThis research proposes perception-focused supervision, enabling Process Reward Models (PRMs) to explicitly detect errors at the visual grounding stage of reasoning. The study covers five multimodal benchmarks (MMMU, PuzzleVQA, AlgoPuzzleVQA, MathVista, and MathVision) and reveals that perception-level supervision leads to significant gains in test-time scaling.\n\n**2. Perception Before Reasoning: Two-Stage Reinforcement Learning**\n\nThis work separates training into two distinct phases, enabling targeted learning for each capability, unlike single-stage approaches that jointly train both perception and reasoning abilities. The research uses the MathVista benchmark for evaluation.\n\n**3. CogFlow: Bridging Perception and Reasoning**\n\nCogFlow integrates perception enhancement into a unified reinforcement learning framework through Synergistic Visual Rewards (SynVRs), enabling dynamic perception-reasoning interaction and improving generalization.\n\n**4. V-Triune (Visual Triple Unified Reinforcement Learning)**\n\nV-Triune is the first unified RL system for post-training vision-language models on both visual reasoning and perception tasks.\n\nThese papers collectively demonstrate the growing focus on combining perception-level rewards with reinforcement learning for improved visual mathematical reasoning, particularly in test-time scaling scenarios."
    ],
    "durationSeconds": 9.286660600999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "30f83512-4e5d-4bb9-80b1-c044670fc5a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning  ## Core Problem  How can we provide formally verifiable, diagnostic reward signals for the visual per…",
  "leafUuid": "fff0f5b2-334b-4bc4-9b45-941d463a50eb",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal geometric perception rewards for vision-language reasoning",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

### Tool call

_source line 23 · 2026-05-27T08:54:13.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W5cYKHEA8cqs6vg5mfoZHC`</summary>

```json
{
  "query": "\"perception-centric process reward\" OR \"perception verification\" geometric diagram VLM error diagnosis 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff0f5b2-334b-4bc4-9b45-941d463a50eb",
  "isSidechain": false,
  "requestId": "req_011CbSntS2e6N5LnFdkziP2E",
  "type": "assistant",
  "uuid": "a4da550a-e4c3-43fb-b48e-b8a66da81b43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013QtU69eqrhf4KTp6LCNqpp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 23437,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 23437,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 762
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T08:54:22.895Z_

<details><summary>↩ Tool result · `toolu_01W5cYKHEA8cqs6vg5mfoZHC`</summary>

```text
Web search results for query: ""perception-centric process reward" OR "perception verification" geometric diagram VLM error diagnosis 2025 2026"

Links: [{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models","url":"https://arxiv.org/html/2603.16253"},{"title":"Improving Vision-language Models with Perception-centric Process Reward Models","url":"https://arxiv.org/html/2604.24583"},{"title":"[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models","url":"https://arxiv.org/abs/2604.24583"},{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/pdf/2602.22703"},{"title":"Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned","url":"https://arxiv.org/html/2509.23250v3"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"},{"title":"Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned","url":"https://arxiv.org/pdf/2509.23250"}]

Based on the search results, I found several highly relevant papers from 2025-2026 on perception-centric approaches and visual verification for VLM error diagnosis:

## Key Papers Found:

1. **"Improving Vision-language Models with Perception-centric Process Reward Models"** (2026)
   Perceval is a process reward model (PRM) that enables token-level error grounding, which can extract image-related claims from the response and compare them one by one with the visual evidence in the image, ultimately returning claims that contain perceptual errors. Perceval is trained with perception-intensive supervised training data and is integrated into the RL training process.

2. **"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models"** (March 2026)
   The paper introduces Explicit Visual Premise Verification (EVPV) as a lightweight mechanism that makes a PRM "qualified" to judge reasoning steps by prompting the policy to provide a visual checklist of explicit visual premises, while extracting structured visual facts from the image into a constraint set.

3. **"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning"** (2025)
   The approach GEODPO keeps VLMs in the NL regime and introduces an NL-to-DSL translator trained on synthetic NL-DSL pairs, assigning fine-grained DSL-level scores to model outputs converted into reward signals, mitigating distribution shift and yielding perception-focused supervision at scale.

4. **"Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning"** (October 2025)
   Prior studies suggest perception is a major bottleneck in multimodal reasoning, and the paper addresses whether VL-PRMs can be designed to capture perception errors explicitly.

These papers represent the latest advances in perception-centric process reward models and geometric diagram understanding for VLM error diagnosis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4da550a-e4c3-43fb-b48e-b8a66da81b43",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "ab20c1dd-4490-407f-91ab-d2622d8d32ea",
  "toolUseResult": {
    "query": "\"perception-centric process reward\" OR \"perception verification\" geometric diagram VLM error diagnosis 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XM8NWVgdeE75bq1b9t5qF8",
        "content": [
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models",
            "url": "https://arxiv.org/html/2603.16253"
          },
          {
            "title": "Improving Vision-language Models with Perception-centric Process Reward Models",
            "url": "https://arxiv.org/html/2604.24583"
          },
          {
            "title": "[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models",
            "url": "https://arxiv.org/abs/2604.24583"
          },
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.22703"
          },
          {
            "title": "Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned",
            "url": "https://arxiv.org/html/2509.23250v3"
          },
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.16253"
          },
          {
            "title": "Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning: Key Insights and Lessons Learned",
            "url": "https://arxiv.org/pdf/2509.23250"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers from 2025-2026 on perception-centric approaches and visual verification for VLM error diagnosis:\n\n## Key Papers Found:\n\n1. **\"Improving Vision-language Models with Perception-centric Process Reward Models\"** (2026)\n   Perceval is a process reward model (PRM) that enables token-level error grounding, which can extract image-related claims from the response and compare them one by one with the visual evidence in the image, ultimately returning claims that contain perceptual errors. Perceval is trained with perception-intensive supervised training data and is integrated into the RL training process.\n\n2. **\"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models\"** (March 2026)\n   The paper introduces Explicit Visual Premise Verification (EVPV) as a lightweight mechanism that makes a PRM \"qualified\" to judge reasoning steps by prompting the policy to provide a visual checklist of explicit visual premises, while extracting structured visual facts from the image into a constraint set.\n\n3. **\"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning\"** (2025)\n   The approach GEODPO keeps VLMs in the NL regime and introduces an NL-to-DSL translator trained on synthetic NL-DSL pairs, assigning fine-grained DSL-level scores to model outputs converted into reward signals, mitigating distribution shift and yielding perception-focused supervision at scale.\n\n4. **\"Training Vision-Language Process Reward Models for Test-Time Scaling in Multimodal Reasoning\"** (October 2025)\n   Prior studies suggest perception is a major bottleneck in multimodal reasoning, and the paper addresses whether VL-PRMs can be designed to capture perception errors explicitly.\n\nThese papers represent the latest advances in perception-centric process reward models and geometric diagram understanding for VLM error diagnosis."
    ],
    "durationSeconds": 9.224509670999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a4da550a-e4c3-43fb-b48e-b8a66da81b43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T08:54:28.633Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019GTkH2LjYy6wQcpuiGaU97`</summary>

```json
{
  "query": "Perceval perception-centric process reward model token-level error grounding arXiv 2604.24583"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab20c1dd-4490-407f-91ab-d2622d8d32ea",
  "isSidechain": false,
  "requestId": "req_011CbSnuMaXZ1J5BWqw3cSUD",
  "type": "assistant",
  "uuid": "3b265d56-0c12-4b11-bc10-df212b6bb21d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MR4znUWJJxbze2L183Cak",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 24199,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 912,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 24199,
          "cache_creation_input_tokens": 912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 912
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T08:54:35.384Z_

<details><summary>↩ Tool result · `toolu_019GTkH2LjYy6wQcpuiGaU97`</summary>

```text
Web search results for query: "Perceval perception-centric process reward model token-level error grounding arXiv 2604.24583"

Links: [{"title":"[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models","url":"https://arxiv.org/abs/2604.24583"},{"title":"Improving Vision-language Models with Perception-centric Process Reward Models","url":"https://arxiv.org/html/2604.24583"},{"title":"Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought","url":"https://arxiv.org/pdf/2603.22847"},{"title":"Spotlight on Token Perception for Multimodal Reinforcement Learning","url":"https://arxiv.org/html/2510.09285v1"},{"title":"Spotlight on Token Perception for Multimodal Reinforcement Learning","url":"https://arxiv.org/pdf/2510.09285"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"}]

Based on the search results, here's what I found about the paper:

Perceval is a process reward model (PRM) that enables token-level error grounding, which can extract image-related claims from the response and compare them one by one with the visual evidence in the image, ultimately returning claims that contain perceptual errors.

Recent advancements in reinforcement learning with verifiable rewards (RLVR) have significantly improved the complex reasoning ability of vision-language models (VLMs), but outcome-level supervision is too coarse to diagnose and correct errors within the reasoning chain. Perceval is trained with perception-intensive supervised training data.

Compared to traditional GRPO, which applies sequence-level advantages, Perceval applies token-level advantages by targeting penalties on hallucinated spans identified by Perceval, thus enabling fine-grained supervision signals.

The paper (arXiv 2604.24583) was authored by Yingqian Min and colleagues from Renmin University of China, Bytedance, UC San Diego, and Hong Kong University of Science and Technology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b265d56-0c12-4b11-bc10-df212b6bb21d",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "bf165511-d656-48d0-aa30-6befa915cb92",
  "toolUseResult": {
    "query": "Perceval perception-centric process reward model token-level error grounding arXiv 2604.24583",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MVS8336pWuhbXNPhhQasQo",
        "content": [
          {
            "title": "[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models",
            "url": "https://arxiv.org/abs/2604.24583"
          },
          {
            "title": "Improving Vision-language Models with Perception-centric Process Reward Models",
            "url": "https://arxiv.org/html/2604.24583"
          },
          {
            "title": "Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought",
            "url": "https://arxiv.org/pdf/2603.22847"
          },
          {
            "title": "Spotlight on Token Perception for Multimodal Reinforcement Learning",
            "url": "https://arxiv.org/html/2510.09285v1"
          },
          {
            "title": "Spotlight on Token Perception for Multimodal Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2510.09285"
          },
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.16253"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\nPerceval is a process reward model (PRM) that enables token-level error grounding, which can extract image-related claims from the response and compare them one by one with the visual evidence in the image, ultimately returning claims that contain perceptual errors.\n\nRecent advancements in reinforcement learning with verifiable rewards (RLVR) have significantly improved the complex reasoning ability of vision-language models (VLMs), but outcome-level supervision is too coarse to diagnose and correct errors within the reasoning chain. Perceval is trained with perception-intensive supervised training data.\n\nCompared to traditional GRPO, which applies sequence-level advantages, Perceval applies token-level advantages by targeting penalties on hallucinated spans identified by Perceval, thus enabling fine-grained supervision signals.\n\nThe paper (arXiv 2604.24583) was authored by Yingqian Min and colleagues from Renmin University of China, Bytedance, UC San Diego, and Hong Kong University of Science and Technology."
    ],
    "durationSeconds": 6.746156155000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3b265d56-0c12-4b11-bc10-df212b6bb21d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T08:54:38.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015vN1tLWXzY7EDc5etJAM9h`</summary>

```json
{
  "query": "test-time self-correction VLM geometric constraint feedback re-perception iterative refinement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf165511-d656-48d0-aa30-6befa915cb92",
  "isSidechain": false,
  "requestId": "req_011CbSnvFuVXwhiJmBXFZRNL",
  "type": "assistant",
  "uuid": "670d1748-30b5-4b99-8f27-9eea11c19c24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjSTP3ze5BAiSPyLZMPZMN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 25111,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 25111,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 628
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-27T08:54:48.564Z_

<details><summary>↩ Tool result · `toolu_015vN1tLWXzY7EDc5etJAM9h`</summary>

```text
Web search results for query: "test-time self-correction VLM geometric constraint feedback re-perception iterative refinement 2025 2026"

Links: [{"title":"TANGRAMSR: CAN VISION-LANGUAGE MODELS REASON IN CONTINUOUS GEOMETRIC SPACE?","url":"https://arxiv.org/pdf/2602.05570"},{"title":"Toward More Reliable Artificial Intelligence: Reducing Hallucinations in Vision-Language Models","url":"https://arxiv.org/pdf/2512.07564"},{"title":"SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling","url":"https://arxiv.org/html/2501.19306v3"},{"title":"Self-Correction is More than Refinement: A Learning Framework for Visual and Language Reasoning Tasks","url":"https://arxiv.org/pdf/2410.04055"},{"title":"ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification","url":"https://arxiv.org/pdf/2502.14565"},{"title":"Self-Correction is More than Refinement: A Learning ...","url":"https://aclanthology.org/2025.findings-acl.331.pdf"},{"title":"SETS: Leveraging Self-Verification and Self-Correction for ...","url":"https://arxiv.org/pdf/2501.19306"},{"title":"Can Large Vision-Language Models Correct Semantic Grounding Errors By Themselves?","url":"https://arxiv.org/pdf/2404.06510"}]

I found several highly relevant research papers on test-time self-correction in Vision-Language Models with geometric constraints and iterative refinement. Here are the key findings:

## Test-Time Self-Correction Frameworks for VLMs

A framework establishes a test-time self-improvement pipeline for VLMs operating in continuous geometric space, with applications in scientific discovery and robotics. This approach applies reward-based feedback (IoU) to iteratively refine spatial predictions through verifier–refiner loops at test time.

## Iterative Refinement Approaches

One system iteratively refines VLM responses through three main stages: multi-dimensional uncertainty quantification identifies potentially hallucinated claims, attention-guided visual re-examination generates targeted crops of under-explored regions, and iterative refinement integrates verification results until convergence or maximum iterations are reached.

## Self-Verification and Self-Correction at Test-Time

Self-Enhanced Test-Time Scaling (SETS) combines parallel and sequential scaling with Sampling, Self-Verify and Self-Correct operations to scale test-time compute, yielding more effective test-time compute scaling compared to alternatives such as repeated sampling and SELF-REFINE.

## Challenges and Recent Findings

LLMs often struggle to self-correct their responses without external feedback. However, VLMs benefit from automatic iterative feedback by improving semantic grounding accuracy up to nearly 5 accuracy points.

The research indicates active development in this area, with multiple approaches emerging in 2025-2026 that leverage geometric constraints, feedback mechanisms, and iterative refinement to improve VLM performance at test time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "670d1748-30b5-4b99-8f27-9eea11c19c24",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "64f206f6-c44f-4d5b-9662-aa5c0ea333a6",
  "toolUseResult": {
    "query": "test-time self-correction VLM geometric constraint feedback re-perception iterative refinement 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RPJ4ojhSWWo8H3FzZgxDj9",
        "content": [
          {
            "title": "TANGRAMSR: CAN VISION-LANGUAGE MODELS REASON IN CONTINUOUS GEOMETRIC SPACE?",
            "url": "https://arxiv.org/pdf/2602.05570"
          },
          {
            "title": "Toward More Reliable Artificial Intelligence: Reducing Hallucinations in Vision-Language Models",
            "url": "https://arxiv.org/pdf/2512.07564"
          },
          {
            "title": "SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling",
            "url": "https://arxiv.org/html/2501.19306v3"
          },
          {
            "title": "Self-Correction is More than Refinement: A Learning Framework for Visual and Language Reasoning Tasks",
            "url": "https://arxiv.org/pdf/2410.04055"
          },
          {
            "title": "ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification",
            "url": "https://arxiv.org/pdf/2502.14565"
          },
          {
            "title": "Self-Correction is More than Refinement: A Learning ...",
            "url": "https://aclanthology.org/2025.findings-acl.331.pdf"
          },
          {
            "title": "SETS: Leveraging Self-Verification and Self-Correction for ...",
            "url": "https://arxiv.org/pdf/2501.19306"
          },
          {
            "title": "Can Large Vision-Language Models Correct Semantic Grounding Errors By Themselves?",
            "url": "https://arxiv.org/pdf/2404.06510"
          }
        ]
      },
      "I found several highly relevant research papers on test-time self-correction in Vision-Language Models with geometric constraints and iterative refinement. Here are the key findings:\n\n## Test-Time Self-Correction Frameworks for VLMs\n\nA framework establishes a test-time self-improvement pipeline for VLMs operating in continuous geometric space, with applications in scientific discovery and robotics. This approach applies reward-based feedback (IoU) to iteratively refine spatial predictions through verifier–refiner loops at test time.\n\n## Iterative Refinement Approaches\n\nOne system iteratively refines VLM responses through three main stages: multi-dimensional uncertainty quantification identifies potentially hallucinated claims, attention-guided visual re-examination generates targeted crops of under-explored regions, and iterative refinement integrates verification results until convergence or maximum iterations are reached.\n\n## Self-Verification and Self-Correction at Test-Time\n\nSelf-Enhanced Test-Time Scaling (SETS) combines parallel and sequential scaling with Sampling, Self-Verify and Self-Correct operations to scale test-time compute, yielding more effective test-time compute scaling compared to alternatives such as repeated sampling and SELF-REFINE.\n\n## Challenges and Recent Findings\n\nLLMs often struggle to self-correct their responses without external feedback. However, VLMs benefit from automatic iterative feedback by improving semantic grounding accuracy up to nearly 5 accuracy points.\n\nThe research indicates active development in this area, with multiple approaches emerging in 2025-2026 that leverage geometric constraints, feedback mechanisms, and iterative refinement to improve VLM performance at test time."
    ],
    "durationSeconds": 9.684274720000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "670d1748-30b5-4b99-8f27-9eea11c19c24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-27T08:54:48.572Z_

```json
{
  "parentUuid": "64f206f6-c44f-4d5b-9662-aa5c0ea333a6",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0b8960cb-7403-4b25-b078-4a835a8b1b27",
  "timestamp": "2026-05-27T08:54:48.572Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-27T08:54:51.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MkNpLha6bJXNrs7Yatwaoe`</summary>

```json
{
  "query": "diagnostic reward signal RL training specific error localization feedback structured reward beyond scalar 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b8960cb-7403-4b25-b078-4a835a8b1b27",
  "isSidechain": false,
  "requestId": "req_011CbSnwEHniaJJAg9zFEjSf",
  "type": "assistant",
  "uuid": "f3948181-5d76-4b0a-afb9-1073821b0e51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NaGzLcFG87qcUjdvAEx36u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 25739,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 25739,
          "cache_creation_input_tokens": 940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 940
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T08:54:59.829Z_

<details><summary>↩ Tool result · `toolu_01MkNpLha6bJXNrs7Yatwaoe`</summary>

```text
Web search results for query: "diagnostic reward signal RL training specific error localization feedback structured reward beyond scalar 2025 2026"

Links: [{"title":"Learning from Failures: Understanding LLM Alignment through Failure-Aware Inverse RL","url":"https://arxiv.org/pdf/2510.06092"},{"title":"Reinforcement Learning via Self-Distillation","url":"https://arxiv.org/pdf/2601.20802"},{"title":"MedLoc-R1: Performance-Aware Curriculum Reward Scheduling for GRPO-Based Medical Visual Grounding","url":"https://arxiv.org/pdf/2603.28120"},{"title":"How Top AI Labs Are Building RL Agents in 2026","url":"https://blog.dailydoseofds.com/p/how-top-ai-labs-are-building-rl-agents"},{"title":"Reinforcement Learning from Human Feedback (RLHF) Explained | IntuitionLabs","url":"https://intuitionlabs.ai/articles/reinforcement-learning-human-feedback"},{"title":"A Comparison of Reinforcement Learning (RL) and RLHF | IntuitionLabs","url":"https://intuitionlabs.ai/articles/reinforcement-learning-vs-rlhf"},{"title":"Learning Transferable Reward for Query Object Localization with Policy   Adaptation","url":"https://arxiv.org/pdf/2202.12403"},{"title":"Correctness is its own reward: bootstrapping error signals in self-guided reinforcement learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12393258/"}]

Based on the search results, I found several relevant papers and discussions about reward signals, RL training, and structured feedback approaches from 2025-2026:

## Key Findings

**Diagnostic and Rich Feedback Approaches:**

Research by Chen et al. (2025c) applies on-policy self-distillation in grid world settings where feedback is scalar reward, and a reflection stage in the self-teacher diagnoses possible mistakes, showing improved credit assignment compared to learning value networks for advantage estimation.

Reinforcement Learning with Rich Feedback (RLRF) utilizes tokenized feedback, providing a significantly richer signal than scalar reward, as the feedback can encapsulate both the reward as well as detailed observations like runtime errors.

**Error Localization and Structured Rewards:**

One approach integrates failures directly into inverse RL objectives through ambiguous or misclassified preference pairs to drive dual-path reward modeling and margin tightening, which hardens reward models while mitigating IRL non-identifiability.

Recent work shows that error signals produced by predictive models can train RL agents effectively, suggesting that local learning via predictive cancellation suffices for bootstrapping error signals capable of guiding self-directed learning.

**Curriculum-Based Reward Scheduling:**

In challenging localization tasks, domains with difficult characteristics can lead RL policies to experience "frustration," resulting in training failure to converge when models cannot obtain sufficient positive rewards from multiple attempts.

These recent works represent movements beyond simple scalar rewards toward structured, diagnostic feedback mechanisms that provide richer error localization information for RL training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3948181-5d76-4b0a-afb9-1073821b0e51",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "f4645db0-c001-4ffe-834f-a9614492df36",
  "toolUseResult": {
    "query": "diagnostic reward signal RL training specific error localization feedback structured reward beyond scalar 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016sLKn6GoETEoB2XiDdC4mA",
        "content": [
          {
            "title": "Learning from Failures: Understanding LLM Alignment through Failure-Aware Inverse RL",
            "url": "https://arxiv.org/pdf/2510.06092"
          },
          {
            "title": "Reinforcement Learning via Self-Distillation",
            "url": "https://arxiv.org/pdf/2601.20802"
          },
          {
            "title": "MedLoc-R1: Performance-Aware Curriculum Reward Scheduling for GRPO-Based Medical Visual Grounding",
            "url": "https://arxiv.org/pdf/2603.28120"
          },
          {
            "title": "How Top AI Labs Are Building RL Agents in 2026",
            "url": "https://blog.dailydoseofds.com/p/how-top-ai-labs-are-building-rl-agents"
          },
          {
            "title": "Reinforcement Learning from Human Feedback (RLHF) Explained | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/reinforcement-learning-human-feedback"
          },
          {
            "title": "A Comparison of Reinforcement Learning (RL) and RLHF | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/reinforcement-learning-vs-rlhf"
          },
          {
            "title": "Learning Transferable Reward for Query Object Localization with Policy   Adaptation",
            "url": "https://arxiv.org/pdf/2202.12403"
          },
          {
            "title": "Correctness is its own reward: bootstrapping error signals in self-guided reinforcement learning",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12393258/"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and discussions about reward signals, RL training, and structured feedback approaches from 2025-2026:\n\n## Key Findings\n\n**Diagnostic and Rich Feedback Approaches:**\n\nResearch by Chen et al. (2025c) applies on-policy self-distillation in grid world settings where feedback is scalar reward, and a reflection stage in the self-teacher diagnoses possible mistakes, showing improved credit assignment compared to learning value networks for advantage estimation.\n\nReinforcement Learning with Rich Feedback (RLRF) utilizes tokenized feedback, providing a significantly richer signal than scalar reward, as the feedback can encapsulate both the reward as well as detailed observations like runtime errors.\n\n**Error Localization and Structured Rewards:**\n\nOne approach integrates failures directly into inverse RL objectives through ambiguous or misclassified preference pairs to drive dual-path reward modeling and margin tightening, which hardens reward models while mitigating IRL non-identifiability.\n\nRecent work shows that error signals produced by predictive models can train RL agents effectively, suggesting that local learning via predictive cancellation suffices for bootstrapping error signals capable of guiding self-directed learning.\n\n**Curriculum-Based Reward Scheduling:**\n\nIn challenging localization tasks, domains with difficult characteristics can lead RL policies to experience \"frustration,\" resulting in training failure to converge when models cannot obtain sufficient positive rewards from multiple attempts.\n\nThese recent works represent movements beyond simple scalar rewards toward structured, diagnostic feedback mechanisms that provide richer error localization information for RL training."
    ],
    "durationSeconds": 8.382808102999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f3948181-5d76-4b0a-afb9-1073821b0e51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T08:55:02.598Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UyUJj49VkNvwv1FtU7k2We`</summary>

```json
{
  "query": "FGeo-Parser CDL accuracy VLM geometric diagram formal language translation feasibility limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4645db0-c001-4ffe-834f-a9614492df36",
  "isSidechain": false,
  "requestId": "req_011CbSnx4QzXmipkQQYzTLQx",
  "type": "assistant",
  "uuid": "fdb92c31-9dda-4d24-8dc3-5655d3280c25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQRgk2fdT1gAifCvy3XUwf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 26679,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 26679,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 852
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning  ## Core Problem  How can we provide formally verifiable, diagnostic reward signals for the visual per…",
  "leafUuid": "fdb92c31-9dda-4d24-8dc3-5655d3280c25",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal geometric perception rewards for vision-language reasoning",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

### Tool result

_source line 35 · 2026-05-27T08:55:09.993Z_

<details><summary>↩ Tool result · `toolu_01UyUJj49VkNvwv1FtU7k2We`</summary>

```text
Web search results for query: "FGeo-Parser CDL accuracy VLM geometric diagram formal language translation feasibility limitations"

Links: [{"title":"(PDF) FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems","url":"https://www.researchgate.net/publication/387376974_FGeo-Parser_Autoformalization_and_Solution_of_Plane_Geometric_Problems"},{"title":"FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems | MDPI","url":"https://www.mdpi.com/2073-8994/17/1/8"},{"title":"GitHub - RuRuo0/GeoParser","url":"https://github.com/RuRuo0/GeoParser"},{"title":"FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024Symm...17....8Z/abstract"},{"title":"(PDF) FGeo-TP: A Language Model-Enhanced Solver for Euclidean Geometry Problems","url":"https://www.researchgate.net/publication/379563827_FGeo-TP_A_Language_Model-Enhanced_Solver_for_Euclidean_Geometry_Problems"},{"title":"GeoFM: Enhancing Geometric Reasoning of MLLMs via Synthetic Data Generation through Formal Language","url":"https://arxiv.org/html/2510.27448"},{"title":"Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver⋆ Equal contribution. ✉Corresponding author. Our model and dataset are available at https://github.com/zezeze97/DFE-GPS.","url":"https://arxiv.org/html/2409.04214v2"},{"title":"FormalGeo: Formal representation and solving for Euclidean plane geometry problems","url":"https://formalgeo.github.io/"},{"title":"Concise Geometric Description as a Bridge: Unleashing the Potential of LLM for Plane Geometry Problem Solving","url":"https://arxiv.org/html/2601.21164"}]

Based on the search results, here's information about FGeo-Parser, CDL accuracy, VLM geometric diagram translation, and related limitations:

## FGeo-Parser Overview

FGeo-Parser is an automatic parser for geometric problems that converts geometric images and text into the formal language of FormalGeo, divided into a Diagram Parser based on the BLIP model and a Text Parser based on the T5 model.

## Accuracy Performance

The parser achieved a match accuracy of 91.51% and a perfect accuracy of 56.47% on the FormalGeo7K dataset. The neuro-symbolic solver obtained an overall problem-solving success rate of 63.45%.

## CDL (Concise Geometric Description Language) Translation

The diagram parser outputs construction CDL and image CDL, while the text parser outputs text CDL and goal CDL, which together form a geometric problem represented in formal language. Converting geometric diagram and text into formal language involves cross-modal comprehension and reasoning capabilities, challenging due to the complexity of geometric shapes and diversity of geometric relationships.

## Limitations and Feasibility Challenges

Although methods achieve relatively high problem-solving success rates on the FormalGeo7K dataset, the formalization process requires substantial human effort, highlighting the need for research into geometric problem autoformalization. Additionally, the incorporation of synthetic data leads to significant improvements in performance, while excluding synthetic data results in considerable decline, especially in terms of full-expression accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdb92c31-9dda-4d24-8dc3-5655d3280c25",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "457a1f8a-9c02-473a-8b57-b003c1632ebd",
  "toolUseResult": {
    "query": "FGeo-Parser CDL accuracy VLM geometric diagram formal language translation feasibility limitations",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GmK7u5eoDZRFg5tZHoh3Cx",
        "content": [
          {
            "title": "(PDF) FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems",
            "url": "https://www.researchgate.net/publication/387376974_FGeo-Parser_Autoformalization_and_Solution_of_Plane_Geometric_Problems"
          },
          {
            "title": "FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems | MDPI",
            "url": "https://www.mdpi.com/2073-8994/17/1/8"
          },
          {
            "title": "GitHub - RuRuo0/GeoParser",
            "url": "https://github.com/RuRuo0/GeoParser"
          },
          {
            "title": "FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024Symm...17....8Z/abstract"
          },
          {
            "title": "(PDF) FGeo-TP: A Language Model-Enhanced Solver for Euclidean Geometry Problems",
            "url": "https://www.researchgate.net/publication/379563827_FGeo-TP_A_Language_Model-Enhanced_Solver_for_Euclidean_Geometry_Problems"
          },
          {
            "title": "GeoFM: Enhancing Geometric Reasoning of MLLMs via Synthetic Data Generation through Formal Language",
            "url": "https://arxiv.org/html/2510.27448"
          },
          {
            "title": "Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver⋆ Equal contribution. ✉Corresponding author. Our model and dataset are available at https://github.com/zezeze97/DFE-GPS.",
            "url": "https://arxiv.org/html/2409.04214v2"
          },
          {
            "title": "FormalGeo: Formal representation and solving for Euclidean plane geometry problems",
            "url": "https://formalgeo.github.io/"
          },
          {
            "title": "Concise Geometric Description as a Bridge: Unleashing the Potential of LLM for Plane Geometry Problem Solving",
            "url": "https://arxiv.org/html/2601.21164"
          }
        ]
      },
      "Based on the search results, here's information about FGeo-Parser, CDL accuracy, VLM geometric diagram translation, and related limitations:\n\n## FGeo-Parser Overview\n\nFGeo-Parser is an automatic parser for geometric problems that converts geometric images and text into the formal language of FormalGeo, divided into a Diagram Parser based on the BLIP model and a Text Parser based on the T5 model.\n\n## Accuracy Performance\n\nThe parser achieved a match accuracy of 91.51% and a perfect accuracy of 56.47% on the FormalGeo7K dataset. The neuro-symbolic solver obtained an overall problem-solving success rate of 63.45%.\n\n## CDL (Concise Geometric Description Language) Translation\n\nThe diagram parser outputs construction CDL and image CDL, while the text parser outputs text CDL and goal CDL, which together form a geometric problem represented in formal language. Converting geometric diagram and text into formal language involves cross-modal comprehension and reasoning capabilities, challenging due to the complexity of geometric shapes and diversity of geometric relationships.\n\n## Limitations and Feasibility Challenges\n\nAlthough methods achieve relatively high problem-solving success rates on the FormalGeo7K dataset, the formalization process requires substantial human effort, highlighting the need for research into geometric problem autoformalization. Additionally, the incorporation of synthetic data leads to significant improvements in performance, while excluding synthetic data results in considerable decline, especially in terms of full-expression accuracy."
    ],
    "durationSeconds": 7.389889070999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fdb92c31-9dda-4d24-8dc3-5655d3280c25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-27T08:55:12.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012wWLoQpEN8toEezbB6bfma`</summary>

```json
{
  "query": "Perceval arXiv 2604.24583 perception PRM token-level hallucination grounding claim extraction method details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "457a1f8a-9c02-473a-8b57-b003c1632ebd",
  "isSidechain": false,
  "requestId": "req_011CbSnxosfDgcwc5oc6UFK3",
  "type": "assistant",
  "uuid": "3458b20d-86a7-44fb-8432-402f74a14da4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhntPQyqyq47gckbmrA1vp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 27531,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 27531,
          "cache_creation_input_tokens": 940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 940
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-27T08:55:20.581Z_

<details><summary>↩ Tool result · `toolu_012wWLoQpEN8toEezbB6bfma`</summary>

```text
Web search results for query: "Perceval arXiv 2604.24583 perception PRM token-level hallucination grounding claim extraction method details"

Links: [{"title":"[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models","url":"https://arxiv.org/abs/2604.24583"},{"title":"Improving Vision-language Models with Perception-centric Process Reward Models","url":"https://arxiv.org/html/2604.24583"},{"title":"Detecting Token-Level Hallucinations Using Variance Signals: A Reference-Free Approach","url":"https://arxiv.org/pdf/2507.04137"},{"title":"Beyond the Global Scores: Fine-Grained Token Grounding as a Robust Detector of LVLM Hallucinations","url":"https://arxiv.org/pdf/2604.04863"},{"title":"Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding","url":"https://arxiv.org/pdf/2601.21969"}]

Based on the search results, here are the key details about the Perceval paper (arXiv 2604.24583):

## Overview
Perceval is a process reward model (PRM) that enables token-level error grounding, which can extract image-related claims from the response and compare them one by one with the visual evidence in the image, ultimately returning claims that contain perceptual errors.

## Method Details

**Claim Extraction and Grounding:** The method extracts image-related claims from the response and compares them one by one with the visual evidence in the image to identify claims that contain perceptual errors.

**Training:** Perceval is trained with perception-intensive supervised training data.

**Integration with RL:** Perceval is integrated into the RL training process to train the policy models.

## Token-Level Hallucination Detection

Compared to traditional GRPO, which applies sequence-level advantages, the method applies token-level advantages by targeting penalties on hallucinated spans identified by Perceval, thus enabling fine-grained supervision signals.

The paper addresses a key limitation in vision-language models: outcome-level supervision is too coarse to diagnose and correct errors within the reasoning chain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3458b20d-86a7-44fb-8432-402f74a14da4",
  "isSidechain": false,
  "promptId": "0c476860-0fc1-435f-8fe6-b3a2d20cdda9",
  "type": "user",
  "uuid": "6dfdf8a5-4e17-4b23-8993-5265c5d94b7b",
  "toolUseResult": {
    "query": "Perceval arXiv 2604.24583 perception PRM token-level hallucination grounding claim extraction method details",
    "results": [
      {
        "tool_use_id": "srvtoolu_016tsnAMZdz6f8drCTUXBzFJ",
        "content": [
          {
            "title": "[2604.24583] Improving Vision-language Models with Perception-centric Process Reward Models",
            "url": "https://arxiv.org/abs/2604.24583"
          },
          {
            "title": "Improving Vision-language Models with Perception-centric Process Reward Models",
            "url": "https://arxiv.org/html/2604.24583"
          },
          {
            "title": "Detecting Token-Level Hallucinations Using Variance Signals: A Reference-Free Approach",
            "url": "https://arxiv.org/pdf/2507.04137"
          },
          {
            "title": "Beyond the Global Scores: Fine-Grained Token Grounding as a Robust Detector of LVLM Hallucinations",
            "url": "https://arxiv.org/pdf/2604.04863"
          },
          {
            "title": "Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding",
            "url": "https://arxiv.org/pdf/2601.21969"
          }
        ]
      },
      "Based on the search results, here are the key details about the Perceval paper (arXiv 2604.24583):\n\n## Overview\nPerceval is a process reward model (PRM) that enables token-level error grounding, which can extract image-related claims from the response and compare them one by one with the visual evidence in the image, ultimately returning claims that contain perceptual errors.\n\n## Method Details\n\n**Claim Extraction and Grounding:** The method extracts image-related claims from the response and compares them one by one with the visual evidence in the image to identify claims that contain perceptual errors.\n\n**Training:** Perceval is trained with perception-intensive supervised training data.\n\n**Integration with RL:** Perceval is integrated into the RL training process to train the policy models.\n\n## Token-Level Hallucination Detection\n\nCompared to traditional GRPO, which applies sequence-level advantages, the method applies token-level advantages by targeting penalties on hallucinated spans identified by Perceval, thus enabling fine-grained supervision signals.\n\nThe paper addresses a key limitation in vision-language models: outcome-level supervision is too coarse to diagnose and correct errors within the reasoning chain."
    ],
    "durationSeconds": 7.613543770000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3458b20d-86a7-44fb-8432-402f74a14da4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-27T08:56:39.175Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize what I've learned and assess this proposal. Let me think carefully about the key dimensions.

**Key findings from my research:**

1. **Perceval (arXiv:2604.24583)** - This is a very important paper that the proposal does NOT cite. Perceval provides a perception-centric PRM with token-level error grounding — it extracts image-related claims and compares them against visual evidence, returning specific perceptual errors. This is somewhat similar to FPR's "diagnostic" output, though Perceval uses a neural approach rather than formal verification. This is a critical missing related work.


2. **SymHPR (arXiv:2512.03126)** - Already cited, and the proposal correctly identifies it as the closest perception-stage structured reward approach.
3. **FGeo-Parser accuracy** - The 91.5% sentence-level match but only 56.5% perfect full-expression accuracy is a significant concern that the proposal acknowledges.
4. **"Perception Before Reasoning" (arXiv:2509.13031)** and **V-Triune (arXiv:2505.18129)** - Both relevant two-stage and unified RL approaches for visual reasoning that aren't cited.

Now I'm assessing the proposal's novelty and contributions...

The core claim about being the first to use formal geometric constraint propagation for diagnostic reward signals in perception-stage RL is well-articulated. The key advantages over existing work are clear: formal guarantees and diagnostic output versus SymHPR's rule-based approach, formal grounding versus neural judges in other methods, perception-stage focus versus reasoning-stage alternatives, and reward signals versus data generation like TrustGeoGen. But there's a critical gap—Perceval also provides per-claim error localization, so the distinction would need to emphasize that Perceval relies on neural extraction and comparison while this approach uses formal constraint propagation.

The significance hinges on whether formal verification can actually catch a meaningful portion of perception errors (though missing-primitive errors will slip through) and whether the CDL translation quality is sufficient for formal verification to work reliably—that 56.5% full-expression accuracy is a real concern. The proposal directly addresses whether training-time formal rewards outperform simpler test-time formal filtering with best-of-N sampling, which is the right question to tackle.

I need to flag a critical gap: Perceval provides claim-level error localization through neural methods, and the proposal must clearly differentiate itself in the comparison table—this omission could trigger reviewer rejection. There's also a sharpness issue with the "diagnostic" framing: the proposal claims a qualitative shift from scoring to diagnosing, but the actual question is whether the VLM leverages diagnostic information during training, since GRPO ultimately reduces the reward signal to a scalar value per trajectory.

Actually, the per-fact reward structure IS fundamentally different from scalar rewards—each fact gets its own score, so the model learns targeted correctness. The diagnostic output itself (the constraint explanation) isn't directly consumed during training, but the formal verification enables per-fact reward precision that's more informative than holistic scoring. The real contribution is that formal verification provides correctness guarantees and per-fact granularity during training, while the diagnostic output becomes most useful at test time for targeted re-perception.

Now I'm seeing a critical vulnerability: with only 56.5% perfect full-expression accuracy, most rollouts will produce syntactically invalid CDL that formal verification can't even evaluate. This creates a chicken-and-egg problem where you need good CDL to get formal rewards, but need formal rewards to learn good CDL in the first place. The SFT warm-start and reward curriculum help, but the effective coverage of formal rewards during training could still be quite limited—this is exactly what reviewers will scrutinize. The proposal does address this with FVUR-syntax and DYR metrics, which is solid, but the fundamental risk remains. There's also room to sharpen the novelty angle here.

The framing could be stronger around formal verification as a perception teacher—the idea that formal constraints encode domain knowledge neural systems can't easily discover independently. This positions the work as neuro-symbolic integration rather than just engineering a better reward function. And the "zero false positive" claim needs careful qualification: it only holds when CDL is syntactically valid *and* semantically correct, meaning it actually represents what the VLM perceived. If the CDL is syntactically valid but describes the wrong geometric configuration, the constraint system won't catch that error.

Actually, re-reading the proposal clarifies this—the formal verifier checks whether the VLM's stated facts are internally consistent with geometric constraints, not whether they match the actual image. So the zero false positive claim is accurate for internal consistency checking, which is what the proposal actually claims. That's well-stated.

I should focus on genuine high-value issues like the missing Perceval comparison in the related work section.

Beyond that, there are some stronger framings worth considering: the diagnostic capability here goes further than existing work because it doesn't just flag errors but explains *why* they violate specific geometric theorems. The core paradigm of using formal constraint propagation as a perception reward signal could also extend to other domains with formal specifications like circuit design or molecular structures, though I need to be careful not to suggest scope that's too speculative for the current work.

But there's a subtler issue I'm noticing with the proposal's framing. The training-time formal rewards and test-time re-perception are somewhat independent contributions, and a reviewer might question whether the formal verification at training time actually adds much value if SymHPR's rule-based approach already produces low-noise labels in practice. The real differentiator seems to be the targeted re-perception at test time, which doesn't necessarily require formal rewards during training—you could train with SymHPR and still apply formal verification at inference.

That said, the proposal's argument would be that training with formal rewards helps internalize geometric constraint awareness, improving the base perception quality itself. The ablation studies should clarify this: comparing formal versus rule-based F1 at training time, and separately evaluating test-time re-perception, will show whether the training-time formal rewards provide genuine value beyond what rule-based training achieves.

Now I'm ready to formulate my assessment.

**State:** 有发掘空间

Key excavation points:

1. **Critical missing related work:** The comparison table against Perceval and similar systems is incomplete, which could invite reviewer criticism.

2. **Significance framing:** The narrative around "formal domain knowledge as a perception teacher" could be articulated more compellingly.

3. **The diagnostic explanation is undersold:** The theorem-level "why it's wrong" explanation is genuinely novel and more valuable than just identifying per-claim errors.

4. **Novelty distinction:** The proposal conflates "per-fact granularity" and "diagnostic explanation" — these should be separated as two distinct contributions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dfdf8a5-4e17-4b23-8993-5265c5d94b7b",
  "isSidechain": false,
  "requestId": "req_011CbSnyc7G2sgQqMggPBLRm",
  "type": "assistant",
  "uuid": "ab6de63d-8fa6-4e51-9be9-859d78e8ba8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GtArn5j3Aq9cu744dTecu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 28471,
      "output_tokens": 6420,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6420,
          "cache_read_input_tokens": 28471,
          "cache_creation_input_tokens": 637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 637
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-27T08:58:06.196Z_

Now I have sufficient research to make an informed assessment. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- **Perceval (arXiv:2604.24583, April 2026)**: Perception-centric PRM，提供 token-level error grounding——从 VLM 响应中提取 image-related claims，逐一与图像视觉证据比对，返回含感知错误的 claims，并集成到 GRPO 训练中施加 token-level advantages。**本 proposal 未引用此工作，但它是当前最接近"per-claim 感知诊断"的方法，是对 FPR novelty claim 最直接的威胁。**
- **SymHPR (arXiv:2512.03126, Dec 2025)**: Hierarchical per-primitive rewards (point-on-line, line-on-shape F1/L2)，symbolic auto-encoder 将 diagram 编码为结构化 primitives。在 chart reconstruction 上超 GPT-4o 0.6%。Proposal 已正确定位为最近的 perception-stage structured reward 工作。
- **EVPV (arXiv:2603.16253, Mar 2026)**: 提出 explicit visual premise verification——policy 提供 visual checklist，从图像提取 structured visual facts 构成 constraint set。验证 perception→symbolic→constraint pipeline 在 PRM 中的有效性。
- **FGeo-Parser (Symmetry 2025)**: 91.5% sentence-level match，56.5% perfect full-expression accuracy。CDL translation 是系统 bottleneck 的经验上界。
- **"Perception Before Reasoning" (arXiv:2509.13031)**: 两阶段 RL 分离 perception 和 reasoning 训练。未被引用但验证了 perception-stage 独立训练的价值。
- **GeoFM (arXiv:2510.27448)**: 通过 formal language 合成数据增强 MLLM geometric reasoning，验证了 formal language 在几何领域的生成侧价值。
- 调研总结：当前领域正沿两个方向快速推进——(1) perception-specific reward/PRM 从 scalar 向 per-claim/per-fact 细粒度发展（Perceval, SymHPR, EVPV），(2) formal verification 从 reasoning stage 向 data generation 扩展（TrustGeoGen, FoVer）。**将 formal verification 应用于 perception-stage reward 确实是两个趋势的交汇点，尚无人占位**，但 Perceval 的 per-claim 诊断能力已部分侵入 FPR 的 novelty 空间。

---

【发掘点 1】
- 维度: related work 差异化 / 前提假设质疑
- 内容: **Perceval (arXiv:2604.24583) 是本 proposal 未引用的最危险竞争者，必须在 comparison table 中明确定位并差异化。** Perceval 已实现 per-claim 感知错误定位 + token-level reward 集成到 GRPO——这直接挑战 FPR 的 "first to provide per-fact diagnostic" claim。当前 comparison table 缺少它，reviewer 如果注意到这篇 4 月底的论文（距 AAAI 2026 deadline 很近），会认为 novelty survey 不充分。**关键差异化应聚焦于：Perceval 是 neural claim-comparison（能说"这个 claim 错了"但无法解释为什么错，依赖神经网络比对，有 false positive），FPR 是 formal constraint propagation（能说"∠ABC=90° 因违反 inscribed angle theorem 而与 A on circle with diameter BC 矛盾"，且在 valid CDL 上 zero FP）。** 这是 "error identification" vs. "error explanation with formal proof" 的质的区别，也是 FPR 能支持 targeted re-perception 而 Perceval 不能高效支持的原因——re-perception 需要知道 which constraint is violated，不只是 which claim is wrong。
- 价值: 直接堵住 reviewer 最可能的 novelty 攻击向量。如果 Perceval 未被对比，reviewer 完全有理由给 borderline reject。补上之后，FPR 的 formal guarantee + explanatory diagnostic 优势反而更凸显。(命中 Novelty + Related Work)
- 调研依据: Perceval (arXiv:2604.24583) 的 token-level error grounding 机制

【发掘点 2】
- 维度: 核心 claim 强化 / novelty 锐化
- 内容: **Proposal 当前将 "per-fact granularity" 和 "diagnostic explanation" 混为一谈，但这实际上是两个独立的 novelty 层次，应当显式拆分并分别论证其不可替代性。** 第一层：per-fact reward granularity（每个 geometric fact 单独获得 reward）——这本身不够 novel，因为 SymHPR 已有 per-primitive reward，Perceval 已有 per-claim reward。第二层：**formal explanation（哪条 geometric fact 违反了哪条定理，为什么矛盾）**——这才是真正不可替代的贡献。建议在 contribution chain 中将第二层的独特价值更显式地与 test-time re-perception 绑定：之所以 targeted re-perception 可行，不是因为我们知道"哪个 fact 错了"（Perceval 也能做到），而是因为我们知道"错在哪条几何约束上"——这让 re-perception prompt 能包含 theorem-level guidance（"re-examine ∠ABC because it contradicts the inscribed angle theorem"），这种 guidance 的信息量远超 "∠ABC is wrong, re-examine it"。
- 价值: 将 novelty 的锐度从"per-fact formal reward"（与 Perceval/SymHPR 有重叠）提升到"theorem-grounded diagnostic explanation"（无任何已有工作覆盖），使 novelty claim 刀锋更窄但更锋利。(命中 Novelty)
- 调研依据: 与 Perceval 和 SymHPR 的对比分析

【发掘点 3】
- 维度: significance 提升
- 内容: **当前 proposal 的 significance framing 主要在"解决 perception bottleneck"——这是一个共享的、已被多篇工作定位的问题（GeoDPO, Perception-R1, "Bad Seeing or Bad Thinking?", PDCR 都在解决同一个问题）。建议增加一个更深层的 significance 叙事：FPR 代表了一种 "formal domain knowledge as perception teacher" 的范式**——用形式化的数学领域知识（几何定理库）作为 perception 的 teacher signal，而非用另一个神经网络（neural judge）或规则（rule-based F1）。这连接了 neuro-symbolic integration 的更大叙事：传统 neuro-symbolic 工作主要将 formal knowledge 用于 reasoning verification（SGVR, FoVer, InternGeometry），FPR 首次将其引入 perception training，展示了 formal knowledge 可以 "teach perception" 而不仅仅 "verify reasoning"。这个 framing 使 FPR 的贡献从"一个更好的 perception reward function"提升为"一种新的 neuro-symbolic 交互范式在 perception 层的实例化"。
- 价值: 将 paper 的定位从 application-level contribution（更好的 reward for geometry perception）提升到 paradigm-level insight（formal knowledge teaching perception），增加 significance 维度的吸引力。(命中 Significance)
- 调研依据: 基于领域整体趋势判断——当前 formal verification 仅应用于 reasoning stage (SGVR, FoVer, InternGeometry) 和 data generation (TrustGeoGen)，perception stage 是空白；neuro-symbolic 文献中 "symbolic knowledge as teacher" 的叙事框架

【发掘点 4】
- 维度: trivial alternative 威胁
- 内容: **训练时 formal reward 和测试时 targeted re-perception 是两个相对独立的模块，reviewer 可能会提出一个 trivial decomposition attack："用 SymHPR（更简单、不需要 CDL translation）做训练，测试时单独加 formal verification 做 re-perception——这样绕过了 CDL translation 的 chicken-and-egg problem，且两个模块各取最优。"** Proposal 当前的反驳（"training-time formal rewards internalize geometric constraint awareness"）是合理的但需要更强的论证。建议在 core claim 中增加一个显式的论点：**training with formal rewards 不仅提高 perception 质量，还训练模型生成 formally verifiable CDL 的能力——这是 test-time re-perception 的前提条件。** 如果训练阶段不使用 formal reward（不要求模型输出 valid CDL），测试时模型产出的 CDL 质量会差，formal verification 根本无法有效 fire。换言之，training-time 和 test-time 两个模块之间存在通过 CDL quality 传递的正向耦合，不可简单拆分。这个论点在当前 proposal 中缺失。
- 价值: 预防 reviewer 的 decomposition attack，同时暴露了一个 idea 层面的逻辑链缺口（training 和 test-time 的耦合论证）。(命中 Novelty + Significance)
- 调研依据: 基于 FGeo-Parser 56.5% full-expression accuracy 数据——如果不在训练中强化 CDL generation，test-time CDL quality 可能远低于 formal verification 的可用门槛

【发掘点 5】
- 维度: 前提假设质疑
- 内容: **"Zero false positive on valid CDL" 的 claim 逻辑上成立，但实际中 "valid CDL" 的定义需要更精确。** 当前 proposal 的逻辑是：syntactically valid CDL → formal constraint propagation → 检测到的矛盾一定是真矛盾（zero FP）。但存在一个微妙情况：CDL 可以 syntactically valid 但 semantically incomplete（模型正确描述了它看到的部分事实，但遗漏了关键的条件，如遗漏了"BD 是直径"）。在不完整的 CDL 上，formal verification 可能产生 **false negatives（漏检真正的矛盾）而非 false positives**，但更重要的是：如果 CDL 遗漏了某些 construction conditions，formal verification 可能将一个实际上 valid 的 fact 标记为 contradiction（因为在不完整的约束系统下，某些 fact 缺少支撑条件而显得矛盾）——这就是 **false positive**。建议在论文中更精确地界定 "zero FP" 的前提条件：不仅需要 syntactically valid CDL，还需要 construction-complete CDL（所有 geometric construction conditions 都被正确捕获）。并在 M1 pilot study 中测量 construction-completeness rate 作为 FPR 有效性的一个先决指标。
- 价值: 预防 reviewer 对 "zero false positive" 的质疑——这是 core claim 的根基，如果被攻破整个 formal guarantee 叙事会崩塌。主动精确化条件比被动回应 reviewer 强得多。(命中 Novelty)
- 调研依据: FGeo-Parser 的 sentence-level vs. full-expression accuracy gap (91.5% vs. 56.5%) 表明 semantic incompleteness 是常态而非边缘情况

---

**总结性判断：** 这个 proposal 整体质量相当高——研究问题定位精准（formal verification × perception reward 的交汇点确实无人占位），方法论逻辑链清晰，对已有工作的覆盖广泛。上述 5 个发掘点中，**发掘点 1（Perceval 缺失）是最紧迫的**，直接关系到 novelty claim 的存亡；**发掘点 2（novelty 层次拆分）和发掘点 4（training-test 耦合论证）** 能显著提升 idea 的说服力；发掘点 3 和 5 是锦上添花但也有实质价值。

Sources:
- [Perceval: Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583)
- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)
- [EVPV: Grounding the Score](https://arxiv.org/html/2603.16253)
- [FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems](https://www.mdpi.com/2073-8994/17/1/8)
- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/pdf/2602.22703)
- [SGVR: Milestones over Outcome](https://arxiv.org/pdf/2601.05073)
- [GeoFM: Enhancing Geometric Reasoning via Synthetic Data through Formal Language](https://arxiv.org/html/2510.27448)
- [Perception Before Reasoning: Two-Stage RL for Visual Reasoning](https://arxiv.org/html/2509.13031v1)
- [FormalGeo Framework](https://formalgeo.github.io/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab6de63d-8fa6-4e51-9be9-859d78e8ba8a",
  "isSidechain": false,
  "requestId": "req_011CbSnyc7G2sgQqMggPBLRm",
  "type": "assistant",
  "uuid": "dd85f542-5c89-4f44-8556-ba21737fbca6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GtArn5j3Aq9cu744dTecu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 28471,
      "output_tokens": 6420,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 637,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6420,
          "cache_read_input_tokens": 28471,
          "cache_creation_input_tokens": 637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 637
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning  ## Core Problem  How can we provide formally verifiable, diagnostic reward signals for the visual per…",
  "leafUuid": "dd85f542-5c89-4f44-8556-ba21737fbca6",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal geometric perception rewards for vision-language reasoning",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning  ## Core Problem  How can we provide formally verifiable, diagnostic reward signals for the visual per…",
  "leafUuid": "dd85f542-5c89-4f44-8556-ba21737fbca6",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal geometric perception rewards for vision-language reasoning",
  "sessionId": "273c115b-c627-458d-8f13-0cbe4eaa144a"
}
```

---
