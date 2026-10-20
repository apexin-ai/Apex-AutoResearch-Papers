# Research conversation: Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition ## Core Problem How can we achieve near

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/c4d4da7f-989d-4eaa-b5b4-c481b8d60bad.jsonl`
- **Structured JSON:** [`836dd8cc8443c9cd3945.json`](../../sessions/83/836dd8cc8443c9cd3945.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T12:58:32.936Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T12:58:32.936Z",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "content": "# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition\n\n## Core Problem\n\nHow can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain and structurally critical proof blocks to formal verification?\n\n## Thesis and Contributions\n\nWe advance two claims, each supported by a corresponding contribution:\n\n**Claim 1 (Architectural Insight):** Modular proof decomposition — as instantiated by Pseudo-Formalization (Barkallah et al., 2026) — serves as a natural bridge between informal and formal verification of mathematical proofs. Each PF block's explicit typed premises map directly to Lean 4 hypothesis lists, its single explicit conclusion maps to a Lean 4 goal statement, and its self-contained nature eliminates the context-completion problem that fundamentally limits whole-proof autoformalization to ~35% end-to-end success (miniF2F-Lean Revisited, NeurIPS 2025). We empirically validate this by demonstrating that PF-block-level autoformalization achieves substantially higher success rates than raw-NL-fragment autoformalization in a controlled paired comparison.\n\n**Claim 2 (System Design):** Building on this bridge, we design a two-tier selective verification pipeline that combines calibrated uncertainty scoring with dependency-graph criticality to route only the 10-20% most uncertain or structurally critical blocks to Lean 4 formal verification. This achieves near-formal reliability at ~1.5-2x cost overhead versus Safe's 4-8x for universal formalization, and represents a viable path toward scaling formal verification to research-level proofs — where whole-proof autoformalization is fundamentally intractable.\n\n## Research Opportunity\n\nWhole-proof autoformalization faces a fundamental scalability barrier: context-completion difficulties and compounding error across steps limit end-to-end success to ~35% even with SOTA tools (66% autoformalization accuracy × ~70% theorem proving success; miniF2F-Lean Revisited, NeurIPS 2025). This barrier does not diminish with stronger models — it is architectural, arising from the unbounded context dependencies in monolithic proofs. Consequently, universal formal verification (Safe, Liu et al., ACL 2025) imposes 4-8x cost overhead per step while still being limited by autoformalization failures. Meanwhile, LLM-only verification (PF+Block Verification; Barkallah et al., May 2026) is cheap but leaves ~50% of research-level errors undetected on ArxivMathGradingBench. PF's modular block structure offers a way through this impasse: self-contained blocks with explicit premises and conclusions are structurally aligned with formal theorem statements, making block-level autoformalization fundamentally more tractable than whole-proof autoformalization. Step-level formalization has independently been shown more tractable than whole-proof approaches (Process-Driven Autoformalization in Lean 4, 2024). By adding calibrated uncertainty and dependency-graph criticality as a dual triage signal, we can route only the most critical blocks to formal verification, catching errors that LLM verification misses while operating within the tractability boundary of block-level autoformalization.\n\n## Research Landscape\n\n**LLM-based verification (cheap, unreliable):** Best PRM drops from 78.3% to 37.3% on Hard2Verify (Pandit et al., 2025). PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026). ThinkPRM (2025) advances data-efficient verbalized PRMs outperforming discriminative PRMs with 1% of process labels, representing the current strongest step-level LLM verifier. Specialized prompt ensembles can close much of the gap between small and frontier models for proof verification (Do We Need Frontier Models to Verify Mathematical Proofs?, arXiv 2604.02450, 2026), raising the LLM-only performance ceiling.\n\n**Universal formal verification (reliable, expensive):** Safe verifies each step in Lean 4 with ~80% success at 4-8x cost (Liu et al., ACL 2025). End-to-end autoformalization achieves only ~35% success (miniF2F-Lean Revisited, NeurIPS 2025). StepFun-Formalizer-32B achieves BEq@1 of 40.5% on FormalMATH-Lite for statement-level autoformalization.\n\n**Selective/adaptive verification (emerging):** Ganguly et al. (NeurIPS 2025) achieve 14-100% error reduction via selective SMT-based formalization using PCFG-based uncertainty. Our work differs on three levels: (1) uncertainty source — Ganguly models generation-side distribution (LLM→SMT-LIB), we model verification-side judgment uncertainty (BV ensemble disagreement on existing proofs); (2) routing target heterogeneity — Ganguly routes within a single verification paradigm (verify vs. abstain on SMT), we route across fundamentally different paradigms (LLM verification → formal verification); (3) structural criticality — Ganguly uses no structural signal, we introduce dependency-graph criticality as an orthogonal routing dimension. Qu (arXiv 2026) achieves 44% fewer verifier calls via adaptive allocation on MATH but operates within LLM-tier verification only.\n\n**Proof generation vs. verification taxonomy:** HERMES (Ospanov et al., ICML 2026) interleaves informal reasoning with Lean 4 verification during proof generation, achieving 67% accuracy improvement with 80% fewer FLOPs — but addresses proof generation (where output format is controllable) with uniform formalization, not proof verification of arbitrary NL input. Our work addresses the fundamentally different verification setting where PF decomposition is necessary to create structured formalization targets from arbitrary input. VERGE (Singh et al., arXiv 2026) routes between SMT solvers and LLM-ensemble verification for first-order logic claims, not mathematical proof blocks. UCCI (arXiv 2026) provides calibrated uncertainty for LLM cascade routing (small→large model), not across formal/informal verification tiers. ProofSketcher (arXiv 2026) produces typed proof sketches without uncertainty-guided routing. ProofFlow (2025) uses dependency graphs for autoformalization fidelity but not for verification routing decisions.\n\n## Proposed Approach\n\n**Phase 0 — Pilot study (go/no-go).** Before full pipeline development, we validate the core architectural assumption: randomly sample 50-100 PF blocks across mathematical domains and difficulty levels, test StepFun-Formalizer-32B autoformalization success rate and Goedel-Prover-V2-32B proof search success rate, establish block-level end-to-end success rate baseline. Threshold: if end-to-end success rate < 30%, Tier 2 requires redesign (e.g., multi-shot formalization with compiler-feedback self-correction). Report decomposed success rates: formalization type-check rate → proof search success rate → end-to-end rate.\n\n**Tier 1 — LLM Block Verification with calibrated uncertainty.** Decompose proof into PF blocks (Barkallah et al., 2026) with explicit premises, conclusions, and dependency graphs. Run Block Verification using QwQ-32B with dual uncertainty scoring: (i) ensemble disagreement via N=5 stochastic forward passes with temperature sampling, (ii) token-level CoT entropy. Calibrate via Platt scaling on synthetic evaluation set and miniF2F verification data (NOT on ArxivMathGradingBench, which is reserved for evaluation only), with temperature scaling as calibration method ablation.\n\n**Dual-signal routing.** Route blocks based on: uncertainty score × dependency criticality (primary: fan-out degree in inter-block dependency DAG; supplementary sensitivity analysis: dominator nodes, betweenness centrality). This dual signal mitigates the \"confident-but-wrong\" risk inherent in LLM overconfidence: (a) ensemble disagreement captures inter-model uncertainty more reliably than single-model confidence; (b) dependency criticality provides an uncertainty-independent signal — high-fan-out blocks receive formal verification even if BV is confident; (c) structural difficulty heuristics (block-internal step count, cited theorem count) serve as additional features.\n\n**Why calibrated uncertainty, not just structural heuristics?** Simple heuristics (block length, step count) capture surface complexity but miss blocks that are structurally simple yet reasoning-subtle — e.g., a one-step block applying a theorem in a non-obvious way. Ensemble disagreement flags exactly these cases: when model copies disagree on a seemingly-simple block, this signals hidden reasoning difficulty invisible to structural features. We validate this claim via head-to-head ablation against heuristic-only routing.\n\n**Tier 2 — Selective formal verification.** Routed blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging PF block structure (premises→Lean 4 hypotheses, conclusion→Lean 4 goal, no context completion needed) — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction (up to k=3 retry rounds using Lean compiler feedback). Per-block timeout: 5 min; per-proof timeout: 30 min. Fallback strategy for autoformalization failure or proof search timeout is an ablation variable.\n\n## Evaluation Plan\n\n**Benchmarks:**\n- ArxivMathGradingBench (Barkallah et al., 2026): 35 papers, 40 known errors. Held-out evaluation only (not used for calibration). Error detection precision/recall/F1, bootstrap CI (1000 resamples), McNemar's test, effect size (Cohen's h). Supplementary: per-paper accuracy.\n- Synthetic Error Detection Set: 400-500 instances from Hard2Verify competition-level problems. Multi-source error construction: (i) LLM-generated incorrect proofs, (ii) controlled perturbation of correct proofs (deleted steps, swapped theorems, computation errors), (iii) extracted known-error steps from Hard2Verify annotations. Ground-truth verification via answer matching + Lean 4 proof for correct proofs. Human validation on 50-80 instance subsample (Cohen's κ). Used for calibration and as co-primary evaluation benchmark.\n- miniF2F Verification Protocol: Generate ≥8 candidate proofs per problem (≥100 problems) using QwQ-32B, evaluate verification precision/recall. Aligned with Safe's miniF2F setting.\n\n**Baselines (7 methods):**\n- PF + BV single-pass (Barkallah et al., 2026)\n- PF + BV ensemble (N=5, no routing to formal verification)\n- PF + BV with specialized prompt ensemble (per arXiv 2604.02450, 2026): best-effort LLM verification upper bound\n- ThinkPRM (2025): SOTA data-efficient verbalized PRM\n- Qwen2.5-Math-PRM-7B: strongest open-source discriminative PRM at comparable scale\n- Safe universal formalization (Liu et al., ACL 2025)\n- HERMES (Ospanov et al., ICML 2026): if applicable to verification setting\n\n**Cost framework:** Unified metric: GPU-seconds per proof. Detailed breakdown: PF decomposition + ensemble BV (5× single BV) + routing overhead + autoformalization (per routed block) + proof search including retries and timeouts + fallback cost for Tier 2 failures. Pareto curve (cost vs. error detection recall) plotting all methods.\n\n**Ablations (8 experiments):**\n1. Uncertainty signal decomposition: ensemble disagreement only / CoT entropy only / combined — AUROC, ECE, recall@fixed-cost\n2. Routing signal: uncertainty only / dependency criticality only / simple structural heuristic only / dual signal — recall and cost\n3. Ensemble size: N=3 / N=5 / N=7\n4. Autoformalization failure fallback: accept / reject / majority-vote re-verification\n5. Threshold sweep: routing percentage 5%-50% — Pareto curve\n6. **PF blocks vs. raw NL autoformalization (Contribution 1 validation):** Paired comparison on same proofs. PF block input vs. raw NL fragment input to StepFun-Formalizer-32B. Metrics: Lean 4 type-check rate, proof search success rate. Paired Wilcoxon signed-rank test. This is a core result, not merely an ablation.\n7. Confident-but-wrong analysis: proportion of BV errors at >0.8 confidence, fraction captured by dual-signal vs. uncertainty-only routing\n8. Tier 2 sensitivity analysis: system Pareto curves under assumed Tier 2 success rates of 30%/50%/70%/90%, demonstrating robustness\n\n**Calibration method ablation:** Platt scaling vs. temperature scaling, cross-validated on calibration set, evaluated by ECE and routing decision quality.\n\n## Key References\n\n- Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., arXiv 2026)\n- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (Liu et al., ACL 2025)\n- Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (Pandit et al., arXiv 2025)\n- miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)\n- Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (Ganguly et al., NeurIPS 2025)\n- Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (Qu, arXiv 2026)\n- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (Singh et al., arXiv 2026)\n- HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (Ospanov et al., ICML 2026)\n- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)\n- Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)\n- ThinkPRM: Process Reward Models That Think (2025)\n- Qwen2.5-Math-PRM (2025)\n- ProofSketcher (arXiv 2026)\n- UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing (arXiv 2026)\n- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (2025)\n- Do We Need Frontier Models to Verify Mathematical Proofs? (arXiv 2604.02450, 2026)\n- Process-Driven Autoformalization in Lean 4 (2024)\n\n## Resource Estimate\n\n- **Phase 0 pilot:** ~30-50 GPU-hours (A100-80GB), 1-2 weeks. Go/no-go decision point.\n- **Full pipeline (Phase 1-3):** GPU hours: 400-550 (ensemble BV ~80h; StepFun-Formalizer ~80h; Goedel-Prover-V2 proof search ~130h including retries/timeouts; synthetic set construction ~40h; baselines + ablations ~120-170h). CPU hours: ~60h (Lean 4 kernel type-checking). Timeline: 14-18 weeks (2-3 researchers), including 2-3 week contingency for PF pipeline reproduction if code unavailable.\n- **Estimated GPU cost:** $1200-1650\n- **Lean 4 proof search:** Per-block timeout 5 min, per-proof timeout 30 min. ArxivMathGradingBench single pass: ~9h wall-clock (35 papers × ~30 blocks × 15% routing × 3.5 min/block). Independent blocks parallelizable.\n- **Critical path:** Phase 0 pilot (weeks 1-2) → PF pipeline setup + synthetic set (weeks 2-5) → uncertainty calibration (weeks 5-8) → full pipeline + ablations (weeks 8-15) → analysis + writing (weeks 15-18)."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T12:58:32.941Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T12:58:32.941Z",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-27T12:58:32.970Z_

# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition

## Core Problem

How can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain and structurally critical proof blocks to formal verification?

## Thesis and Contributions

We advance two claims, each supported by a corresponding contribution:

**Claim 1 (Architectural Insight):** Modular proof decomposition — as instantiated by Pseudo-Formalization (Barkallah et al., 2026) — serves as a natural bridge between informal and formal verification of mathematical proofs. Each PF block's explicit typed premises map directly to Lean 4 hypothesis lists, its single explicit conclusion maps to a Lean 4 goal statement, and its self-contained nature eliminates the context-completion problem that fundamentally limits whole-proof autoformalization to ~35% end-to-end success (miniF2F-Lean Revisited, NeurIPS 2025). We empirically validate this by demonstrating that PF-block-level autoformalization achieves substantially higher success rates than raw-NL-fragment autoformalization in a controlled paired comparison.

**Claim 2 (System Design):** Building on this bridge, we design a two-tier selective verification pipeline that combines calibrated uncertainty scoring with dependency-graph criticality to route only the 10-20% most uncertain or structurally critical blocks to Lean 4 formal verification. This achieves near-formal reliability at ~1.5-2x cost overhead versus Safe's 4-8x for universal formalization, and represents a viable path toward scaling formal verification to research-level proofs — where whole-proof autoformalization is fundamentally intractable.

## Research Opportunity

Whole-proof autoformalization faces a fundamental scalability barrier: context-completion difficulties and compounding error across steps limit end-to-end success to ~35% even with SOTA tools (66% autoformalization accuracy × ~70% theorem proving success; miniF2F-Lean Revisited, NeurIPS 2025). This barrier does not diminish with stronger models — it is architectural, arising from the unbounded context dependencies in monolithic proofs. Consequently, universal formal verification (Safe, Liu et al., ACL 2025) imposes 4-8x cost overhead per step while still being limited by autoformalization failures. Meanwhile, LLM-only verification (PF+Block Verification; Barkallah et al., May 2026) is cheap but leaves ~50% of research-level errors undetected on ArxivMathGradingBench. PF's modular block structure offers a way through this impasse: self-contained blocks with explicit premises and conclusions are structurally aligned with formal theorem statements, making block-level autoformalization fundamentally more tractable than whole-proof autoformalization. Step-level formalization has independently been shown more tractable than whole-proof approaches (Process-Driven Autoformalization in Lean 4, 2024). By adding calibrated uncertainty and dependency-graph criticality as a dual triage signal, we can route only the most critical blocks to formal verification, catching errors that LLM verification misses while operating within the tractability boundary of block-level autoformalization.

## Research Landscape

**LLM-based verification (cheap, unreliable):** Best PRM drops from 78.3% to 37.3% on Hard2Verify (Pandit et al., 2025). PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026). ThinkPRM (2025) advances data-efficient verbalized PRMs outperforming discriminative PRMs with 1% of process labels, representing the current strongest step-level LLM verifier. Specialized prompt ensembles can close much of the gap between small and frontier models for proof verification (Do We Need Frontier Models to Verify Mathematical Proofs?, arXiv 2604.02450, 2026), raising the LLM-only performance ceiling.

**Universal formal verification (reliable, expensive):** Safe verifies each step in Lean 4 with ~80% success at 4-8x cost (Liu et al., ACL 2025). End-to-end autoformalization achieves only ~35% success (miniF2F-Lean Revisited, NeurIPS 2025). StepFun-Formalizer-32B achieves BEq@1 of 40.5% on FormalMATH-Lite for statement-level autoformalization.

**Selective/adaptive verification (emerging):** Ganguly et al. (NeurIPS 2025) achieve 14-100% error reduction via selective SMT-based formalization using PCFG-based uncertainty. Our work differs on three levels: (1) uncertainty source — Ganguly models generation-side distribution (LLM→SMT-LIB), we model verification-side judgment uncertainty (BV ensemble disagreement on existing proofs); (2) routing target heterogeneity — Ganguly routes within a single verification paradigm (verify vs. abstain on SMT), we route across fundamentally different paradigms (LLM verification → formal verification); (3) structural criticality — Ganguly uses no structural signal, we introduce dependency-graph criticality as an orthogonal routing dimension. Qu (arXiv 2026) achieves 44% fewer verifier calls via adaptive allocation on MATH but operates within LLM-tier verification only.

**Proof generation vs. verification taxonomy:** HERMES (Ospanov et al., ICML 2026) interleaves informal reasoning with Lean 4 verification during proof generation, achieving 67% accuracy improvement with 80% fewer FLOPs — but addresses proof generation (where output format is controllable) with uniform formalization, not proof verification of arbitrary NL input. Our work addresses the fundamentally different verification setting where PF decomposition is necessary to create structured formalization targets from arbitrary input. VERGE (Singh et al., arXiv 2026) routes between SMT solvers and LLM-ensemble verification for first-order logic claims, not mathematical proof blocks. UCCI (arXiv 2026) provides calibrated uncertainty for LLM cascade routing (small→large model), not across formal/informal verification tiers. ProofSketcher (arXiv 2026) produces typed proof sketches without uncertainty-guided routing. ProofFlow (2025) uses dependency graphs for autoformalization fidelity but not for verification routing decisions.

## Proposed Approach

**Phase 0 — Pilot study (go/no-go).** Before full pipeline development, we validate the core architectural assumption: randomly sample 50-100 PF blocks across mathematical domains and difficulty levels, test StepFun-Formalizer-32B autoformalization success rate and Goedel-Prover-V2-32B proof search success rate, establish block-level end-to-end success rate baseline. Threshold: if end-to-end success rate < 30%, Tier 2 requires redesign (e.g., multi-shot formalization with compiler-feedback self-correction). Report decomposed success rates: formalization type-check rate → proof search success rate → end-to-end rate.

**Tier 1 — LLM Block Verification with calibrated uncertainty.** Decompose proof into PF blocks (Barkallah et al., 2026) with explicit premises, conclusions, and dependency graphs. Run Block Verification using QwQ-32B with dual uncertainty scoring: (i) ensemble disagreement via N=5 stochastic forward passes with temperature sampling, (ii) token-level CoT entropy. Calibrate via Platt scaling on synthetic evaluation set and miniF2F verification data (NOT on ArxivMathGradingBench, which is reserved for evaluation only), with temperature scaling as calibration method ablation.

**Dual-signal routing.** Route blocks based on: uncertainty score × dependency criticality (primary: fan-out degree in inter-block dependency DAG; supplementary sensitivity analysis: dominator nodes, betweenness centrality). This dual signal mitigates the "confident-but-wrong" risk inherent in LLM overconfidence: (a) ensemble disagreement captures inter-model uncertainty more reliably than single-model confidence; (b) dependency criticality provides an uncertainty-independent signal — high-fan-out blocks receive formal verification even if BV is confident; (c) structural difficulty heuristics (block-internal step count, cited theorem count) serve as additional features.

**Why calibrated uncertainty, not just structural heuristics?** Simple heuristics (block length, step count) capture surface complexity but miss blocks that are structurally simple yet reasoning-subtle — e.g., a one-step block applying a theorem in a non-obvious way. Ensemble disagreement flags exactly these cases: when model copies disagree on a seemingly-simple block, this signals hidden reasoning difficulty invisible to structural features. We validate this claim via head-to-head ablation against heuristic-only routing.

**Tier 2 — Selective formal verification.** Routed blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging PF block structure (premises→Lean 4 hypotheses, conclusion→Lean 4 goal, no context completion needed) — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction (up to k=3 retry rounds using Lean compiler feedback). Per-block timeout: 5 min; per-proof timeout: 30 min. Fallback strategy for autoformalization failure or proof search timeout is an ablation variable.

## Evaluation Plan

**Benchmarks:**
- ArxivMathGradingBench (Barkallah et al., 2026): 35 papers, 40 known errors. Held-out evaluation only (not used for calibration). Error detection precision/recall/F1, bootstrap CI (1000 resamples), McNemar's test, effect size (Cohen's h). Supplementary: per-paper accuracy.
- Synthetic Error Detection Set: 400-500 instances from Hard2Verify competition-level problems. Multi-source error construction: (i) LLM-generated incorrect proofs, (ii) controlled perturbation of correct proofs (deleted steps, swapped theorems, computation errors), (iii) extracted known-error steps from Hard2Verify annotations. Ground-truth verification via answer matching + Lean 4 proof for correct proofs. Human validation on 50-80 instance subsample (Cohen's κ). Used for calibration and as co-primary evaluation benchmark.
- miniF2F Verification Protocol: Generate ≥8 candidate proofs per problem (≥100 problems) using QwQ-32B, evaluate verification precision/recall. Aligned with Safe's miniF2F setting.

**Baselines (7 methods):**
- PF + BV single-pass (Barkallah et al., 2026)
- PF + BV ensemble (N=5, no routing to formal verification)
- PF + BV with specialized prompt ensemble (per arXiv 2604.02450, 2026): best-effort LLM verification upper bound
- ThinkPRM (2025): SOTA data-efficient verbalized PRM
- Qwen2.5-Math-PRM-7B: strongest open-source discriminative PRM at comparable scale
- Safe universal formalization (Liu et al., ACL 2025)
- HERMES (Ospanov et al., ICML 2026): if applicable to verification setting

**Cost framework:** Unified metric: GPU-seconds per proof. Detailed breakdown: PF decomposition + ensemble BV (5× single BV) + routing overhead + autoformalization (per routed block) + proof search including retries and timeouts + fallback cost for Tier 2 failures. Pareto curve (cost vs. error detection recall) plotting all methods.

**Ablations (8 experiments):**
1. Uncertainty signal decomposition: ensemble disagreement only / CoT entropy only / combined — AUROC, ECE, recall@fixed-cost
2. Routing signal: uncertainty only / dependency criticality only / simple structural heuristic only / dual signal — recall and cost
3. Ensemble size: N=3 / N=5 / N=7
4. Autoformalization failure fallback: accept / reject / majority-vote re-verification
5. Threshold sweep: routing percentage 5%-50% — Pareto curve
6. **PF blocks vs. raw NL autoformalization (Contribution 1 validation):** Paired comparison on same proofs. PF block input vs. raw NL fragment input to StepFun-Formalizer-32B. Metrics: Lean 4 type-check rate, proof search success rate. Paired Wilcoxon signed-rank test. This is a core result, not merely an ablation.
7. Confident-but-wrong analysis: proportion of BV errors at >0.8 confidence, fraction captured by dual-signal vs. uncertainty-only routing
8. Tier 2 sensitivity analysis: system Pareto curves under assumed Tier 2 success rates of 30%/50%/70%/90%, demonstrating robustness

**Calibration method ablation:** Platt scaling vs. temperature scaling, cross-validated on calibration set, evaluated by ECE and routing decision quality.

## Key References

- Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., arXiv 2026)
- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (Liu et al., ACL 2025)
- Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (Pandit et al., arXiv 2025)
- miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)
- Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (Ganguly et al., NeurIPS 2025)
- Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (Qu, arXiv 2026)
- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (Singh et al., arXiv 2026)
- HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (Ospanov et al., ICML 2026)
- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)
- Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)
- ThinkPRM: Process Reward Models That Think (2025)
- Qwen2.5-Math-PRM (2025)
- ProofSketcher (arXiv 2026)
- UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing (arXiv 2026)
- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (2025)
- Do We Need Frontier Models to Verify Mathematical Proofs? (arXiv 2604.02450, 2026)
- Process-Driven Autoformalization in Lean 4 (2024)

## Resource Estimate

- **Phase 0 pilot:** ~30-50 GPU-hours (A100-80GB), 1-2 weeks. Go/no-go decision point.
- **Full pipeline (Phase 1-3):** GPU hours: 400-550 (ensemble BV ~80h; StepFun-Formalizer ~80h; Goedel-Prover-V2 proof search ~130h including retries/timeouts; synthetic set construction ~40h; baselines + ablations ~120-170h). CPU hours: ~60h (Lean 4 kernel type-checking). Timeline: 14-18 weeks (2-3 researchers), including 2-3 week contingency for PF pipeline reproduction if code unavailable.
- **Estimated GPU cost:** $1200-1650
- **Lean 4 proof search:** Per-block timeout 5 min, per-proof timeout 30 min. ArxivMathGradingBench single pass: ~9h wall-clock (35 papers × ~30 blocks × 15% routing × 3.5 min/block). Independent blocks parallelizable.
- **Critical path:** Phase 0 pilot (weeks 1-2) → PF pipeline setup + synthetic set (weeks 2-5) → uncertainty calibration (weeks 5-8) → full pipeline + ablations (weeks 8-15) → analysis + writing (weeks 15-18).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "ce99f861-e99b-43a5-a5d4-8383604873a1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T12:58:32.968Z_

```json
{
  "parentUuid": "ce99f861-e99b-43a5-a5d4-8383604873a1",
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
  "uuid": "a46ae228-a896-473f-bdb6-f2a2995f45e2",
  "timestamp": "2026-05-27T12:58:32.968Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T12:58:32.968Z_

```json
{
  "parentUuid": "a46ae228-a896-473f-bdb6-f2a2995f45e2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c5ae9431-2add-41fb-910a-78d2593c2506",
  "timestamp": "2026-05-27T12:58:32.968Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
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
  "lastPrompt": "# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we achieve near-formal-verification reliability for natural language mathematical proof che…",
  "leafUuid": "c5ae9431-2add-41fb-910a-78d2593c2506",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective formal verification via uncertainty and dependency routing",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Assistant

_source line 8 · 2026-05-27T12:58:39.724Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about uncertainty-guided selective formal verification for mathematical proofs, using pseudo-formal decomposition as a bridge. Let me first do thorough literature research to understand the landscape before making any judgments.

Let me search for the key papers and concepts mentioned in this proposal to validate the novelty claims and understand the competitive landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5ae9431-2add-41fb-910a-78d2593c2506",
  "isSidechain": false,
  "requestId": "req_011CbT7XG5EVg2Eb4jS7YnyW",
  "type": "assistant",
  "uuid": "43a74cda-261c-483e-8690-ec7b4c1ad80a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DKybaT7GJuv7RStV2uiFc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5372,
      "cache_read_input_tokens": 14184,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5372
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

_source line 9 · 2026-05-27T12:58:41.299Z_

I need to do thorough literature research before evaluating this proposal. Let me start by loading the WebSearch tool and conducting targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43a74cda-261c-483e-8690-ec7b4c1ad80a",
  "isSidechain": false,
  "requestId": "req_011CbT7XG5EVg2Eb4jS7YnyW",
  "type": "assistant",
  "uuid": "9df24d49-d431-47b8-9881-b46c4f5ad3d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DKybaT7GJuv7RStV2uiFc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5372,
      "cache_read_input_tokens": 14184,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5372
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

_source line 10 · 2026-05-27T12:58:41.548Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012Gi3CEd2p9txaPaeSK5nR8`</summary>

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
  "parentUuid": "9df24d49-d431-47b8-9881-b46c4f5ad3d6",
  "isSidechain": false,
  "requestId": "req_011CbT7XG5EVg2Eb4jS7YnyW",
  "type": "assistant",
  "uuid": "c3de11c0-6ec2-4202-a0c6-678dab083bb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DKybaT7GJuv7RStV2uiFc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5372,
      "cache_read_input_tokens": 14184,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5372
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

_source line 11 · 2026-05-27T12:58:41.556Z_

<details><summary>↩ Tool result · `toolu_012Gi3CEd2p9txaPaeSK5nR8`</summary>

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
  "parentUuid": "c3de11c0-6ec2-4202-a0c6-678dab083bb2",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "19ff88d2-182e-42dd-8c4d-bd3af390ddcb",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "c3de11c0-6ec2-4202-a0c6-678dab083bb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T12:58:49.482Z_

Now let me conduct my front-loaded literature research. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19ff88d2-182e-42dd-8c4d-bd3af390ddcb",
  "isSidechain": false,
  "requestId": "req_011CbT7Xtsohg9SKxrVpELWL",
  "type": "assistant",
  "uuid": "00135a97-69a7-4ce6-aa3e-95ec89a74b14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ES8ZY76zD4QKt3iaFZD2po",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 19556,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 19556,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 13 · 2026-05-27T12:58:49.688Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019dQiuqHbEY9S1KsAk6CH91`</summary>

```json
{
  "query": "selective formal verification mathematical proofs uncertainty routing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00135a97-69a7-4ce6-aa3e-95ec89a74b14",
  "isSidechain": false,
  "requestId": "req_011CbT7Xtsohg9SKxrVpELWL",
  "type": "assistant",
  "uuid": "9ed63bf7-0a43-4671-8cc9-b64ce35733b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ES8ZY76zD4QKt3iaFZD2po",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 19556,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 19556,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 14 · 2026-05-27T12:58:59.697Z_

<details><summary>↩ Tool result · `toolu_019dQiuqHbEY9S1KsAk6CH91`</summary>

```text
Web search results for query: "selective formal verification mathematical proofs uncertainty routing 2025 2026"

Links: [{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/pdf/2602.03975"},{"title":"Formal Verification – Why It Matters | PQShield","url":"https://pqshield.com/formal-verification-why-it-matters/"},{"title":"A Review of Automated Formal Verification of Ad Hoc Routing Protocols   for Wireless Sensor Networks","url":"https://arxiv.org/pdf/1305.7410"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/pdf/2506.04592"},{"title":"Submitted as a conference paper at ICLR 2026 TYPED CHAIN-OF-THOUGHT:","url":"https://arxiv.org/pdf/2510.01069"},{"title":"From Informal to Formal -- Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs","url":"https://arxiv.org/pdf/2501.16207"}]

Based on the search results, I found several relevant papers and resources related to formal verification, mathematical proofs, and uncertainty in recent work (2025-2026):

## Key Findings:

**Selective Verification with Uncertainty:**
Recent work allocates verification according to state-local uncertainty rather than uniform rules, using deterministic gating and hybrid pre-verification scores that combine learned distance-to-goal signals with learned residuals, choosing state-conditional verification budgets so that ambiguous branching points receive more verification while clear decisions receive less.

**Formal Verification and Mathematical Proofs:**
Formal verification uses deep mathematical proofs and logic to guarantee a system's security. Formal verification involves using mathematical proofs to verify that a cryptographic implementation strictly adheres to its formal specification and that the specification itself meets the required security properties.

**Recent Advances (2025-2026):**
Recent advances have sparked a surge of interest in applying AI to formal mathematical reasoning, with AlphaProof becoming the first AI to achieve the silver-medal level in the IMO in 2024, followed by strong results from ByteDance and Harmonic in IMO 2025.

**Step-Aware Formal Verification:**
A retrospective, step-aware formal verification framework called Safe has been proposed that articulates mathematical claims in formal mathematical language Lean 4 at each reasoning step and provides formal proofs to identify hallucinations.

The search results indicate active research in combining formal verification, uncertainty-aware routing of computational resources, and mathematical proof verification for improving AI reasoning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ed63bf7-0a43-4671-8cc9-b64ce35733b9",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "7f6418b7-bece-40ec-867f-b33287970060",
  "toolUseResult": {
    "query": "selective formal verification mathematical proofs uncertainty routing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XNgAavXZrjTGKAt4szdG7y",
        "content": [
          {
            "title": "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure",
            "url": "https://arxiv.org/pdf/2602.03975"
          },
          {
            "title": "Formal Verification – Why It Matters | PQShield",
            "url": "https://pqshield.com/formal-verification-why-it-matters/"
          },
          {
            "title": "A Review of Automated Formal Verification of Ad Hoc Routing Protocols   for Wireless Sensor Networks",
            "url": "https://arxiv.org/pdf/1305.7410"
          },
          {
            "title": "Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM",
            "url": "https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"
          },
          {
            "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification",
            "url": "https://arxiv.org/pdf/2506.04592"
          },
          {
            "title": "Submitted as a conference paper at ICLR 2026 TYPED CHAIN-OF-THOUGHT:",
            "url": "https://arxiv.org/pdf/2510.01069"
          },
          {
            "title": "From Informal to Formal -- Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs",
            "url": "https://arxiv.org/pdf/2501.16207"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources related to formal verification, mathematical proofs, and uncertainty in recent work (2025-2026):\n\n## Key Findings:\n\n**Selective Verification with Uncertainty:**\nRecent work allocates verification according to state-local uncertainty rather than uniform rules, using deterministic gating and hybrid pre-verification scores that combine learned distance-to-goal signals with learned residuals, choosing state-conditional verification budgets so that ambiguous branching points receive more verification while clear decisions receive less.\n\n**Formal Verification and Mathematical Proofs:**\nFormal verification uses deep mathematical proofs and logic to guarantee a system's security. Formal verification involves using mathematical proofs to verify that a cryptographic implementation strictly adheres to its formal specification and that the specification itself meets the required security properties.\n\n**Recent Advances (2025-2026):**\nRecent advances have sparked a surge of interest in applying AI to formal mathematical reasoning, with AlphaProof becoming the first AI to achieve the silver-medal level in the IMO in 2024, followed by strong results from ByteDance and Harmonic in IMO 2025.\n\n**Step-Aware Formal Verification:**\nA retrospective, step-aware formal verification framework called Safe has been proposed that articulates mathematical claims in formal mathematical language Lean 4 at each reasoning step and provides formal proofs to identify hallucinations.\n\nThe search results indicate active research in combining formal verification, uncertainty-aware routing of computational resources, and mathematical proof verification for improving AI reasoning systems."
    ],
    "durationSeconds": 10.002524368000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9ed63bf7-0a43-4671-8cc9-b64ce35733b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T12:59:04.791Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J3w85UdCRzpMRyucby7QkR`</summary>

```json
{
  "query": "Ganguly \"Grammars of Formal Uncertainty\" NeurIPS 2025 selective SMT formalization PCFG"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f6418b7-bece-40ec-867f-b33287970060",
  "isSidechain": false,
  "requestId": "req_011CbT7ZEASyQ2PkivNRRy9V",
  "type": "assistant",
  "uuid": "d2d88aae-9e7d-42ae-b614-eb5f74e234c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZKd54aJPJyMEseYUdWqhz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 20279,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 20279,
          "cache_creation_input_tokens": 823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 823
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

_source line 16 · 2026-05-27T12:59:16.729Z_

<details><summary>↩ Tool result · `toolu_01J3w85UdCRzpMRyucby7QkR`</summary>

```text
Web search results for query: "Ganguly "Grammars of Formal Uncertainty" NeurIPS 2025 selective SMT formalization PCFG"

Links: [{"title":"GitHub - DebarghaG/grammars-formal-uncertainty: [NeurIPS 2025] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://github.com/DebarghaG/grammars-formal-uncertainty"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://openreview.net/attachment?id=QfKpJ00t2L&name=pdf"},{"title":"[2505.20047] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/abs/2505.20047"},{"title":"Srinivasan Iyengar - Microsoft | LinkedIn","url":"https://www.linkedin.com/in/srinivasani/"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/grammars-of-formal-uncertainty-when-to-trust-llms-in-automated-reasoning-tasks/"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks | OpenReview","url":"https://openreview.net/forum?id=QfKpJ00t2L"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/html/2505.20047v1"},{"title":"NeurIPS Poster Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://neurips.cc/virtual/2025/poster/118114"},{"title":"Paper page - Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://huggingface.co/papers/2505.20047"}]

I found the research paper you're looking for! Here's what I found:

## "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks"

This is a NeurIPS 2025 paper by Debargha Ganguly and colleagues.

### Key Research Components:

**Main Framework:** The paper introduces a probabilistic context-free grammar (PCFG) framework to model LLM outputs, yielding a refined uncertainty taxonomy.

**SMT and Autoformalization:** The paper's systematic evaluation of five frontier LLMs reveals Satisfiability Modulo Theories (SMT) based autoformalization's domain-specific impact on accuracy (from +34.8% on logical tasks to -44.5% on factual ones). The approach involves LLM-generated SMT-LIB solved by Z3 (autoformalization).

**Key Findings:** Uncertainty signals are task-dependent (e.g., grammar entropy for logic, AUROC>0.93), and a lightweight fusion of these signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention.

**PCFG Analysis:** The paper analyzes SMT-LIB program distributions with PCFGs, analyzing ensembles of LLM-generated SMT-LIB programs as samples from the model's internal probability distribution, which reveals strategic diversity, common structural motifs, and areas of high model uncertainty.

The paper is available on [arXiv](https://arxiv.org/abs/2505.20047), [OpenReview](https://openreview.net/forum?id=QfKpJ00t2L), and has an accompanying [GitHub repository](https://github.com/DebarghaG/grammars-formal-uncertainty).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2d88aae-9e7d-42ae-b614-eb5f74e234c8",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "2974cc50-85aa-4dde-8a78-ffb2f0b784bb",
  "toolUseResult": {
    "query": "Ganguly \"Grammars of Formal Uncertainty\" NeurIPS 2025 selective SMT formalization PCFG",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NsRcQNWcWRDkFHX8RhEW4h",
        "content": [
          {
            "title": "GitHub - DebarghaG/grammars-formal-uncertainty: [NeurIPS 2025] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://github.com/DebarghaG/grammars-formal-uncertainty"
          },
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://openreview.net/attachment?id=QfKpJ00t2L&name=pdf"
          },
          {
            "title": "[2505.20047] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://arxiv.org/abs/2505.20047"
          },
          {
            "title": "Srinivasan Iyengar - Microsoft | LinkedIn",
            "url": "https://www.linkedin.com/in/srinivasani/"
          },
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/publication/grammars-of-formal-uncertainty-when-to-trust-llms-in-automated-reasoning-tasks/"
          },
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks | OpenReview",
            "url": "https://openreview.net/forum?id=QfKpJ00t2L"
          },
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://arxiv.org/html/2505.20047v1"
          },
          {
            "title": "NeurIPS Poster Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://neurips.cc/virtual/2025/poster/118114"
          },
          {
            "title": "Paper page - Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://huggingface.co/papers/2505.20047"
          }
        ]
      },
      "I found the research paper you're looking for! Here's what I found:\n\n## \"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks\"\n\nThis is a NeurIPS 2025 paper by Debargha Ganguly and colleagues.\n\n### Key Research Components:\n\n**Main Framework:** The paper introduces a probabilistic context-free grammar (PCFG) framework to model LLM outputs, yielding a refined uncertainty taxonomy.\n\n**SMT and Autoformalization:** The paper's systematic evaluation of five frontier LLMs reveals Satisfiability Modulo Theories (SMT) based autoformalization's domain-specific impact on accuracy (from +34.8% on logical tasks to -44.5% on factual ones). The approach involves LLM-generated SMT-LIB solved by Z3 (autoformalization).\n\n**Key Findings:** Uncertainty signals are task-dependent (e.g., grammar entropy for logic, AUROC>0.93), and a lightweight fusion of these signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention.\n\n**PCFG Analysis:** The paper analyzes SMT-LIB program distributions with PCFGs, analyzing ensembles of LLM-generated SMT-LIB programs as samples from the model's internal probability distribution, which reveals strategic diversity, common structural motifs, and areas of high model uncertainty.\n\nThe paper is available on [arXiv](https://arxiv.org/abs/2505.20047), [OpenReview](https://openreview.net/forum?id=QfKpJ00t2L), and has an accompanying [GitHub repository](https://github.com/DebarghaG/grammars-formal-uncertainty)."
    ],
    "durationSeconds": 11.933614357000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d2d88aae-9e7d-42ae-b614-eb5f74e234c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T12:59:20.261Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G78ufHp1zSBwxqS62uMmUP`</summary>

```json
{
  "query": "HERMES \"interleave informal formal\" Lean 4 proof generation Ospanov 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2974cc50-85aa-4dde-8a78-ffb2f0b784bb",
  "isSidechain": false,
  "requestId": "req_011CbT7aUxxxXa6FHTWbD95T",
  "type": "assistant",
  "uuid": "c44de483-afb6-4d9d-a82c-b39ccce9ec09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VMBvx1EP6k9WhqvLhFg34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1051,
      "cache_read_input_tokens": 21102,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 21102,
          "cache_creation_input_tokens": 1051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1051
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

_source line 18 · 2026-05-27T12:59:27.946Z_

<details><summary>↩ Tool result · `toolu_01G78ufHp1zSBwxqS62uMmUP`</summary>

```text
Web search results for query: "HERMES "interleave informal formal" Lean 4 proof generation Ospanov 2025 2026"

Links: [{"title":"(PDF) HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://www.researchgate.net/publication/397933683_HERMES_Towards_Efficient_and_Verifiable_Mathematical_Reasoning_in_LLMs"},{"title":"[2511.18760] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760"},{"title":"[2511.18760v1] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760v1"},{"title":"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/pdf/2511.18760"},{"title":"[PDF] APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/APOLLO:-Automated-LLM-and-Lean-Collaboration-for-Ospanov-Farnia/ec6a8bc007ba9573809ff9a972f6ed300dfd89ce"},{"title":"APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning","url":"https://arxiv.org/html/2505.05758v1"}]

I found relevant information about HERMES. Here are the search results:

HERMES is the first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean. The framework performs intermediate formal checking to prevent reasoning drift and employs a memory module that maintains proof continuity across long, multi-step reasoning chains, enabling both exploration and verification within a single workflow.

On difficult datasets such as AIME'25, HERMES achieves up to a 67% accuracy improvement while using 80% fewer total inference FLOPs. The implementation and codebase are publicly available at https://github.com/aziksh-ospanov/HERMES.

The paper was authored by Azim Ospanov, Farzan Farnia, and Roozbeh Yousefzadeh and appears to have been released in November 2025 based on the arxiv timestamps found in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c44de483-afb6-4d9d-a82c-b39ccce9ec09",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "b5b9af6f-457c-4e11-b31a-86127b461b14",
  "toolUseResult": {
    "query": "HERMES \"interleave informal formal\" Lean 4 proof generation Ospanov 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JAupkn6WdFUVnc7mkHMtku",
        "content": [
          {
            "title": "(PDF) HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://www.researchgate.net/publication/397933683_HERMES_Towards_Efficient_and_Verifiable_Mathematical_Reasoning_in_LLMs"
          },
          {
            "title": "[2511.18760] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/abs/2511.18760"
          },
          {
            "title": "[2511.18760v1] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/abs/2511.18760v1"
          },
          {
            "title": "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2511.18760"
          },
          {
            "title": "[PDF] APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/APOLLO:-Automated-LLM-and-Lean-Collaboration-for-Ospanov-Farnia/ec6a8bc007ba9573809ff9a972f6ed300dfd89ce"
          },
          {
            "title": "APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning",
            "url": "https://arxiv.org/html/2505.05758v1"
          }
        ]
      },
      "I found relevant information about HERMES. Here are the search results:\n\nHERMES is the first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean. The framework performs intermediate formal checking to prevent reasoning drift and employs a memory module that maintains proof continuity across long, multi-step reasoning chains, enabling both exploration and verification within a single workflow.\n\nOn difficult datasets such as AIME'25, HERMES achieves up to a 67% accuracy improvement while using 80% fewer total inference FLOPs. The implementation and codebase are publicly available at https://github.com/aziksh-ospanov/HERMES.\n\nThe paper was authored by Azim Ospanov, Farzan Farnia, and Roozbeh Yousefzadeh and appears to have been released in November 2025 based on the arxiv timestamps found in the search results."
    ],
    "durationSeconds": 7.679950646999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c44de483-afb6-4d9d-a82c-b39ccce9ec09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T12:59:31.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W9U6DZPG5niyn3t3uWqx7y`</summary>

```json
{
  "query": "Barkallah pseudo-formalization proof verification 2026 PF block ArxivMathGradingBench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5b9af6f-457c-4e11-b31a-86127b461b14",
  "isSidechain": false,
  "requestId": "req_011CbT7bJuzrA2EdVEfxN2Wf",
  "type": "assistant",
  "uuid": "a47c566c-0ccc-463f-b203-7b570162842a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRBGgXM7CwdJQtiNKmTgCq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 22153,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 22153,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 701
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

_source line 20 · 2026-05-27T12:59:40.788Z_

<details><summary>↩ Tool result · `toolu_01W9U6DZPG5niyn3t3uWqx7y`</summary>

```text
Web search results for query: "Barkallah pseudo-formalization proof verification 2026 PF block ArxivMathGradingBench"

Links: [{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Proving TCS and Math Theorems in Lean | CS 294-268 (Spring 2026)","url":"https://ucb-lean-course-sp26.github.io/"},{"title":"Automated Conjecture Resolution with Formal Verification","url":"https://arxiv.org/html/2604.03789"},{"title":"Advancing Mathematics Research with AI-Driven Formal Proof Search","url":"https://arxiv.org/html/2605.22763v1"},{"title":"Towards LLM-based Generation of Human-Readable Proofs in Polynomial Formal Verification","url":"https://arxiv.org/pdf/2505.23311"}]

I found the paper you're looking for! The paper "Pseudo-Formalization for Automatic Proof Verification" by Slim Barkallah and colleagues was published on arXiv on May 19, 2026.

Here's what the paper is about:

The paper proposes Pseudo-Formalization (PF), a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language. A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language.

To verify the correctness of a regular natural language proof, an LLM translates it to Pseudo-Formal and then verifies each module independently, an algorithm called Block Verification (which corresponds to the "PF block" you mentioned in your query).

The motivation for this work is that reliable verification of proofs is a bottleneck for training and evaluating AI systems on hard mathematical reasoning. While fully formal proofs in languages like Lean are easy to verify because they are unambiguous and modular, most proofs—particularly those written by AI systems—have neither property, and translating them into formal languages remains challenging in many frontier math settings.

The paper's arXiv ID is 2605.20531.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a47c566c-0ccc-463f-b203-7b570162842a",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "963369b4-6ccc-461a-b042-6e743adef763",
  "toolUseResult": {
    "query": "Barkallah pseudo-formalization proof verification 2026 PF block ArxivMathGradingBench",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HbdeVWiV7UNe83LyTdHzUv",
        "content": [
          {
            "title": "[2605.20531] Pseudo-Formalization for Automatic Proof Verification",
            "url": "https://arxiv.org/abs/2605.20531"
          },
          {
            "title": "Pseudo-Formalization for Automatic Proof Verification",
            "url": "https://arxiv.org/html/2605.20531"
          },
          {
            "title": "130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?",
            "url": "https://arxiv.org/pdf/2601.03298"
          },
          {
            "title": "Proving TCS and Math Theorems in Lean | CS 294-268 (Spring 2026)",
            "url": "https://ucb-lean-course-sp26.github.io/"
          },
          {
            "title": "Automated Conjecture Resolution with Formal Verification",
            "url": "https://arxiv.org/html/2604.03789"
          },
          {
            "title": "Advancing Mathematics Research with AI-Driven Formal Proof Search",
            "url": "https://arxiv.org/html/2605.22763v1"
          },
          {
            "title": "Towards LLM-based Generation of Human-Readable Proofs in Polynomial Formal Verification",
            "url": "https://arxiv.org/pdf/2505.23311"
          }
        ]
      },
      "I found the paper you're looking for! The paper \"Pseudo-Formalization for Automatic Proof Verification\" by Slim Barkallah and colleagues was published on arXiv on May 19, 2026.\n\nHere's what the paper is about:\n\nThe paper proposes Pseudo-Formalization (PF), a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language. A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language.\n\nTo verify the correctness of a regular natural language proof, an LLM translates it to Pseudo-Formal and then verifies each module independently, an algorithm called Block Verification (which corresponds to the \"PF block\" you mentioned in your query).\n\nThe motivation for this work is that reliable verification of proofs is a bottleneck for training and evaluating AI systems on hard mathematical reasoning. While fully formal proofs in languages like Lean are easy to verify because they are unambiguous and modular, most proofs—particularly those written by AI systems—have neither property, and translating them into formal languages remains challenging in many frontier math settings.\n\nThe paper's arXiv ID is 2605.20531."
    ],
    "durationSeconds": 9.400596186000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a47c566c-0ccc-463f-b203-7b570162842a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
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
  "lastPrompt": "# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we achieve near-formal-verification reliability for natural language mathematical proof che…",
  "leafUuid": "963369b4-6ccc-461a-b042-6e743adef763",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective formal verification via uncertainty and dependency routing",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Tool call

_source line 23 · 2026-05-27T12:59:44.937Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CdtAbsN6nJ8Z6zU7mZ7vHU`</summary>

```json
{
  "query": "autoformalization block-level step-level vs whole-proof success rate Lean 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "963369b4-6ccc-461a-b042-6e743adef763",
  "isSidechain": false,
  "requestId": "req_011CbT7cFqjg6pasyVNKG92N",
  "type": "assistant",
  "uuid": "8e54a5b5-b188-4ba4-b600-f1cf0d607328",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192dSawyGzayZTGSKu3FZdD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 22854,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 22854,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 24 · 2026-05-27T13:00:00.525Z_

<details><summary>↩ Tool result · `toolu_01CdtAbsN6nJ8Z6zU7mZ7vHU`</summary>

```text
Web search results for query: "autoformalization block-level step-level vs whole-proof success rate Lean 2025 2026"

Links: [{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"Aristotle: IMO-level Automated Theorem Proving The Harmonic Team Abstract","url":"https://harmonic.fun/pdf/Aristotle_IMO_Level_Automated_Theorem_Proving.pdf"},{"title":"RLMEval: Evaluating Autoformalization on Research-Level Mathematics","url":"http://aitp-conference.org/2025/abstract/AITP_2025_paper_8.pdf"},{"title":"Evaluating Research-Level Neural Theorem Proving","url":"https://aclanthology.org/2025.findings-emnlp.581.pdf"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/html/2511.03108v1"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"}]

I found relevant information about autoformalization in Lean from 2025-2026. Here are the key findings from the search results:

## Success Rates and Performance Metrics

A 2025 method achieves 68.4% pass rate on benchmarks such as MiniF2F. Additionally, FormL4 trains on GPT-4 informalized Mathlib proofs with process-supervised step-level Lean compilation feedback.

Models still struggle to generate well-typed and semantically accurate statements, achieving at best a 59.37% type-check rate and 30.33% BEq+ score.

## Step-Level vs Whole-Proof Approaches

The research shows different architectural approaches are being pursued: Over the last two years, the leader on other automated theorem proving benchmarks has gone back and forth between step-wise and whole proof systems. 

Aristotle, a system that achieved gold-medal-level performance on the 2025 IMO problems, utilizes a sophisticated proof search algorithm to complete formal proofs, integrating a system that generates and formalizes high-level lemmas.

## Recent Notable Results

ProofNet showed a 4.04% → 26.15% improvement with only 859 unlabeled samples, and uproof improved from 2.4% → 9.6% (pass@1) and 24.4% → 33.6% (pass@16).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e54a5b5-b188-4ba4-b600-f1cf0d607328",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "4cf52f4d-be0d-488d-93b3-af3367a5ef8d",
  "toolUseResult": {
    "query": "autoformalization block-level step-level vs whole-proof success rate Lean 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0191cL9NY4zo1tHCqPDeqMiK",
        "content": [
          {
            "title": "Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2505.23486v1"
          },
          {
            "title": "Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics",
            "url": "https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"
          },
          {
            "title": "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings",
            "url": "https://arxiv.org/html/2510.15681v1"
          },
          {
            "title": "Aristotle: IMO-level Automated Theorem Proving The Harmonic Team Abstract",
            "url": "https://harmonic.fun/pdf/Aristotle_IMO_Level_Automated_Theorem_Proving.pdf"
          },
          {
            "title": "RLMEval: Evaluating Autoformalization on Research-Level Mathematics",
            "url": "http://aitp-conference.org/2025/abstract/AITP_2025_paper_8.pdf"
          },
          {
            "title": "Evaluating Research-Level Neural Theorem Proving",
            "url": "https://aclanthology.org/2025.findings-emnlp.581.pdf"
          },
          {
            "title": "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward",
            "url": "https://arxiv.org/html/2511.03108v1"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4 | OpenReview",
            "url": "https://openreview.net/forum?id=k8KsI84Ds7"
          }
        ]
      },
      "I found relevant information about autoformalization in Lean from 2025-2026. Here are the key findings from the search results:\n\n## Success Rates and Performance Metrics\n\nA 2025 method achieves 68.4% pass rate on benchmarks such as MiniF2F. Additionally, FormL4 trains on GPT-4 informalized Mathlib proofs with process-supervised step-level Lean compilation feedback.\n\nModels still struggle to generate well-typed and semantically accurate statements, achieving at best a 59.37% type-check rate and 30.33% BEq+ score.\n\n## Step-Level vs Whole-Proof Approaches\n\nThe research shows different architectural approaches are being pursued: Over the last two years, the leader on other automated theorem proving benchmarks has gone back and forth between step-wise and whole proof systems. \n\nAristotle, a system that achieved gold-medal-level performance on the 2025 IMO problems, utilizes a sophisticated proof search algorithm to complete formal proofs, integrating a system that generates and formalizes high-level lemmas.\n\n## Recent Notable Results\n\nProofNet showed a 4.04% → 26.15% improvement with only 859 unlabeled samples, and uproof improved from 2.4% → 9.6% (pass@1) and 24.4% → 33.6% (pass@16)."
    ],
    "durationSeconds": 15.581261157999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8e54a5b5-b188-4ba4-b600-f1cf0d607328",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T13:00:03.363Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uw9TDrj9Tm4RKwUW9o5wdK`</summary>

```json
{
  "query": "ThinkPRM process reward model verbalized 2025 step verification LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf52f4d-be0d-488d-93b3-af3367a5ef8d",
  "isSidechain": false,
  "requestId": "req_011CbT7diE1bzds7e88e9YgU",
  "type": "assistant",
  "uuid": "935a88cd-edb3-4641-8c7f-6a42066387a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLz5rrBBsJFVqrYH1Jmyi1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 23572,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 23572,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 866
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

_source line 26 · 2026-05-27T13:00:11.905Z_

<details><summary>↩ Tool result · `toolu_01Uw9TDrj9Tm4RKwUW9o5wdK`</summary>

```text
Web search results for query: "ThinkPRM process reward model verbalized 2025 step verification LLM"

Links: [{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"Process Reward Models That Think | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.16828v5"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"[2504.16828] Process Reward Models That Think - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2504.16828"},{"title":"ThinkPRM: Process Reward Models That Think","url":"https://mukhal.github.io/projects/thinkprm/"},{"title":"[2504.16828v1] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828v1"},{"title":"[2504.16828v3] Process Reward Models That Think","url":"http://arxiv.org/abs/2504.16828v3"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/html/2504.16828v5"}]

Based on the search results, here's what I found about ThinkPRM:

## Overview

ThinkPRM is a generative process reward model that enables large language models to provide verbalized, long Chain-of-Thought (CoT) verification for their reasoning steps.

## Key Characteristics

ThinkPRM is a long chain-of-thought verifier that uses minimal supervision to outperform discriminative PRMs and LLM-as-a-Judge across various benchmarks and token budgets. 

It works as a verbalized step-wise reward model that verifies every step in the solution by generating a verification chain-of-thought (CoT).

## Data Efficiency

A major advantage of ThinkPRM is its data efficiency. The approach outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks. More specifically, a generative PRM fine-tuned with as few as 8K synthetic verification chains substantially improves over LLM-as-a-Judge PRMs, and outperforms discriminative PRMs trained on datasets orders of magnitude larger.

## Performance

ThinkPRM beats baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "935a88cd-edb3-4641-8c7f-6a42066387a1",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "c43ccf46-c21f-4ac7-812a-aa001e17f79c",
  "toolUseResult": {
    "query": "ThinkPRM process reward model verbalized 2025 step verification LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WUNTidrSPCxycxHJpxVanP",
        "content": [
          {
            "title": "Paper page - Process Reward Models That Think",
            "url": "https://huggingface.co/papers/2504.16828"
          },
          {
            "title": "Process Reward Models That Think | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2504.16828v5"
          },
          {
            "title": "Process Reward Models That Think | OpenReview",
            "url": "https://openreview.net/forum?id=V727xqBYIW"
          },
          {
            "title": "[2504.16828] Process Reward Models That Think",
            "url": "https://arxiv.org/abs/2504.16828"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "[2504.16828] Process Reward Models That Think - ar5iv - arXiv",
            "url": "https://ar5iv.labs.arxiv.org/html/2504.16828"
          },
          {
            "title": "ThinkPRM: Process Reward Models That Think",
            "url": "https://mukhal.github.io/projects/thinkprm/"
          },
          {
            "title": "[2504.16828v1] Process Reward Models That Think",
            "url": "https://arxiv.org/abs/2504.16828v1"
          },
          {
            "title": "[2504.16828v3] Process Reward Models That Think",
            "url": "http://arxiv.org/abs/2504.16828v3"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/html/2504.16828v5"
          }
        ]
      },
      "Based on the search results, here's what I found about ThinkPRM:\n\n## Overview\n\nThinkPRM is a generative process reward model that enables large language models to provide verbalized, long Chain-of-Thought (CoT) verification for their reasoning steps.\n\n## Key Characteristics\n\nThinkPRM is a long chain-of-thought verifier that uses minimal supervision to outperform discriminative PRMs and LLM-as-a-Judge across various benchmarks and token budgets. \n\nIt works as a verbalized step-wise reward model that verifies every step in the solution by generating a verification chain-of-thought (CoT).\n\n## Data Efficiency\n\nA major advantage of ThinkPRM is its data efficiency. The approach outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks. More specifically, a generative PRM fine-tuned with as few as 8K synthetic verification chains substantially improves over LLM-as-a-Judge PRMs, and outperforms discriminative PRMs trained on datasets orders of magnitude larger.\n\n## Performance\n\nThinkPRM beats baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search."
    ],
    "durationSeconds": 8.537781262000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "935a88cd-edb3-4641-8c7f-6a42066387a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T13:00:14.818Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HykhaLRt1HhUafberosoDC`</summary>

```json
{
  "query": "\"uncertainty guided\" \"formal verification\" selective routing proof verification 2025 2026 calibrated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c43ccf46-c21f-4ac7-812a-aa001e17f79c",
  "isSidechain": false,
  "requestId": "req_011CbT7eYtiC6AXkjBdERLuP",
  "type": "assistant",
  "uuid": "51d8be20-b60d-41c0-9045-07eb6d2b7914",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SjzZjwZLNVVJ3XdXG1PjHb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 24438,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 785,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 24438,
          "cache_creation_input_tokens": 785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 785
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

_source line 28 · 2026-05-27T13:00:39.347Z_

<details><summary>↩ Tool result · `toolu_01HykhaLRt1HhUafberosoDC`</summary>

```text
Web search results for query: ""uncertainty guided" "formal verification" selective routing proof verification 2025 2026 calibrated"

Links: [{"title":"2025 was the year of enforcement. 2026 will be the year of example. - 1Route","url":"https://www.1routegroup.com/telecom-validation-enforcement-2025-2026/"},{"title":"ProofCoop: Collaborative Automated Formal Verification (ICSE 2026 - Research Track) - ICSE 2026","url":"https://conf.researchr.org/details/icse-2026/icse-2026-research-track/255/ProofCoop-Collaborative-Automated-Formal-Verification"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/pdf/2505.20047"},{"title":"Verification, Validation, and Uncertainty Quantification Symposium 2026","url":"https://event.asme.org/VandV"},{"title":"System and method for guiding and optimizing formal verification for a circuit design","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7065726"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"},{"title":"A blueprint for formal verification of Apple corecrypto - Apple Security Research","url":"https://security.apple.com/blog/formal-verification-corecrypto/"}]

Based on the search results, I found relevant information about uncertainty-guided approaches in formal verification:

The central thesis of one recent paper is that the inherent probabilistic uncertainty in LLM outputs for formal reasoning tasks, particularly when generating formal artifacts like SMT-LIB programs, is not a mere nuisance but a valuable source of information for guiding verification. Existing methods often ignore this by selecting only the highest-probability output, a simplification that undermines the rigorous standards required for formal reasoning.

Additionally, AI can drastically reduce the cost of formal verification by automating the formalization and proof effort needed to formally certify complex systems, and AI-based formal reasoning has reached an inflection point, with significant progress coming in the near future.

The search also revealed recent work on collaborative formal verification approaches. ProofCoop, presented at ICSE 2026, demonstrates collaborative cooperation between models for the first time.

Regarding the specific terms "selective routing" and "calibrated" in your query: the search results include information on uncertainty-guided approaches to formal verification and proof verification in 2025-2026, but do not contain specific information about "selective routing" or "calibrated" in the context of these formal verification methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51d8be20-b60d-41c0-9045-07eb6d2b7914",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "896f97d7-40af-43d9-9af7-a1122b402081",
  "toolUseResult": {
    "query": "\"uncertainty guided\" \"formal verification\" selective routing proof verification 2025 2026 calibrated",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EtqaDJSuQD3uxswdoFxkuc",
        "content": [
          {
            "title": "2025 was the year of enforcement. 2026 will be the year of example. - 1Route",
            "url": "https://www.1routegroup.com/telecom-validation-enforcement-2025-2026/"
          },
          {
            "title": "ProofCoop: Collaborative Automated Formal Verification (ICSE 2026 - Research Track) - ICSE 2026",
            "url": "https://conf.researchr.org/details/icse-2026/icse-2026-research-track/255/ProofCoop-Collaborative-Automated-Formal-Verification"
          },
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://arxiv.org/pdf/2505.20047"
          },
          {
            "title": "Verification, Validation, and Uncertainty Quantification Symposium 2026",
            "url": "https://event.asme.org/VandV"
          },
          {
            "title": "System and method for guiding and optimizing formal verification for a circuit design",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7065726"
          },
          {
            "title": "Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM",
            "url": "https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"
          },
          {
            "title": "A blueprint for formal verification of Apple corecrypto - Apple Security Research",
            "url": "https://security.apple.com/blog/formal-verification-corecrypto/"
          }
        ]
      },
      "Based on the search results, I found relevant information about uncertainty-guided approaches in formal verification:\n\nThe central thesis of one recent paper is that the inherent probabilistic uncertainty in LLM outputs for formal reasoning tasks, particularly when generating formal artifacts like SMT-LIB programs, is not a mere nuisance but a valuable source of information for guiding verification. Existing methods often ignore this by selecting only the highest-probability output, a simplification that undermines the rigorous standards required for formal reasoning.\n\nAdditionally, AI can drastically reduce the cost of formal verification by automating the formalization and proof effort needed to formally certify complex systems, and AI-based formal reasoning has reached an inflection point, with significant progress coming in the near future.\n\nThe search also revealed recent work on collaborative formal verification approaches. ProofCoop, presented at ICSE 2026, demonstrates collaborative cooperation between models for the first time.\n\nRegarding the specific terms \"selective routing\" and \"calibrated\" in your query: the search results include information on uncertainty-guided approaches to formal verification and proof verification in 2025-2026, but do not contain specific information about \"selective routing\" or \"calibrated\" in the context of these formal verification methods."
    ],
    "durationSeconds": 24.521576228999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "51d8be20-b60d-41c0-9045-07eb6d2b7914",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-27T13:00:39.356Z_

```json
{
  "parentUuid": "896f97d7-40af-43d9-9af7-a1122b402081",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2bc2eb57-4401-4cd1-b8b9-17a3c88cfffb",
  "timestamp": "2026-05-27T13:00:39.356Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-27T13:00:52.352Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0197yLUNYPuSgHNU5mfrbpL2`</summary>

```json
{
  "query": "Safe Liu ACL 2025 step-aware formal verification Lean 4 cost overhead autoformalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bc2eb57-4401-4cd1-b8b9-17a3c88cfffb",
  "isSidechain": false,
  "requestId": "req_011CbT7gaFsVWcSdsr3HxcNf",
  "type": "assistant",
  "uuid": "91945e2e-ae47-43e1-bcb0-43648a6d75ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xhV3LLJptMePe5by3yGup",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 25223,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 25223,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 875
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

_source line 31 · 2026-05-27T13:01:03.522Z_

<details><summary>↩ Tool result · `toolu_0197yLUNYPuSgHNU5mfrbpL2`</summary>

```text
Web search results for query: "Safe Liu ACL 2025 step-aware formal verification Lean 4 cost overhead autoformalization"

Links: [{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.594/"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification | Request PDF","url":"https://www.researchgate.net/publication/394301322_Safe_Enhancing_Mathematical_Reasoning_in_Large_Language_Models_via_Retrospective_Step-aware_Formal_Verification"},{"title":"Towards a Common Framework for Autoformalization","url":"https://arxiv.org/pdf/2509.09810"},{"title":"GitHub - liuchengwucn/Safe: (ACL 2025 Main) Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - Official Implementation & Dataset","url":"https://github.com/liuchengwucn/Safe"},{"title":"(PDF) Process-Driven Autoformalization in Lean 4","url":"https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4"},{"title":"[2506.04592] Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/abs/2506.04592"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/pdf/2506.04592"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"}]

Based on the search results, I found comprehensive information about the paper you're asking about:

## Overview

Safe is a retrospective, step-aware formal verification framework that articulates mathematical claims in formal mathematical language Lean 4 at each reasoning step and provides formal proofs to identify hallucinations.

## Key Contributions

This represents the first endeavor to utilize formal mathematical language Lean 4 for verifying natural language content generated by LLMs. The paper proposes FormalStep as a benchmark for step correctness theorem proving with 30,809 formal statements.

## Framework and Approach

The work draws inspiration from the idea that "the gold standard for supporting a mathematical claim is to provide a proof". Rather than using opaque methods like process reward models, the framework demonstrates significant performance improvement while offering interpretable and verifiable evidence across multiple language models and various mathematical datasets.

## Autoformalization Pipeline

The paper proposes an autoformalization pipeline based on large language models with error feedback, achieving a fully automatic and training-free formalization approach.

The official implementation and dataset are available on GitHub at https://github.com/liuchengwucn/Safe, and the paper was published as part of ACL 2025 Main Conference proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91945e2e-ae47-43e1-bcb0-43648a6d75ba",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "24d30014-985d-49b7-a5df-a2be113c4239",
  "toolUseResult": {
    "query": "Safe Liu ACL 2025 step-aware formal verification Lean 4 cost overhead autoformalization",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SzdCmvUqDr8G67WewpAuec",
        "content": [
          {
            "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.594/"
          },
          {
            "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification | Request PDF",
            "url": "https://www.researchgate.net/publication/394301322_Safe_Enhancing_Mathematical_Reasoning_in_Large_Language_Models_via_Retrospective_Step-aware_Formal_Verification"
          },
          {
            "title": "Towards a Common Framework for Autoformalization",
            "url": "https://arxiv.org/pdf/2509.09810"
          },
          {
            "title": "GitHub - liuchengwucn/Safe: (ACL 2025 Main) Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - Official Implementation & Dataset",
            "url": "https://github.com/liuchengwucn/Safe"
          },
          {
            "title": "(PDF) Process-Driven Autoformalization in Lean 4",
            "url": "https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4"
          },
          {
            "title": "[2506.04592] Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification",
            "url": "https://arxiv.org/abs/2506.04592"
          },
          {
            "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification",
            "url": "https://arxiv.org/pdf/2506.04592"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/pdf/2406.01940"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're asking about:\n\n## Overview\n\nSafe is a retrospective, step-aware formal verification framework that articulates mathematical claims in formal mathematical language Lean 4 at each reasoning step and provides formal proofs to identify hallucinations.\n\n## Key Contributions\n\nThis represents the first endeavor to utilize formal mathematical language Lean 4 for verifying natural language content generated by LLMs. The paper proposes FormalStep as a benchmark for step correctness theorem proving with 30,809 formal statements.\n\n## Framework and Approach\n\nThe work draws inspiration from the idea that \"the gold standard for supporting a mathematical claim is to provide a proof\". Rather than using opaque methods like process reward models, the framework demonstrates significant performance improvement while offering interpretable and verifiable evidence across multiple language models and various mathematical datasets.\n\n## Autoformalization Pipeline\n\nThe paper proposes an autoformalization pipeline based on large language models with error feedback, achieving a fully automatic and training-free formalization approach.\n\nThe official implementation and dataset are available on GitHub at https://github.com/liuchengwucn/Safe, and the paper was published as part of ACL 2025 Main Conference proceedings."
    ],
    "durationSeconds": 11.163535360999987,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "91945e2e-ae47-43e1-bcb0-43648a6d75ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T13:01:07.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013exdPKThnqNnRGu6nGCRDc`</summary>

```json
{
  "query": "VERGE formal refinement guidance engine verifiable LLM reasoning Singh 2026 SMT solver routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24d30014-985d-49b7-a5df-a2be113c4239",
  "isSidechain": false,
  "requestId": "req_011CbT7iMaw5XhKx9pbnijkS",
  "type": "assistant",
  "uuid": "66ae96c2-a087-4d47-8e83-09fd886bed80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVXH2sHDnWU1ayx8kZ3QRv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 26098,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 26098,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 833
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

_source line 33 · 2026-05-27T13:01:24.613Z_

<details><summary>↩ Tool result · `toolu_013exdPKThnqNnRGu6nGCRDc`</summary>

```text
Web search results for query: "VERGE formal refinement guidance engine verifiable LLM reasoning Singh 2026 SMT solver routing"

Links: [{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News","url":"https://news.ycombinator.com/item?id=46813257"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable ...","url":"https://ubos.tech/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning-2/"},{"title":"llm formal method | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/search?highlight=1&query=LLM+formal+method&sort=0"},{"title":"From Implicit Exploration to Structured Reasoning: Leveraging Guideline and Refinement for LLMs","url":"https://arxiv.org/pdf/2509.06284"},{"title":"Formal Refinement and Guidance Engine for Verifiable ...","url":"https://www.researchgate.net/publication/400178327_VERGE_Formal_Refinement_and_Guidance_Engine_for_Verifiable_LLM_Reasoning"}]

Based on the search results, I found detailed information about VERGE:

## VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning

VERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. The paper was authored by Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, and Sam Bayless in 2026.

### Key Components and Innovations

The approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving.

The framework introduces three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, (2) semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS).

### Purpose and Context

The work addresses the challenge that despite the syntactic fluency of Large Language Models, ensuring their logical correctness in high-stakes domains remains a fundamental challenge.

The paper is available on arXiv (2601.20055) and was updated in May 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66ae96c2-a087-4d47-8e83-09fd886bed80",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "25f31864-658b-4885-bd0e-78358d0ba4ee",
  "toolUseResult": {
    "query": "VERGE formal refinement guidance engine verifiable LLM reasoning Singh 2026 SMT solver routing",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DHsDe8EDq25zpqLqsN7hrF",
        "content": [
          {
            "title": "[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/abs/2601.20055"
          },
          {
            "title": "[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"
          },
          {
            "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/html/2601.20055"
          },
          {
            "title": "dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.",
            "url": "https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"
          },
          {
            "title": "Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://huggingface.co/papers/2601.20055"
          },
          {
            "title": "Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News",
            "url": "https://news.ycombinator.com/item?id=46813257"
          },
          {
            "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable ...",
            "url": "https://ubos.tech/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning-2/"
          },
          {
            "title": "llm formal method | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/search?highlight=1&query=LLM+formal+method&sort=0"
          },
          {
            "title": "From Implicit Exploration to Structured Reasoning: Leveraging Guideline and Refinement for LLMs",
            "url": "https://arxiv.org/pdf/2509.06284"
          },
          {
            "title": "Formal Refinement and Guidance Engine for Verifiable ...",
            "url": "https://www.researchgate.net/publication/400178327_VERGE_Formal_Refinement_and_Guidance_Engine_for_Verifiable_LLM_Reasoning"
          }
        ]
      },
      "Based on the search results, I found detailed information about VERGE:\n\n## VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning\n\nVERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. The paper was authored by Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, and Sam Bayless in 2026.\n\n### Key Components and Innovations\n\nThe approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving.\n\nThe framework introduces three key innovations: (1) multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, (2) semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning, and (3) precise logical error localization via Minimal Correction Subsets (MCS).\n\n### Purpose and Context\n\nThe work addresses the challenge that despite the syntactic fluency of Large Language Models, ensuring their logical correctness in high-stakes domains remains a fundamental challenge.\n\nThe paper is available on arXiv (2601.20055) and was updated in May 2026."
    ],
    "durationSeconds": 17.159565778999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "66ae96c2-a087-4d47-8e83-09fd886bed80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we achieve near-formal-verification reliability for natural language mathematical proof che…",
  "leafUuid": "25f31864-658b-4885-bd0e-78358d0ba4ee",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective formal verification via uncertainty and dependency routing",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Tool call

_source line 36 · 2026-05-27T13:01:27.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01258xERMsr7PckP3CaGBYFk`</summary>

```json
{
  "query": "ProofFlow dependency graph autoformalization proof 2025 ProofSketcher typed proof sketch 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25f31864-658b-4885-bd0e-78358d0ba4ee",
  "isSidechain": false,
  "requestId": "req_011CbT7juhzbDCdCrAzCJoGu",
  "type": "assistant",
  "uuid": "52c5575d-2e71-4170-a7c9-2c7d10b1f312",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012B7PQBrjtk54mnX85mEJky",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 26931,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 26931,
          "cache_creation_input_tokens": 993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 993
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

_source line 37 · 2026-05-27T13:01:42.853Z_

<details><summary>↩ Tool result · `toolu_01258xERMsr7PckP3CaGBYFk`</summary>

```text
Web search results for query: "ProofFlow dependency graph autoformalization proof 2025 ProofSketcher typed proof sketch 2026"

Links: [{"title":"[2510.15981] ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/abs/2510.15981"},{"title":"GitHub - Huawei-AI4Math/ProofFlow · GitHub","url":"https://github.com/Huawei-AI4Math/ProofFlow"},{"title":"(PDF) ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://www.researchgate.net/publication/396716261_ProofFlow_A_Dependency_Graph_Approach_to_Faithful_Proof_Autoformalization"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/html/2510.15981v1"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/pdf/2510.15981"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization | OpenReview","url":"https://openreview.net/forum?id=s9t2FJVsBH"},{"title":"PROOFFLOW:ADEPENDENCY GRAPH APPROACH TO ...","url":"https://openreview.net/pdf?id=s9t2FJVsBH"},{"title":"ProofFlow - ICLR 2026 video presentation - YouTube","url":"https://www.youtube.com/watch?v=EVJIO2XmOz8"}]

Links: [{"title":"ProofSketcher: Hybrid LLM + Lightweight Proof Checker for Reliable Math/Logic Reasoning","url":"https://arxiv.org/html/2604.06401"},{"title":"ProofSketcher: Hybrid LLM + Lightweight Proof Checker for Reliable Math/Logic Reasoning","url":"https://arxiv.org/pdf/2604.06401"},{"title":"ProofSketch: Efficient Verified Reasoning for Large Language Models","url":"https://arxiv.org/pdf/2510.24811"},{"title":"Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs | OpenReview","url":"https://openreview.net/forum?id=SMa9EAovKMC"},{"title":"Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal   Proofs","url":"https://arxiv.org/pdf/2210.12283"}]

Based on the search results, here's what I found:

## ProofFlow (2025)

ProofFlow is a novel pipeline that treats structural fidelity as a primary objective by constructing a directed acyclic graph (DAG) to map the logical dependencies between proof steps. It automatically converts natural language (NL) proofs into machine-verifiable code like Lean 4.

The pipeline achieves state-of-the-art autoformalization with a ProofScore of 0.545, substantially exceeding baselines like full-proof formalization (0.123) and step-proof formalization (0.072). ProofFlow is a Python package that translates NL proofs into verifiable Lean 4 code by first constructing a dependency graph to map the proof's logical flow.

The work was presented at ICLR 2026.

## ProofSketcher (2026)

ProofSketcher is a hybrid design where the LLM writes a typed proof sketch rather than a full formal proof, with the sketch being a structured plan with explicit step types (rewrite, case split, induction, contradiction) and typed holes. A lightweight kernel expands each sketch node into concrete proof obligations that are discharged by a small set of trusted inference rules or external tools that must return a proof certificate that a small checker can validate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52c5575d-2e71-4170-a7c9-2c7d10b1f312",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "a60966a7-fd1b-4376-8abe-99a53d243b9e",
  "toolUseResult": {
    "query": "ProofFlow dependency graph autoformalization proof 2025 ProofSketcher typed proof sketch 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Voi61W4uB9pgtxWBeUotFP",
        "content": [
          {
            "title": "[2510.15981] ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://arxiv.org/abs/2510.15981"
          },
          {
            "title": "GitHub - Huawei-AI4Math/ProofFlow · GitHub",
            "url": "https://github.com/Huawei-AI4Math/ProofFlow"
          },
          {
            "title": "(PDF) ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://www.researchgate.net/publication/396716261_ProofFlow_A_Dependency_Graph_Approach_to_Faithful_Proof_Autoformalization"
          },
          {
            "title": "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://arxiv.org/html/2510.15981v1"
          },
          {
            "title": "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://arxiv.org/pdf/2510.15981"
          },
          {
            "title": "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization | OpenReview",
            "url": "https://openreview.net/forum?id=s9t2FJVsBH"
          },
          {
            "title": "PROOFFLOW:ADEPENDENCY GRAPH APPROACH TO ...",
            "url": "https://openreview.net/pdf?id=s9t2FJVsBH"
          },
          {
            "title": "ProofFlow - ICLR 2026 video presentation - YouTube",
            "url": "https://www.youtube.com/watch?v=EVJIO2XmOz8"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01X4qxaN4NPWoWXPVoLQkceW",
        "content": [
          {
            "title": "ProofSketcher: Hybrid LLM + Lightweight Proof Checker for Reliable Math/Logic Reasoning",
            "url": "https://arxiv.org/html/2604.06401"
          },
          {
            "title": "ProofSketcher: Hybrid LLM + Lightweight Proof Checker for Reliable Math/Logic Reasoning",
            "url": "https://arxiv.org/pdf/2604.06401"
          },
          {
            "title": "ProofSketch: Efficient Verified Reasoning for Large Language Models",
            "url": "https://arxiv.org/pdf/2510.24811"
          },
          {
            "title": "Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs | OpenReview",
            "url": "https://openreview.net/forum?id=SMa9EAovKMC"
          },
          {
            "title": "Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal   Proofs",
            "url": "https://arxiv.org/pdf/2210.12283"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\n## ProofFlow (2025)\n\nProofFlow is a novel pipeline that treats structural fidelity as a primary objective by constructing a directed acyclic graph (DAG) to map the logical dependencies between proof steps. It automatically converts natural language (NL) proofs into machine-verifiable code like Lean 4.\n\nThe pipeline achieves state-of-the-art autoformalization with a ProofScore of 0.545, substantially exceeding baselines like full-proof formalization (0.123) and step-proof formalization (0.072). ProofFlow is a Python package that translates NL proofs into verifiable Lean 4 code by first constructing a dependency graph to map the proof's logical flow.\n\nThe work was presented at ICLR 2026.\n\n## ProofSketcher (2026)\n\nProofSketcher is a hybrid design where the LLM writes a typed proof sketch rather than a full formal proof, with the sketch being a structured plan with explicit step types (rewrite, case split, induction, contradiction) and typed holes. A lightweight kernel expands each sketch node into concrete proof obligations that are discharged by a small set of trusted inference rules or external tools that must return a proof certificate that a small checker can validate."
    ],
    "durationSeconds": 15.441765102000005,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "52c5575d-2e71-4170-a7c9-2c7d10b1f312",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-27T13:01:48.728Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011NxbZ51UmSiDiU5YtURK9B`</summary>

```json
{
  "query": "\"Do We Need Frontier Models to Verify Mathematical Proofs\" arXiv 2604.02450 prompt ensemble verification 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a60966a7-fd1b-4376-8abe-99a53d243b9e",
  "isSidechain": false,
  "requestId": "req_011CbT7mFiYHaUxQKjUAZsjY",
  "type": "assistant",
  "uuid": "c21c8988-e0f8-4b76-9f8e-d4abde3cdda0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017efRNC63F4tNMc2ttt4w39",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 27924,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1059,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 27924,
          "cache_creation_input_tokens": 1059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1059
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

_source line 39 · 2026-05-27T13:02:04.189Z_

<details><summary>↩ Tool result · `toolu_011NxbZ51UmSiDiU5YtURK9B`</summary>

```text
Web search results for query: ""Do We Need Frontier Models to Verify Mathematical Proofs" arXiv 2604.02450 prompt ensemble verification 2026"

Links: [{"title":"[2604.02450] Do We Need Frontier Models to Verify Mathematical Proofs?","url":"https://arxiv.org/abs/2604.02450"},{"title":"[2604.02450v1] Do We Need Frontier Models to Verify Mathematical Proofs?","url":"https://arxiv.org/abs/2604.02450v1"},{"title":"Do We Need Frontier Models to Verify Mathematical Proofs?","url":"https://arxiv.org/html/2604.02450v1"},{"title":"Do We Need Frontier Models to Verify Mathematical Proofs?","url":"https://arxiv.org/pdf/2604.02450"},{"title":"Automated Conjecture Resolution with Formal Verification","url":"https://arxiv.org/html/2604.03789v1"}]

Based on the search results, I found the paper you're looking for. Here's what it covers:

The paper "Do We Need Frontier Models to Verify Mathematical Proofs?" is by Aaditya Naik, Guruprerana Shabadi, Rajeev Alur, and Mayur Naik from the University of Pennsylvania.

**Key Findings:**

The authors systematically evaluated four open-source and two frontier LLMs on datasets of human-graded natural language proofs of competition-level problems, using two key metrics: verifier accuracy and self-consistency.

They observed that smaller open-source models are only up to ~10% behind frontier models in accuracy but they are up to ~25% more inconsistent.

**Main Result with Prompt Ensemble Verification:**

The paper demonstrates that smaller models possess the mathematical capabilities to verify proofs at the level of frontier models, but struggle to reliably elicit these capabilities with general judging prompts. Through an LLM-guided prompt search, they synthesized an ensemble of specialized prompts that overcome the specific failure modes of smaller models, boosting their performance by up to 9.1% in accuracy and 15.9% in self-consistency.

These gains allow models like Qwen3.5-35B to perform on par with frontier models such as Gemini 3.1 Pro for proof verification.

The paper was submitted to arXiv on April 2, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c21c8988-e0f8-4b76-9f8e-d4abde3cdda0",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "6d86debc-23a7-4f06-8bd8-695fec72b1fe",
  "toolUseResult": {
    "query": "\"Do We Need Frontier Models to Verify Mathematical Proofs\" arXiv 2604.02450 prompt ensemble verification 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HPwLfM26v6mmfwV1ANHa7Z",
        "content": [
          {
            "title": "[2604.02450] Do We Need Frontier Models to Verify Mathematical Proofs?",
            "url": "https://arxiv.org/abs/2604.02450"
          },
          {
            "title": "[2604.02450v1] Do We Need Frontier Models to Verify Mathematical Proofs?",
            "url": "https://arxiv.org/abs/2604.02450v1"
          },
          {
            "title": "Do We Need Frontier Models to Verify Mathematical Proofs?",
            "url": "https://arxiv.org/html/2604.02450v1"
          },
          {
            "title": "Do We Need Frontier Models to Verify Mathematical Proofs?",
            "url": "https://arxiv.org/pdf/2604.02450"
          },
          {
            "title": "Automated Conjecture Resolution with Formal Verification",
            "url": "https://arxiv.org/html/2604.03789v1"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what it covers:\n\nThe paper \"Do We Need Frontier Models to Verify Mathematical Proofs?\" is by Aaditya Naik, Guruprerana Shabadi, Rajeev Alur, and Mayur Naik from the University of Pennsylvania.\n\n**Key Findings:**\n\nThe authors systematically evaluated four open-source and two frontier LLMs on datasets of human-graded natural language proofs of competition-level problems, using two key metrics: verifier accuracy and self-consistency.\n\nThey observed that smaller open-source models are only up to ~10% behind frontier models in accuracy but they are up to ~25% more inconsistent.\n\n**Main Result with Prompt Ensemble Verification:**\n\nThe paper demonstrates that smaller models possess the mathematical capabilities to verify proofs at the level of frontier models, but struggle to reliably elicit these capabilities with general judging prompts. Through an LLM-guided prompt search, they synthesized an ensemble of specialized prompts that overcome the specific failure modes of smaller models, boosting their performance by up to 9.1% in accuracy and 15.9% in self-consistency.\n\nThese gains allow models like Qwen3.5-35B to perform on par with frontier models such as Gemini 3.1 Pro for proof verification.\n\nThe paper was submitted to arXiv on April 2, 2026."
    ],
    "durationSeconds": 15.456236594999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c21c8988-e0f8-4b76-9f8e-d4abde3cdda0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-27T13:02:08.677Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F3GK4FCWv4XjHc3jNSTDLU`</summary>

```json
{
  "query": "ensemble disagreement uncertainty calibration LLM verification routing selective compute allocation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d86debc-23a7-4f06-8bd8-695fec72b1fe",
  "isSidechain": false,
  "requestId": "req_011CbT7npwas28Gv2ekfg19Z",
  "type": "assistant",
  "uuid": "588224b8-7df0-4546-9b95-3fadb8640ace",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pxf7dm2Sovoh2r89SrKG5p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 28983,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 28983,
          "cache_creation_input_tokens": 677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 677
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

_source line 41 · 2026-05-27T13:02:22.138Z_

<details><summary>↩ Tool result · `toolu_01F3GK4FCWv4XjHc3jNSTDLU`</summary>

```text
Web search results for query: "ensemble disagreement uncertainty calibration LLM verification routing selective compute allocation 2025 2026"

Links: [{"title":"Similarity-Distance-Magnitude Universal Verification","url":"https://arxiv.org/pdf/2502.20167"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"},{"title":"Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification","url":"https://arxiv.org/html/2604.17112v1"},{"title":"RACER: Risk-Aware Calibrated Efficient Routing for Large Language Models","url":"https://arxiv.org/pdf/2603.06616"},{"title":"DiscoUQ: Structured Disagreement Analysis for Uncertainty Quantification in LLM Agent Ensembles","url":"https://arxiv.org/pdf/2603.20975"}]

I found several highly relevant research papers from 2025-2026 on your search topics. Here are the key results:

**Calibration and Uncertainty Estimation in LLMs:**

Uncertainty estimates from calibrated approaches are well-suited for selective classification and conditional branching for additional test-time compute based on predictive uncertainty, including selective LLM generation, routing, and composition over multiple models and retrieval.

Calibrated LLM judges enable systems to route straightforward cases to efficient models while reserving expensive judges or human reviewers for uncertain decisions, dramatically reducing computational and labor costs.

**Ensemble Disagreement for Uncertainty Quantification:**

Recent work capitalizes on the ecosystem of open-weight LLMs by sampling responses from a small, scale-matched ensemble to estimate epistemic uncertainty directly from cross-model semantic disagreement, without additional training.

The DISCOUQ framework extracts and leverages the structure of interagent disagreement—including linguistic properties like evidence overlap and argument strength, and embedding geometry like cluster distances and dispersion—to produce well-calibrated confidence estimates.

**LLM Routing and Selective Compute:**

Recent research has proposed LLM routers to predict the most suitable candidate for each query by training a lightweight model, without calling all LLMs.

These papers demonstrate active development in ensemble-based uncertainty quantification, routing mechanisms, and efficient compute allocation for LLMs in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "588224b8-7df0-4546-9b95-3fadb8640ace",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "f6528757-6120-4489-935a-1f9431ca7317",
  "toolUseResult": {
    "query": "ensemble disagreement uncertainty calibration LLM verification routing selective compute allocation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014JiSLtHuUtiXwkZbs5A6nq",
        "content": [
          {
            "title": "Similarity-Distance-Magnitude Universal Verification",
            "url": "https://arxiv.org/pdf/2502.20167"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/pdf/2512.22245"
          },
          {
            "title": "Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification",
            "url": "https://arxiv.org/html/2604.17112v1"
          },
          {
            "title": "RACER: Risk-Aware Calibrated Efficient Routing for Large Language Models",
            "url": "https://arxiv.org/pdf/2603.06616"
          },
          {
            "title": "DiscoUQ: Structured Disagreement Analysis for Uncertainty Quantification in LLM Agent Ensembles",
            "url": "https://arxiv.org/pdf/2603.20975"
          }
        ]
      },
      "I found several highly relevant research papers from 2025-2026 on your search topics. Here are the key results:\n\n**Calibration and Uncertainty Estimation in LLMs:**\n\nUncertainty estimates from calibrated approaches are well-suited for selective classification and conditional branching for additional test-time compute based on predictive uncertainty, including selective LLM generation, routing, and composition over multiple models and retrieval.\n\nCalibrated LLM judges enable systems to route straightforward cases to efficient models while reserving expensive judges or human reviewers for uncertain decisions, dramatically reducing computational and labor costs.\n\n**Ensemble Disagreement for Uncertainty Quantification:**\n\nRecent work capitalizes on the ecosystem of open-weight LLMs by sampling responses from a small, scale-matched ensemble to estimate epistemic uncertainty directly from cross-model semantic disagreement, without additional training.\n\nThe DISCOUQ framework extracts and leverages the structure of interagent disagreement—including linguistic properties like evidence overlap and argument strength, and embedding geometry like cluster distances and dispersion—to produce well-calibrated confidence estimates.\n\n**LLM Routing and Selective Compute:**\n\nRecent research has proposed LLM routers to predict the most suitable candidate for each query by training a lightweight model, without calling all LLMs.\n\nThese papers demonstrate active development in ensemble-based uncertainty quantification, routing mechanisms, and efficient compute allocation for LLMs in 2025-2026."
    ],
    "durationSeconds": 13.45585230900001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "588224b8-7df0-4546-9b95-3fadb8640ace",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-27T13:02:26.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H6FCxdggirJcusmXra6snD`</summary>

```json
{
  "query": "Goedel-Prover-V2 StepFun-Formalizer-32B autoformalization statement level 2026 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6528757-6120-4489-935a-1f9431ca7317",
  "isSidechain": false,
  "requestId": "req_011CbT7p9gz5aXMT73hCP5rk",
  "type": "assistant",
  "uuid": "dc3b6d66-eb47-4525-a73c-ab83215d1bfd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwYmzRTdS9rymDVSpUpEx4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 655,
      "cache_read_input_tokens": 29660,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 29660,
          "cache_creation_input_tokens": 655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 655
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

_source line 43 · 2026-05-27T13:02:33.885Z_

<details><summary>↩ Tool result · `toolu_01H6FCxdggirJcusmXra6snD`</summary>

```text
Web search results for query: "Goedel-Prover-V2 StepFun-Formalizer-32B autoformalization statement level 2026 ICLR"

Links: [{"title":"[2508.04440] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/abs/2508.04440"},{"title":"arXiv preprint AUTOFORMALIZER WITH TOOL FEEDBACK","url":"https://arxiv.org/pdf/2510.06857"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"},{"title":"StepFun-Formalizer-32B: Autoformalization LLM","url":"https://www.emergentmind.com/topics/stepfun-formalizer-32b"},{"title":"stepfun-ai/StepFun-Formalizer-32B · Hugging Face","url":"https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B"},{"title":"GitHub - Goedel-LM/Goedel-Prover-V2 · GitHub","url":"https://github.com/Goedel-LM/Goedel-Prover-V2"},{"title":"ICLR Poster Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction","url":"https://iclr.cc/virtual/2026/poster/10007912"},{"title":"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction","url":"https://arxiv.org/pdf/2508.03613"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/html/2510.06857v1"}]

Based on the search results, here's what I found about these models and their recent developments:

## StepFun-Formalizer-32B

StepFun-Formalizer is a family of large language models designed to translate natural-language mathematical problems into formal statements in Lean 4. StepFun-Formalizer-32B achieves state-of-the-art BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench, surpassing all prior general-purpose and specialized models.

The model addresses two key abilities for effective autoformalization: comprehensive mastery of formal-language domain knowledge, and reasoning capability of natural language problem understanding and informal-formal alignment.

## Goedel-Prover-V2

Goedel-Prover-V2-32B achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in self-correction mode, outperforming prior SOTA by a large margin. Additionally, the flagship model solves 86 problems on PutnamBench at pass@184, securing the first place among open-source models on the leaderboard.

## 2026 ICLR Connection

These results were presented at ICLR 2026, with the Goedel-Prover-V2 paper appearing as a poster presentation.

Both models represent significant advances in formal mathematics and automated theorem proving, with the StepFun-Formalizer focusing on autoformalization (converting natural language to formal statements) and Goedel-Prover-V2 specializing in formal theorem proving.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc3b6d66-eb47-4525-a73c-ab83215d1bfd",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "8edec948-64c9-4c32-8a60-0dd555bd91a6",
  "toolUseResult": {
    "query": "Goedel-Prover-V2 StepFun-Formalizer-32B autoformalization statement level 2026 ICLR",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CJ7bnnK2zKHvpSmP8JygnF",
        "content": [
          {
            "title": "[2508.04440] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/abs/2508.04440"
          },
          {
            "title": "arXiv preprint AUTOFORMALIZER WITH TOOL FEEDBACK",
            "url": "https://arxiv.org/pdf/2510.06857"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential",
            "url": "https://www.arxiv.org/pdf/2508.04440"
          },
          {
            "title": "StepFun-Formalizer-32B: Autoformalization LLM",
            "url": "https://www.emergentmind.com/topics/stepfun-formalizer-32b"
          },
          {
            "title": "stepfun-ai/StepFun-Formalizer-32B · Hugging Face",
            "url": "https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B"
          },
          {
            "title": "GitHub - Goedel-LM/Goedel-Prover-V2 · GitHub",
            "url": "https://github.com/Goedel-LM/Goedel-Prover-V2"
          },
          {
            "title": "ICLR Poster Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction",
            "url": "https://iclr.cc/virtual/2026/poster/10007912"
          },
          {
            "title": "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction",
            "url": "https://arxiv.org/pdf/2508.03613"
          },
          {
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/html/2510.06857v1"
          }
        ]
      },
      "Based on the search results, here's what I found about these models and their recent developments:\n\n## StepFun-Formalizer-32B\n\nStepFun-Formalizer is a family of large language models designed to translate natural-language mathematical problems into formal statements in Lean 4. StepFun-Formalizer-32B achieves state-of-the-art BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench, surpassing all prior general-purpose and specialized models.\n\nThe model addresses two key abilities for effective autoformalization: comprehensive mastery of formal-language domain knowledge, and reasoning capability of natural language problem understanding and informal-formal alignment.\n\n## Goedel-Prover-V2\n\nGoedel-Prover-V2-32B achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in self-correction mode, outperforming prior SOTA by a large margin. Additionally, the flagship model solves 86 problems on PutnamBench at pass@184, securing the first place among open-source models on the leaderboard.\n\n## 2026 ICLR Connection\n\nThese results were presented at ICLR 2026, with the Goedel-Prover-V2 paper appearing as a poster presentation.\n\nBoth models represent significant advances in formal mathematics and automated theorem proving, with the StepFun-Formalizer focusing on autoformalization (converting natural language to formal statements) and Goedel-Prover-V2 specializing in formal theorem proving."
    ],
    "durationSeconds": 7.643397984000011,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dc3b6d66-eb47-4525-a73c-ab83215d1bfd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-27T13:02:37.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UKoaeC4xWeA9s2HBFxFv43`</summary>

```json
{
  "query": "dependency graph criticality routing verification fan-out dominator betweenness centrality proof structure 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8edec948-64c9-4c32-8a60-0dd555bd91a6",
  "isSidechain": false,
  "requestId": "req_011CbT7q1uSsHHkwX92UfD7o",
  "type": "assistant",
  "uuid": "88aca376-8540-43a8-9a81-e1370ccf0691",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E6bpDvaodCQQ5PXqQpW2Dd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1008,
      "cache_read_input_tokens": 30315,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1008,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 30315,
          "cache_creation_input_tokens": 1008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1008
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

_source line 45 · 2026-05-27T13:02:46.298Z_

<details><summary>↩ Tool result · `toolu_01UKoaeC4xWeA9s2HBFxFv43`</summary>

```text
Web search results for query: "dependency graph criticality routing verification fan-out dominator betweenness centrality proof structure 2025 2026"

Links: [{"title":"(PDF) Using Centrality Measures in Dependency Risk Graphs for Efficient Risk Mitigation","url":"https://www.academia.edu/44221329/Using_Centrality_Measures_in_Dependency_Risk_Graphs_for_Efficient_Risk_Mitigation"},{"title":"Structure of betweenness uniform graphs with low values of betweenness   centrality","url":"https://arxiv.org/pdf/2401.00347"},{"title":"Graph centrality analysis of feature dependencies to unveil ...","url":"https://www.cad-journal.net/files/vol_15/CAD_15(5)_2018_684-696.pdf"},{"title":"Parallel Verification of Natural Deduction Proof Graphs","url":"https://arxiv.org/pdf/2311.10440"},{"title":"Betweenness Centrality : Algorithms and Lower Bounds","url":"https://arxiv.org/pdf/0809.1906"},{"title":"Active Betweenness Cardinality: Algorithms and Applications","url":"https://arxiv.org/pdf/1711.10634"},{"title":"Hierarchical Decomposition for Betweenness Centrality Measure of Complex Networks","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5397849/"},{"title":"Visualization system to identify structurally vulnerable links in OHT railway network in semiconductor FAB using betweenness centrality","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11244790/"}]

I've completed a web search for your query about dependency graph criticality routing verification with fan-out, dominator, betweenness centrality, and proof structures. Here are the relevant results:

The search returned several academic papers and resources related to these topics:

1. **Betweenness Centrality in Dependency Analysis**: Betweenness centrality of a node measures the number of shortest paths the node is involved with, serving as a measure of the importance of the node in the network.

2. **Centrality Measures for Critical Network Elements**: Centrality metrics such as closeness centrality, graph centrality, stress centrality and betweenness centrality are used to measure the importance of network elements (nodes or edges). Brandes showed that betweenness centrality can be computed in the same asymptotic time bounds as n Single Source Shortest Path (SSSP) computations.

3. **Practical Applications**: Betweenness centrality has been employed to evaluate the structural vulnerability of networks, and has been widely recognized for its effectiveness in identifying critical points within a network in graph theory.

4. **Proof Structures and Verification**: Directed acyclic hypergraphical representations where nodes hold statements and hyperedges represent inference rules provide a method of comparing the performance of different verification strategies on various proof structures.

The search results contain academic resources from arXiv, scholarly databases, and peer-reviewed publications, though I didn't find results specifically focused on 2025-2026 publications on these exact combined topics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88aca376-8540-43a8-9a81-e1370ccf0691",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "ecfdeb26-280e-4306-a0c6-da859cf32436",
  "toolUseResult": {
    "query": "dependency graph criticality routing verification fan-out dominator betweenness centrality proof structure 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012a3sdkWyUewzN7JwJM49T2",
        "content": [
          {
            "title": "(PDF) Using Centrality Measures in Dependency Risk Graphs for Efficient Risk Mitigation",
            "url": "https://www.academia.edu/44221329/Using_Centrality_Measures_in_Dependency_Risk_Graphs_for_Efficient_Risk_Mitigation"
          },
          {
            "title": "Structure of betweenness uniform graphs with low values of betweenness   centrality",
            "url": "https://arxiv.org/pdf/2401.00347"
          },
          {
            "title": "Graph centrality analysis of feature dependencies to unveil ...",
            "url": "https://www.cad-journal.net/files/vol_15/CAD_15(5)_2018_684-696.pdf"
          },
          {
            "title": "Parallel Verification of Natural Deduction Proof Graphs",
            "url": "https://arxiv.org/pdf/2311.10440"
          },
          {
            "title": "Betweenness Centrality : Algorithms and Lower Bounds",
            "url": "https://arxiv.org/pdf/0809.1906"
          },
          {
            "title": "Active Betweenness Cardinality: Algorithms and Applications",
            "url": "https://arxiv.org/pdf/1711.10634"
          },
          {
            "title": "Hierarchical Decomposition for Betweenness Centrality Measure of Complex Networks",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5397849/"
          },
          {
            "title": "Visualization system to identify structurally vulnerable links in OHT railway network in semiconductor FAB using betweenness centrality",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11244790/"
          }
        ]
      },
      "I've completed a web search for your query about dependency graph criticality routing verification with fan-out, dominator, betweenness centrality, and proof structures. Here are the relevant results:\n\nThe search returned several academic papers and resources related to these topics:\n\n1. **Betweenness Centrality in Dependency Analysis**: Betweenness centrality of a node measures the number of shortest paths the node is involved with, serving as a measure of the importance of the node in the network.\n\n2. **Centrality Measures for Critical Network Elements**: Centrality metrics such as closeness centrality, graph centrality, stress centrality and betweenness centrality are used to measure the importance of network elements (nodes or edges). Brandes showed that betweenness centrality can be computed in the same asymptotic time bounds as n Single Source Shortest Path (SSSP) computations.\n\n3. **Practical Applications**: Betweenness centrality has been employed to evaluate the structural vulnerability of networks, and has been widely recognized for its effectiveness in identifying critical points within a network in graph theory.\n\n4. **Proof Structures and Verification**: Directed acyclic hypergraphical representations where nodes hold statements and hyperedges represent inference rules provide a method of comparing the performance of different verification strategies on various proof structures.\n\nThe search results contain academic resources from arXiv, scholarly databases, and peer-reviewed publications, though I didn't find results specifically focused on 2025-2026 publications on these exact combined topics."
    ],
    "durationSeconds": 8.334385756000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "88aca376-8540-43a8-9a81-e1370ccf0691",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we achieve near-formal-verification reliability for natural language mathematical proof che…",
  "leafUuid": "ecfdeb26-280e-4306-a0c6-da859cf32436",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective formal verification via uncertainty and dependency routing",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Assistant

_source line 48 · 2026-05-27T13:02:51.323Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more targeted search to understand if there's any work that combines dependency-graph structure with uncertainty-based routing for formal verification specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecfdeb26-280e-4306-a0c6-da859cf32436",
  "isSidechain": false,
  "requestId": "req_011CbT7qvzYkGdeUWZFAqLDx",
  "type": "assistant",
  "uuid": "17cf6463-e944-4b09-a50b-5a499d3d3ace",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LK3UbW1EEDM2JY25b21d5q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 31323,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 31323,
          "cache_creation_input_tokens": 864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 864
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

_source line 49 · 2026-05-27T13:02:52.040Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CmUgF7zqcp2VHgejcD4f1a`</summary>

```json
{
  "query": "UCCI calibrated uncertainty cost-optimal LLM cascade routing 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17cf6463-e944-4b09-a50b-5a499d3d3ace",
  "isSidechain": false,
  "requestId": "req_011CbT7qvzYkGdeUWZFAqLDx",
  "type": "assistant",
  "uuid": "04f5f762-78a6-4294-be62-bf04d2089e00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LK3UbW1EEDM2JY25b21d5q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 31323,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 31323,
          "cache_creation_input_tokens": 864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 864
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

_source line 50 · 2026-05-27T13:03:00.366Z_

<details><summary>↩ Tool result · `toolu_01CmUgF7zqcp2VHgejcD4f1a`</summary>

```text
Web search results for query: "UCCI calibrated uncertainty cost-optimal LLM cascade routing 2026 arXiv"

Links: [{"title":"[2605.18796] UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing","url":"https://arxiv.org/abs/2605.18796"},{"title":"UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing","url":"https://arxiv.org/html/2605.18796"},{"title":"A Unified Approach to Routing and Cascading for LLMs","url":"https://arxiv.org/pdf/2410.10347"},{"title":"Leveraging Uncertainty Estimation for Efficient LLM Routing","url":"https://arxiv.org/pdf/2502.11021"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.09902"},{"title":"Routing, Cascades, and User Choice for LLMs","url":"https://arxiv.org/html/2602.09902"},{"title":"[2603.04445] Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey","url":"https://arxiv.org/abs/2603.04445"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing

**Author:** Varun Kotte

**Submission Date:** Submitted on 11 May 2026

**arXiv ID:** 2605.18796

**Summary:** UCCI is a calibration-first router that maps token-level margin uncertainty to a per-query error probability via isotonic regression and selects the escalation threshold by constrained cost minimization. LLM cascades and model routing promise lower inference cost by sending easy queries to a small model and escalating hard ones to a large model, but most deployed routers use uncalibrated confidence scores and require per-workload threshold tuning.

**Technical Contribution:** Under three explicit assumptions, threshold policies on the calibrated score are cost-optimal, and isotonic calibration achieves O(n^{-1/3}) sample complexity for expected calibration error (ECE).

The paper is available on arXiv at: https://arxiv.org/abs/2605.18796


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04f5f762-78a6-4294-be62-bf04d2089e00",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "39570ce3-6710-4d83-bb88-8a0ed5d9778a",
  "toolUseResult": {
    "query": "UCCI calibrated uncertainty cost-optimal LLM cascade routing 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BmuCYCiJMvAjVpMVewxpPC",
        "content": [
          {
            "title": "[2605.18796] UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing",
            "url": "https://arxiv.org/abs/2605.18796"
          },
          {
            "title": "UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing",
            "url": "https://arxiv.org/html/2605.18796"
          },
          {
            "title": "A Unified Approach to Routing and Cascading for LLMs",
            "url": "https://arxiv.org/pdf/2410.10347"
          },
          {
            "title": "Leveraging Uncertainty Estimation for Efficient LLM Routing",
            "url": "https://arxiv.org/pdf/2502.11021"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2602.09902"
          },
          {
            "title": "Routing, Cascades, and User Choice for LLMs",
            "url": "https://arxiv.org/html/2602.09902"
          },
          {
            "title": "[2603.04445] Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey",
            "url": "https://arxiv.org/abs/2603.04445"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Paper Title:** UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing\n\n**Author:** Varun Kotte\n\n**Submission Date:** Submitted on 11 May 2026\n\n**arXiv ID:** 2605.18796\n\n**Summary:** UCCI is a calibration-first router that maps token-level margin uncertainty to a per-query error probability via isotonic regression and selects the escalation threshold by constrained cost minimization. LLM cascades and model routing promise lower inference cost by sending easy queries to a small model and escalating hard ones to a large model, but most deployed routers use uncalibrated confidence scores and require per-workload threshold tuning.\n\n**Technical Contribution:** Under three explicit assumptions, threshold policies on the calibrated score are cost-optimal, and isotonic calibration achieves O(n^{-1/3}) sample complexity for expected calibration error (ECE).\n\nThe paper is available on arXiv at: https://arxiv.org/abs/2605.18796"
    ],
    "durationSeconds": 8.321497280999989,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "04f5f762-78a6-4294-be62-bf04d2089e00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-27T13:03:04.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0128TUsHgtwpvVZxxhVthMTo`</summary>

```json
{
  "query": "process-driven autoformalization Lean 4 step level formalization compilation feedback 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39570ce3-6710-4d83-bb88-8a0ed5d9778a",
  "isSidechain": false,
  "requestId": "req_011CbT7ry6ayrGwBrhqovFK9",
  "type": "assistant",
  "uuid": "91e9e1a7-c9f2-4370-b234-c54e1e4122c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Amc5f4ry6tn9ZBaFRRFqgP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 32187,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 32187,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 52 · 2026-05-27T13:03:11.357Z_

<details><summary>↩ Tool result · `toolu_0128TUsHgtwpvVZxxhVthMTo`</summary>

```text
Web search results for query: "process-driven autoformalization Lean 4 step level formalization compilation feedback 2024"

Links: [{"title":"PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://openreview.net/pdf?id=k8KsI84Ds7"},{"title":"Work in progress PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://arxiv.org/pdf/2406.01940"},{"title":"FORMAL: DEMOCRATIZING LEAN 4 FORMALIZATION","url":"https://mustafasameen.github.io/assets/publications/2025-formal/paper.pdf"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/html/2406.01940v1"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4/fulltext/666038b385a4ee7261a6723b/Process-Driven-Autoformalization-in-Lean-4.pdf?origin=scientificContributions"},{"title":"(PDF) Process-Driven Autoformalization in Lean 4","url":"https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4"}]

Based on the search results, here's what I found about process-driven autoformalization in Lean 4:

## Overview

A Process-Driven Autoformalization (PDA) framework was proposed for iterative performance improvement and automated assessment. The research introduces Formalization for Lean 4 (FORML4), an extensive dataset for training and evaluating LLMs' autoformalization capabilities, derived from Mathlib 4 theorems and rigorously quality-checked manually.

## Framework Process

The PDA framework begins with training an autoformalization model on FORML4, with the model's output then processed by the Lean 4 Compiler, generating automated feedback. This feedback generates process-level annotations for the autoformalization output, utilized to train a process-supervised verifier (PSV), with the autoformalization model then fine-tuned based on the verifier's feedback.

## Key Innovation

By utilizing both statements and proofs, FORML4 facilitates comprehensive feedback from the Lean 4 compiler, enabling strict assessments of syntax and semantic integrity in reasoning logic. Extensive experiments demonstrate that PDA significantly enhances autoformalization in Lean 4, achieving better results with less training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91e9e1a7-c9f2-4370-b234-c54e1e4122c4",
  "isSidechain": false,
  "promptId": "2c02e551-5c84-4029-87f7-16d10443db68",
  "type": "user",
  "uuid": "71bf8928-47bc-4a75-9694-72917f955b1c",
  "toolUseResult": {
    "query": "process-driven autoformalization Lean 4 step level formalization compilation feedback 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GUa4Ar1wpCv8PGJaKofLj2",
        "content": [
          {
            "title": "PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4",
            "url": "https://openreview.net/pdf?id=k8KsI84Ds7"
          },
          {
            "title": "Work in progress PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4",
            "url": "https://arxiv.org/pdf/2406.01940"
          },
          {
            "title": "FORMAL: DEMOCRATIZING LEAN 4 FORMALIZATION",
            "url": "https://mustafasameen.github.io/assets/publications/2025-formal/paper.pdf"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/html/2406.01940v1"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4/fulltext/666038b385a4ee7261a6723b/Process-Driven-Autoformalization-in-Lean-4.pdf?origin=scientificContributions"
          },
          {
            "title": "(PDF) Process-Driven Autoformalization in Lean 4",
            "url": "https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4"
          }
        ]
      },
      "Based on the search results, here's what I found about process-driven autoformalization in Lean 4:\n\n## Overview\n\nA Process-Driven Autoformalization (PDA) framework was proposed for iterative performance improvement and automated assessment. The research introduces Formalization for Lean 4 (FORML4), an extensive dataset for training and evaluating LLMs' autoformalization capabilities, derived from Mathlib 4 theorems and rigorously quality-checked manually.\n\n## Framework Process\n\nThe PDA framework begins with training an autoformalization model on FORML4, with the model's output then processed by the Lean 4 Compiler, generating automated feedback. This feedback generates process-level annotations for the autoformalization output, utilized to train a process-supervised verifier (PSV), with the autoformalization model then fine-tuned based on the verifier's feedback.\n\n## Key Innovation\n\nBy utilizing both statements and proofs, FORML4 facilitates comprehensive feedback from the Lean 4 compiler, enabling strict assessments of syntax and semantic integrity in reasoning logic. Extensive experiments demonstrate that PDA significantly enhances autoformalization in Lean 4, achieving better results with less training data."
    ],
    "durationSeconds": 6.683557857999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "91e9e1a7-c9f2-4370-b234-c54e1e4122c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-27T13:05:10.256Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a solid understanding of the landscape. Let me synthesize my findings and provide my analysis as the 发掘 agent.

Let me think about this proposal critically:

**Core idea**: Use PF (Pseudo-Formalization) blocks as the bridge between informal and formal verification, then use calibrated uncertainty + dependency graph criticality to selectively route only the most critical/uncertain blocks to Lean 4 formal verification.

**Key observations from my research:**

1. **Barkallah et al. (May 2026)** - PF is very recent (literally published 8 days ago from today's date of May 27, 2026). 

The proposal leverages this cutting-edge work, which gives it novelty but also means the community hasn't yet validated whether PF actually works at scale.

2. **ProofFlow (ICLR 2026)** - Uses dependency graphs for autoformalization fidelity, while the proposal uses them for routing decisions—related concepts but applied differently.

3. **Ganguly et al. (NeurIPS 2025)** - The closest competitor in selective formal verification with uncertainty. The proposal differentiates by sourcing uncertainty from verification rather than generation, routing across paradigms instead of within them, and using dual signals for criticality instead of a single metric.

4. **

VERGE (2026)** - Routes between SMT solvers and LLM ensembles for first-order logic, which shares the routing philosophy but operates in a different domain.

5. **UCCI (May 2026)** - Provides calibrated uncertainty for cascade routing, methodologically relevant but routes between model sizes rather than verification paradigms.

Now I'm questioning whether the routing actually needs calibrated uncertainty—could simple heuristics like block length or complexity work just as well? The proposal claims routing all blocks to formal verification costs 4-8x more, and the 10-20% routing rate saves significantly, but I should think through whether that justifies the added complexity over basic heuristics. The proposal does plan an ablation to address this, and the core argument hinges on ensemble disagreement being a stronger signal than surface-level features.

The three key premises are that PF blocks are naturally suited to autoformalization since they have explicit premises and conclusions, that combining calibrated uncertainty with dependency criticality outperforms either signal alone, and that routing just 10-20% of blocks catches most errors the base verifier misses. The first seems validated by the pilot study, the second is testable through ablation, and the third depends on whether errors actually concentrate in high-uncertainty, high-criticality regions.

As I assess novelty, the combination of PF decomposition with uncertainty-guided selective routing is the distinctive contribution here.  Individual pieces exist elsewhere—PF from prior work, uncertainty routing from other papers, dependency graphs from ProofFlow—but nobody's put them together this way or recognized that PF blocks serve as natural formalization units. The real significance hinges on whether block-level autoformalization actually achieves meaningfully higher success rates than trying to formalize entire proofs at once, because if it doesn't, the whole approach loses its foundation.

There are some real vulnerabilities though. The claim that whole-proof autoformalization hits an architectural ceiling that stronger models can't overcome is stated confidently but hard to defend—larger models might just close that gap. And the intuition that errors in high-fan-out blocks are more dangerous makes sense, but it's not guaranteed; a low-fan-out block at the end of the proof could harbor the critical flaw. They do have preliminary data supporting the block-level approach, which helps. The architectural barrier claim could be strengthened by pointing to recent work showing step-level methods consistently outperform whole-proof approaches, rather than asserting it as an immutable property.

The dual-signal routing deserves a deeper framing too. Instead of just "catching what the base verifier misses," it's really addressing two distinct failure modes in LLM verification: epistemic uncertainty (the model genuinely doesn't know) versus structural importance (the cost of being wrong is high regardless of model confidence). This makes the approach feel less like an ad-hoc engineering fix and more like a principled decomposition of the verification problem.

Now I'm re-reading the proposal itself to see what's already there and what actually needs sharpening. The core claims about PF blocks mapping to Lean 4 structure and the dual-signal mitigating confident-but-wrong errors are already present, so I should focus on what's genuinely missing rather than restating what's been covered.

The real gap is that the proposal mentions the context-completion problem as a bottleneck in whole-proof autoformalization but doesn't make this the centerpiece of the theoretical argument. The key advantage of block-level formalization is that each PF block is self-contained — it declares its premises explicitly, so the autoformalization tool doesn't need to infer context from surrounding text or maintain a running formal state across the entire proof. This closed-world property directly addresses why block-level approaches should outperform whole-proof methods, and it's the insight that should anchor the contribution.

On the error propagation angle, the proposal does touch on fan-out degree in the dependency graph, but it frames this mainly as a routing signal rather than developing the deeper point: errors in high-fan-out blocks have a multiplier effect because they invalidate all downstream conclusions that depend on them. The cost of a verification failure should scale with the number of blocks transitively reachable from that block, weighted by their own uncertainty — this formalization of error impact could strengthen the criticality-based routing strategy.

The dual-signal routing (uncertainty × criticality) also deserves sharper theoretical grounding. Rather than treating these as two independent heuristics, the proposal could frame them through decision theory: uncertainty captures the probability of a wrong judgment, criticality captures the cost of that error, so the routing policy is essentially optimizing for expected loss. This risk-based framing makes the mechanism more principled and connects it to established decision-theoretic principles.

Now stepping back to assess where the proposal stands: it's already quite detailed and well-structured, so the main development opportunities are around tightening the theoretical foundations for why PF works as a solution.

I should also think more carefully about what trivial alternatives exist and whether the proposal adequately addresses them. The obvious one is just running everything through formal verification—the proposal argues this is too expensive, but as autoformalization tools improve, that cost gap might shrink, which could undermine the value of selective routing. The proposal should be more explicit about why selective routing remains valuable even as verification costs decline.

Another alternative is using better LLM verifiers with improved prompting strategies instead of formal verification. There's evidence that prompt ensembles can boost smaller model performance significantly, and the proposal does include this as a baseline. The key counterargument is that even optimized LLM verification still misses roughly half the errors on the benchmark, so formal verification genuinely adds value for the hardest cases.

Now I'm ready to structure my analysis around the core findings and position this work relative to recent developments in the field.

The closest competitor is Ganguly et al. from NeurIPS 2025, but it differs across all three key dimensions. ProofFlow uses dependency graphs for autoformalization rather than routing, so I need to clarify where the overlap actually lies. The "architectural barrier" framing needs refinement—it's really about how context dependency accumulates rather than a fundamental architectural constraint. There's also an underdeveloped decision-theoretic angle to the dual-signal routing that could strengthen the theoretical foundation.

The decision-theoretic framing is the most promising genuine contribution here. Right now the uncertainty × criticality weighting reads as an engineering choice, but reframing it as expected loss—where P(error) × C(error) determines routing decisions—grounds it in decision theory and connects to established literature.

ProofFlow's use of dependency graphs for structural faithfulness in autoformalization actually validates the core assumption that dependency structure matters, so I should position this as supporting evidence rather than competition. The "architectural barrier" claim becomes much stronger when I'm precise about the mechanism: error accumulation through sequential context dependency in monolithic formalization, which proof blocks break by making each block self-contained. On robustness, I need to address whether selective routing becomes obsolete if autoformalization improves dramatically—the argument should be that the value remains stable even with perfect autoformalization, since formal proof search itself still benefits from targeted routing.

Looking at whether this fundamentally works, the approach rests on several assumptions: ProofFlow decomposition is effective, block-level autoformalization is more tractable than whole-proof formalization, uncertainty calibration can identify where the base verifier fails, dependency criticality signals useful routing decisions, and the combination catches errors the base verifier misses alone. I don't see a fundamental flaw here—the risks are manageable through the pilot study and ablations. On novelty, the ProofFlow-as-bridge insight is the key differentiator.

Now I'm thinking through how to frame the main contributions. I want to recast the dual-signal routing through a decision-theoretic lens—treating uncertainty and criticality as components of expected verification loss rather than just two signals being combined. This grounds the routing in principled risk optimization. I'm also planning to sharpen the comparison with related work and clarify what makes this approach distinct. the "PF as minimal sufficient formalization structure" claim** — Currently framed as "natural bridge." The stronger framing is that PF blocks provide *exactly* the structural information (typed premises, explicit conclusion, self-containment) needed for tractable autoformalization, making them the *optimal* decomposition granularity for the formalization-verification pipeline.

3. **Robustness argument against improving autoformalization** — The value of selective routing is not contingent on autoformalization being hard; it's about cost efficiency. Even with perfect autoformalization, proof search is expensive. This makes the system robust to future improvements in the field.

Actually, let me reconsider. Point 3 might be more of a defensive argument than a real contribution. Let me think about whether there's something more compelling.

**Alternative point 3: Leverage the "confident-but-wrong" analysis as a standalone contribution.** The proposal plans this analysis as an ablation, but it could be elevated to something more significant. If I can characterize when and why BV fails confidently, that provides generalizable insights about LLM verification reliability. If the analysis reveals systematic patterns—certain proof structures or mathematical domains consistently triggering confident-but-wrong failures—that becomes valuable knowledge beyond just this system.

Yes, that's stronger. It transforms an ablation into a real contribution.

So my three 发掘 points are: decision-theoretic framing of dual-signal routing, PF as optimal decomposition granularity, and elevating the confident-but-wrong analysis to a contribution. Let me think about whether I'm missing something else about potential extensions or implications.

Actually, I should also consider whether there are threats to novelty from related work. ProofFlow uses dependency graphs for autoformalization, and this proposal uses them for routing—the differentiation needs to be clearer. ProofFlow's insight is that preserving dependency structure improves formalization fidelity; this proposal's insight is that dependency structure determines verification priority. They're different uses of the same structure, but I need to make that explicit rather than just saying "we also use dependency graphs."

VERGE is probably the most similar system—it also routes between verification paradigms. But VERGE routes based on claim type (logical vs. commonsense), not uncertainty; it operates on atomic first-order logic claims rather than proof blocks; and it doesn't leverage dependency structure. The proposal should be more explicit about these distinctions.

I'm thinking through the key novelty points: the decision-theoretic framing of dual-signal routing, the use of proof blocks as the structurally minimal formalization unit, and the VERGE differentiation. Though actually, the VERGE point feels more like a related work clarification than a core novelty contribution. Let me focus on the decision-theoretic routing framework and strengthening the context-completion argument instead.

Looking back at the proposal, the context-completion problem is already mentioned but could be sharpened considerably. The key insight is that proof blocks provide closed-world formalization targets where all necessary context is explicitly declared, which fundamentally differs from whole-proof autoformalization. I should develop this more rigorously by formally defining the context-completion problem and showing how the block structure solves it, then contrast this with the limitations of end-to-end approaches.

This reframing positions the contribution more precisely: it's not just that blocks are better than whole proofs, but that they solve a specific, well-defined bottleneck that other step-level methods only partially address. I'll go with these three points and move to the final output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71bf8928-47bc-4a75-9694-72917f955b1c",
  "isSidechain": false,
  "requestId": "req_011CbT7sn6Kf9JKPnYm3FAzz",
  "type": "assistant",
  "uuid": "93286ffe-5902-4b81-9039-29f18bc1d734",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NS8bqqsxWP8FMihur8NYjk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 32907,
      "output_tokens": 8509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8509,
          "cache_read_input_tokens": 32907,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 54 · 2026-05-27T13:06:30.250Z_

Now I have enough research to provide a thorough analysis. Let me compile my findings.

【状态】: 有发掘空间

【前置调研发现】
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531) (arXiv, May 2026): 本 proposal 的直接基础。PF 将证明分解为自包含模块，每个模块显式声明前提、结论和证明。Block Verification 在 ArxivMathGradingBench 上 Pareto-dominates LLM-as-judge 但仍遗漏 ~50% 的错误。该论文发表仅 8 天（相对于今天 2026-05-27），说明 proposal 紧跟前沿。
- [Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047) (NeurIPS 2025): 最接近的竞争者。用 PCFG 建模 LLM→SMT-LIB 的生成端不确定性，实现选择性验证，误差降低 14-100%。proposal 声称的三维差异化（不确定性来源、跨范式路由、结构关键性）经调研确认为真实差异，非表面区分。
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 在 first-order logic claims 上跨验证范式路由（SMT solver vs LLM ensemble），使用 claim 类型（logical vs commonsense）而非不确定性作为路由信号。这是架构层面最接近的系统——都是跨范式路由。
- [ProofFlow](https://arxiv.org/abs/2510.15981) (ICLR 2026): 用依赖 DAG 保持 autoformalization 的结构忠实度，ProofScore 0.545 远超 whole-proof (0.123) 和 step-proof (0.072)。验证了依赖图结构在证明形式化中的价值，但用途不同：ProofFlow 用于 autoformalization 忠实度，proposal 用于验证路由。
- [UCCI](https://arxiv.org/abs/2605.18796) (arXiv, May 2026): 用 isotonic regression 校准 token-level margin uncertainty 做 LLM cascade routing。方法论高度相关但路由目标不同（小模型→大模型 vs LLM verification→formal verification）。
- [Process-Driven Autoformalization in Lean 4](https://openreview.net/forum?id=k8KsI84Ds7) (2024): 展示 step-level formalization + compiler feedback 优于 whole-proof。部分支持 proposal 的核心假设，但 PDA 的 step-level 仍需维护 running context，与 PF block 的完全自包含不同。
- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450) (arXiv 2026): 通过 specialized prompt ensemble，小模型可达到 frontier 模型的验证水平（准确率提升 9.1%，一致性提升 15.9%）。这提升了 LLM-only verification 的天花板，但 proposal 已将此纳入 baseline。
- [ThinkPRM](https://arxiv.org/abs/2504.16828) (2025): 用 1% 的 process labels 训练的 verbalized PRM 超过 discriminative PRM。代表当前最强的 step-level LLM verifier。
- [StepFun-Formalizer-32B](https://arxiv.org/abs/2508.04440) / [Goedel-Prover-V2](https://github.com/Goedel-LM/Goedel-Prover-V2) (ICLR 2026): Proposal 选用的具体工具链。StepFun-Formalizer BEq@1 40.5% on FormalMATH-Lite；Goedel-Prover-V2 MiniF2F pass@32 达 88.1%。工具选型合理。
- 调研总结: 该领域当前的突破方向有两条：(1) 降低 autoformalization 粒度（whole-proof → step-level → block-level）以提高成功率；(2) 用不确定性信号做选择性验证以降低成本。本 proposal 的核心 insight 在于将这两条线索交叉：用 PF block 作为最佳粒度单位，用不确定性+结构关键性做选择性路由。这个交叉点目前尚无人占据。

---

【发掘点 1】
- 维度: 核心 claim 强化 / novelty 锐化
- 内容: **将 dual-signal routing 重新表述为决策论风险最小化框架。** 当前 proposal 将 uncertainty × dependency criticality 呈现为工程组合（"dual signal mitigates confident-but-wrong risk"）。但这其实是一个决策论问题的自然解：每个 block b 的验证路由决策应最小化 Expected Verification Loss = P(BV_error | b) × C(error | b)，其中 P 由校准后的 ensemble uncertainty 估计，C 由依赖图关键性（b 的传递可达 block 数量 × 各下游 block 的 uncertainty 权重）估计。当 E[Loss] 超过 formal verification 的边际成本时路由到 Tier 2。这个重新表述的价值在于：(1) 将两个看似 ad hoc 的信号统一为一个有原则的目标函数；(2) 路由阈值不再是超参数，而是成本-风险均衡的自然结果；(3) 与 Ganguly 等人的差异变得更本质——他们优化的是 abstention policy（是否验证），你优化的是 cross-tier routing policy（如何验证），目标函数的结构完全不同。
- 价值: 这一重新表述将 Novelty 从 "组合了两个信号" 提升为 "提出了一个有原则的跨范式验证路由框架"。审稿人面对 "我们把 A 和 B 乘在一起" 容易说 "trivial combination"；面对 "我们定义了一个风险最小化目标，A 和 B 分别估计目标的两个因子" 则很难说 trivial。
- 调研依据: UCCI (arXiv 2605.18796) 将校准后的 uncertainty 直接连接到 cost-optimal escalation threshold，用约束优化选择路由阈值——这验证了 "校准 uncertainty → 成本最优路由" 这一范式在 LLM routing 中的有效性。本建议将同样的原则扩展到 cross-paradigm verification routing，并引入 cost-of-error 维度。

【发掘点 2】
- 维度: 核心 claim 强化 / significance 提升
- 内容: **精确定义 "context-completion problem" 并将其作为 Claim 1 的理论核心，明确 PF block 与现有 step-level 方法的结构差异。** 当前 proposal 说 PF block 的 "self-contained nature eliminates the context-completion problem"，但没有精确定义这个 problem 是什么以及为什么 PF block 是比现有 step-level 方法更好的解法。具体建议：(1) 精确定义 context-completion problem——在 whole-proof 和普通 step-level formalization 中，每步的形式化依赖于前序所有步骤的正确形式化，构成一条 sequential error accumulation chain；任何一步形式化失败会导致后续所有步的 context 不完整，从而连锁失败。(2) 对比 PF block 与 Process-Driven Autoformalization (PDA, 2024) 的关键结构差异：PDA 是 step-level 但每步仍依赖 running Lean context（前序 `have`/`let` 声明），编译反馈只能修复当前步但无法消除跨步依赖；PF block 是 *closed-world* 形式化目标——所有 premise 显式声明，autoformalization 不需要推断或维护跨 block 的形式化上下文。(3) 这意味着 PF block 的形式化成功率在理论上独立于其他 block 的形式化结果，允许各 block *并行*独立形式化且互不影响——这是 step-level 方法做不到的。
- 价值: 当前 Claim 1 的 framing 是 "PF block 是 informal 和 formal 之间的自然桥梁"。精确定义后变为 "PF block 是已知唯一提供 closed-world 形式化属性的自然语言证明分解粒度，从根本上消除了限制 whole-proof 和普通 step-level autoformalization 的 sequential error accumulation"。这将 Claim 1 从描述性观察提升为结构性定理级别的论断，大幅强化 Significance 和 Novelty。
- 调研依据: Process-Driven Autoformalization (2024) 展示 step-level 优于 whole-proof，但其框架仍需 Lean compiler 的 running context feedback；ProofFlow (ICLR 2026) 展示 step-proof 的 ProofScore 仅 0.072 vs dependency-aware 的 0.545——这恰恰说明 step-level 本身不够，*结构化* 的分解（保留 dependency 信息、提供自包含 context）才是关键。PF block 正好提供了这种结构。

【发掘点 3】
- 维度: significance 提升 / novelty 锐化
- 内容: **将 "confident-but-wrong" 分析从 ablation 提升为独立贡献，定位为对 LLM 数学验证可靠性的系统性诊断。** 当前 proposal 将 confident-but-wrong 分析放在 ablation 7 中（"proportion of BV errors at >0.8 confidence"）。但如果这一分析揭示了系统性模式——例如，某些数学领域（代数 vs 分析）、某些证明手法（构造性 vs 反证法）、某些 block 结构特征（引用定理数量、隐含假设密度）系统性地导致 BV 高置信度误判——这将成为一个独立有价值的发现。建议：(1) 对 confident-but-wrong cases 做结构化归因分析（数学领域、证明策略、block 复杂度特征），超越简单的比例统计；(2) 如果发现系统性模式，这就成为对 LLM 数学验证的 *failure mode taxonomy*——告诉领域研究者 "在哪些场景下你不能信任 LLM 验证器的高置信度判断"。这一发现的价值独立于本 proposal 的具体系统设计。
- 价值: 将一个常规 ablation 变为一个独立 contribution，同时为 dual-signal routing 的必要性提供实证支撑（如果 confident-but-wrong 有系统性模式，单纯的 ensemble uncertainty 可能仍然不够，dependency criticality 作为 uncertainty-independent 信号的价值就被凸显）。这同时提升 Significance（对整个 LLM verification 领域的诊断价值）和 Novelty（现有工作未系统性地刻画 BV confident-but-wrong 的 failure modes）。
- 调研依据: Hard2Verify (Pandit et al., 2025) 展示了 PRM 在难问题上的大幅性能下降（78.3%→37.3%），但只报告了 aggregate 数字而未分析 failure mode 的结构性模式。ThinkPRM (2025) 同样关注 overall performance 而非 failure mode 归因。将 confident-but-wrong 分析结构化将填补这一诊断空白。

Sources:
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)
- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [ProofFlow (ICLR 2026)](https://arxiv.org/abs/2510.15981)
- [UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing](https://arxiv.org/abs/2605.18796)
- [Process-Driven Autoformalization in Lean 4](https://openreview.net/forum?id=k8KsI84Ds7)
- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [Safe: Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)
- [StepFun-Formalizer-32B](https://arxiv.org/abs/2508.04440)
- [Goedel-Prover-V2 (ICLR 2026)](https://github.com/Goedel-LM/Goedel-Prover-V2)
- [HERMES (ICML 2026)](https://arxiv.org/abs/2511.18760)
- [Hard2Verify (2025)](https://arxiv.org/abs/2505.20047)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93286ffe-5902-4b81-9039-29f18bc1d734",
  "isSidechain": false,
  "requestId": "req_011CbT7sn6Kf9JKPnYm3FAzz",
  "type": "assistant",
  "uuid": "c13d8da4-1ecf-42df-8d15-fecc0c6935fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NS8bqqsxWP8FMihur8NYjk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 32907,
      "output_tokens": 8509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8509,
          "cache_read_input_tokens": 32907,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we achieve near-formal-verification reliability for natural language mathematical proof che…",
  "leafUuid": "c13d8da4-1ecf-42df-8d15-fecc0c6935fa",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective formal verification via uncertainty and dependency routing",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we achieve near-formal-verification reliability for natural language mathematical proof che…",
  "leafUuid": "c13d8da4-1ecf-42df-8d15-fecc0c6935fa",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Selective formal verification via uncertainty and dependency routing",
  "sessionId": "c4d4da7f-989d-4eaa-b5b4-c481b8d60bad"
}
```

---
