# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Uncertainty-Guided Selective Form

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/4c2a7143-0934-4965-a436-7f8626ecca83.jsonl`
- **Structured JSON:** [`afdaff4b3cb5184382f9.json`](../../sessions/af/afdaff4b3cb5184382f9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T13:13:22.948Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T13:13:22.948Z",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition\n\n## Core Problem\n\nHow can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain and structurally critical proof blocks to formal verification?\n\n## Thesis and Contributions\n\nWe advance two claims, each supported by a corresponding contribution:\n\n**Claim 1 (Architectural Insight):** Modular proof decomposition — as instantiated by Pseudo-Formalization (Barkallah et al., 2026) — serves as a natural bridge between informal and formal verification of mathematical proofs. Each PF block's explicit typed premises map directly to Lean 4 hypothesis lists, its single explicit conclusion maps to a Lean 4 goal statement, and its self-contained nature eliminates the context-completion problem that fundamentally limits whole-proof autoformalization to ~35% end-to-end success (miniF2F-Lean Revisited, NeurIPS 2025). We empirically validate this by demonstrating that PF-block-level autoformalization achieves substantially higher success rates than raw-NL-fragment autoformalization in a controlled paired comparison.\n\n**Claim 2 (System Design):** Building on this bridge, we design a two-tier selective verification pipeline that combines calibrated uncertainty scoring with dependency-graph criticality to route only the 10-20% most uncertain or structurally critical blocks to Lean 4 formal verification. This achieves near-formal reliability at ~1.5-2x cost overhead versus Safe's 4-8x for universal formalization, and represents a viable path toward scaling formal verification to research-level proofs — where whole-proof autoformalization is fundamentally intractable.\n\n## Research Opportunity\n\nWhole-proof autoformalization faces a fundamental scalability barrier: context-completion difficulties and compounding error across steps limit end-to-end success to ~35% even with SOTA tools (66% autoformalization accuracy × ~70% theorem proving success; miniF2F-Lean Revisited, NeurIPS 2025). This barrier does not diminish with stronger models — it is architectural, arising from the unbounded context dependencies in monolithic proofs. Consequently, universal formal verification (Safe, Liu et al., ACL 2025) imposes 4-8x cost overhead per step while still being limited by autoformalization failures. Meanwhile, LLM-only verification (PF+Block Verification; Barkallah et al., May 2026) is cheap but leaves ~50% of research-level errors undetected on ArxivMathGradingBench. PF's modular block structure offers a way through this impasse: self-contained blocks with explicit premises and conclusions are structurally aligned with formal theorem statements, making block-level autoformalization fundamentally more tractable than whole-proof autoformalization. Step-level formalization has independently been shown more tractable than whole-proof approaches (Process-Driven Autoformalization in Lean 4, 2024). By adding calibrated uncertainty and dependency-graph criticality as a dual triage signal, we can route only the most critical blocks to formal verification, catching errors that LLM verification misses while operating within the tractability boundary of block-level autoformalization.\n\n## Research Landscape\n\n**LLM-based verification (cheap, unreliable):** Best PRM drops from 78.3% to 37.3% on Hard2Verify (Pandit et al., 2025). PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026). ThinkPRM (2025) advances data-efficient verbalized PRMs outperforming discriminative PRMs with 1% of process labels, representing the current strongest step-level LLM verifier. Specialized prompt ensembles can close much of the gap between small and frontier models for proof verification (Do We Need Frontier Models to Verify Mathematical Proofs?, arXiv 2604.02450, 2026), raising the LLM-only performance ceiling.\n\n**Universal formal verification (reliable, expensive):** Safe verifies each step in Lean 4 with ~80% success at 4-8x cost (Liu et al., ACL 2025). End-to-end autoformalization achieves only ~35% success (miniF2F-Lean Revisited, NeurIPS 2025). StepFun-Formalizer-32B achieves BEq@1 of 40.5% on FormalMATH-Lite for statement-level autoformalization.\n\n**Selective/adaptive verification (emerging):** Ganguly et al. (NeurIPS 2025) achieve 14-100% error reduction via selective SMT-based formalization using PCFG-based uncertainty. Our work differs on three levels: (1) uncertainty source — Ganguly models generation-side distribution (LLM→SMT-LIB), we model verification-side judgment uncertainty (BV ensemble disagreement on existing proofs); (2) routing target heterogeneity — Ganguly routes within a single verification paradigm (verify vs. abstain on SMT), we route across fundamentally different paradigms (LLM verification → formal verification); (3) structural criticality — Ganguly uses no structural signal, we introduce dependency-graph criticality as an orthogonal routing dimension. Qu (arXiv 2026) achieves 44% fewer verifier calls via adaptive allocation on MATH but operates within LLM-tier verification only.\n\n**Proof generation vs. verification taxonomy:** HERMES (Ospanov et al., ICML 2026) interleaves informal reasoning with Lean 4 verification during proof generation, achieving 67% accuracy improvement with 80% fewer FLOPs — but addresses proof generation (where output format is controllable) with uniform formalization, not proof verification of arbitrary NL input. Our work addresses the fundamentally different verification setting where PF decomposition is necessary to create structured formalization targets from arbitrary input. VERGE (Singh et al., arXiv 2026) routes between SMT solvers and LLM-ensemble verification for first-order logic claims, not mathematical proof blocks. UCCI (arXiv 2026) provides calibrated uncertainty for LLM cascade routing (small→large model), not across formal/informal verification tiers. ProofSketcher (arXiv 2026) produces typed proof sketches without uncertainty-guided routing. ProofFlow (2025) uses dependency graphs for autoformalization fidelity but not for verification routing decisions.\n\n## Proposed Approach\n\n**Phase 0 — Pilot study (go/no-go).** Before full pipeline development, we validate the core architectural assumption: randomly sample 50-100 PF blocks across mathematical domains and difficulty levels, test StepFun-Formalizer-32B autoformalization success rate and Goedel-Prover-V2-32B proof search success rate, establish block-level end-to-end success rate baseline. Threshold: if end-to-end success rate < 30%, Tier 2 requires redesign (e.g., multi-shot formalization with compiler-feedback self-correction). Report decomposed success rates: formalization type-check rate → proof search success rate → end-to-end rate.\n\n**Tier 1 — LLM Block Verification with calibrated uncertainty.** Decompose proof into PF blocks (Barkallah et al., 2026) with explicit premises, conclusions, and dependency graphs. Run Block Verification using QwQ-32B with dual uncertainty scoring: (i) ensemble disagreement via N=5 stochastic forward passes with temperature sampling, (ii) token-level CoT entropy. Calibrate via Platt scaling on synthetic evaluation set and miniF2F verification data (NOT on ArxivMathGradingBench, which is reserved for evaluation only), with temperature scaling as calibration method ablation.\n\n**Dual-signal routing.** Route blocks based on: uncertainty score × dependency criticality (primary: fan-out degree in inter-block dependency DAG; supplementary sensitivity analysis: dominator nodes, betweenness centrality). This dual signal mitigates the \"confident-but-wrong\" risk inherent in LLM overconfidence: (a) ensemble disagreement captures inter-model uncertainty more reliably than single-model confidence; (b) dependency criticality provides an uncertainty-independent signal — high-fan-out blocks receive formal verification even if BV is confident; (c) structural difficulty heuristics (block-internal step count, cited theorem count) serve as additional features.\n\n**Why calibrated uncertainty, not just structural heuristics?** Simple heuristics (block length, step count) capture surface complexity but miss blocks that are structurally simple yet reasoning-subtle — e.g., a one-step block applying a theorem in a non-obvious way. Ensemble disagreement flags exactly these cases: when model copies disagree on a seemingly-simple block, this signals hidden reasoning difficulty invisible to structural features. We validate this claim via head-to-head ablation against heuristic-only routing.\n\n**Tier 2 — Selective formal verification.** Routed blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging PF block structure (premises→Lean 4 hypotheses, conclusion→Lean 4 goal, no context completion needed) — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction (up to k=3 retry rounds using Lean compiler feedback). Per-block timeout: 5 min; per-proof timeout: 30 min. Fallback strategy for autoformalization failure or proof search timeout is an ablation variable.\n\n## Evaluation Plan\n\n**Benchmarks:**\n- ArxivMathGradingBench (Barkallah et al., 2026): 35 papers, 40 known errors. Held-out evaluation only (not used for calibration). Error detection precision/recall/F1, bootstrap CI (1000 resamples), McNemar's test, effect size (Cohen's h). Supplementary: per-paper accuracy.\n- Synthetic Error Detection Set: 400-500 instances from Hard2Verify competition-level problems. Multi-source error construction: (i) LLM-generated incorrect proofs, (ii) controlled perturbation of correct proofs (deleted steps, swapped theorems, computation errors), (iii) extracted known-error steps from Hard2Verify annotations. Ground-truth verification via answer matching + Lean 4 proof for correct proofs. Human validation on 50-80 instance subsample (Cohen's κ). Used for calibration and as co-primary evaluation benchmark.\n- miniF2F Verification Protocol: Generate ≥8 candidate proofs per problem (≥100 problems) using QwQ-32B, evaluate verification precision/recall. Aligned with Safe's miniF2F setting.\n\n**Baselines (7 methods):**\n- PF + BV single-pass (Barkallah et al., 2026)\n- PF + BV ensemble (N=5, no routing to formal verification)\n- PF + BV with specialized prompt ensemble (per arXiv 2604.02450, 2026): best-effort LLM verification upper bound\n- ThinkPRM (2025): SOTA data-efficient verbalized PRM\n- Qwen2.5-Math-PRM-7B: strongest open-source discriminative PRM at comparable scale\n- Safe universal formalization (Liu et al., ACL 2025)\n- HERMES (Ospanov et al., ICML 2026): if applicable to verification setting\n\n**Cost framework:** Unified metric: GPU-seconds per proof. Detailed breakdown: PF decomposition + ensemble BV (5× single BV) + routing overhead + autoformalization (per routed block) + proof search including retries and timeouts + fallback cost for Tier 2 failures. Pareto curve (cost vs. error detection recall) plotting all methods.\n\n**Ablations (8 experiments):**\n1. Uncertainty signal decomposition: ensemble disagreement only / CoT entropy only / combined — AUROC, ECE, recall@fixed-cost\n2. Routing signal: uncertainty only / dependency criticality only / simple structural heuristic only / dual signal — recall and cost\n3. Ensemble size: N=3 / N=5 / N=7\n4. Autoformalization failure fallback: accept / reject / majority-vote re-verification\n5. Threshold sweep: routing percentage 5%-50% — Pareto curve\n6. **PF blocks vs. raw NL autoformalization (Contribution 1 validation):** Paired comparison on same proofs. PF block input vs. raw NL fragment input to StepFun-Formalizer-32B. Metrics: Lean 4 type-check rate, proof search success rate. Paired Wilcoxon signed-rank test. This is a core result, not merely an ablation.\n7. Confident-but-wrong analysis: proportion of BV errors at >0.8 confidence, fraction captured by dual-signal vs. uncertainty-only routing\n8. Tier 2 sensitivity analysis: system Pareto curves under assumed Tier 2 success rates of 30%/50%/70%/90%, demonstrating robustness\n\n**Calibration method ablation:** Platt scaling vs. temperature scaling, cross-validated on calibration set, evaluated by ECE and routing decision quality.\n\n## Key References\n\n- Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., arXiv 2026)\n- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (Liu et al., ACL 2025)\n- Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (Pandit et al., arXiv 2025)\n- miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)\n- Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (Ganguly et al., NeurIPS 2025)\n- Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (Qu, arXiv 2026)\n- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (Singh et al., arXiv 2026)\n- HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (Ospanov et al., ICML 2026)\n- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)\n- Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)\n- ThinkPRM: Process Reward Models That Think (2025)\n- Qwen2.5-Math-PRM (2025)\n- ProofSketcher (arXiv 2026)\n- UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing (arXiv 2026)\n- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (2025)\n- Do We Need Frontier Models to Verify Mathematical Proofs? (arXiv 2604.02450, 2026)\n- Process-Driven Autoformalization in Lean 4 (2024)\n\n## Resource Estimate\n\n- **Phase 0 pilot:** ~30-50 GPU-hours (A100-80GB), 1-2 weeks. Go/no-go decision point.\n- **Full pipeline (Phase 1-3):** GPU hours: 400-550 (ensemble BV ~80h; StepFun-Formalizer ~80h; Goedel-Prover-V2 proof search ~130h including retries/timeouts; synthetic set construction ~40h; baselines + ablations ~120-170h). CPU hours: ~60h (Lean 4 kernel type-checking). Timeline: 14-18 weeks (2-3 researchers), including 2-3 week contingency for PF pipeline reproduction if code unavailable.\n- **Estimated GPU cost:** $1200-1650\n- **Lean 4 proof search:** Per-block timeout 5 min, per-proof timeout 30 min. ArxivMathGradingBench single pass: ~9h wall-clock (35 papers × ~30 blocks × 15% routing × 3.5 min/block). Independent blocks parallelizable.\n- **Critical path:** Phase 0 pilot (weeks 1-2) → PF pipeline setup + synthetic set (weeks 2-5) → uncertainty calibration (weeks 5-8) → full pipeline + ablations (weeks 8-15) → analysis + writing (weeks 15-18)."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T13:13:22.953Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T13:13:22.953Z",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

## Round 1

51 recorded events

### User

_source line 3 · 2026-05-27T13:13:22.967Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
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
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "0a8558d9-7ffe-427d-b13c-1296b7a64595",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T13:13:22.966Z_

```json
{
  "parentUuid": "0a8558d9-7ffe-427d-b13c-1296b7a64595",
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
  "uuid": "e0154d3e-5690-41cb-b387-ef16d6d038a1",
  "timestamp": "2026-05-27T13:13:22.966Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T13:13:22.966Z_

```json
{
  "parentUuid": "e0154d3e-5690-41cb-b387-ef16d6d038a1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "00c402cf-e80a-4651-b1a9-ed140aad53c6",
  "timestamp": "2026-05-27T13:13:22.966Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we ac…",
  "leafUuid": "00c402cf-e80a-4651-b1a9-ed140aad53c6",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate selective formal verification proposal acceptance probability",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Assistant

_source line 8 · 2026-05-27T13:13:31.571Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026 submission. I need to follow the rubric carefully:

1. First, do 3-5 WebSearches to understand the field
2. Then evaluate Novelty, Significance, and Related Work
3. Answer the Trivial Alternative and Premise Assumption checks
4. Estimate probability

Let me start by searching for the key topics and papers mentioned in this proposal. The proposal is about:
- Uncertainty-guided selective formal verification of mathematical proofs
- Using Pseudo-Formalization (PF) blocks as a bridge between informal and formal verification


- Routing uncertain/critical blocks to Lean 4 formal verification

I should search for the related works they mention—Safe from ACL 2025, the Ganguly et al. paper from NeurIPS 2025, HERMES, and the Barkallah et al. work on Pseudo-Formalization—to understand the landscape better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00c402cf-e80a-4651-b1a9-ed140aad53c6",
  "isSidechain": false,
  "requestId": "req_011CbT8esLqb7bnNyTZy1opy",
  "type": "assistant",
  "uuid": "8f0891c9-0fdf-4ff0-8e5c-db815c69e3b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWkTPgT6suvgBNhXMbRt9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5437,
      "cache_read_input_tokens": 13968,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5437,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 332,
          "cache_read_input_tokens": 13968,
          "cache_creation_input_tokens": 5437,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5437
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

_source line 9 · 2026-05-27T13:13:31.574Z_

I need to do thorough field research before evaluating this proposal. Let me start by searching for the key related works and the current state of the field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f0891c9-0fdf-4ff0-8e5c-db815c69e3b7",
  "isSidechain": false,
  "requestId": "req_011CbT8esLqb7bnNyTZy1opy",
  "type": "assistant",
  "uuid": "9ff5543a-aaff-4dc6-b3bd-9f869fcbb130",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWkTPgT6suvgBNhXMbRt9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5437,
      "cache_read_input_tokens": 13968,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5437,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 332,
          "cache_read_input_tokens": 13968,
          "cache_creation_input_tokens": 5437,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5437
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

_source line 10 · 2026-05-27T13:13:31.611Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HCr2Zv3Gahjbohs6YBJdQg`</summary>

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
  "parentUuid": "9ff5543a-aaff-4dc6-b3bd-9f869fcbb130",
  "isSidechain": false,
  "requestId": "req_011CbT8esLqb7bnNyTZy1opy",
  "type": "assistant",
  "uuid": "8b2d0e50-6ce1-4478-b437-cfe3a09106db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWkTPgT6suvgBNhXMbRt9d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5437,
      "cache_read_input_tokens": 13968,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5437,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 332,
          "cache_read_input_tokens": 13968,
          "cache_creation_input_tokens": 5437,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5437
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

_source line 11 · 2026-05-27T13:13:31.618Z_

<details><summary>↩ Tool result · `toolu_01HCr2Zv3Gahjbohs6YBJdQg`</summary>

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
  "parentUuid": "8b2d0e50-6ce1-4478-b437-cfe3a09106db",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "32c023cd-5d81-473b-8e58-d5a86db1a6b0",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "8b2d0e50-6ce1-4478-b437-cfe3a09106db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T13:13:34.703Z_

Now let me conduct the field research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32c023cd-5d81-473b-8e58-d5a86db1a6b0",
  "isSidechain": false,
  "requestId": "req_011CbT8fWFc4FmGSrWQvRpNC",
  "type": "assistant",
  "uuid": "94e305b2-6ff6-4f5b-b291-2d1091d5e0fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnhWVSo3jUMhg5MmYFiPNi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 19405,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 19405,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 13 · 2026-05-27T13:13:35.182Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013J7EpGKNxhqtUGbTuisjLY`</summary>

```json
{
  "query": "Safe step-aware formal verification mathematical reasoning LLM Liu ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94e305b2-6ff6-4f5b-b291-2d1091d5e0fc",
  "isSidechain": false,
  "requestId": "req_011CbT8fWFc4FmGSrWQvRpNC",
  "type": "assistant",
  "uuid": "c7a6a13c-45d0-4824-8468-87e95cba1357",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnhWVSo3jUMhg5MmYFiPNi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 19405,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 19405,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 14 · 2026-05-27T13:13:35.655Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014fcwo7Jjv1jybKHLT51vnM`</summary>

```json
{
  "query": "Pseudo-Formalization automatic proof verification Barkallah 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a6a13c-45d0-4824-8468-87e95cba1357",
  "isSidechain": false,
  "requestId": "req_011CbT8fWFc4FmGSrWQvRpNC",
  "type": "assistant",
  "uuid": "8471b7f5-8411-4133-8c0f-df959cb0873f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnhWVSo3jUMhg5MmYFiPNi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 19405,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 19405,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 15 · 2026-05-27T13:13:36.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PDidfgNB77bBTa37JCxb94`</summary>

```json
{
  "query": "selective formal verification uncertainty routing mathematical proofs 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8471b7f5-8411-4133-8c0f-df959cb0873f",
  "isSidechain": false,
  "requestId": "req_011CbT8fWFc4FmGSrWQvRpNC",
  "type": "assistant",
  "uuid": "e8704164-7317-4793-ac54-9194de50be08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnhWVSo3jUMhg5MmYFiPNi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 19405,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 19405,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 16 · 2026-05-27T13:13:37.394Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SxyKiCa5fSL3x2xau9Nayd`</summary>

```json
{
  "query": "HERMES efficient verifiable mathematical reasoning Ospanov ICML 2026 Lean interleave"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8704164-7317-4793-ac54-9194de50be08",
  "isSidechain": false,
  "requestId": "req_011CbT8fWFc4FmGSrWQvRpNC",
  "type": "assistant",
  "uuid": "9605e7fd-e75f-4fb5-9e28-679818e7f53b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnhWVSo3jUMhg5MmYFiPNi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 19405,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 19405,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 17 · 2026-05-27T13:13:37.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AFEH8Wa8EcvxB8iBV7yHLn`</summary>

```json
{
  "query": "Ganguly grammars formal uncertainty LLM automated reasoning NeurIPS 2025 selective SMT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9605e7fd-e75f-4fb5-9e28-679818e7f53b",
  "isSidechain": false,
  "requestId": "req_011CbT8fWFc4FmGSrWQvRpNC",
  "type": "assistant",
  "uuid": "6761f7ef-371d-444a-b6f0-08fe25ae5122",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnhWVSo3jUMhg5MmYFiPNi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 19405,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 19405,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 18 · 2026-05-27T13:13:42.299Z_

<details><summary>↩ Tool result · `toolu_013J7EpGKNxhqtUGbTuisjLY`</summary>

```text
Web search results for query: "Safe step-aware formal verification mathematical reasoning LLM Liu ACL 2025"

Links: [{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.594/"},{"title":"GitHub - liuchengwucn/Safe: (ACL 2025 Main) Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - Official Implementation & Dataset","url":"https://github.com/liuchengwucn/Safe"},{"title":"[2506.04592] Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/abs/2506.04592"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/html/2506.04592v1"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification | Request PDF","url":"https://www.researchgate.net/publication/394301322_Safe_Enhancing_Mathematical_Reasoning_in_Large_Language_Models_via_Retrospective_Step-aware_Formal_Verification"},{"title":"Self-Verifiable Mathematical Reasoning","url":"https://www.emergentmind.com/topics/self-verifiable-mathematical-reasoning"}]

Based on the web search results, I found information about the paper you're looking for:

## Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification

This paper was authored by Chengwu Liu, Ye Yuan, Yichun Yin, Yan Xu, Xin Xu, Zaoyu Chen, Yasheng Wang, Lifeng Shang, Qun Liu, and Ming Zhang, and was published at ACL 2025.

**Key Contributions:**

The paper proposes a retrospective, step-aware formal verification framework called Safe that articulates mathematical claims in formal mathematical language Lean 4 at each reasoning step and provides formal proofs to identify hallucinations.

The work represents the first endeavor to utilize formal mathematical language Lean 4 for verifying content generated by LLMs.

The framework was evaluated across multiple language models and various mathematical datasets, demonstrating significant performance improvement while offering interpretable and verifiable evidence.

The paper also proposes FormalStep as a benchmark for step correctness theorem proving with 30,809 formal statements.

The official implementation and dataset are available on GitHub at https://github.com/liuchengwucn/Safe, and the paper is published in the proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7a6a13c-45d0-4824-8468-87e95cba1357",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "d4eaf429-a67b-4c94-8938-de5ef0c60869",
  "toolUseResult": {
    "query": "Safe step-aware formal verification mathematical reasoning LLM Liu ACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011dEUB2YUHbgWqR3e9ov44b",
        "content": [
          {
            "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.594/"
          },
          {
            "title": "GitHub - liuchengwucn/Safe: (ACL 2025 Main) Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - Official Implementation & Dataset",
            "url": "https://github.com/liuchengwucn/Safe"
          },
          {
            "title": "[2506.04592] Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification",
            "url": "https://arxiv.org/abs/2506.04592"
          },
          {
            "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification",
            "url": "https://arxiv.org/html/2506.04592v1"
          },
          {
            "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification | Request PDF",
            "url": "https://www.researchgate.net/publication/394301322_Safe_Enhancing_Mathematical_Reasoning_in_Large_Language_Models_via_Retrospective_Step-aware_Formal_Verification"
          },
          {
            "title": "Self-Verifiable Mathematical Reasoning",
            "url": "https://www.emergentmind.com/topics/self-verifiable-mathematical-reasoning"
          }
        ]
      },
      "Based on the web search results, I found information about the paper you're looking for:\n\n## Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification\n\nThis paper was authored by Chengwu Liu, Ye Yuan, Yichun Yin, Yan Xu, Xin Xu, Zaoyu Chen, Yasheng Wang, Lifeng Shang, Qun Liu, and Ming Zhang, and was published at ACL 2025.\n\n**Key Contributions:**\n\nThe paper proposes a retrospective, step-aware formal verification framework called Safe that articulates mathematical claims in formal mathematical language Lean 4 at each reasoning step and provides formal proofs to identify hallucinations.\n\nThe work represents the first endeavor to utilize formal mathematical language Lean 4 for verifying content generated by LLMs.\n\nThe framework was evaluated across multiple language models and various mathematical datasets, demonstrating significant performance improvement while offering interpretable and verifiable evidence.\n\nThe paper also proposes FormalStep as a benchmark for step correctness theorem proving with 30,809 formal statements.\n\nThe official implementation and dataset are available on GitHub at https://github.com/liuchengwucn/Safe, and the paper is published in the proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025)."
    ],
    "durationSeconds": 7.1128806990000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c7a6a13c-45d0-4824-8468-87e95cba1357",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T13:13:43.975Z_

<details><summary>↩ Tool result · `toolu_01PDidfgNB77bBTa37JCxb94`</summary>

```text
Web search results for query: "selective formal verification uncertainty routing mathematical proofs 2025 2026"

Links: [{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in ...","url":"https://arxiv.org/pdf/2505.20047"},{"title":"24 January 2026, Preprint v3 · CC-BY 4.0 PREPRINT Review Article","url":"https://www.qeios.com/read/H7D715.3/pdf"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/pdf/2602.03975"},{"title":"A Review of Automated Formal Verification of Ad Hoc Routing Protocols   for Wireless Sensor Networks","url":"https://arxiv.org/pdf/1305.7410"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/pdf/2506.04592"},{"title":"Submitted as a conference paper at ICLR 2026 TYPED CHAIN-OF-THOUGHT:","url":"https://arxiv.org/pdf/2510.01069"}]

Based on the search results, here are the key findings related to selective formal verification, uncertainty routing, and mathematical proofs from 2025-2026:

## Recent Developments in Formal Verification and Mathematical Reasoning

**Uncertainty-Guided Verification:** Recent work demonstrates how to systematically capture and analyze output uncertainty by modeling LLM-generated formal programs with Probabilistic Context-Free Grammars, rather than just selecting the highest-probability output.

**Selective Verification with Uncertainty:** One approach allocates verification according to state-local uncertainty rather than uniform rules, using learned heuristics that combine distance-to-goal signals with verification budgets that vary based on local uncertainty so that ambiguous branching points receive more verification while clear decisions receive less.

**AI Advances in Mathematical Proofs:** In 2024, AlphaProof became the first AI to achieve silver-medal level in the IMO, followed by strong results from ByteDance and Harmonic in IMO 2025.

**Step-aware Formal Verification:** Recent approaches utilize LLMs to automatically generate formal statements that substantiate the correctness of individual steps, which can be addressed by automated theorem provers, then aggregate these formal proofs to evaluate overall reasoning trajectories.

**Formal Methods in Quantum Verification:** Theorem proving offers the highest level of assurance through rigorous mathematical proofs and is being applied to emerging domains like quantum computing verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8704164-7317-4793-ac54-9194de50be08",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "f6c279c9-22fc-4a74-98d1-45785553d728",
  "toolUseResult": {
    "query": "selective formal verification uncertainty routing mathematical proofs 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JHnFy8XTa1AycJcg15P4KN",
        "content": [
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in ...",
            "url": "https://arxiv.org/pdf/2505.20047"
          },
          {
            "title": "24 January 2026, Preprint v3 · CC-BY 4.0 PREPRINT Review Article",
            "url": "https://www.qeios.com/read/H7D715.3/pdf"
          },
          {
            "title": "Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM",
            "url": "https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"
          },
          {
            "title": "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure",
            "url": "https://arxiv.org/pdf/2602.03975"
          },
          {
            "title": "A Review of Automated Formal Verification of Ad Hoc Routing Protocols   for Wireless Sensor Networks",
            "url": "https://arxiv.org/pdf/1305.7410"
          },
          {
            "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification",
            "url": "https://arxiv.org/pdf/2506.04592"
          },
          {
            "title": "Submitted as a conference paper at ICLR 2026 TYPED CHAIN-OF-THOUGHT:",
            "url": "https://arxiv.org/pdf/2510.01069"
          }
        ]
      },
      "Based on the search results, here are the key findings related to selective formal verification, uncertainty routing, and mathematical proofs from 2025-2026:\n\n## Recent Developments in Formal Verification and Mathematical Reasoning\n\n**Uncertainty-Guided Verification:** Recent work demonstrates how to systematically capture and analyze output uncertainty by modeling LLM-generated formal programs with Probabilistic Context-Free Grammars, rather than just selecting the highest-probability output.\n\n**Selective Verification with Uncertainty:** One approach allocates verification according to state-local uncertainty rather than uniform rules, using learned heuristics that combine distance-to-goal signals with verification budgets that vary based on local uncertainty so that ambiguous branching points receive more verification while clear decisions receive less.\n\n**AI Advances in Mathematical Proofs:** In 2024, AlphaProof became the first AI to achieve silver-medal level in the IMO, followed by strong results from ByteDance and Harmonic in IMO 2025.\n\n**Step-aware Formal Verification:** Recent approaches utilize LLMs to automatically generate formal statements that substantiate the correctness of individual steps, which can be addressed by automated theorem provers, then aggregate these formal proofs to evaluate overall reasoning trajectories.\n\n**Formal Methods in Quantum Verification:** Theorem proving offers the highest level of assurance through rigorous mathematical proofs and is being applied to emerging domains like quantum computing verification."
    ],
    "durationSeconds": 7.843810402000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e8704164-7317-4793-ac54-9194de50be08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T13:13:44.144Z_

<details><summary>↩ Tool result · `toolu_01SxyKiCa5fSL3x2xau9Nayd`</summary>

```text
Web search results for query: "HERMES efficient verifiable mathematical reasoning Ospanov ICML 2026 Lean interleave"

Links: [{"title":"(PDF) HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://www.researchgate.net/publication/397933683_HERMES_Towards_Efficient_and_Verifiable_Mathematical_Reasoning_in_LLMs"},{"title":"ICML Poster HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://icml.cc/virtual/2026/poster/60844"},{"title":"Self-Verifiable Mathematical Reasoning","url":"https://www.emergentmind.com/topics/self-verifiable-mathematical-reasoning"},{"title":"[2511.18760] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760"},{"title":"[2511.18760v1] HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/abs/2511.18760v1"},{"title":"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs","url":"https://arxiv.org/pdf/2511.18760"}]

Based on the search results, here's what I found about HERMES:

HERMES is the first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean. The framework performs intermediate formal checking to prevent reasoning drift and employs a memory module that maintains proof continuity across long, multi-step reasoning chains, enabling both exploration and verification within a single workflow.

HERMES reliably improves the reasoning accuracy of base models while substantially reducing token usage and computational cost compared to reward-based approaches. On difficult datasets such as AIME'25, HERMES achieves up to a 67% accuracy improvement while using 80% fewer total inference FLOPs.

The work is authored by Azim Ospanov, Farzan Farnia, and Roozbeh Yousefzadeh. The implementation and codebase are publicly available at https://github.com/aziksh-ospanov/HERMES.

The paper addresses the fundamental challenge of combining informal mathematical reasoning (which offers flexibility but is prone to errors) with formal theorem proving (which is rigorous and verifiable but lacks exploratory freedom). HERMES appears to be presented at ICML 2026 based on the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9605e7fd-e75f-4fb5-9e28-679818e7f53b",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "90a68087-7fa1-4df9-8918-40a328dc6c4c",
  "toolUseResult": {
    "query": "HERMES efficient verifiable mathematical reasoning Ospanov ICML 2026 Lean interleave",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S4JRb4JKw67Ey8AEmDqPkL",
        "content": [
          {
            "title": "(PDF) HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://www.researchgate.net/publication/397933683_HERMES_Towards_Efficient_and_Verifiable_Mathematical_Reasoning_in_LLMs"
          },
          {
            "title": "ICML Poster HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
            "url": "https://icml.cc/virtual/2026/poster/60844"
          },
          {
            "title": "Self-Verifiable Mathematical Reasoning",
            "url": "https://www.emergentmind.com/topics/self-verifiable-mathematical-reasoning"
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
          }
        ]
      },
      "Based on the search results, here's what I found about HERMES:\n\nHERMES is the first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean. The framework performs intermediate formal checking to prevent reasoning drift and employs a memory module that maintains proof continuity across long, multi-step reasoning chains, enabling both exploration and verification within a single workflow.\n\nHERMES reliably improves the reasoning accuracy of base models while substantially reducing token usage and computational cost compared to reward-based approaches. On difficult datasets such as AIME'25, HERMES achieves up to a 67% accuracy improvement while using 80% fewer total inference FLOPs.\n\nThe work is authored by Azim Ospanov, Farzan Farnia, and Roozbeh Yousefzadeh. The implementation and codebase are publicly available at https://github.com/aziksh-ospanov/HERMES.\n\nThe paper addresses the fundamental challenge of combining informal mathematical reasoning (which offers flexibility but is prone to errors) with formal theorem proving (which is rigorous and verifiable but lacks exploratory freedom). HERMES appears to be presented at ICML 2026 based on the search results."
    ],
    "durationSeconds": 6.747953656000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9605e7fd-e75f-4fb5-9e28-679818e7f53b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-27T13:13:44.202Z_

<details><summary>↩ Tool result · `toolu_014fcwo7Jjv1jybKHLT51vnM`</summary>

```text
Web search results for query: "Pseudo-Formalization automatic proof verification Barkallah 2026 arXiv"

Links: [{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"Baldur: Whole-Proof Generation and Repair with Large Language Models","url":"https://arxiv.org/pdf/2303.04910"},{"title":"Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification","url":"https://arxiv.org/pdf/2603.19715"},{"title":"Automated Conjecture Resolution with Formal Verification","url":"https://arxiv.org/html/2604.03789v1"},{"title":"Automated Conjecture Resolution with Formal Verification","url":"https://arxiv.org/pdf/2604.03789"},{"title":"Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal   Proofs","url":"https://arxiv.org/pdf/2210.12283"}]

I found the research paper you're looking for! Here's what the search revealed:

"Pseudo-Formalization for Automatic Proof Verification" is a paper by Slim Barkallah and colleagues, published on arXiv (2605.20531) on May 19, 2026.

The paper proposes Pseudo-Formalization (PF), a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language. A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language.

The motivation behind this work is that reliable verification of proofs remains a bottleneck for training and evaluating AI systems on hard mathematical reasoning. While fully formal proofs in languages like Lean are easy to verify because they are unambiguous and modular, most proofs, particularly those written by AI systems, have neither property, and translating them into formal languages remains challenging in many frontier math settings.

To verify the correctness of a regular natural language proof, an LLM translates it to Pseudo-Formal and then verifies each module independently, an algorithm they call Block Verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8471b7f5-8411-4133-8c0f-df959cb0873f",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "20928831-6bec-41c8-ab5c-0f5a9009d8d7",
  "toolUseResult": {
    "query": "Pseudo-Formalization automatic proof verification Barkallah 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BUwzHg5nchbh6zVwwrAba3",
        "content": [
          {
            "title": "Pseudo-Formalization for Automatic Proof Verification",
            "url": "https://arxiv.org/html/2605.20531"
          },
          {
            "title": "[2605.20531] Pseudo-Formalization for Automatic Proof Verification",
            "url": "https://arxiv.org/abs/2605.20531"
          },
          {
            "title": "A New Approach Towards Autoformalization",
            "url": "https://arxiv.org/pdf/2310.07957"
          },
          {
            "title": "Baldur: Whole-Proof Generation and Repair with Large Language Models",
            "url": "https://arxiv.org/pdf/2303.04910"
          },
          {
            "title": "Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification",
            "url": "https://arxiv.org/pdf/2603.19715"
          },
          {
            "title": "Automated Conjecture Resolution with Formal Verification",
            "url": "https://arxiv.org/html/2604.03789v1"
          },
          {
            "title": "Automated Conjecture Resolution with Formal Verification",
            "url": "https://arxiv.org/pdf/2604.03789"
          },
          {
            "title": "Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal   Proofs",
            "url": "https://arxiv.org/pdf/2210.12283"
          }
        ]
      },
      "I found the research paper you're looking for! Here's what the search revealed:\n\n\"Pseudo-Formalization for Automatic Proof Verification\" is a paper by Slim Barkallah and colleagues, published on arXiv (2605.20531) on May 19, 2026.\n\nThe paper proposes Pseudo-Formalization (PF), a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language. A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language.\n\nThe motivation behind this work is that reliable verification of proofs remains a bottleneck for training and evaluating AI systems on hard mathematical reasoning. While fully formal proofs in languages like Lean are easy to verify because they are unambiguous and modular, most proofs, particularly those written by AI systems, have neither property, and translating them into formal languages remains challenging in many frontier math settings.\n\nTo verify the correctness of a regular natural language proof, an LLM translates it to Pseudo-Formal and then verifies each module independently, an algorithm they call Block Verification."
    ],
    "durationSeconds": 8.545179319,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8471b7f5-8411-4133-8c0f-df959cb0873f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we ac…",
  "leafUuid": "20928831-6bec-41c8-ab5c-0f5a9009d8d7",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate selective formal verification proposal acceptance probability",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Tool result

_source line 24 · 2026-05-27T13:13:46.211Z_

<details><summary>↩ Tool result · `toolu_01AFEH8Wa8EcvxB8iBV7yHLn`</summary>

```text
Web search results for query: "Ganguly grammars formal uncertainty LLM automated reasoning NeurIPS 2025 selective SMT"

Links: [{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://openreview.net/attachment?id=QfKpJ00t2L&name=pdf"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/grammars-of-formal-uncertainty-when-to-trust-llms-in-automated-reasoning-tasks/"},{"title":"GitHub - DebarghaG/grammars-formal-uncertainty: [NeurIPS 2025] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://github.com/DebarghaG/grammars-formal-uncertainty"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks | OpenReview","url":"https://openreview.net/forum?id=QfKpJ00t2L"},{"title":"[2505.20047] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/abs/2505.20047"},{"title":"NeurIPS Poster Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118114"},{"title":"Paper page - Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://huggingface.co/papers/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/html/2505.20047v1"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in ...","url":"https://arxiv.org/pdf/2505.20047"}]

I found the research paper you're looking for! Here are the key details:

## Paper Overview

"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks" is authored by Debargha Ganguly, Vikash Singh, Sreehari Sankar, Biyao Zhang, Xuecen Zhang, Srinivasan Iyengar, Xiaotian Han, Amit Sharma, S. Kalyanaraman, and Vipin Chaudhary, published at NeurIPS 2025 in May 2025.

## Core Problem and Solution

The paper addresses the fundamental tension that LLMs are probabilistic while formal verification demands deterministic guarantees, by comprehensively investigating failure modes and uncertainty quantification (UQ) in LLM-generated formal artifacts.

## Key Findings

The systematic evaluation of five frontier LLMs reveals SMT-based autoformalization's domain-specific impact on accuracy (from +34.8% on logical tasks to -44.5% on factual ones), with known UQ techniques like entropy of token probabilities failing to identify these errors.

The authors introduce a probabilistic context-free grammar (PCFG) framework to model LLM outputs, with uncertainty signals that are task-dependent (e.g., grammar entropy for logic, AUROC>0.93).

## Practical Impact

A lightweight fusion of uncertainty signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention, transforming LLM-driven formalization into a reliable engineering discipline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6761f7ef-371d-444a-b6f0-08fe25ae5122",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "a559ae29-b523-4487-9285-be2bb23e647f",
  "toolUseResult": {
    "query": "Ganguly grammars formal uncertainty LLM automated reasoning NeurIPS 2025 selective SMT",
    "results": [
      {
        "tool_use_id": "srvtoolu_016vg5MMHb78ccFcSsXtDsi8",
        "content": [
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://openreview.net/attachment?id=QfKpJ00t2L&name=pdf"
          },
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/publication/grammars-of-formal-uncertainty-when-to-trust-llms-in-automated-reasoning-tasks/"
          },
          {
            "title": "GitHub - DebarghaG/grammars-formal-uncertainty: [NeurIPS 2025] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://github.com/DebarghaG/grammars-formal-uncertainty"
          },
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks | OpenReview",
            "url": "https://openreview.net/forum?id=QfKpJ00t2L"
          },
          {
            "title": "[2505.20047] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://arxiv.org/abs/2505.20047"
          },
          {
            "title": "NeurIPS Poster Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/118114"
          },
          {
            "title": "Paper page - Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://huggingface.co/papers/2505.20047"
          },
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks",
            "url": "https://arxiv.org/html/2505.20047v1"
          },
          {
            "title": "Grammars of Formal Uncertainty: When to Trust LLMs in ...",
            "url": "https://arxiv.org/pdf/2505.20047"
          }
        ]
      },
      "I found the research paper you're looking for! Here are the key details:\n\n## Paper Overview\n\n\"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks\" is authored by Debargha Ganguly, Vikash Singh, Sreehari Sankar, Biyao Zhang, Xuecen Zhang, Srinivasan Iyengar, Xiaotian Han, Amit Sharma, S. Kalyanaraman, and Vipin Chaudhary, published at NeurIPS 2025 in May 2025.\n\n## Core Problem and Solution\n\nThe paper addresses the fundamental tension that LLMs are probabilistic while formal verification demands deterministic guarantees, by comprehensively investigating failure modes and uncertainty quantification (UQ) in LLM-generated formal artifacts.\n\n## Key Findings\n\nThe systematic evaluation of five frontier LLMs reveals SMT-based autoformalization's domain-specific impact on accuracy (from +34.8% on logical tasks to -44.5% on factual ones), with known UQ techniques like entropy of token probabilities failing to identify these errors.\n\nThe authors introduce a probabilistic context-free grammar (PCFG) framework to model LLM outputs, with uncertainty signals that are task-dependent (e.g., grammar entropy for logic, AUROC>0.93).\n\n## Practical Impact\n\nA lightweight fusion of uncertainty signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention, transforming LLM-driven formalization into a reliable engineering discipline."
    ],
    "durationSeconds": 8.444499356,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6761f7ef-371d-444a-b6f0-08fe25ae5122",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-27T13:13:49.814Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed the existence of key references. Let me now search for a few more specific papers and concepts mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a559ae29-b523-4487-9285-be2bb23e647f",
  "isSidechain": false,
  "requestId": "req_011CbT8gaT9XT5SJLFBbXg7Y",
  "type": "assistant",
  "uuid": "cd0fd3f2-35b3-47b7-9a01-c170acd6ad65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVomvV5wyCjv1meLSveBR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 20265,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 20265,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 26 · 2026-05-27T13:13:50.317Z_

Good, I've confirmed several key papers. Let me do a few more targeted searches to understand the competitive landscape better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd0fd3f2-35b3-47b7-9a01-c170acd6ad65",
  "isSidechain": false,
  "requestId": "req_011CbT8gaT9XT5SJLFBbXg7Y",
  "type": "assistant",
  "uuid": "612b7174-cb52-4ee3-b4f9-b8b25bc4909c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVomvV5wyCjv1meLSveBR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 20265,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 20265,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 27 · 2026-05-27T13:13:51.310Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011dSLWqsZkZpMaHtkzUtDwg`</summary>

```json
{
  "query": "miniF2F-Lean Revisited limitations autoformalization NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "612b7174-cb52-4ee3-b4f9-b8b25bc4909c",
  "isSidechain": false,
  "requestId": "req_011CbT8gaT9XT5SJLFBbXg7Y",
  "type": "assistant",
  "uuid": "40f28efb-bfbc-4b17-a16e-30c123f87098",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVomvV5wyCjv1meLSveBR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 20265,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 20265,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 28 · 2026-05-27T13:13:52.199Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B6VbModkYbEpZiiSdaNiA1`</summary>

```json
{
  "query": "process-driven autoformalization Lean 4 step-level 2024 block-level formalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40f28efb-bfbc-4b17-a16e-30c123f87098",
  "isSidechain": false,
  "requestId": "req_011CbT8gaT9XT5SJLFBbXg7Y",
  "type": "assistant",
  "uuid": "59678f03-1f2a-4cf4-839f-cb43bd63cc0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVomvV5wyCjv1meLSveBR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 20265,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 20265,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 29 · 2026-05-27T13:13:53.136Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U2c6r4wbxiBbV69RprsQjw`</summary>

```json
{
  "query": "StepFun-Formalizer-32B autoformalization Goedel-Prover-V2 theorem proving 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59678f03-1f2a-4cf4-839f-cb43bd63cc0e",
  "isSidechain": false,
  "requestId": "req_011CbT8gaT9XT5SJLFBbXg7Y",
  "type": "assistant",
  "uuid": "0d95fc78-decb-4ebe-9a3f-5b4005ff5c29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVomvV5wyCjv1meLSveBR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 20265,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 20265,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 30 · 2026-05-27T13:13:53.897Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NJkZsxfQkVrpeziS95vaJq`</summary>

```json
{
  "query": "ThinkPRM process reward model verbalized 2025 step verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d95fc78-decb-4ebe-9a3f-5b4005ff5c29",
  "isSidechain": false,
  "requestId": "req_011CbT8gaT9XT5SJLFBbXg7Y",
  "type": "assistant",
  "uuid": "407cc88a-5776-4b90-951e-33129cc18950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVomvV5wyCjv1meLSveBR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 20265,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 20265,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 31 · 2026-05-27T13:13:57.589Z_

<details><summary>↩ Tool result · `toolu_011dSLWqsZkZpMaHtkzUtDwg`</summary>

```text
Web search results for query: "miniF2F-Lean Revisited limitations autoformalization NeurIPS 2025"

Links: [{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward | OpenReview","url":"https://openreview.net/forum?id=KtaHv0YUyh"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://openreview.net/pdf?id=KtaHv0YUyh"},{"title":"[2511.03108] miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/abs/2511.03108"},{"title":"[Quick Review] miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://liner.com/review/minif2flean-revisited-reviewing-limitations-and-charting-path-forward"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/html/2511.03108v1"},{"title":"Paper page - miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://huggingface.co/papers/2511.03108"},{"title":"(PDF) miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://www.researchgate.net/publication/397322220_miniF2F-Lean_Revisited_Reviewing_Limitations_and_Charting_a_Path_Forward"},{"title":"NeurIPS Poster miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://neurips.cc/virtual/2025/poster/118598"}]

Based on the search results, here's what I found about the "miniF2F-Lean Revisited" paper:

## Overview

This is a NeurIPS 2025 paper that performs a thorough analysis of the formal and informal statements in the miniF2F benchmark from the perspective of an AI system tasked to participate in a math Olympiad.

## Key Limitations and Findings

The paper identifies significant limitations in current autoformalization approaches:

1. **End-to-End Accuracy Gap**: The best accuracy of the full pipeline can be about 36% using state-of-the-art models, considerably lower than the individual state-of-the-art accuracies of 97% and 69% reported in the autoformalization and theorem proving literature.

2. **Discrepancies in Benchmarks**: A considerable portion of the accuracy drop traces back to discrepancies between the formal and informal statements for more than half of the problems in miniF2F.

3. **Inflated Reported Accuracies**: The reported accuracy of autoformalization models in the literature are largely inflated as those evaluations are typically performed by LLMs; for example, when human review was performed on Herald outputs that LLM marked as 97% correct, the actual accuracy was 66%.

## Solution: miniF2F-v2

The researchers corrected all errors, discrepancies and simplifications in formal and informal statements, presenting miniF2F-v2 with fully verified statements and proofs, which achieves 70% accuracy on the full theorem proving pipeline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40f28efb-bfbc-4b17-a16e-30c123f87098",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "838eb769-b94a-4a6e-ab1a-d1e7de6e4375",
  "toolUseResult": {
    "query": "miniF2F-Lean Revisited limitations autoformalization NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QbgDSspn5CZ3oVsZq6gH9N",
        "content": [
          {
            "title": "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward | OpenReview",
            "url": "https://openreview.net/forum?id=KtaHv0YUyh"
          },
          {
            "title": "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward",
            "url": "https://openreview.net/pdf?id=KtaHv0YUyh"
          },
          {
            "title": "[2511.03108] miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward",
            "url": "https://arxiv.org/abs/2511.03108"
          },
          {
            "title": "[Quick Review] miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward",
            "url": "https://liner.com/review/minif2flean-revisited-reviewing-limitations-and-charting-path-forward"
          },
          {
            "title": "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward",
            "url": "https://arxiv.org/html/2511.03108v1"
          },
          {
            "title": "Paper page - miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward",
            "url": "https://huggingface.co/papers/2511.03108"
          },
          {
            "title": "(PDF) miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward",
            "url": "https://www.researchgate.net/publication/397322220_miniF2F-Lean_Revisited_Reviewing_Limitations_and_Charting_a_Path_Forward"
          },
          {
            "title": "NeurIPS Poster miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward",
            "url": "https://neurips.cc/virtual/2025/poster/118598"
          }
        ]
      },
      "Based on the search results, here's what I found about the \"miniF2F-Lean Revisited\" paper:\n\n## Overview\n\nThis is a NeurIPS 2025 paper that performs a thorough analysis of the formal and informal statements in the miniF2F benchmark from the perspective of an AI system tasked to participate in a math Olympiad.\n\n## Key Limitations and Findings\n\nThe paper identifies significant limitations in current autoformalization approaches:\n\n1. **End-to-End Accuracy Gap**: The best accuracy of the full pipeline can be about 36% using state-of-the-art models, considerably lower than the individual state-of-the-art accuracies of 97% and 69% reported in the autoformalization and theorem proving literature.\n\n2. **Discrepancies in Benchmarks**: A considerable portion of the accuracy drop traces back to discrepancies between the formal and informal statements for more than half of the problems in miniF2F.\n\n3. **Inflated Reported Accuracies**: The reported accuracy of autoformalization models in the literature are largely inflated as those evaluations are typically performed by LLMs; for example, when human review was performed on Herald outputs that LLM marked as 97% correct, the actual accuracy was 66%.\n\n## Solution: miniF2F-v2\n\nThe researchers corrected all errors, discrepancies and simplifications in formal and informal statements, presenting miniF2F-v2 with fully verified statements and proofs, which achieves 70% accuracy on the full theorem proving pipeline."
    ],
    "durationSeconds": 6.274930821000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "40f28efb-bfbc-4b17-a16e-30c123f87098",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-27T13:13:59.575Z_

<details><summary>↩ Tool result · `toolu_01B6VbModkYbEpZiiSdaNiA1`</summary>

```text
Web search results for query: "process-driven autoformalization Lean 4 step-level 2024 block-level formalization"

Links: [{"title":"(PDF) Process-Driven Autoformalization in Lean 4","url":"https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4"},{"title":"PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://openreview.net/pdf?id=k8KsI84Ds7"},{"title":"Work in progress PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://arxiv.org/pdf/2406.01940"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/html/2406.01940v1"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"FORMAL: DEMOCRATIZING LEAN 4 FORMALIZATION","url":"https://mustafasameen.github.io/assets/publications/2025-formal/paper.pdf"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://github.com/rookie-joe/PDA"},{"title":"[2406.01940] Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/abs/2406.01940"},{"title":"[PDF] Process-Driven Autoformalization in Lean 4 | Semantic Scholar","url":"https://www.semanticscholar.org/paper/db0f9376882cf7805f36def33600805d330e5386"}]

Based on the search results, I found relevant information about process-driven autoformalization in Lean 4:

## Process-Driven Autoformalization in Lean 4

Autoformalization is the conversion of natural language mathematics into formal languages, which offers significant potential for advancing mathematical reasoning. Existing efforts are limited to formal languages with substantial online corpora and struggle to keep pace with rapidly evolving languages like Lean 4.

### Key Innovation: Step-Level Process Information

One key advantage of formal languages is that their compilers can provide detailed step-level information on generated proofs. FormL4 can fully utilize feedback from the Lean 4 compiler, which encompasses both syntax checking and reasoning verification.

### The Framework

A Process-Driven Autoformalization (PDA) framework was proposed for iterative performance improvement and automated assessment, beginning with training an autoformalization model on FORML4. The model's output is then processed by the Lean 4 Compiler, generating automated feedback that generates process-level proofs in natural and formal languages.

### Performance Improvements

Extensive experiments demonstrate that a process-supervised verifier (PSV) can significantly enhance the autoformalizer, enabling it to achieve higher performance in autoformalization using less filtered training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59678f03-1f2a-4cf4-839f-cb43bd63cc0e",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "67800665-3648-456e-a09a-dec93ae982fe",
  "toolUseResult": {
    "query": "process-driven autoformalization Lean 4 step-level 2024 block-level formalization",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Dgsbvd4x5LNjMy64PEUxpM",
        "content": [
          {
            "title": "(PDF) Process-Driven Autoformalization in Lean 4",
            "url": "https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4"
          },
          {
            "title": "PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4",
            "url": "https://openreview.net/pdf?id=k8KsI84Ds7"
          },
          {
            "title": "Work in progress PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4",
            "url": "https://arxiv.org/pdf/2406.01940"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/html/2406.01940v1"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4 | OpenReview",
            "url": "https://openreview.net/forum?id=k8KsI84Ds7"
          },
          {
            "title": "FORMAL: DEMOCRATIZING LEAN 4 FORMALIZATION",
            "url": "https://mustafasameen.github.io/assets/publications/2025-formal/paper.pdf"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://github.com/rookie-joe/PDA"
          },
          {
            "title": "[2406.01940] Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/abs/2406.01940"
          },
          {
            "title": "[PDF] Process-Driven Autoformalization in Lean 4 | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/db0f9376882cf7805f36def33600805d330e5386"
          }
        ]
      },
      "Based on the search results, I found relevant information about process-driven autoformalization in Lean 4:\n\n## Process-Driven Autoformalization in Lean 4\n\nAutoformalization is the conversion of natural language mathematics into formal languages, which offers significant potential for advancing mathematical reasoning. Existing efforts are limited to formal languages with substantial online corpora and struggle to keep pace with rapidly evolving languages like Lean 4.\n\n### Key Innovation: Step-Level Process Information\n\nOne key advantage of formal languages is that their compilers can provide detailed step-level information on generated proofs. FormL4 can fully utilize feedback from the Lean 4 compiler, which encompasses both syntax checking and reasoning verification.\n\n### The Framework\n\nA Process-Driven Autoformalization (PDA) framework was proposed for iterative performance improvement and automated assessment, beginning with training an autoformalization model on FORML4. The model's output is then processed by the Lean 4 Compiler, generating automated feedback that generates process-level proofs in natural and formal languages.\n\n### Performance Improvements\n\nExtensive experiments demonstrate that a process-supervised verifier (PSV) can significantly enhance the autoformalizer, enabling it to achieve higher performance in autoformalization using less filtered training data."
    ],
    "durationSeconds": 7.372121479000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "59678f03-1f2a-4cf4-839f-cb43bd63cc0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-27T13:14:03.185Z_

<details><summary>↩ Tool result · `toolu_01NJkZsxfQkVrpeziS95vaJq`</summary>

```text
Web search results for query: "ThinkPRM process reward model verbalized 2025 step verification"

Links: [{"title":"ThinkPRM: Data-Efficient Process Reward Models","url":"https://www.emergentmind.com/papers/2504.16828"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"ThinkPRM: Process Reward Models That Think","url":"https://mukhal.github.io/projects/thinkprm/"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Process Reward Models That Think | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.16828v5"},{"title":"[2504.16828v1] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"},{"title":"(PDF) Process Reward Models That Think","url":"https://www.researchgate.net/publication/391058520_Process_Reward_Models_That_Think"}]

Based on the search results, here's what I found about ThinkPRM:

## Overview

ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. It is designed as a verbalized step-wise reward model that verifies every step in the solution by generating a verification chain-of-thought (CoT).

## Key Innovation

The main approach involves generating detailed reasoning chains to verify each solution step instead of binary judgments. The goal is a verbalized PRM that, given a problem-solution pair, verifies every step in the solution via an extended chain-of-thought (CoT).

## Performance Results

ThinkPRM outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks. ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search.

## Training Efficiency

By utilizing verbalized step-wise reward models, ThinkPRM achieves state-of-the-art performance with just 1% of the training data required by traditional approaches.

The paper was published in April 2025 and represents an advancement in making process reward models more data-efficient and interpretable for AI reasoning verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "407cc88a-5776-4b90-951e-33129cc18950",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "53fe9ed0-f002-48f8-9a81-e5fb66c1225d",
  "toolUseResult": {
    "query": "ThinkPRM process reward model verbalized 2025 step verification",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VM7VktnVfCzJMhNnihhxJy",
        "content": [
          {
            "title": "ThinkPRM: Data-Efficient Process Reward Models",
            "url": "https://www.emergentmind.com/papers/2504.16828"
          },
          {
            "title": "Paper page - Process Reward Models That Think",
            "url": "https://huggingface.co/papers/2504.16828"
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
            "title": "ThinkPRM: Process Reward Models That Think",
            "url": "https://mukhal.github.io/projects/thinkprm/"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "Process Reward Models That Think | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2504.16828v5"
          },
          {
            "title": "[2504.16828v1] Process Reward Models That Think",
            "url": "https://arxiv.org/abs/2504.16828v1"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"
          },
          {
            "title": "(PDF) Process Reward Models That Think",
            "url": "https://www.researchgate.net/publication/391058520_Process_Reward_Models_That_Think"
          }
        ]
      },
      "Based on the search results, here's what I found about ThinkPRM:\n\n## Overview\n\nThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. It is designed as a verbalized step-wise reward model that verifies every step in the solution by generating a verification chain-of-thought (CoT).\n\n## Key Innovation\n\nThe main approach involves generating detailed reasoning chains to verify each solution step instead of binary judgments. The goal is a verbalized PRM that, given a problem-solution pair, verifies every step in the solution via an extended chain-of-thought (CoT).\n\n## Performance Results\n\nThinkPRM outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks. ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search.\n\n## Training Efficiency\n\nBy utilizing verbalized step-wise reward models, ThinkPRM achieves state-of-the-art performance with just 1% of the training data required by traditional approaches.\n\nThe paper was published in April 2025 and represents an advancement in making process reward models more data-efficient and interpretable for AI reasoning verification."
    ],
    "durationSeconds": 9.285412566,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "407cc88a-5776-4b90-951e-33129cc18950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we ac…",
  "leafUuid": "53fe9ed0-f002-48f8-9a81-e5fb66c1225d",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate selective formal verification proposal acceptance probability",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Tool result

_source line 36 · 2026-05-27T13:14:09.143Z_

<details><summary>↩ Tool result · `toolu_01U2c6r4wbxiBbV69RprsQjw`</summary>

```text
Web search results for query: "StepFun-Formalizer-32B autoformalization Goedel-Prover-V2 theorem proving 2026"

Links: [{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"},{"title":"StepFun-Formalizer-32B: Autoformalization LLM","url":"https://www.emergentmind.com/topics/stepfun-formalizer-32b"},{"title":"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction","url":"https://arxiv.org/pdf/2508.03613"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40691"},{"title":"stepfun-ai/StepFun-Formalizer-32B · Hugging Face","url":"https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion","url":"https://arxiv.org/html/2508.04440v2"},{"title":"[2508.04440] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/abs/2508.04440"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/html/2510.06857v1"}]

Based on the search results, here's what I found:

## StepFun-Formalizer-32B

StepFun-Formalizer-32B is a large language model designed to autoformalize informal mathematical statements into rigorous Lean 4 code. It employs a hybrid training pipeline combining knowledge distillation, template-guided reasoning, and reinforcement learning with verifiable rewards.

StepFun-Formalizer-32B achieves SOTA BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench, surpassing all prior general-purpose and specialized models.

## Goedel-Prover-V2

Goedel-Prover-V2-32B achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in selfcorrection mode, outperforming prior SOTA by a large margin. The flagship model solves 86 problems on PutnamBench at pass@184, securing the first place among open-source models on the leaderboard, surpassing DeepSeek-Prover-V2-671B's record of solving 47 problems.

At the time of its release (July-August 2025), Goedel-Prover-V2 achieves the strongest overall performance among all open-source theorem provers.

Both models represent significant advances in formal mathematics and automated theorem proving capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d95fc78-decb-4ebe-9a3f-5b4005ff5c29",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "16d74da9-4856-4fe2-87f9-2c1d3df3d3dc",
  "toolUseResult": {
    "query": "StepFun-Formalizer-32B autoformalization Goedel-Prover-V2 theorem proving 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01As17XZbwuD3beV4DsDQiWG",
        "content": [
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential",
            "url": "https://www.arxiv.org/pdf/2508.04440"
          },
          {
            "title": "StepFun-Formalizer-32B: Autoformalization LLM",
            "url": "https://www.emergentmind.com/topics/stepfun-formalizer-32b"
          },
          {
            "title": "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction",
            "url": "https://arxiv.org/pdf/2508.03613"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40691"
          },
          {
            "title": "stepfun-ai/StepFun-Formalizer-32B · Hugging Face",
            "url": "https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/html/2508.04440v2"
          },
          {
            "title": "[2508.04440] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/abs/2508.04440"
          },
          {
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/html/2510.06857v1"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\n## StepFun-Formalizer-32B\n\nStepFun-Formalizer-32B is a large language model designed to autoformalize informal mathematical statements into rigorous Lean 4 code. It employs a hybrid training pipeline combining knowledge distillation, template-guided reasoning, and reinforcement learning with verifiable rewards.\n\nStepFun-Formalizer-32B achieves SOTA BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench, surpassing all prior general-purpose and specialized models.\n\n## Goedel-Prover-V2\n\nGoedel-Prover-V2-32B achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in selfcorrection mode, outperforming prior SOTA by a large margin. The flagship model solves 86 problems on PutnamBench at pass@184, securing the first place among open-source models on the leaderboard, surpassing DeepSeek-Prover-V2-671B's record of solving 47 problems.\n\nAt the time of its release (July-August 2025), Goedel-Prover-V2 achieves the strongest overall performance among all open-source theorem provers.\n\nBoth models represent significant advances in formal mathematics and automated theorem proving capabilities."
    ],
    "durationSeconds": 16.003365341,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0d95fc78-decb-4ebe-9a3f-5b4005ff5c29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-27T13:14:09.149Z_

```json
{
  "parentUuid": "16d74da9-4856-4fe2-87f9-2c1d3df3d3dc",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "21259d7c-4327-48fd-baa9-25bd832177bd",
  "timestamp": "2026-05-27T13:14:09.149Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-27T13:14:13.344Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for a couple more things to be thorough - particularly around whether the specific combination of ideas in this proposal has already been done, and around the ArxivMathGradingBench benchmark.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21259d7c-4327-48fd-baa9-25bd832177bd",
  "isSidechain": false,
  "requestId": "req_011CbT8iGc9zj1xw7XPB4dRB",
  "type": "assistant",
  "uuid": "9b9f7e2e-72c2-4073-9dac-23d0843b6035",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LF1RZHBwikbbWQ54W2SeyX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 2900,
      "cache_read_input_tokens": 24236,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 256,
          "cache_read_input_tokens": 24236,
          "cache_creation_input_tokens": 2900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2900
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

_source line 39 · 2026-05-27T13:14:14.026Z_

Let me do a few more critical searches to round out my understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b9f7e2e-72c2-4073-9dac-23d0843b6035",
  "isSidechain": false,
  "requestId": "req_011CbT8iGc9zj1xw7XPB4dRB",
  "type": "assistant",
  "uuid": "9f452ae0-4c28-4021-85dc-5a4bda93a3df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LF1RZHBwikbbWQ54W2SeyX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 2900,
      "cache_read_input_tokens": 24236,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 256,
          "cache_read_input_tokens": 24236,
          "cache_creation_input_tokens": 2900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2900
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

_source line 40 · 2026-05-27T13:14:14.340Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fo4A2YYP4atEh3fdtHvELg`</summary>

```json
{
  "query": "ArxivMathGradingBench benchmark mathematical proof grading research-level 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f452ae0-4c28-4021-85dc-5a4bda93a3df",
  "isSidechain": false,
  "requestId": "req_011CbT8iGc9zj1xw7XPB4dRB",
  "type": "assistant",
  "uuid": "9a0a0c9f-fdf4-4a88-bacc-1b895b64aaa7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LF1RZHBwikbbWQ54W2SeyX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 2900,
      "cache_read_input_tokens": 24236,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 256,
          "cache_read_input_tokens": 24236,
          "cache_creation_input_tokens": 2900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2900
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

_source line 41 · 2026-05-27T13:14:15.744Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X9tXQKj8fv6jLujWt5Mqmo`</summary>

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
  "parentUuid": "9a0a0c9f-fdf4-4a88-bacc-1b895b64aaa7",
  "isSidechain": false,
  "requestId": "req_011CbT8iGc9zj1xw7XPB4dRB",
  "type": "assistant",
  "uuid": "834bd8ca-435d-4c91-84c4-badbbe406d64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LF1RZHBwikbbWQ54W2SeyX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 2900,
      "cache_read_input_tokens": 24236,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 256,
          "cache_read_input_tokens": 24236,
          "cache_creation_input_tokens": 2900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2900
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

_source line 42 · 2026-05-27T13:14:16.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014QutZXzPLNgD72kfvTXfCc`</summary>

```json
{
  "query": "uncertainty calibration LLM ensemble disagreement proof verification routing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "834bd8ca-435d-4c91-84c4-badbbe406d64",
  "isSidechain": false,
  "requestId": "req_011CbT8iGc9zj1xw7XPB4dRB",
  "type": "assistant",
  "uuid": "6238ede9-7d21-4fbe-9ff8-f3302487f06d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LF1RZHBwikbbWQ54W2SeyX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 2900,
      "cache_read_input_tokens": 24236,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 256,
          "cache_read_input_tokens": 24236,
          "cache_creation_input_tokens": 2900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2900
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

_source line 43 · 2026-05-27T13:14:23.730Z_

<details><summary>↩ Tool result · `toolu_01X9tXQKj8fv6jLujWt5Mqmo`</summary>

```text
Web search results for query: "VERGE formal refinement guidance engine verifiable LLM reasoning Singh 2026 SMT solver routing"

Links: [{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055v2"},{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News","url":"https://news.ycombinator.com/item?id=46813257"}]

Based on the web search results, here's what I found about VERGE:

## Overview

VERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. The paper was authored by Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, and Sam Bayless (2026).

## Key Features

The approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving.

The framework includes three main innovations:

1. **Multi-Model Consensus**: VERGE generates multiple candidate logical formulas for each claim and checks for semantic equivalence between candidates rather than relying on superficial syntactic metrics.

2. **Semantic Routing**: This dynamically classifies atomic claims to handle non-formalizable natural language; verifiable logic is sent to SMT solvers (Z3) for proof, while ambiguous or commonsense claims are routed to a consensus-based "soft verifier."

3. **Precise Error Localization**: Minimal Correction Subsets (MCS) pinpoint the precise subset of conflicting claims to revise, enabling the model to iteratively refine its reasoning with an 18.7% performance uplift.

## Performance

VERGE demonstrated an average performance uplift of 18.7% at convergence across reasoning benchmarks (FOLIO, ZebraLogic, AR-LSAT, BBEH, HLE) compared to single-pass approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "834bd8ca-435d-4c91-84c4-badbbe406d64",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "545301e7-f0a3-45c4-b4b5-d3e442588671",
  "toolUseResult": {
    "query": "VERGE formal refinement guidance engine verifiable LLM reasoning Singh 2026 SMT solver routing",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QQSVqUcum6fDNAV7ZrZBd2",
        "content": [
          {
            "title": "[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/abs/2601.20055"
          },
          {
            "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/html/2601.20055v2"
          },
          {
            "title": "Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://huggingface.co/papers/2601.20055"
          },
          {
            "title": "[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"
          },
          {
            "title": "dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.",
            "url": "https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"
          },
          {
            "title": "Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News",
            "url": "https://news.ycombinator.com/item?id=46813257"
          }
        ]
      },
      "Based on the web search results, here's what I found about VERGE:\n\n## Overview\n\nVERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement. The paper was authored by Vikash Singh, Darion Cassel, Nathaniel Weir, Nick Feng, and Sam Bayless (2026).\n\n## Key Features\n\nThe approach decomposes LLM outputs into atomic claims, autoformalizes them into first-order logic, and verifies their logical consistency using automated theorem proving.\n\nThe framework includes three main innovations:\n\n1. **Multi-Model Consensus**: VERGE generates multiple candidate logical formulas for each claim and checks for semantic equivalence between candidates rather than relying on superficial syntactic metrics.\n\n2. **Semantic Routing**: This dynamically classifies atomic claims to handle non-formalizable natural language; verifiable logic is sent to SMT solvers (Z3) for proof, while ambiguous or commonsense claims are routed to a consensus-based \"soft verifier.\"\n\n3. **Precise Error Localization**: Minimal Correction Subsets (MCS) pinpoint the precise subset of conflicting claims to revise, enabling the model to iteratively refine its reasoning with an 18.7% performance uplift.\n\n## Performance\n\nVERGE demonstrated an average performance uplift of 18.7% at convergence across reasoning benchmarks (FOLIO, ZebraLogic, AR-LSAT, BBEH, HLE) compared to single-pass approaches."
    ],
    "durationSeconds": 7.982162183000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "834bd8ca-435d-4c91-84c4-badbbe406d64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-27T13:14:24.688Z_

<details><summary>↩ Tool result · `toolu_01Fo4A2YYP4atEh3fdtHvELg`</summary>

```text
Web search results for query: "ArxivMathGradingBench benchmark mathematical proof grading research-level 2026"

Links: [{"title":"LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics","url":"https://arxiv.org/html/2602.24173v1"},{"title":"IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation | OpenReview","url":"https://openreview.net/forum?id=219Pn3D4Md"},{"title":"IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation","url":"https://arxiv.org/html/2509.26076v1"},{"title":"[2509.26076v1] IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation","url":"https://arxiv.org/abs/2509.26076v1"},{"title":"[2509.26076] IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation","url":"https://arxiv.org/abs/2509.26076"},{"title":"IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation","url":"https://arxiv.org/pdf/2509.26076"},{"title":"LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics","url":"https://arxiv.org/pdf/2602.24173"},{"title":"QEDBench: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs","url":"https://arxiv.org/html/2602.20629v1"}]

Based on the search results, I found relevant information about research-level mathematical proof grading benchmarks from 2025-2026, though the exact "ArxivMathGradingBench" benchmark wasn't returned. Here are the key benchmarks for evaluating mathematical proof grading:

## Recent Research-Level Mathematical Proof Grading Benchmarks

**IMProofBench** - A private benchmark consisting of 39 peer-reviewed problems developed by expert mathematicians, where each problem requires a detailed proof and is paired with subproblems that have final answers, supporting both human expert evaluation and automated grading. GPT-5 obtains the best performance for proof generation, achieving a fully correct solution for 22% of problems.

**LemmaBench** - A live benchmark built directly from the latest research-level mathematical results proved by mathematicians on the arXiv. Two iterations of the benchmark have been performed—one in September 2025 corresponding to articles submitted in August 2025 and another in February 2026 corresponding to articles submitted in the first week of February 2026.

**QEDBench** - A public benchmark for evaluating and improving AI judges of mathematical proofs.

These benchmarks represent the current state of research-level mathematical proof evaluation and grading in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a0a0c9f-fdf4-4a88-bacc-1b895b64aaa7",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "5b5466ac-e691-481a-8b82-f4f3a4dd8074",
  "toolUseResult": {
    "query": "ArxivMathGradingBench benchmark mathematical proof grading research-level 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y9cK3PiExVre6D1A1VN5Jv",
        "content": [
          {
            "title": "LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics",
            "url": "https://arxiv.org/html/2602.24173v1"
          },
          {
            "title": "IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation | OpenReview",
            "url": "https://openreview.net/forum?id=219Pn3D4Md"
          },
          {
            "title": "IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation",
            "url": "https://arxiv.org/html/2509.26076v1"
          },
          {
            "title": "[2509.26076v1] IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation",
            "url": "https://arxiv.org/abs/2509.26076v1"
          },
          {
            "title": "[2509.26076] IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation",
            "url": "https://arxiv.org/abs/2509.26076"
          },
          {
            "title": "IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation",
            "url": "https://arxiv.org/pdf/2509.26076"
          },
          {
            "title": "LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics",
            "url": "https://arxiv.org/pdf/2602.24173"
          },
          {
            "title": "QEDBench: Quantifying the Alignment Gap in Automated Evaluation of University-Level Mathematical Proofs",
            "url": "https://arxiv.org/html/2602.20629v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about research-level mathematical proof grading benchmarks from 2025-2026, though the exact \"ArxivMathGradingBench\" benchmark wasn't returned. Here are the key benchmarks for evaluating mathematical proof grading:\n\n## Recent Research-Level Mathematical Proof Grading Benchmarks\n\n**IMProofBench** - A private benchmark consisting of 39 peer-reviewed problems developed by expert mathematicians, where each problem requires a detailed proof and is paired with subproblems that have final answers, supporting both human expert evaluation and automated grading. GPT-5 obtains the best performance for proof generation, achieving a fully correct solution for 22% of problems.\n\n**LemmaBench** - A live benchmark built directly from the latest research-level mathematical results proved by mathematicians on the arXiv. Two iterations of the benchmark have been performed—one in September 2025 corresponding to articles submitted in August 2025 and another in February 2026 corresponding to articles submitted in the first week of February 2026.\n\n**QEDBench** - A public benchmark for evaluating and improving AI judges of mathematical proofs.\n\nThese benchmarks represent the current state of research-level mathematical proof evaluation and grading in 2025-2026."
    ],
    "durationSeconds": 10.343669881000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9a0a0c9f-fdf4-4a88-bacc-1b895b64aaa7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-27T13:14:28.392Z_

<details><summary>↩ Tool result · `toolu_014QutZXzPLNgD72kfvTXfCc`</summary>

```text
Web search results for query: "uncertainty calibration LLM ensemble disagreement proof verification routing 2025 2026"

Links: [{"title":"A Survey of Confidence Estimation and Calibration in Large Language Models","url":"https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"},{"title":"LLM Calibration and Uncertainty Quantification in Production AI Agents | Zylos Research","url":"https://zylos.ai/research/2026-04-18-llm-calibration-uncertainty-production-agents"},{"title":"Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification","url":"https://arxiv.org/html/2604.17112v1"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"},{"title":"DiscoUQ: Structured Disagreement Analysis for Uncertainty Quantification in LLM Agent Ensembles","url":"https://arxiv.org/pdf/2603.20975"},{"title":"GitHub - userTogrul/large-model-calibration-and-uncertainty: A collection of source codes for various methods of quantification of uncertainty and calibration in large models. · GitHub","url":"https://github.com/userTogrul/large-model-calibration-and-uncertainty"},{"title":"Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey","url":"https://arxiv.org/html/2503.15850"}]

Based on the web search results, here's what I found regarding uncertainty calibration, LLM ensemble disagreement, proof verification, and routing in 2025-2026:

## Recent Developments in LLM Calibration and Uncertainty (2025-2026)

**Calibration Methods and Training Approaches:**

An ICML 2025 paper introduces CFT as a modification of the fine-tuning objective that explicitly preserves calibration properties alongside optimizing for helpfulness. The key insight is that the tradeoff between alignment and calibration is not fundamental — it is an artifact of current training procedures that ignore calibration in the loss function. By adding a calibration regularization term, CFT dramatically reduces ECE while maintaining or improving accuracy.

**Ensemble Disagreement and Uncertainty Quantification:**

Multi-agent LLM systems, in which several role-specialized instances of a language model independently reason about the same question, have emerged as a powerful paradigm for improving both accuracy and robustness. Researchers formalize the notion of disagreement structure in multi-agent LLM systems as a set of linguistically and geometrically motivated features. Three methods of increasing complexity—DISCOUQ-LLM, DISCOUQ-Embed, and DISCOUQ-Learn—use these features for uncertainty quantification, with DISCOUQ-LLM achieving the best average AUROC (0.802) and best calibration (ECE 0.036).

**Routing and Decision-Making:**

Calibrated LLM judges enable systems to route straightforward cases to efficient models while reserving expensive judges or human reviewers for uncertain decisions, dramatically reducing computational and labor costs.

**Verification Under Uncertainty:**

A 2025 paper titled "Verify when Uncertain: Beyond Self-Consistency in Black Box Hallucination Detection" by Xue et al. addresses uncertainty-aware verification approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6238ede9-7d21-4fbe-9ff8-f3302487f06d",
  "isSidechain": false,
  "promptId": "9ae99baa-2fb4-4bee-a538-53cbdfbb618a",
  "type": "user",
  "uuid": "813e521f-16a4-4d48-b8a5-9dd9cba1af6a",
  "toolUseResult": {
    "query": "uncertainty calibration LLM ensemble disagreement proof verification routing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013mXBmxKEvKadqPsao6YCiv",
        "content": [
          {
            "title": "A Survey of Confidence Estimation and Calibration in Large Language Models",
            "url": "https://www.researchgate.net/publication/382633391_A_Survey_of_Confidence_Estimation_and_Calibration_in_Large_Language_Models"
          },
          {
            "title": "LLM Calibration and Uncertainty Quantification in Production AI Agents | Zylos Research",
            "url": "https://zylos.ai/research/2026-04-18-llm-calibration-uncertainty-production-agents"
          },
          {
            "title": "Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification",
            "url": "https://arxiv.org/html/2604.17112v1"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/pdf/2512.22245"
          },
          {
            "title": "DiscoUQ: Structured Disagreement Analysis for Uncertainty Quantification in LLM Agent Ensembles",
            "url": "https://arxiv.org/pdf/2603.20975"
          },
          {
            "title": "GitHub - userTogrul/large-model-calibration-and-uncertainty: A collection of source codes for various methods of quantification of uncertainty and calibration in large models. · GitHub",
            "url": "https://github.com/userTogrul/large-model-calibration-and-uncertainty"
          },
          {
            "title": "Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2503.15850"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding uncertainty calibration, LLM ensemble disagreement, proof verification, and routing in 2025-2026:\n\n## Recent Developments in LLM Calibration and Uncertainty (2025-2026)\n\n**Calibration Methods and Training Approaches:**\n\nAn ICML 2025 paper introduces CFT as a modification of the fine-tuning objective that explicitly preserves calibration properties alongside optimizing for helpfulness. The key insight is that the tradeoff between alignment and calibration is not fundamental — it is an artifact of current training procedures that ignore calibration in the loss function. By adding a calibration regularization term, CFT dramatically reduces ECE while maintaining or improving accuracy.\n\n**Ensemble Disagreement and Uncertainty Quantification:**\n\nMulti-agent LLM systems, in which several role-specialized instances of a language model independently reason about the same question, have emerged as a powerful paradigm for improving both accuracy and robustness. Researchers formalize the notion of disagreement structure in multi-agent LLM systems as a set of linguistically and geometrically motivated features. Three methods of increasing complexity—DISCOUQ-LLM, DISCOUQ-Embed, and DISCOUQ-Learn—use these features for uncertainty quantification, with DISCOUQ-LLM achieving the best average AUROC (0.802) and best calibration (ECE 0.036).\n\n**Routing and Decision-Making:**\n\nCalibrated LLM judges enable systems to route straightforward cases to efficient models while reserving expensive judges or human reviewers for uncertain decisions, dramatically reducing computational and labor costs.\n\n**Verification Under Uncertainty:**\n\nA 2025 paper titled \"Verify when Uncertain: Beyond Self-Consistency in Black Box Hallucination Detection\" by Xue et al. addresses uncertainty-aware verification approaches."
    ],
    "durationSeconds": 12.188437865000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6238ede9-7d21-4fbe-9ff8-f3302487f06d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we ac…",
  "leafUuid": "813e521f-16a4-4d48-b8a5-9dd9cba1af6a",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate selective formal verification proposal acceptance probability",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Assistant

_source line 48 · 2026-05-27T13:15:35.683Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the field. Let me now carefully evaluate this proposal.

### Understanding the Proposal

The core idea is:
1. Use Pseudo-Formalization (PF) to decompose natural language mathematical proofs into self-contained blocks with explicit premises and conclusions
2. Run LLM-based Block Verification on all blocks with calibrated uncertainty scoring (ensemble disagreement + CoT entropy)
3. Use a dual-signal routing mechanism (uncertainty × dependency-graph criticality) to select 10-20% of blocks for Tier 2 formal verification in Lean 4
4. The claim is that PF blocks are structurally aligned with formal theorem statements, making block-level autoformalization more tractable than whole-proof autoformalization


5. This achieves near-formal reliability at ~1.5-2x cost vs. Safe's 4-8x

### Trivial Alternative Check

I should consider whether simpler approaches could work: running just an ensemble of block verifiers without formal verification seems insufficient since the proposal shows ensemble methods miss roughly half of errors, so formal verification is genuinely needed for the hardest cases. Using basic heuristics like block length or step count for routing instead of calibrated uncertainty might miss the reasoning-subtle blocks that ensemble disagreement catches, though this really needs empirical validation. Random routing of 10-20% to formal verification would be a natural baseline to compare against, though the proposal doesn't explicitly address this comparison.

The ablations mentioned (uncertainty only, criticality only, heuristic only, dual signal) would help validate some of this, but the key question is whether random routing achieves similar error detection rates — if it does, then all the uncertainty calibration machinery becomes unnecessary.

### Premise Assumption Check

The core assumption is that PF blocks are more tractable for autoformalization than whole proofs or raw natural language fragments. This is validated in Ablation 6 and makes intuitive sense — self-contained blocks with explicit premises and conclusions should map more naturally to formal theorem statements, which aligns with independent work on step-level formalization. But I need to see what the actual success rates are.

The second assumption relies on ensemble disagreement as a reliable signal for verification uncertainty, though I'm aware that LLM ensembles can be correlated in their errors — all models might confidently agree on something that's wrong. The proposal acknowledges this "confident-but-wrong" problem but may not fully address it.

The third assumption is that block-level autoformalization success rates will be high enough to matter. The Phase 0 threshold is set at 30% end-to-end success, but existing benchmarks show StepFun-Formalizer-32B achieving only 40.5% on statement-level autoformalization, and while Goedel-Prover-V2 shows high pass rates on miniF2F, those are competition-level problems rather than research-level ones.

Now I'm noticing a tension in the proposal's math. It claims a 35% end-to-end autoformalization barrier is architectural and won't improve with stronger models, but the calculation of 66% autoformalization accuracy times 70% theorem proving success gives roughly 46%, not 35%. This discrepancy suggests either the numbers need recalibration or there's something else constraining the pipeline that I'm not fully accounting for.

Looking at the novelty angle, using proof fragments as a bridge for autoformalization feels like a natural extension of existing work rather than a fundamental breakthrough. The core idea—that smaller, self-contained blocks should be easier to formalize than full proofs—is intuitive and builds directly on prior tools. Uncertainty-based routing for error detection has also been explored before, so the main contribution seems to be combining these pieces rather than introducing genuinely new concepts. The real question is whether combining these pieces creates something genuinely better than using them separately—whether the system produces emergent benefits that justify the approach. The problem itself is significant: LLM-only verification catches only about half of errors in research-level proofs, while full formal verification is prohibitively expensive, so selective verification could fill a practical gap. The proposal shows strong coverage of related work across LLM verification, formal methods, and adaptive approaches, though the core research contribution hinges on whether the insights are novel or straightforward applications of existing techniques.

The dual-signal routing based on uncertainty and criticality is clever, and the experimental plan is thorough with good ablations. But the fundamental limitation is that this feels more like sensible engineering than surprising insight—most researchers in this space would likely arrive at similar designs. The approach also relies heavily on combining external tools rather than introducing new capabilities, and the advance over prior work like Ganguly et al. is incremental since both use uncertainty signals for selective verification.

For a top-tier venue like AAAI 2026, the proposal sits in an awkward middle ground: it's well-executed and the system-level contribution is real, but reviewers might view it as a reasonable engineering effort rather than a conceptual breakthrough. The success of the whole approach hinges on whether block-level autoformalization in ProofFlow achieves sufficient accuracy—if that bottleneck is severe, the value proposition collapses.

My estimate is around 25-35% acceptance probability, with a median of 30%. The problem framing is genuinely strong and the dual-signal routing approach is technically sound, but the "surprise factor" is limited. The real test will be whether empirical results demonstrate that selective routing at modest cost overhead can catch a meaningful portion of errors compared to simpler baselines.

AAAI's broader scope might be slightly more receptive to systems-oriented work in AI for mathematics than venues like NeurIPS, though the novelty concern persists since the individual components feel incremental even if their combination is novel. The proposal itself is exceptionally well-written with thorough experimental planning, but I need to evaluate substance over presentation. My final assessment: the novelty is medium—the combination is novel but builds on existing work like Ganguly et al.—while the significance is medium-to-strong given the real-world problem and practical importance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "813e521f-16a4-4d48-b8a5-9dd9cba1af6a",
  "isSidechain": false,
  "requestId": "req_011CbT8jgikuTH5xjKkyTAGh",
  "type": "assistant",
  "uuid": "8767cf9d-3f61-4463-99be-bbef10c8fc6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqgt4JcRsmwTwnMh6f18EV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3370,
      "cache_read_input_tokens": 27136,
      "output_tokens": 7568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7568,
          "cache_read_input_tokens": 27136,
          "cache_creation_input_tokens": 3370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3370
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

_source line 49 · 2026-05-27T13:17:17.080Z_

Now I have enough information to conduct a thorough evaluation. Let me synthesize all my findings.

---

```
【阶段】: Triage

【领域调研】:

1. **Safe (Liu et al., ACL 2025)**: 首个使用 Lean 4 对 LLM 生成内容进行逐步形式化验证的框架。每一步都自动形式化并用定理证明器验证，报告 ~80% 验证成功率，但带来 4-8x 计算开销。这是本 proposal Tier 2 "全面形式化验证"基线的直接来源。proposal 中对其成本和局限的描述与原论文一致。

2. **Pseudo-Formalization (Barkallah et al., arXiv 2605.20531, May 2026)**: 提出将自然语言证明分解为自包含模块（PF blocks），每个模块有明确前提、结论和证明。Block Verification (BV) 算法逐模块验证。该论文非常新（2026年5月），是本 proposal 的核心基础设施依赖。proposal 对 PF 的描述准确。注意：该论文极其新近（仅发布数天），本 proposal 高度依赖其基础设施和方法。

3. **Ganguly et al. "Grammars of Formal Uncertainty" (NeurIPS 2025)**: 使用 PCFG 建模 LLM 生成形式化产物（SMT-LIB）的不确定性，实现选择性验证，减少 14-100% 错误。这是本 proposal 最直接的竞争工作——同样是"不确定性引导的选择性形式化验证"。proposal 声称的三个差异点（uncertainty source、routing target heterogeneity、structural criticality）是真实的，但核心理念（用不确定性信号决定哪些部分需要形式化验证）高度重叠。

4. **HERMES (Ospanov et al., ICML 2026)**: 在证明生成过程中交替使用非形式推理和 Lean 4 形式化验证，实现 67% 准确率提升、80% FLOPs 减少。关键区别：HERMES 解决的是**生成**问题（输出格式可控），本 proposal 解决的是**验证**问题（输入为任意自然语言）。这个区分是合理的。

5. **miniF2F-Lean Revisited (NeurIPS 2025)**: 系统评估发现端到端自动形式化管线最佳准确率约 36%；LLM 评估报告的 97% 正确率经人工审核仅为 66%。该论文直接支撑了 proposal 中"全证明自动形式化存在根本性可扩展性障碍"的论点。数据基本吻合。

6. **ThinkPRM (2025)**: 使用仅 1% 过程标签训练的 verbalized PRM，在多个 benchmark 上超越判别式 PRM。代表当前最强的数据高效逐步 LLM 验证器。proposal 将其作为 baseline 是合理的。

7. **StepFun-Formalizer-32B (AAAI 2026)**: 在 FormalMATH-Lite 上 BEq@1 达 40.5%，是当前最强的自动形式化模型之一。Goedel-Prover-V2 在 miniF2F 上 pass@32 达 88.1%。两者都是 proposal Tier 2 的核心依赖工具。需注意：40.5% 是在竞赛级 statement-level 任务上的表现，研究级证明的 block-level 形式化成功率可能更低或更高，尚无直接证据。

8. **VERGE (Singh et al., 2026)**: 将 LLM 输出分解为原子 claim，路由到 SMT solver 或 soft verifier。与本 proposal 的路由理念有概念重叠，但 VERGE 面向一阶逻辑 claim 验证，非数学证明 block 验证。

9. **Process-Driven Autoformalization in Lean 4 (2024)**: 独立验证了步骤级形式化比全证明形式化更可行的假设，支撑了 proposal 的 Claim 1。

10. **DiscoUQ / 集成不确定性量化 (2025-2026)**: 多智能体 LLM 系统的不确定性量化方法日趋成熟，ensemble disagreement 用于 UQ 已有成熟方法论。proposal 使用的 ensemble disagreement + Platt scaling 是标准做法，不构成方法论创新。

- **调研总结**: 该领域正处于"LLM 验证不够可靠、形式化验证太贵"的瓶颈期，选择性/自适应验证是一个活跃且合理的研究方向。Ganguly et al. (NeurIPS 2025) 已经建立了"不确定性引导选择性形式化验证"的范式。本 proposal 在此基础上引入 PF block 作为形式化单元、ensemble disagreement 作为 UQ 信号、dependency-graph criticality 作为结构信号——属于在已有范式上的增量推进，而非范式创新。

---

【Trivial Alternative 检验】:

存在以下更简单的替代方案需要考量：

1. **随机路由 10-20% 的 blocks 到形式化验证**：如果 PF block 级自动形式化本身成功率较高（proposal 假设 >30%），那么随机选择 15% 的 blocks 进行形式化验证可能已经能捕获相当比例的错误，因为错误在 blocks 中的分布可能足够均匀。proposal 的不确定性校准 + 图关键性路由的增量价值需要与这个 trivial baseline 对比。proposal 的 ablation 4 (routing signal 消融) 部分覆盖了这一点，但没有明确包含 "random routing" baseline。

2. **仅用 ensemble BV (N=5) + 专家 prompt ensemble，不做任何形式化验证**：proposal 引用的 arXiv 2604.02450 (2026) 表明 specialized prompt ensembles 能显著提升 LLM 验证的 ceiling。如果 ensemble BV + prompt engineering 能把错误检测率从 ~50% 提到 ~70%，那么额外引入 Lean 4 形式化验证的边际收益可能不足以 justify 系统复杂度。

3. **Ganguly et al. 的方法直接迁移到 PF blocks**：将 PCFG-based uncertainty 直接应用于 PF block 的形式化产物，而不需要 ensemble BV disagreement 作为新的 UQ 信号。

**增量价值判断**：proposal 的核心增量在于"跨验证范式路由"（LLM tier → formal tier）和"dual signal"（uncertainty × criticality）。如果消融实验证明 dual signal 显著优于 random routing 和 heuristic-only routing，增量价值成立。但这是一个**经验性赌注**，而非理论保证。

---

【前提假设检验】:

核心逻辑链中存在以下未经验证的前提：

1. **"PF block 级自动形式化比全证明形式化本质上更可行"（Claim 1 核心前提）**：虽然有直觉支撑（自包含、明确前提/结论），且 Process-Driven Autoformalization (2024) 间接支持了步骤级形式化的可行性，但**尚无直接实证**证明 PF block 格式在 StepFun-Formalizer 上的形式化成功率。Phase 0 pilot 设计为测试此假设，阈值设为 30%——但 StepFun-Formalizer-32B 在竞赛级 statement-level 任务上仅达 40.5%，研究级证明 block 的成功率可能更低。这是整个系统的**阿喀琉斯之踵**。

2. **"Ensemble disagreement 能有效捕获 LLM 验证中的 confident-but-wrong 错误"**：proposal 承认了这一风险并通过 dependency criticality 作为补充信号来 mitigate。但 LLM 集成在数学推理中的校准质量本身尚不确定——如果所有集成成员系统性地在同类推理步骤上犯同样错误（correlated failures），disagreement 信号将失效。这一假设需要实证验证。

3. **"自动形式化失败 ≠ 验证失败，可以通过 fallback 策略处理"**：如果 Tier 2 形式化成功率偏低（如 <40%），大量被路由到 Tier 2 的 blocks 会 fallback 到某种替代策略。此时系统退化为"偶尔能做形式化验证的增强版 LLM 验证"，相对于纯 LLM 验证的优势可能不显著。Ablation 8 的 sensitivity analysis (假设 30/50/70/90% 成功率) 部分覆盖了这一点，但如果实际落在 30% 区间，系统的 value proposition 将大幅削弱。

4. **"35% 端到端自动形式化成功率是'架构性'障碍"**：proposal 将此归因于"monolithic proofs 中无界的上下文依赖"，但这可能只是当前工具的经验上限，而非理论硬限。miniF2F-v2（修正 benchmark 后）已将管线准确率提升到 70%。随着 autoformalizer 和 prover 的改进，这一"障碍"可能消退，削弱 proposal 的动机论证。

---

【3 维度打分】:

1. **Novelty: 弱-中（偏弱）**
   - 核心理念"用不确定性引导选择性形式化验证"已由 Ganguly et al. (NeurIPS 2025) 建立。proposal 声称的三个差异点（UQ 信号来源、跨范式路由、结构关键性信号）是真实的 deltas，但属于同一范式内的变体，而非范式创新。
   - PF block 作为形式化单元是 PF (Barkallah et al., 2026) 的自然延伸——论文本身就强调了模块化和自包含性。将 PF block 映射到 Lean 4 theorem statement 是顺理成章的下一步，难以称之为"surprising"。
   - Ensemble disagreement 作为 UQ 信号、Platt scaling 作为校准方法、dependency graph 的 fan-out degree 作为关键性指标——这些都是各自领域的标准做法，组合在一起并未产生方法论创新。
   - **核心问题**：如果最终结果是 positive（selective routing at 15% cost overhead catches 80% of errors），审稿人可能会说"this is a well-engineered system"而非"this is surprising"。
   - 支撑：Ganguly et al. (NeurIPS 2025) 已证明选择性形式化验证可行；PDA (2024) 已证明步骤级形式化更可行；DiscoUQ (2025-2026) 已证明 ensemble disagreement 用于 UQ 的有效性。本 proposal 的"新"主要在组合层面。

2. **Significance: 中-强（偏中）**
   - **问题重要性高**：LLM 证明验证可靠性不足（Hard2Verify 上 PRM 从 78.3% 降至 37.3%）和形式化验证成本过高（Safe 的 4-8x 开销）之间的 gap 是真实且重要的。
   - **实用价值潜力大**：如果系统成功工作，为研究级数学证明的自动化验证提供了一条实际可行的路径。
   - **影响力受限**：方法高度依赖 PF 生态系统（PF decomposition + BV + specific benchmarks），可推广性受限。如果 PF 方法未被广泛采纳，本工作的影响力将局限在一个较小的 niche。
   - **Conditional significance**：本工作的重要性高度依赖于 PF block 级形式化成功率。如果 Phase 0 pilot 失败（<30%），整个 narrative 的前提崩塌。

3. **Related Work: 强**
   - 对领域的覆盖非常全面：LLM 验证（PF+BV、ThinkPRM、PRM 模型）、形式化验证（Safe、自动形式化工具）、选择性/自适应方法（Ganguly、Qu）、相关但不同的系统（HERMES、VERGE、UCCI、ProofSketcher、ProofFlow）。
   - 与每个相关工作的差异化定位清晰且准确。特别是对 Ganguly et al. 的三层差异分析（uncertainty source / routing target / structural criticality）和对 HERMES 的 generation-vs-verification 区分都是精确的。
   - 引用的关键论文均已通过搜索验证真实存在，描述基本准确。miniF2F-Lean Revisited 的数据引用（~35% end-to-end / 66% autoformalization）与原文一致。
   - **轻微不足**：未讨论 miniF2F-v2 修正后管线准确率提升到 70% 这一事实，这可能削弱"35% 是架构性障碍"的论点。

---

【概率估计】: 22% - 32%，中位 26%

【估计理由】:
- Related Work 维度为 强，说明作者对领域有深刻理解，定位清晰——这提供了坚实的下限保障。
- Significance 维度 中-强，问题本身重要且实用，但高度依赖 PF 生态系统的采纳度。
- **Novelty 维度是主要限制因素**。Ganguly et al. (NeurIPS 2025) 已建立了"不确定性引导选择性形式化验证"的范式，本 proposal 的核心贡献在于将此范式迁移到 PF block 上下文并添加结构关键性信号。这是真实的增量，但可能不足以让顶会审稿人认为是"sufficient novelty"。
- 概率上界被 novelty 限制在 ~32%：即使实验结果完美，"系统集成"层面的贡献在顶会评审中通常难以获得高分。
- 概率下界由 related work 质量和问题重要性支撑在 ~22%：即使审稿人对 novelty 有疑虑，扎实的实验和清晰的定位可以避免底分。

【主要风险】:
1. **Novelty 不足**：最直接的竞争对手 Ganguly et al. (NeurIPS 2025) 已建立了高度相似的范式（uncertainty-guided selective formal verification），审稿人可能认为本 proposal 仅是 Ganguly + PF 的自然组合，novelty delta 不足以支撑一篇顶会论文。
2. **核心前提脆弱**："PF block 级自动形式化比全证明形式化本质上更可行"是整个系统的基石，但目前无直接实证。如果 Phase 0 pilot 显示 block-level 端到端成功率与 whole-proof 相差不大（例如都在 30-40%），则 Claim 1 的论证基础将瓦解，系统的 value proposition 大幅削弱。
```

Sources:
- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/)
- [Pseudo-Formalization for Automatic Proof Verification (arXiv 2605.20531)](https://arxiv.org/abs/2605.20531)
- [Ganguly et al. - Grammars of Formal Uncertainty (NeurIPS 2025)](https://openreview.net/forum?id=QfKpJ00t2L)
- [HERMES: Efficient and Verifiable Mathematical Reasoning (ICML 2026)](https://arxiv.org/abs/2511.18760)
- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [StepFun-Formalizer-32B (AAAI 2026)](https://arxiv.org/abs/2508.04440)
- [Goedel-Prover-V2](https://arxiv.org/pdf/2508.03613)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)
- [DiscoUQ: Structured Disagreement Analysis](https://arxiv.org/pdf/2603.20975)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8767cf9d-3f61-4463-99be-bbef10c8fc6a",
  "isSidechain": false,
  "requestId": "req_011CbT8jgikuTH5xjKkyTAGh",
  "type": "assistant",
  "uuid": "2853b026-0207-455d-9492-58bf80b245d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqgt4JcRsmwTwnMh6f18EV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3370,
      "cache_read_input_tokens": 27136,
      "output_tokens": 7568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7568,
          "cache_read_input_tokens": 27136,
          "cache_creation_input_tokens": 3370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3370
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we ac…",
  "leafUuid": "2853b026-0207-455d-9492-58bf80b245d0",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate selective formal verification proposal acceptance probability",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition  ## Core Problem  How can we ac…",
  "leafUuid": "2853b026-0207-455d-9492-58bf80b245d0",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate selective formal verification proposal acceptance probability",
  "sessionId": "4c2a7143-0934-4965-a436-7f8626ecca83"
}
```

---
