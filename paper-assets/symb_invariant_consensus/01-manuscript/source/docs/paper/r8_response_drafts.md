# R8 Reviewer Response Drafts

Status: DRAFT. Dir-J1/J2 COMPLETE. Pending Dir-J3 only.
Round 7 score: 3.0 (Significance 2.5 bottleneck).

---

## Q1: "How does SICA perform on stronger models?"

**Data**: Dir-I-3 (exp028b): Qwen3-14B thinking mode, FOLIO n=204, 12 traces/problem.

**Draft response**:
We added Qwen3-14B in thinking mode (86.27% SC baseline) to Table 1. SICA yields 86.76% ($\Delta = +0.49$pp, McNemar $p = 1.0$, 3 discordant pairs out of 204). This confirms our finding across a 32pp capability range: from Mistral-7B (54% SC) to Qwen3-14B thinking mode (86% SC), no model benefits significantly from SICA. Stronger models actually exacerbate the independence bottleneck: Qwen3-14B produces $\kappa = 0.91$ ($K_{\text{eff}} = 1.09$), meaning 12 sampled traces contain approximately 1 effective independent vote. The Symbolic Mirage is not a capability-dependent artifact but a structural property of self-extraction.

---

## Q2: "Have you tested on other datasets beyond FOLIO?"

**Data**: exp-090 (ProofWriter), LogiQA results, Dir-J1 (COMPLETE).

**Draft response**:
Yes. Table 1 includes ProofWriter depth-5 ($n = 600$) and LogiQA ($n = 200$) alongside FOLIO ($n = 204$). On ProofWriter, SICA significantly *degrades* performance ($-2.83$pp, $p = 0.014$), while LogiQA shows null effect ($+0.50$pp, $p = 1.0$). The cross-architecture DeBERTa NLI combo achieves its strongest result on ProofWriter ($+3.50$pp, $p = 0.013$, BH-adjusted $p = 0.038$), precisely where same-model SICA fails worst. Dir-J1 confirms NLI does *not* generalize to LogiQA: NLI standalone achieves only 29%, and combo modes yield $\Delta \leq +1$pp (all $p > 0.5$). The cross-architecture escape requires task-verifier alignment — NLI is effective only when the task naturally decomposes into premise-conclusion entailment.

---

## Q3: "Have you tested on other LLMs beyond Mistral-7B?"

**Data**: Dir-I-2, Table 1 full results.

**Draft response**:
Table 1 reports results across six models spanning four families: Mistral-7B-Instruct (54% SC), LLaMA-3.1-8B (66--72%), Qwen2.5-7B (76%), Qwen2.5-14B (75--78%), Qwen3-14B (84--86%), and QwQ-32B (degenerate, $C_0 < 5\%$). Confirmation bias generalizes across all families with bias ratios of $4.97\times$ (Mistral), $3.93\times$ (Qwen-14B), and $2.88\times$ (LLaMA) (Table cross-model-bias). The independence bottleneck is equally universal: all four families produce $\kappa \geq 0.41$ (Table kappa-generalization). No model family escapes the Symbolic Mirage.

---

## Q4: "What about ensemble approaches combining multiple LLMs?"

**Data**: Dir-I HGE (6 configurations).

**Draft response**:
We tested six Heterogeneous Generator Ensemble (HGE) configurations combining models with different biases. All six underperform the best single model by 1.81--2.84pp (Appendix Table additional-interventions). Generator-side mixing incurs an anti-diversity penalty: cross-model constraints use incompatible variable naming conventions, causing Z3 to treat identically-intended propositions as unrelated symbols. Rather than providing complementary signal, diverse generators produce constraints that are trivially jointly satisfiable, and MAX-SAT aggregation reduces to a noisy weighted vote that underperforms the strongest individual model's majority vote.

---

## Q5: "Why does NLI only work on ProofWriter and not FOLIO/LogiQA?"

**Data**: Dir-J1 (COMPLETE), existing per-label analysis.

**Draft response**:
The DeBERTa NLI verifier achieves significance on ProofWriter ($+3.50$pp, $p = 0.013$) but not FOLIO ($+2.94$pp, $p = 0.210$) or LogiQA (combo $\Delta \leq +1$pp, all $p > 0.5$). The cross-architecture escape requires *task-verifier alignment*: ProofWriter problems are programmatically derived direct entailment tasks structurally matched to NLI's (premise, hypothesis) classification format. FOLIO involves more complex multi-step natural language reasoning, and LogiQA's multiple-choice format lacks the premise-conclusion structure NLI expects (NLI standalone achieves only 29% on LogiQA). A per-label caveat: DeBERTa over-predicts False on ProofWriter (67.8% of predictions) and performs poorly on Unknown (3.5%), suggesting NLI's "neutral" cannot capture logical unknowability. This limitation is now explicitly noted in the paper's Limitations section.

---

## Q6: "Does the cross-architecture approach work with stronger base models?"

**Data**: Dir-J2 (COMPLETE): Qwen3-14B FOLIO, SC=86.27%, combo w=1 −0.49pp, w=3 +0.49pp, w=5 +0.49pp, all p=1.0.

**Draft response**:
We tested the DeBERTa NLI combo with Qwen3-14B (thinking mode, 86.27% SC) as the base generator on FOLIO. All weight settings produce null effects: $w{=}1$ $\Delta = -0.49$pp, $w{=}3$ $\Delta = +0.49$pp, $w{=}5$ $\Delta = +0.49$pp (all $p = 1.0$). The cross-architecture benefit diminishes with stronger base models because the error set shrinks and the remaining errors fall outside NLI's competence. DeBERTa achieves only 49.51% standalone on FOLIO, far below Qwen3's 86.27% — the verifier's signal is overwhelmed by the generator's high accuracy. This is a genuine limitation: cross-architecture verification requires the verifier to exceed chance on the generator's specific error distribution, a condition DeBERTa meets for Mistral-7B's False-label errors (71.43% vs 38.10%) but not for Qwen3-14B's smaller, harder error set.

---

## Q7: "Have you tested other NLI verifiers beyond DeBERTa?"

**Data**: [PENDING: Dir-J3 multi-verifier]

**Draft response (placeholder)**:
[PENDING Dir-J3 data.] If positive: "We tested [N] additional NLI verifiers ([model names]). Results show [consistency/variation], suggesting the cross-architecture benefit is [robust/verifier-specific]." If negative: "Alternative NLI verifiers [performed worse / showed similar patterns], suggesting that the DeBERTa-large result reflects a specific architecture-task match rather than a general cross-architecture principle."

---

## Significance 2.5 Bottleneck — Strategic Notes

The 2.5 Significance score likely reflects:
1. **No significant positive SICA result** — mitigated by framing as diagnostic/negative result paper
2. **Cross-arch PoC is limited scope** — needs Dir-J/K generalization data
3. **"So what?" factor** — the practical takeaway needs strengthening

Potential response angles:
- Diagnostic value: BR and K_eff are reusable metrics for any trace-aggregation system
- Negative result significance: 27 interventions exhaustively closing a research direction
- Cross-arch escape route: proof-of-concept showing where the field should go next
- Capability-range universality: 54%→86% SC, same conclusion (NEW with Dir-I-3)

---

## Data Dependency Tracker

| Response | Data Status | Blocker |
|----------|-------------|---------|
| Q1 (strong models) | COMPLETE | — |
| Q2 (datasets) | COMPLETE | Dir-J1 ✅ |
| Q3 (other LLMs) | COMPLETE | — |
| Q4 (ensembles) | COMPLETE | — |
| Q5 (NLI dataset-specific) | COMPLETE | Dir-J1 ✅ |
| Q6 (strong base + NLI) | COMPLETE | Dir-J2 ✅ |
| Q7 (other verifiers) | PENDING | Dir-J3 |
