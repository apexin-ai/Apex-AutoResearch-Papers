---
dream_id: dream_20260514T162530
tier: median
overall_score: 3/6 Weak Reject
timestamp: 2026-05-14T17:14:10.921742+00:00
---

# Dream Review Report — Consolidated Roundtable

**Paper:** "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

**Reviewers:** R1 (Methods & Experiments), R2 (Novelty & Related Work)
**Initial scores:** R1 = 4/6 (Weak Accept), R2 = 3/6 (Weak Reject)
**Converged score: 3/6 (Weak Reject)**
**Confidence: 4/5**

---

## Roundtable Process

### Step 1: Independent Reviews

**R1 (Methods & Experiments) — 4/6:**
Praised the statistical discipline (54 training runs across strategy × encoder × seed, bootstrap CIs, multi-benchmark evaluation) and found the ablation suite unusually comprehensive for an analysis paper. Identified the BM25 vs. embedding separation as the paper's strongest contribution. Main concerns: n=2 encoders insufficient for the representation saturation mechanism, dataflow is a mixture strategy (34% structural + 66% random fallback), SWE-bench underpowered, effect sizes (1–2pp) small enough that uncontrolled implementation details could explain them, and checkpoint selection criterion unspecified.

**R2 (Novelty & Related Work) — 3/6:**
Acknowledged the honest framing and ablation breadth but found fundamental deficiencies. The core recommendation ("use embedding-distance mining") recapitulates ANCE (2021) applied to code—not a novel contribution. The CoCoHaNeRe correction argument lacks evidentiary foundation (no proof CoCoHaNeRe actually used BM25 as proxy, p > 0.05, magnitude gap from −1.9pp to −27pp unexplained). The bibliography contains only 2 citations, critically insufficient for a "systematic study" paper. The dataflow contribution is dead weight (null result). Effect sizes at realistic pool sizes (200+) shrink to +0.2–0.5pp, within noise.

### Step 2: Cross-Sharing — Points of Agreement

Both reviewers converged on the following assessments:

1. **The paper's intellectual honesty is commendable.** Claims are properly hedged, limitations are transparent, and the "analysis paper" positioning is appropriate for the evidence.

2. **The ablation suite is unusually thorough.** Temperature, pool size, data scaling, hop count, static/dynamic, weighted/binary, and fusion head ablations each address a specific methodological question.

3. **The stratified analysis by negative difficulty quartile is the paper's strongest analytical finding.** The monotonic Q1→Q4 pattern (embedding Δ from +0.3pp to +1.6pp) provides a plausible representation-geometry explanation.

4. **n=2 encoders cannot support the representation geometry mechanism.** Both reviewers flagged that attributing the encoder–strategy interaction to pos_sim saturation from two data points is post-hoc and unfalsifiable.

5. **The dataflow contribution is essentially null** across conditions and does not justify its inclusion as a named contribution.

6. **Effect sizes are too small for practical impact** at realistic pool sizes.

### Step 3: Convergence Discussion

**R1 adjusted downward** after considering R2's bibliography and novelty critiques. R1 acknowledged that:
- The 2-citation bibliography is a serious scholarly deficiency that undermines the paper's positioning as a systematic study. Multiple methods are mentioned by name (SweRank, SWE-Fixer, GraphCodeBERT, CodexGraph, LocAgent, RANGER, ARISE, CoCoHaNeRe) without proper citations.
- The core recommendation is indeed ANCE applied to code, reducing the novelty of the main finding.
- The CoCoHaNeRe correction narrative requires concrete evidence of proxy conflation to be credible.

**R2 adjusted slightly** after considering R1's statistical rigor analysis:
- The 54-run experimental matrix with bootstrap CIs represents above-average execution quality.
- The pool-size sensitivity analysis with 100% ranking stability on Qwen across pool=50–500 provides useful external validity.

**Final convergence: 3/6 (Weak Reject).** The execution quality is good, but the contribution does not meet the bar for a top venue. The combination of minimal novelty, marginal effect sizes, statistically unsupported correction narrative, and inadequate bibliography is not addressable through minor revision.

---

## Consolidated Assessment

### Strengths

- **S1: Exemplary statistical practice.** 54 training runs (4 strategies × 2 encoders × 3 seeds + ablations), bootstrap CIs on all comparisons, power analysis for SWE-bench. This level of rigor is rare in code retrieval papers and sets a good methodological example.

- **S2: Comprehensive ablation suite with clear purpose.** Each of 8 ablations answers a specific question (Is the finding temperature-dependent? Does it scale with data? Is dynamic re-mining worth the cost?). Results are reported even when null, avoiding publication bias.

- **S3: Honest framing and claim calibration.** The paper does not overclaim. "Tends to help," "exploratory observation," and "directional support" are appropriate qualifications. The SWE-bench evaluation is correctly labeled as a sanity check. Limitations are thorough and specific.

- **S4: Stratified analysis provides mechanistic insight.** The negative difficulty quartile decomposition (Q1: +0.3pp → Q4: +1.6pp for embedding) and structural availability stratification (34% with dataflow data vs. 66% fallback) provide the clearest explanations for when and why mining strategies differ.

- **S5: Conceptual separation of BM25-proxy from true embedding mining.** Even without statistical significance, making this distinction explicit is a useful contribution to clarity in the field.

### Weaknesses

- **W1 (Major): Insufficient novelty.** The universal recommendation ("use embedding-distance mining") recapitulates ANCE (Xiong et al., 2021). The code-specific application does not constitute a novel methodological insight. The dataflow strategy, which would have been the novel element, is a null result. Analysis papers at top venues need to deliver substantial new understanding—this paper's core insight ("hard negatives help more when they're harder") is well-established in contrastive learning.

- **W2 (Major): CoCoHaNeRe correction argument lacks foundation.** Three critical gaps: (a) BM25 harm is not statistically significant (p=0.12, p=0.18), (b) the magnitude gap between our −1.9pp and CoCoHaNeRe's −27pp is unexplained beyond vague "different protocol/pool size" hand-waving, and (c) no concrete evidence that CoCoHaNeRe actually used BM25 as a proxy for embedding-distance negatives. Without (c), the entire "proxy conflation" hypothesis is speculative.

- **W3 (Major): Effect sizes at noise floor for practical relevance.** At pool=50 (training-time setup): +1.0pp Qwen, +0.7pp StarCoder. At pool=200 (realistic): +0.7pp Qwen, +0.4pp StarCoder. At pool=500: +0.5pp Qwen, +0.2pp StarCoder. SWE-bench downstream: < 1pp, p > 0.6. The practical takeaway is "negative mining strategy probably doesn't matter much," which is useful to know but thin as a publication contribution.

- **W4 (Major): Bibliography critically insufficient.** Only 2 references cited. Missing: RocketQA, TAS-B, GPL, ColBERTv2 (hard negative mining for dense retrieval); ContraCode, contrastive learning for source code; formal citations for SweRank, SWE-Fixer, GraphCodeBERT, CodexGraph, LocAgent, RANGER, ARISE, CoCoHaNeRe. A "systematic study" paper cannot have a 2-entry bibliography.

- **W5 (Major): n=2 encoders insufficient for mechanism claims.** The "representation saturation" hypothesis (Qwen pos_sim=0.99 benefits from structural negatives; StarCoder pos_sim=0.80 does not) is inferred from two data points. Any two encoders differ in multiple dimensions; attributing the interaction to pos_sim is unfalsifiable without more encoders.

- **W6 (Significant): Dataflow contribution is dead weight.** Neutral on Qwen (+0.2pp overall, CI includes 0), negative on StarCoder (−0.6pp). Only 34% structural coverage; 66% falls back to random. Hop-count ablation < 0.5pp. Weighted-vs-binary ablation not significant. Including this as Contribution 4 dilutes the paper's focus without adding value.

- **W7 (Significant): Dataflow is a confounded mixture strategy.** The "dataflow" condition is actually 34% structural + 66% random. The headline comparison in Table 1 mixes signal from two different strategies. A cleaner design would report the 34% stratum separately as the primary dataflow result.

- **W8 (Moderate): 3 seeds with df=2 severely underpowers statistical tests.** With 3 seeds, t-test critical values are 4.303, making significance detection near-impossible for the observed deltas. Bootstrap with n=3 yields only 27 resamples. The paper should be explicit about this limitation.

- **W9 (Moderate): Checkpoint selection unspecified.** The paper evaluates at steps {200, 500, 1000, 1500, 2000} and selects "best checkpoint" but does not specify the selection criterion or whether it could change strategy rankings.

### Questions for Authors

1. Can you provide specific evidence (CoCoHaNeRe code, methodology description, or author communication) that they used BM25 as a proxy for embedding-distance negatives? Without this, the "proxy conflation" hypothesis is speculative.

2. What is the checkpoint selection criterion, and does it favor one strategy over another?

3. At pool=500 on StarCoder, dataflow slightly exceeds embedding (0.197 vs. 0.196). Is this within noise? How robust is the "embedding mining maintains advantage" claim at realistic pool sizes?

4. Have you evaluated a dataflow variant that falls back to embedding-distance (instead of random) for the 66% without structural data? This would isolate the structural signal more cleanly.

5. What are the pos_sim values (query-positive cosine similarity) for each encoder? This is central to the representation geometry explanation but not reported.

6. Why does the bibliography contain only 2 entries? Is this a formatting artifact? All methods mentioned by name (SweRank, SWE-Fixer, GraphCodeBERT, CodexGraph, LocAgent, RANGER, ARISE, CoCoHaNeRe, curriculum-based approaches) should be formally cited.

7. The paper reports BM25 uses only 1 seed (vs. 3 for other strategies). What is the justification? How does this affect the BM25 CI widths?

### Missing Experiments or Comparisons

1. **More encoders** (at least 3–4) to test the representation geometry hypothesis—currently unfalsifiable with n=2.
2. **Dataflow with embedding fallback** instead of random fallback, to cleanly isolate structural signal.
3. **Per-seed results** for all conditions (currently only means reported), to assess seed-level variance.
4. **CoCoHaNeRe replication** or direct comparison using their exact protocol, to substantiate the correction claim.
5. **Encoder-native embedding negatives** (mine using each encoder's own embeddings vs. a frozen pretrained encoder) to test whether self-mining vs. cross-mining matters.

### Experiment Design Coverage

The paper covers 15/15 experiments from the full design. Coverage is comprehensive. However, several experiments that were designed as appendix-level ablations (hop count, weighted/binary, dynamic/static) produce null results that do not strengthen the paper. The experiments that would most strengthen the paper (more encoders, CoCoHaNeRe replication) are absent from the design.

---

## Final Verdict

**Score: 3/6 (Weak Reject)**
**Confidence: 4/5**

The paper is well-executed and intellectually honest, but does not clear the contribution bar for a top ML venue. The core finding (embedding-distance mining helps modestly) recapitulates known results from ANCE. The CoCoHaNeRe correction narrative lacks the evidentiary foundation to serve as a primary contribution. The dataflow direction produced null results. Effect sizes are at the noise floor at realistic pool sizes. The bibliography is critically deficient.

The strongest elements—stratified analysis, ablation thoroughness, honest framing—would make this a solid workshop paper or a strong contribution to a focused venue (e.g., a software engineering workshop, MSR, or a code intelligence track). For a top ML conference, the paper needs: (a) more encoders to support mechanism claims, (b) concrete evidence for the CoCoHaNeRe proxy hypothesis or a revised narrative, (c) a substantially expanded bibliography, and (d) a clearer articulation of what new understanding emerges beyond "ANCE works for code too."

### Actionable Recommendations for Revision

1. **Drop the "correction" framing** unless concrete evidence of CoCoHaNeRe's proxy usage can be provided. Reframe as "our controlled comparison finds no significant harm from true embedding-distance negatives, in contrast to prior reports that may have been confounded."
2. **Expand bibliography** to 25+ references with proper citations for all mentioned methods.
3. **Add 2–3 more encoders** (e.g., CodeLlama, DeepSeek-Coder, or an encoder-only model like CodeBERT) to test the representation geometry hypothesis.
4. **Remove dataflow from contributions** or merge into a single "exploratory" subsection. It currently occupies significant space for a null result.
5. **Report pool=200 as co-primary** alongside pool=50, since pool=200 is more representative of real-world conditions.
6. **Remove "Representation Geometry" from the title**—the current analysis (pos_sim values for 2 encoders, difficulty quartile stratification) does not constitute a geometric analysis.