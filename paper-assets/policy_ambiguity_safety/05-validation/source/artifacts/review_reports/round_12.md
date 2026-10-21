---
round: 12
review_mode: fresh
overall_score: 3.5 Borderline Conference
timestamp: 2026-05-22T10:09:34.287518+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 12

**Paper**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)
**Reviewers**: R1 (方法严谨性, 3.5/5) + R2 (新颖性/完整性, 3.5/5)
**Cross-response**: 完成，19/22 条 AGREE，2 条 REBUT（taxonomy 术语严重程度 + perturbation control 分工设计）

---

## Summary

This paper presents a matched-pair causal study on τ²-bench examining how six types of policy ambiguity affect safety violations in LLM agents. Using 300 clause pairs evaluated across five models (2,997 episodes), the study finds: (1) ambiguous clauses increase violation rates by 34.0 pp (OR=15.1); (2) incompleteness consistently ranks highest (46–62% across seven models) with a risk gradient rather than sharp tiers; (3) agents exhibit Disambiguation Neglect (≤11% awareness) and systematic nocuity (41.3% majority-convergent violations). The methodology is well-designed with perturbation controls, cross-judge evaluation, and comprehensive statistical analysis. Two additional model families replicate core findings.

---

## Strengths

**S1** [Consensus] First matched-pair causal study of ambiguity type → agent safety violation, filling an important empirical gap. Perturbation control + matched-pair design provides stronger causal inference than observational studies.

**S2** [Consensus] Statistical methodology quality exceeds the field norm — TOST equivalence testing + bootstrap cluster + Holm-Bonferroni correction + sensitivity analysis across seven margins. Claim calibration (C3 inconclusive, C4 exploratory) demonstrates excellent intellectual honesty.

**S3** [Consensus] Seven models across six providers (5 primary + 2 replication) is among the broadest model coverage in agent safety research. ICC=0.919 demonstrates reproducibility (within OpenAI family).

**S4** [Consensus] Disambiguation Neglect (4.6% overall, ≤11% per-model) and systematic nocuity (41.3% majority-convergent, 13% universal) are valuable empirical contributions with direct deployment implications.

**S5** [Consensus] Type → failure mode mapping (§6.1: structural misparse, information gap-filling, boundary violation) is practically valuable, with majority-consistency (≥3/5 models) for each type's dominant failure mode.

**S6** [Consensus] Writing is clear and well-structured within 8-page constraints. Limitations section is candid and specific.

---

## Weaknesses

### MUST-FIX (4 issues — all consensus)

**[MF-1]** "22× more variance" claim is misleading (R2-N1, R1-AGREE)
- §5.1 decomposition: clause identity 22.4% = between-type 0.4% + within-type 22.0%. The taxonomy itself explains only 0.4% of variance — 55× less than within-type clause wording. Placed in the contribution list after C2, readers naturally interpret "22×" as type-level explanatory power. Combined with 76.6% unexplained variance (evaluation pipeline noise), this constitutes overclaiming.
- **Required fix**: (1) Distinguish clause-level vs type-level variance in contributions; (2) Discuss 0.4% implications for taxonomy utility in §5.1; (3) Demote "22×" from headline contribution to supporting evidence; (4) Report 76.6% residual.

**[MF-2]** C2 "risk gradient" claim is margin-dependent (R1-N1, R2-AGREE-w-qualification)
- The gradient structure holds at ±15pp (6/6 mid-tier pairs equivalent) but collapses at ±10pp (3/6). No field-standard SESOI exists. Bootstrap cluster analysis (AU p=0.47) does not corroborate — the singleton partition reproduces in only 34.3% of bootstrap samples. Excluding incompleteness, omnibus p=0.079 (pairwise gradient partially survives: auth scope/lexical > coreferential).
- **Required fix**: (1) Attach margin condition to every C2 claim statement ("at the ±15pp margin"); (2) Abstract/Conclusion must acknowledge margin-dependence; (3) Weaken bootstrap "corroborates" language; (4) Note p=0.079 excluding incompleteness.

**[MF-3]** Cross-judge asymmetry threatens C4 conclusions (R1-N2, R2-AGREE)
- GPT-5.4 judges Claude/GPT-4.1/Qwen3; GPT-4.1 judges GPT-5.4/DeepSeek. Authorization scope 52pp range (Claude 12% → GPT-5.4 64%) crosses the judge boundary, and auth scope has the lowest inter-judge κ (0.385). Within-judge-group auth scope: GPT-5.4-judged range = 34pp (Claude 12%, GPT-4.1 46%, Qwen3 26%), GPT-4.1-judged range = 4pp (GPT-5.4 64%, DeepSeek 60%). Appendix P type ranking ρ=−0.03 across judge groups. Figure 3 and "most model-differentiating type" framing give readers a much stronger impression than caveats warrant.
- **Required fix**: (1) Figure 3 caption annotate judge assignments; (2) Report within-judge-group auth scope ranges; (3) Elevate caveat to Figure 3 caption and Discussion; (4) Position differential nocuity as hypothesis, not established framework.

**[MF-4]** Incompleteness information-addition confound insufficiently controlled (R1-N3, R2-W3, mutual AGREE)
- Incompleteness's unambiguous variant adds entirely new policy content (+34.6 words) rather than merely resolving ambiguity. Token count proxy is admittedly coarse. Cross-type counter-evidence (auth scope +36.1 > incompleteness +34.6) compares semantically different content types — not apples-to-apples. Token delta OR=1.022/token cumulates to ~2.15× odds multiplier over ~35 tokens.
- **Required fix**: (1) Consistently label 49.2pp as "upper bound including potential information-addition inflation"; (2) Use coreferential 18.7pp as confound-free anchor in Abstract/Conclusion; (3) Discuss propositional content analysis as better but unimplemented proxy; (4) Acknowledge cross-type token delta comparison limitations.

### SHOULD-FIX (8 issues)

**[SF-1]** Front-load taxonomy scope limitation (R2-N2 critical, R1-REBUT but agrees on partial fix)
- Incompleteness = information absence, conditional precedence = normative conflict. §3 "Scope of ambiguity" addresses this well but comes too late (page 3). R1 argues against changing terminology, citing RE literature connection.
- **Fix**: Add parenthetical in §1 ("including specification-level gaps that, while not ambiguity in the strict linguistic sense, produce identical behavioral outcomes in LLM agents"). Consider "including specification-level gaps" in Abstract.

**[SF-2]** Mitigation experiment direction contradiction (R2-W1, R1-AGREE)
- §7 GPT-5.4 type-specific incompleteness: +14pp (p=0.118). Appendix B GPT-5.4 incompleteness: −2.6pp. Same model, same type, different prompt and design.
- **Fix**: Report both prompt formulations; discuss prompt sensitivity as a finding; label design differences at first mention.

**[SF-3]** Disambiguation Neglect novelty positioning (R2-W2, R1-AGREE)
- Liu et al. (2023) + Hu et al. (2025) established core phenomenon. Contribution is quantifying in agentic settings.
- **Fix**: Contribution (3) "revealing" → "quantifying in consequential agentic settings and identifying systematic nocuity."

**[SF-4]** Per-type human validation CIs uninformative (R1-W2, R2-AGREE)
- n=32-34 per type. Scopal κ CI=[0.00, 1.00]. Appendix G draws type-level conclusions despite §4.4's "lack power" caveat.
- **Fix**: Appendix G must state per-type results are descriptive/suggestive only.

**[SF-5]** Judge family bias (R1-W3, R2-AGREE)
- Both judges from OpenAI. Claude's 30.3% could reflect genuine robustness or systematic bias.
- **Fix**: Discuss possible bias direction; recommend cross-family judge evaluation in Future Work.

**[SF-6]** C4 2.9% variance vs Discussion weight (R1-W4, R2-AGREE)
- Interaction explains 2.9% variance; Discussion gives it disproportionate theoretical weight.
- **Fix**: Position differential nocuity as hypothesis; attach effect size + uncertainty caveats.

**[SF-7]** Kendall's W selective reporting (R1-W6, R2-AGREE-w-qualification)
- 5-model W=0.398 (p=0.072) non-significant; 7-model excluding coreferential p=0.038 significant.
- **Fix**: §5.2 report 5-model p=0.072; characterize as "trending toward concordance."

**[SF-8]** Single benchmark external validity (R2-W4, R1-AGREE with lower severity)
- All experiments on τ²-bench (retail + airline). Abstract/Conclusion overgeneralize.
- **Fix**: Add domain qualifiers in Abstract and Conclusion.

### MINOR (7 issues)

- [MI-1] 4.6% vs ≤11% awareness numbers used interchangeably — standardize.
- [MI-2] C3 §5.3 can compress from ~6 lines to 3-4.
- [MI-3] Table 2 caption too long — move Tier definitions to footnote.
- [MI-4] Bootstrap ranking preservation (99.5%) must note within GPT-5.4 judge subset only.
- [MI-5] ICC=0.919 within OpenAI family only — note cross-provider untested.
- [MI-6] Pages 4-5 consecutive text-only (Visual check warning).
- [MI-7] Page 8 compresses 5 sections — rushed ending impression (Visual check warning).

---

## Reviewer Consensus

All critical items reached [AGREE]:
1. "22× variance" overclaiming — taxonomy explains 0.4% between-type variance [MF-1]
2. C2 gradient collapses at ±10pp — margin-dependence must enter claim [MF-2]
3. Auth scope 52pp crosses judge boundary with lowest κ — C4 needs stronger caveats [MF-3]
4. Incompleteness confound token count proxy insufficient [MF-4]
5. Mitigation §7 vs Appendix B contradiction needs analysis [SF-2]
6. Disambiguation Neglect is quantification of known phenomenon [SF-3]
7. **Bottleneck is claim calibration, not methodology** — both note fixing claims → 4.0 achievable

## Reviewer Divergence

1. **Taxonomy terminology** (R2-N2 vs R1-REBUT): R2 proposes "policy underspecification"; R1 argues this weakens RE literature connection. Both agree scope should be front-loaded in §1. **Director assessment**: R1's position is stronger — the paper's theoretical contribution depends on extending Berry & Kamsties (2004). Front-loading scope limitation in §1 is the proportionate fix.

2. **Perturbation control applicability** (R1-W5 vs R2-REBUT): R1 argues structural mismatch for specification-layer types. R2 correctly notes §4.5's explicit two-pronged design (perturbation control for surface, logistic regression for information). **Director assessment**: R2's point stands, but the logistic regression's coarse proxy (MF-4) means the compound control for specification-layer types remains weaker. Already covered by MF-4.

---

## Questions for Authors

1. What are the within-judge-group auth scope violation rates? If both groups show ranges far smaller than 52pp, this confirms judge effect.
2. Is propositional content analysis (vs token count) feasible as a follow-up for the incompleteness confound?
3. Given 0.4% between-type variance, should the taxonomy's primary claimed value shift from variance explanation to failure mode prediction (§6.1)?
4. Excluding incompleteness, omnibus p=0.079 — should C2 be reframed around the partial pairwise survival?
5. Any qualitative comparison with DRIP-R's naturally occurring policy ambiguity instances for ecological validity?
6. What are C3's direction and effect size after controlling for token delta?

---

## Missing References

R2 suggests "The Causal Impact of Tool Affordance on Safety Alignment" (arXiv:2603.20320). Existence not verified; if real, marginally relevant to §2 Agent Safety but not critical.

---

## External Review

**Status**: Not requested.

---

## Visual Layout Check (非评分项)

**Status**: Done (2026-05-22 09:54:26 UTC). 0 critical, 2 warning, 6 info.

| Severity | Location | Finding |
|----------|----------|---------|
| ⚠️ Warning | Pages 4-5 | Method §4 连续两页纯文本无 display item，审稿人容易失去视觉锚点 |
| ⚠️ Warning | Page 8 | §6.2–§8+Limitations 压缩 5 个 section 在单页，匆忙收尾印象 |
| ℹ️ Info | Page 6 | Figure 2 bar 标签字号偏小（约正文 60-65%） |
| ℹ️ Info | Page 7 | Figure 3 heatmap 数字字号偏小 |
| ℹ️ Info | Page 2 | Figure 1 三面板视觉风格略不统一 |
| ℹ️ Info | Page 6 | Table 2 格式规范 |
| ℹ️ Info | Page 3 | Table 1 格式整洁 |
| ℹ️ Info | Page 15 | Appendix 末页大面积空白 |

---

## Overall Assessment

**Score: 3.5 / 5 — Borderline Conference**
**Confidence: 4 / 5**
**ARR scale: 3.5 = Borderline Conference**

**Rationale**: The paper addresses an important question — whether ambiguity type in policy specifications causally determines safety violation severity — with a matched-pair methodology exceeding the field's empirical standard. C1 (+34.0pp, OR=15.1) is robust across seven models. The error analysis (Disambiguation Neglect, systematic nocuity) provides actionable deployment insights.

However, the paper's secondary claims require calibration:
- C2's "risk gradient" is margin-dependent (±15pp only), with bootstrap non-supportive and incompleteness potentially confound-inflated
- "22×" contribution headline misrepresents the variance decomposition (clause wording, not type membership)
- C4's auth scope interaction is confounded by cross-judge asymmetry on the lowest-agreement type

**These are claim calibration problems, not methodological design flaws.** The underlying data and statistical framework are sound. Both reviewers independently assess that fixing the four must-fix items (claim recalibration, not new experiments) would bring the paper to 4.0 (Conference level).

**Upgrade path**: Fix MF-1 through MF-4 (claim calibration) + SF-1 through SF-3 (framing adjustments) → 4.0.

---

## Detailed Comments

### Abstract
- "22× more variance" → reframe as clause-level (not type-level) finding
- "risk gradient rather than sharp tiers" → add margin condition or soften
- Add domain qualifier or "specification-level gaps" parenthetical
- Use coreferential 18.7pp as confound-free anchor alongside incompleteness upper bound

### §1 Introduction
- Contribution (2): separate clause identity from type gradient; demote "22×"
- Contribution (3): "revealing" → "quantifying in consequential agentic settings"
- Front-load taxonomy scope limitation with parenthetical

### §3 Taxonomy
- "Scope of ambiguity" paragraph well-written; no changes if §1 front-loads scope

### §4 Method
- §4.4: Add within-judge-group auth scope ranges
- §4.6: Strengthen SESOI domain justification; acknowledge field-standard absence

### §5 Results
- §5.1: Report 76.6% residual; note 22.4% = 0.4% between-type + 22.0% within-type
- §5.2: Attach margin condition; note omnibus p=0.079 sans incompleteness; weaken bootstrap language; report 5-model Kendall's W p=0.072
- §5.3: Compress to 3-4 lines
- §5.4: Annotate Figure 3 judge assignments; report within-judge ranges; elevate caveats

### §6 Analysis
- §6.2: Standardize 4.6% vs ≤11%
- §6.3: Systematic nocuity = strongest novel finding — could receive more emphasis

### §7 Discussion
- Differential nocuity: hypothesis, not framework; reduce reliance on auth scope model differences
- Mitigation: label two experiments' design differences; discuss prompt sensitivity as finding

### §8 Conclusion
- Domain qualifier; margin condition on gradient; coreferential confound-free anchor

### Limitations
- Already comprehensive; add judge family bias direction discussion and cross-family evaluation recommendation