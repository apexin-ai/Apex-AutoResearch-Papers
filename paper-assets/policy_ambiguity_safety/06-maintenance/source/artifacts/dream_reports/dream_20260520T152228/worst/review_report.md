---
dream_id: dream_20260520T152228
tier: worst
overall_score: 3/6 Borderline (Findings-level)
timestamp: 2026-05-20T16:59:28.373431+00:00
---

# Dream Review Report: "Policy Ambiguity Causes Catastrophic Safety Violations in LLM Agents: A Causal Study"

**Dream ID:** 20260520T152228
**Review Mode:** Full (2 Reviewers + Roundtable)
**Venue Standard:** Top ML venue, ~25% acceptance, 6-point scale

---

## 1. Paper Summary

This paper investigates how policy ambiguity causes safety violations in LLM agents. Using a matched-pair causal design with 300 clause pairs across six ambiguity types, five models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-32B-AWQ, Qwen3-8B), and 3,000 agent episodes on τ²-bench, the paper establishes three findings: (1) a +30.2pp binary effect of ambiguity on violation rates (OR=24.1, confirmed by perturbation control with ratio=0.13), (2) "ambiguity blindness" — 92% of violation traces show no meta-cognitive awareness of ambiguity, and (3) model-dependent vulnerability profiles (model×type interaction p=0.008) that preclude universal type-level risk rankings. A DeBERTa PoC classifier achieves F1=0.78 on binary ambiguity detection.

---

## 2. R1 Review — Methods & Experiments

### Strengths

- **S1: Sound causal design.** The matched-pair approach — each ambiguous clause paired with a minimally-edited unambiguous variant — is the correct methodology for isolating ambiguity as a causal factor. This is a clear advance over DRIP-R (interpretation divergence without behavioral consequence measurement) and PhantomPolicy (conflict injection without matched controls).

- **S2: Perturbation control well-executed.** The inclusion of synonym substitution and clause reordering controls directly addresses the prompt brittleness confound. Δ_perturb=4.2pp vs Δ_ambiguity=31.5pp with ratio=0.13 < 0.15 threshold is convincing. All four verdict criteria pass (Table 20).

- **S3: Multi-model coverage.** Five models across three architecture families (OpenAI, Anthropic, Alibaba) at multiple capability tiers (8B to frontier API) substantially strengthens generalizability of the binary effect claim.

- **S4: Transparent measurement reporting.** The paper commendably reports judge calibration per-type (Table 2), including the problematic coreferential F1=0.61 and auth_scope F1=0.68. Cross-judge asymmetry (6pp) is disclosed. Bias-corrected estimates are mentioned. This level of measurement transparency is rare.

- **S5: Reliability testing.** ICC analysis on 900 episodes with per-type breakdown (Table 10) is thorough. The honest reporting of coreferential ICC=0.48 and the SNR=2.6 calculation for the binary effect adds credibility.

### Weaknesses

**W1 (Major): Perturbation control is underpowered.**
180 episodes (30 pairs × 2 × 3 models) yields CI [-1.8, 10.2] for the perturbation effect — a 12pp-wide interval. The study cannot distinguish a true null from a meaningful ~8pp perturbation effect. Clause reordering at +5.3pp with CI [-0.8, 11.4] is particularly concerning — the upper bound approaches the lower range of some per-type ambiguity effects. The perturbation control was run on only 3 API models, excluding the two local models. A more comprehensive control (more pairs, all 5 models, additional perturbation types such as formality shifts or clause-length-matched edits) would substantially strengthen the causal claim.

**W2 (Major): Judge calibration raises measurement concerns for two key types.**
Overall F1=0.72 is below the 0.80 threshold that would provide high confidence in absolute rate estimates. More critically:
- Coreferential F1=0.61 with over-detection bias (precision=0.58) means the reported 34.8% rate likely overestimates the true rate by 5-8pp. This directly inflates coreferential's apparent dangerousness.
- Auth_scope F1=0.68 with under-detection bias (recall=0.56) means the reported 42.8% likely underestimates by 4-6pp.
- These two biases work in opposite directions, artificially compressing the range of per-type rates and reducing Cramér's V. The observed V=0.11 may be partially an artifact of measurement bias.
- The calibration sample of 100 episodes yields ~17 episodes per type — too few for reliable per-type F1 estimates. CIs on per-type F1 are not reported.
- The judge (presumably GPT-5.4-based) evaluating its own model's traces creates a circular dependency.

**W3 (Major): Domain restriction severely limits generalizability.**
All experiments use τ²-bench covering only retail and airline customer service. The paper's title claims "catastrophic safety violations" and the abstract's framing implies general agent safety, but the actual violations are things like granting inappropriate refunds or applying wrong discount policies. High-stakes domains (healthcare, legal, finance) where policy ambiguity has truly catastrophic consequences are untested. The paper should either (a) scope claims to the tested domains or (b) include at least one high-stakes domain.

**W4 (Moderate): Token length confound not fully resolved.**
Specification-layer disambiguation requires avg 3.4 extra tokens vs linguistic-layer 1.7. The partial correlation after type control (r=0.14, n.s.) is reassuring but does not fully rule out information-quantity effects, because type and token delta are structurally confounded (the partial correlation removes the very variance of interest). The paper acknowledges this but the layer gap is n.s. anyway (p=0.14), so this matters less for the revised framing. Still, for per-type comparisons (e.g., auth_scope 42.8% vs coreferential 34.8%), the token delta difference (3.8 vs 2.3) could explain part of the gap.

**W5 (Moderate): Coreferential measurement is triply compromised.**
Coreferential ambiguity has (a) the lowest clause quality pass rate (implied by the judge calibration issues), (b) the lowest ICC (0.48), and (c) the lowest judge F1 (0.61 with over-detection). Any claim involving coreferential rates — including its outsized role in the model×type interaction story (Claude 42%, Qwen3-8B 45%) — should carry explicit measurement uncertainty caveats. The narrative about Claude's "RLHF safety coverage asymmetry" is built on the most unreliable measurement in the study.

**W6 (Moderate): Reliability of type-level claims is insufficient.**
Type-level bootstrap CI width is 14.8pp. The range of per-type pooled rates is only ~12pp (42.8% auth_scope to 30.4% CP). When the CI width exceeds the measured range, type-level comparisons are underpowered. The TOST result (6/15 pairs equivalent at ±15pp, only 2/15 at ±10pp) confirms this: the study cannot reliably distinguish most type pairs. This is consistent with the paper's own conclusion that type rankings are unreliable, but it also means the model×type interaction profiles (Table 8) are built on noisy per-type estimates.

**W7 (Minor): Classifier PoC is marginal contribution.**
DeBERTa trained on 240 examples, tested on 60 (10 per type). Per-type F1 estimates at this sample size have very wide CIs. No comparison against few-shot LLM baselines (the natural production competitor). The 80/20 split is standard but the absolute sizes are too small for confident claims. This section is more of an appendix-level addition than a headline contribution.

**W8 (Minor): Ambiguity blindness coding methodology underspecified.**
The three-level coding scheme (explicit/implicit/surface) for 300 traces is described briefly but key details are missing: Who did the coding? What was the inter-rater reliability? Was it a single annotator? The 92% figure is the paper's second headline finding but the coding methodology is not rigorous enough for a top-venue claims.

### R1 Score: 3 / 6 (Borderline)
### R1 Confidence: 4 / 5

---

## 3. R2 Review — Novelty & Related Work

### Strengths

- **S1: Genuinely novel causal isolation.** No prior work in the agent safety literature uses matched-pair design with perturbation controls to isolate ambiguity as a causal factor. DRIP-R measures interpretation divergence; PhantomPolicy injects conflicts; PolicyBank studies structural gaps. This paper's causal methodology is a real advance.

- **S2: "Ambiguity blindness" is a compelling concept.** The 92% blindness finding, connected to Ferreira et al.'s good-enough processing, is the paper's most original conceptual contribution. The term is evocative and the finding — that agents cannot self-detect the ambiguity harming them — has clear practical implications (external detection is necessary, not optional).

- **S3: Model×type interaction reframes the field.** The shift from "which type is most dangerous" to "danger depends on model architecture" is a genuinely useful insight for practitioners. The three vulnerability profiles (GPT=spec-sensitive, Claude=coref-sensitive, Qwen3-8B=ling-sensitive) are mechanistically interpretable and practically actionable.

- **S4: Coherent argument structure.** The three contributions build on each other logically: (1) ambiguity is universally harmful → (2) agents can't self-detect it → (3) which types are dangerous depends on the model → therefore, invest in binary detection. The narrative is tight.

- **S5: Honest null results.** The paper openly reports the n.s. layer gap (p=0.14) and reframes it as a finding rather than burying it. This is intellectually honest and the reframe (model-dependent profiles) is more informative than the original layer hierarchy would have been.

### Weaknesses

**W1 (Major): References section is empty.**
All citations in the text appear as "(?)" or "(??)". The References section contains no actual entries. This is a fatal formatting issue for any venue submission. While this may be a draft artifact, it makes it impossible to verify:
- Whether the cited prior work actually supports the claims made about it
- Whether the related work coverage is complete
- Whether the "first causal study" claim is accurate
- Whether the psycholinguistic references (Ferreira et al., Frazier & Rayner, Levy) are correctly characterized

**W2 (Major): Related work coverage appears thin.**
Based on the in-text citations (despite their "?" formatting), the paper seems to cite ~15-18 works. For a paper spanning requirements engineering, agent safety, prompt robustness, and psycholinguistics, this is insufficient. Notably missing or underrepresented areas:
- **Pragmatics and communication theory**: Grice's maxims, Clark's common ground theory — directly relevant to why agents fail with underspecified policies
- **RLHF and alignment literature**: The Claude vulnerability profile explanation invokes RLHF safety training but cites no alignment work
- **Legal NLP / contract analysis**: A mature field dealing with exactly this problem (ambiguity in normative documents)
- **Formal verification of agent policies**: Work on policy specification languages and verification
- **Broader agent safety benchmarks**: Only R-Judge, ToolEmu, InjecAgent, AgentPex mentioned; missing SafeAgentBench, AgentHarm, and other 2025-2026 benchmarks
- **Ambiguity in human-AI interaction**: HCI literature on how humans handle ambiguous instructions to AI systems

**W3 (Major): "Catastrophic" framing is not calibrated.**
The title claims "catastrophic safety violations" but the violations occur in simulated retail/airline customer service (τ²-bench). Granting an incorrect refund or applying a wrong discount is a policy violation, not a catastrophic safety event. The word "catastrophic" implies life-threatening or irreversible harm. The paper provides no severity analysis of the violations beyond the tier-1/2/3 breakdown in Table 18 (which is about judge reliability, not violation severity). The abstract's "43% of cases produces a safety violation" counts all violations equally regardless of severity. This overclaiming will attract reviewer criticism at any top venue.

**W4 (Moderate): The specification/linguistic layer distinction adds little value.**
The paper's own results show the layer gap is n.s. (p=0.14), the layer distinction does not predict failure modes (42% cross-layer overlap), and the layer ranking reverses across models. The two-layer taxonomy is presented in §3 as a structural contribution, but the empirical evidence undermines it. The paper correctly pivots to model-dependent profiles, but then why retain the layer taxonomy at all? It occupies space in §3 and §5.2 without earning its keep. The six types could be presented without the layer grouping, and the paper would be cleaner.

**W5 (Moderate): "Ambiguity blindness" novelty is partially overstated.**
While the term is new, the underlying phenomenon — that LLMs process ambiguous text without flagging uncertainty — is well-documented in the prompt sensitivity and calibration literatures. The connection to good-enough processing (Ferreira et al.) is apt but the paper does not argue why this psycholinguistic theory, developed for human sentence processing with eye-tracking evidence, transfers to autoregressive transformer processing. LLMs don't "reanalyze" in the same way humans do. The analogy is suggestive but ungrounded. A more careful treatment would acknowledge the analogy's limits.

**W6 (Moderate): Practical impact of binary detection recommendation is unclear.**
The paper argues for binary ambiguity detection over type-specific triage. But the practical deployment scenario is underspecified:
- Who runs the classifier? The policy author? The agent deployer? A runtime monitor?
- When in the pipeline? Pre-deployment (policy audit) or runtime (per-query)?
- What happens when ambiguity is detected? Rewrite the clause? Flag for human review? Block the agent?
- The DeBERTa PoC (F1=0.78) has 22% false negatives — how many violations would this miss?
- Comparison to simply prompting the agent to "ask for clarification when uncertain" is not made.

**W7 (Minor): Three contributions have uneven weight.**
C1 (binary effect) is primarily a replication-at-scale finding — it confirms what DRIP-R and PhantomPolicy implied. C2 (ambiguity blindness) is the most novel but is qualitative and based on 300 coded traces with unspecified methodology. C3 (model-dependent profiles) is interesting but is essentially a negative result (no universal hierarchy) reframed as a positive finding. The contributions are real but their collective weight may not clear the bar for main conference at a top venue.

**W8 (Minor): Writing quality is generally good but has issues.**
- The paper is well-organized and clearly written overall
- The concluding sentence ("The policy ambiguity problem will not be solved by building better agents. It must be solved by building better policies.") is memorable but slightly misleading — the paper actually argues for building better detection tools, which is a complementary rather than alternative strategy
- Some sentences in §5.2 are dense with statistics and would benefit from reorganization

### R2 Score: 3 / 6 (Borderline)
### R2 Confidence: 4 / 5

---

## 4. Roundtable Discussion

### Step 2: Cross-Sharing

**R1 responds to R2:**
- Agrees references are critically incomplete (empty section is a fatal flaw for submission)
- Agrees "catastrophic" framing is overclaimed given retail/airline domains
- Partially agrees the layer taxonomy adds limited value, but notes it provides useful structure for §3 even if the empirical distinction is n.s.
- Notes that the psycholinguistic grounding concern (W5) connects to R1's concern about ambiguity blindness coding methodology (R1-W8) — both point to the same issue: C2 is asserted more than demonstrated

**R2 responds to R1:**
- Agrees perturbation control underpoweredness (R1-W1) is a real concern — notes that the upper CI bound of 10.2pp for perturbation could explain roughly a third of the weakest per-type binary effects (~25pp for CP)
- Agrees judge calibration (R1-W2) is the most technically concerning weakness, particularly the coreferential over-detection inflating the model×type interaction narrative about Claude
- Partially disagrees on domain restriction severity (R1-W3): the paper uses a standard benchmark (τ²-bench), and requiring multi-domain coverage may be unreasonable for a single paper. However, the title/framing should be scoped.
- Agrees classifier PoC (R1-W7) is a minor contribution at best

### Step 3: Convergence

**Points of consensus:**

1. **The binary effect (+30.2pp) is the paper's strongest and most robust finding.** Both reviewers agree this is large, well-controlled, universal across types/models, and a genuine empirical advance. SNR=2.6 despite moderate ICC confirms robustness.

2. **The paper's methodology (matched-pair + perturbation control) is a real contribution** to the agent safety evaluation literature, even if execution has gaps.

3. **References section is empty — fatal for submission.** All citations show as "(?)" placeholders. This must be fixed before any venue submission.

4. **"Catastrophic" framing is overclaimed.** Retail/airline customer service violations do not meet the bar for "catastrophic." Recommend retitling or adding severity analysis.

5. **Judge calibration is the primary measurement threat.** F1=0.72 overall, with coreferential (0.61) and auth_scope (0.68) exhibiting directional biases that compress the apparent type-level effect range. This doesn't threaten C1 (binary effect) but does threaten the precision of C3 (model-dependent profiles).

6. **Coreferential is triply unreliable** (low ICC, low judge F1, low clause quality pass rate). Claims built on coreferential rates — particularly the Claude RLHF coverage gap narrative — should carry explicit uncertainty flags.

7. **The layer taxonomy earns limited empirical support.** The n.s. layer gap, 42% cross-layer failure mode overlap, and model-dependent reversals collectively undermine the spec/ling distinction as an organizing principle. The paper correctly pivots but the taxonomy persists in §3 without earning its place.

8. **Ambiguity blindness (C2) is conceptually compelling but methodologically underdeveloped.** The coding scheme, annotator details, and inter-rater reliability are not reported. The psycholinguistic analogy (good-enough processing) is suggestive but not argued.

9. **DeBERTa PoC is a minor appendix-level contribution**, not a headline finding. Small data, no few-shot LLM baseline, no transfer evaluation.

**Points of disagreement:**

1. **Severity of domain restriction.** R1 considers this major (limits all claims); R2 considers it moderate (standard benchmark, just needs scoped framing). **Resolution:** Moderate-to-major — the claims need explicit scoping, but requiring multi-domain coverage in a single paper is somewhat unreasonable given the experimental cost (3000+ episodes).

2. **Weight of C3 (model-dependent profiles).** R1 views this as interesting but built on noisy per-type estimates; R2 views it as the paper's most practically useful finding despite being a "negative result reframed." **Resolution:** C3 is informative and novel, but the specific mechanistic explanations (RLHF coverage gaps, pragmatic reasoning capacity) are speculative and built on the least reliable measurements.

### Step 4: Consolidated Assessment

**Overall Score: 3 / 6 — Borderline (Findings-level at a top venue)**

**Justification:**

The paper addresses an important and timely question: does policy ambiguity causally drive safety violations in LLM agents? The matched-pair design with perturbation control is methodologically sound and novel in the agent safety literature. The +30.2pp binary effect is massive, well-replicated across types and models, and represents a genuine empirical contribution.

However, several issues prevent a confident main-conference recommendation:

1. **Fatal formatting issue:** Empty references section with all "(?)" placeholders. This alone would be desk-rejected at any venue.

2. **Measurement concerns:** The LLM judge (F1=0.72) introduces systematic biases for two of six types — the same two types that drive the most interesting model×type interaction narratives. The coreferential type is triply unreliable.

3. **Overclaimed framing:** "Catastrophic" is not earned by retail/airline service violations. The binary effect is still massive and important without hyperbole.

4. **Underdeveloped C2:** Ambiguity blindness is the most novel contribution conceptually but the coding methodology is underspecified for a quantitative claim at a top venue.

5. **Scope vs. claims mismatch:** Two domains, synthetic clauses, and simulated environments. The findings are suggestive but the generalization to real-world policy ambiguity in high-stakes domains is untested.

**Path to acceptance (estimated effort: moderate revision):**

- Fix references (critical)
- Retitle to remove "catastrophic" or add severity analysis
- Expand related work to ~25+ references (pragmatics, RLHF/alignment, legal NLP, broader agent safety)
- Report ambiguity blindness coding methodology: annotator count, IRR, codebook
- Add measurement uncertainty discussion for coreferential-dependent claims
- Strengthen perturbation control (more pairs, all models) or explicitly discuss the power limitation
- Scope generalizability claims to tested domains
- Move classifier PoC to appendix or drop

**If the above issues are addressed**, the paper would be competitive for main conference (score 4). The binary effect finding is strong enough to anchor a solid empirical paper, and the model-dependent vulnerability profiles add practical value.

---

## Summary Scores

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methods + Experiments | 3/6 | 4/5 |
| R2 | Novelty + Related Work | 3/6 | 4/5 |
| **Consolidated** | **Full** | **3/6** | **4/5** |

**Recommendation:** Borderline — suitable for Findings track in current form; competitive for main conference after moderate revision addressing references, framing, and measurement methodology.
