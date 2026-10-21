---
dream_id: dream_20260518T171503
tier: median
overall_score: weak reject (3/6)
timestamp: 2026-05-18T18:06:14.198000+00:00
---

# Dream Review Report — dream_20260518T171503

**Paper:** "The Formulation Design Space for Neural Code Verification: A Controlled Empirical Study"

---

## Reviewer Assignments

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Method + Experiments | 3/6 | 4/5 |
| R2 | Novelty + Related Work | 3/6 | 4/5 |
| **Consensus** | | **3/6 (Weak Reject)** | |

---

## Paper Summary

The paper compares three execution-free code verification formulations (CLS = per-test binary classification, CWM = expected output generation, TRAJ = trajectory-level scoring) under controlled conditions across two model families (Qwen3-8B, DeepSeek-R1-Qwen3-8B) and two complexity levels (function-level, repository-level). It introduces the SWE-bench PerTest dataset (34,790 per-test labels from 418 instances). Core findings: (1) formulations are equivalent at function-level; (2) CLS dominates at repo-level because CWM suffers tokenizer-specific format collapse (52-93% unparseable); (3) per-test CLS matches TRAJ accuracy at 6-9x lower cost; (4) re-repair downstream utility is not demonstrated (CLS +1.5pp, p=0.62).

---

## Consolidated Strengths

**S1. Well-motivated controlled comparison (R1, R2).** The core question is practically important: practitioners lack guidance on which verification formulation to adopt. Holding model, data, and LoRA configuration constant while varying only the formulation is a clean design that fills a genuine gap. No prior work provides this level of control.

**S2. Rigorous statistical methodology (R1).** TOST equivalence testing with explicit margins for the function-level null result is methodologically appropriate and exceeds the rigor of most empirical papers in this area. Fisher's exact test for the cross-model unparseable comparison is correctly applied.

**S3. Honest reporting of negative results (R1, R2).** The paper is transparent about the re-repair study being negative (+1.5pp, p=0.62), about CWM parseable-only accuracy being near the majority baseline (71.8%), and about the gap between oracle potential (+7pp) and realized CLS utility. This self-awareness is uncommon and valuable.

**S4. Informative null result at function-level (R2).** Establishing formal equivalence across formulations at function-level provides a useful calibration point: it shows the CLS advantage at repo-level emerges from complexity, not from an inherent property of the classification formulation.

**S5. Dataset contribution (R1, R2).** SWE-bench PerTest (34,790 per-test labels, 418 instances, 16 candidates each) is a concrete resource contribution enabling future controlled formulation studies.

---

## Consolidated Weaknesses

**W1. Central finding is largely predictable (R2, R1 concurs).** That a 1-token classification output is more robust than variable-length exact-match generation at high complexity follows from first principles. The paper's own theoretical framing (accuracy degrades as q^L for output length L) is a textbook observation. The "formulation x model x complexity interaction" reduces to: CWM breaks when outputs are long, and severity depends on the tokenizer. This is engineering characterization more than scientific insight.

**W2. Missing constrained decoding baseline is a critical gap (R1, R2).** Format non-compliance (52-93% unparseable) is CWM's dominant failure mode at repo-level. The paper never tests constrained/structured decoding (grammar-guided generation, JSON-mode, Outlines-style approaches) which could eliminate this failure entirely. If constrained decoding rescues CWM, the paper's central conclusion is an artifact of unconstrained generation, not a property of the generation formulation. This is the single most important missing experiment.

**W3. "Design space" framing is overstated (R2).** The title promises a "formulation design space" but examines only 3 discrete formulations. There is no architectural exploration (hybrid approaches, chain-of-thought verification), no training objective variations (DPO, process reward), and no input representation variations. This is a formulation comparison, not a design space exploration.

**W4. Limited seed coverage and model diversity at repo-level (R1).** DeepSeek CLS repo-level has only 2 seeds (78.3% and 76.1%). Qwen3 CLS repo-level numbers for 4B and 8B appear to be single-seed. Multi-seed significance testing is acknowledged as impossible for DeepSeek. Only two model families are tested, both decoder-only transformers with related architectures. Testing a structurally different model (e.g., CodeLlama, StarCoder2) would strengthen generalizability claims.

**W5. Scale mismatch with original CWM undermines the comparison (R2).** The original Code World Models paper uses a 32B model with mid-training on execution traces. This paper uses 4-8B models with LoRA rank-16, a fundamentally different capacity regime. The CWM failure at repo-level could reflect insufficient model capacity (LoRA adaptation vs. full mid-training) rather than a formulation-level limitation. The paper acknowledges this in one sentence but does not adequately explore the boundary.

**W6. Class imbalance inflates accuracy and obscures analysis (R1).** The 72.5% pass rate means the majority baseline is 73.0% at repo-level. CWM's unparseable outputs default to a fallback (likely majority class), making "overall accuracy" a mixture of model predictions and default assignments. F1-macro should be the primary metric alongside accuracy. The paper reports F1 for DeepSeek CLS (Table 3) but not consistently across all conditions.

**W7. Thin reference coverage (R2).** Only 10 references for a paper positioning itself as a systematic survey of the verification formulation space. Missing coverage includes: constrained/structured decoding literature, more recent 2024-2025 code verification work, execution prediction beyond CWM, LLM-as-judge approaches, and test generation/mutation testing. A top-venue empirical study in this area should demonstrate broader awareness of the field.

**W8. Re-repair negative result limits the contribution scope (R1, R2).** Per-test diagnostic granularity is framed as a key advantage of CLS over TRAJ throughout the paper. The re-repair study (Section 9) demonstrates that this advantage is theoretical (oracle +7pp) but not realized in practice (CLS +1.5pp, p=0.62). The paper handles this honestly, but it means one of the five listed contributions (Contribution 5) is effectively a negative result, reducing the paper's practical impact.

---

## Key Questions for Authors

**Q1.** Have you tested constrained decoding for CWM? Given that format non-compliance is the dominant failure mode (52-93% unparseable), grammar-guided generation or structured output enforcement could eliminate this entirely. Without this experiment, it is unclear whether the finding reflects a formulation limitation or a decoding strategy limitation.

**Q2.** Can you characterize whether the 82 Docker-failed instances (16.4%) differ systematically from the 418 successful ones in terms of difficulty, repository complexity, or test suite size? Selection bias could inflate all repo-level results.

**Q3.** CWM parseable-only accuracy (71.8% on DeepSeek) barely matches the majority baseline (73.0%). Can you decompose parseable-incorrect predictions into truncation-related, surface-form mismatches (float precision, dict ordering), vs. genuinely wrong semantic predictions?

**Q4.** Given the scale mismatch with original CWM (32B mid-trained vs. 8B LoRA), do you have any evidence on whether the generation formulation performs better with full fine-tuning or larger models? Even a preliminary experiment at 14B or with full fine-tuning would help scope the conclusion.

---

## Roundtable Discussion

### Step 2: Cross-Sharing
R1 and R2 independently converged on the same score (3/6) and flagged the same top-level concerns: predictability of the main finding, missing constrained decoding baseline, and overstated framing. R1 contributed additional statistical rigor concerns (seed coverage, class imbalance, Docker selection bias). R2 contributed additional positioning concerns (thin references, scale mismatch, "design space" overpromise).

### Step 3: Convergence
After cross-examination, both reviewers maintained 3/6. No disagreements required resolution. The paper's methodological care (TOST, Fisher's exact, honest negative reporting) is appreciated but insufficient to elevate the score given the predictability of findings and the critical missing experiment (constrained decoding).

### Step 4: Assessment

**Overall Score: 3/6 (Weak Reject / Findings-borderline)**

The paper is methodologically sound, fills a real gap in controlled formulation comparison, and is commendably honest about negative results. However, the central finding (CLS > CWM at repo-level due to format collapse) is predictable from first principles. The missing constrained decoding experiment is a critical gap that could invalidate the main conclusion. The "design space" framing overpromises relative to the 3-point formulation comparison actually conducted. Limited model diversity (2 families), thin seed coverage at repo-level, and only 10 references further limit the contribution. The re-repair negative result means the practical utility argument (diagnostic granularity) is unsubstantiated.

**Verdict:** Below the bar for a top ML venue main conference (acceptance rate ~25%). The work is a careful empirical study but the insight yield is low relative to the experimental effort. With constrained decoding experiments, broader model coverage, and stronger related work, this could reach Findings-level at a *ACL venue.

**Actionable improvements for resubmission:**
1. Add constrained decoding experiments for CWM (highest priority)
2. Test at least one additional model family (e.g., CodeLlama or StarCoder2)
3. Expand references to 25-30+ covering structured generation, recent verification work
4. Report F1-macro as co-primary metric across all conditions
5. Multi-seed all repo-level conditions (minimum 3 seeds)
6. Reframe title: "formulation comparison" rather than "design space"
7. Strengthen the re-repair study (larger n, better Docker reliability) or downweight the diagnostic granularity claim
