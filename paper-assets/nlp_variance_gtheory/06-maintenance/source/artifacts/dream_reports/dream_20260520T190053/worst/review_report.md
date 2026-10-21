---
dream_id: dream_20260520T190053
tier: worst
overall_score: weak reject
timestamp: 2026-05-20T19:51:49.188124+00:00
---

# Dream Review Report — Full Roundtable

**Paper**: "No Universal Reproducibility Recipe: Variance Attribution in LLM Evaluation Is Benchmark-Conditional and Model-Conditional"

**Review mode**: full | **Reviewers**: R1 (Methods+Experiments), R2 (Novelty+Related Work)

---

## Step 1: Independent Reviews

### Reviewer 1 — Methods & Experiments

**Summary**: The paper applies G-theory to decompose LLM evaluation variance across 4 models, 5 benchmarks, and 172,800+ inference conditions plus a fine-tuning G-study. The experimental scale is ambitious and the float32 confound discovery is a genuine contribution. However, critical methodological gaps—residual dominance, missing uncertainty quantification, and a blocked hardware experiment—undermine the strength of the claims.

**Strengths**:
1. **Large-scale factorial design**: 4 models × 5 benchmarks with multiple crossed facets represents the most comprehensive G-theory study in LLM evaluation to date. The 172,800 MMLU records provide genuine statistical power.
2. **Float32 confound discovery**: The identification of vLLM V1/V0 backend routing as a confound that inflated item variance from 24% to 58% is a standalone methodological contribution. The fix (enforce_eager=True on V0) is immediately actionable.
3. **Honest reporting of failures**: The paper transparently reports the blocked hardware experiment (exp-003), partial 14B results, and the confound discovery that invalidated the original hypothesis. This intellectual honesty is commendable.
4. **Fine-tuning G-study is genuinely novel**: No prior work has applied G-theory to decompose fine-tuning variance. The finding that learning rate dominates (17.8%) with a 10% lr×seed interaction, and inference-training decorrelation (r=0.15), are new and useful.
5. **D-study projections are practically useful**: Showing that optimal allocations diverge qualitatively across benchmarks (MMLU: more items; GSM8K: more seeds) is actionable advice.

**Weaknesses**:
1. **Residual dominance is the paper's Achilles heel** (Tables 1, 3, 5). Residual is the largest component on ALL benchmarks (20–40%). Combined with the opaque "all other" category (26.5% in Table 1), over 54% of MMLU variance is unexplained or aggregated. For a paper whose contribution is variance *attribution*, having the majority of variance *unattributed* is a serious problem. The paper does not adequately discuss what these missing sources might be, nor does it attempt higher-order interaction estimation to decompose the residual.
2. **No confidence intervals or uncertainty quantification**. Variance component estimates are reported as point estimates without bootstrap CIs, jackknife intervals, or any measure of estimation uncertainty. G-theory provides standard methods for this (Brennan 2001, Ch. 8). Without CIs, we cannot assess whether the differences between benchmarks or models are statistically meaningful or within estimation noise. For example, is item_id=24% on MMLU vs 22% on ARC a real difference or sampling variability?
3. **Single GPU architecture severely limits "infrastructure" claims**. Experiment 3 (multi-hardware) was blocked. The paper's title and framing reference "infrastructure" factors, but only numerical precision on one GPU type was tested. The finding that "direct infrastructure×methodology interaction < 0.5%" (Table 4) applies only to precision, not hardware broadly. This should be reflected in the title/abstract.
4. **Model is not treated as a G-theory facet**. The per-model decompositions (Table 1) show item_id ranging from 13.8% (Mistral) to 30.2% (Gemma), suggesting strong model×item interaction. But model is analyzed as a stratification variable, not a facet in the G-study design. A model-as-facet reanalysis of the existing MMLU data (no new experiments needed) would properly attribute this variance and likely reduce the residual.
5. **Fine-tuning G-study uses RoBERTa-large** — an encoder-only model from 2019 — on classification tasks. The relevance to modern LLM fine-tuning (decoder-only models, generation tasks, RLHF/DPO) is questionable. The paper acknowledges this in Limitations but the mismatch weakens the "fine-tuning contribution" claim substantially.
6. **200 items per benchmark**: While adequate for point estimation, the paper does not report sensitivity analyses (e.g., split-half reliability of the variance decomposition, or bootstrap resampling of items) to establish stability. Different 200-item samples from the same benchmark could yield different decompositions, especially for benchmarks with heterogeneous item pools.
7. **REML vs actual estimation method**: The paper states "Variance components are estimated via Restricted Maximum Likelihood (REML)" (Section 3.1) but does not describe the actual implementation. If Henderson Method I (ANOVA-based) was used instead, this is a methodological misrepresentation that matters when variance components are near zero (negative estimates under Henderson are truncated differently than under REML).

**Questions for Authors**:
1. Can you provide bootstrap CIs (e.g., 1000 resamples of items) for the variance components in Tables 1 and 3? This would address whether cross-benchmark differences are real.
2. What happens if model is included as a random facet in the MMLU G-study rather than stratified out? How much of "all other" and "residual" is actually model×item interaction?
3. What specific variance estimation method was implemented? REML, Henderson I, or Henderson III?
4. Have you examined three-way interactions (e.g., model×prompt×item) that might explain the large residual?

**Score**: 3/6 (Weak Reject)
**Confidence**: 4/5

---

### Reviewer 2 — Novelty & Related Work

**Summary**: The paper extends Mesting [2026]'s single-benchmark G-theory study to multiple benchmarks and adds a fine-tuning G-study. The central contribution is a negative result (no universal variance structure), which is valid but incrementally novel. The related work section is severely underdeveloped with only 7 references, missing critical prior work on ML reproducibility, IRT-based item analysis, and benchmark efficiency.

**Strengths**:
1. **Cross-benchmark variance gradient is a genuine empirical contribution**. Showing that variance structure systematically shifts from item-conditional (MMLU) to seed/temperature-conditional (GSM8K/MATH) as benchmarks move from knowledge retrieval to chain-of-thought reasoning is new and interpretable.
2. **D-study allocation divergence has immediate practical value**. The finding that MMLU needs 500 items × 2 prompts × 1 seed while GSM8K needs 250 items × 4 prompts × 4 seeds (Table 7) is directly actionable for benchmark designers.
3. **The confound discovery is a standalone contribution** regardless of the paper's other claims. Documenting that vLLM V0/V1 routing inflates variance estimates warns the community about similar artifacts.
4. **Inference–training decorrelation (r=0.15)** is a novel finding that challenges the assumption that inference-time reproducibility insights transfer to training-time settings.

**Weaknesses**:
1. **Incremental novelty over Mesting [2026]**. The paper's claimed advance over Mesting is (a) adding precision as an infrastructure facet and (b) crossing benchmarks. But precision turns out to be a near-null factor (<1.5% main effect post-fix), so the infrastructure extension yields almost nothing. The paper's strongest findings (benchmark-conditional variance, D-study divergence) would largely emerge from a Mesting-style design without infrastructure crossing.
2. **Severely inadequate bibliography**. 7 references for a top-venue submission is far below standards. Critical omissions include:
   - **Bouthillier et al. (2021, JMLR)**: "Accounting for Variance in Machine Learning Benchmarks" — directly relevant, uses variance decomposition in ML evaluation.
   - **Dodge et al. (2020, EMNLP)**: Fine-tuning instability — essential context for the fine-tuning G-study.
   - **Sellam et al. (2022)**: MultiBERTs — multi-seed BERT training, directly relevant to seed variance.
   - **Dehghani et al. (2021)**: "The Benchmark Lottery" — benchmark selection effects.
   - **Polo et al. (2024)**: tinyBenchmarks — item subsampling for efficient evaluation, directly relevant to item variance.
   - **Rodriguez et al. (2021)**: IRT-based evaluation for NLP — alternative item-level analysis framework.
   - **Shavelson & Webb (1991)**: Foundational G-theory reference beyond Brennan (2001).
   - **Henderson et al. (2018)**: Deep RL reproducibility — established the multi-factor variance decomposition paradigm in ML.
   - **Biderman et al. (2024)**: Lessons from evaluation reproducibility.
   - Any ordering effects literature (the paper includes ordering as a facet but cites no prior work on option ordering effects).
3. **"Diagnostic tool" contribution is unsubstantiated**. The paper claims G-theory as a "practical diagnostic tool" but releases no software, no analysis pipeline, no reusable framework. The "tool" is just applying G-theory, which Mesting [2026] already demonstrated. GeneralizIT and similar R packages already exist. Without a released tool, this contribution claim is empty.
4. **The negative result framing needs more work**. "No universal recipe" is the central claim, but many practitioners already assume this. The paper confirms a suspicion with data but doesn't offer constructive solutions beyond "diagnose your pipeline" — which requires the very G-theory study the paper just demonstrated is expensive (172,800 conditions for one benchmark). Is the recommendation scalable?
5. **Zero figures is unusual and harmful**. For a paper about variance decomposition across benchmarks, visual comparisons (stacked bars, heatmaps, radar charts) would dramatically improve readability. The reliance on 11 tables makes the paper harder to parse and less compelling than it could be.
6. **"Fully crossed" is overstated**. Only Experiment 1 (MMLU) uses the full crossing (3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings). Experiments 2 and the MATH extension use a reduced crossing (2 precisions × 2 temps). This is fine practically but should not be described as a "fully-crossed design spanning 5 benchmarks" in the abstract.
7. **Item dominance on knowledge benchmarks is partially expected from measurement theory**. Items in MMLU span from trivially easy to near-impossible across 57 subjects. A large item variance component is expected given this difficulty range. The paper would benefit from contextualizing this against IRT-based item analysis.

**Questions for Authors**:
1. How does this work relate to Bouthillier et al. (2021), which also decomposed variance in ML benchmarks?
2. Is the recommendation to run a full G-study per benchmark practical? What is the computational cost, and is there a lightweight diagnostic alternative?
3. Why were no figures included? The knowledge-reasoning gradient would be far more compelling as a visualization.
4. Can you release the analysis code alongside the data to substantiate the "diagnostic tool" claim?

**Score**: 3/6 (Weak Reject)
**Confidence**: 4/5

---

## Step 2: Cross-Sharing

**R1 → R2**: The methodological concerns (54% unexplained variance, no CIs, model not as facet) mean the "no universal recipe" finding may partly reflect an underspecified decomposition model rather than a genuine property of evaluation variance. If the residual were decomposed further (e.g., via three-way interactions or model-as-facet), the cross-benchmark differences might narrow or change qualitatively.

**R2 → R1**: The thin related work compounds the experimental concerns. Without positioning against Bouthillier et al., tinyBenchmarks, or IRT-based approaches, it's unclear whether G-theory adds diagnostic power beyond existing methods. The fine-tuning contribution is further weakened because Dodge et al. (2020) already documented seed sensitivity in fine-tuning — the G-theory framing is new but the phenomenon is not.

---

## Step 3: Convergence

**Points of agreement**:
- The paper addresses an important problem (evaluation reproducibility diagnosis)
- The float32 confound discovery is a genuine, standalone contribution
- The cross-benchmark variance gradient is an interesting empirical finding
- Residual dominance (largest component everywhere) is the most serious methodological concern
- Missing statistical uncertainty quantification (no CIs) is a critical gap
- Single GPU limits infrastructure claims; the title/abstract overclaim relative to what was tested
- Related work is severely underdeveloped (7 references)
- Zero figures hurts presentation significantly
- Fine-tuning G-study is novel in framing but limited by RoBERTa on classification tasks
- The "diagnostic tool" contribution is claimed but not delivered (no released software)

**Points of mild disagreement**:
- R1 is slightly more positive about the experimental scale and sees the multi-benchmark extension as substantive; R2 views it as more incremental over Mesting
- R2 emphasizes the bibliography gap more; R1 emphasizes the statistical rigor gap more

**Converged assessment**: Both reviewers agree the paper falls below the acceptance threshold for a top ML venue in its current form, despite addressing a real problem with interesting findings. The gap between claims and delivered evidence is too large.

---

## Step 4: Consolidated Assessment

### Overall Score: 3/6 — Weak Reject

### Headline Assessment
An ambitious and honest study that surfaces interesting empirical patterns (benchmark-conditional variance, float32 confound, inference-training decorrelation), but falls short of top-venue standards due to (1) the majority of variance remaining unattributed, (2) no uncertainty quantification on variance estimates, (3) severely thin related work, and (4) overclaiming relative to what was tested (single GPU ≠ "infrastructure").

### What Would Change Our Minds (Revision Guidance)

**Essential (any two would likely move to borderline)**:
1. **Bootstrap CIs on all variance components** (Tables 1, 3, 5, 9). This is feasible with existing data and would establish whether cross-benchmark differences are statistically meaningful.
2. **Model-as-facet reanalysis** of MMLU data to properly attribute model×item interaction and reduce the opaque residual/all-other categories. No new experiments needed.
3. **Expand bibliography to ≥25 references**, including Bouthillier et al. (2021), Dodge et al. (2020), Sellam et al. (2022), Polo et al. (2024), Rodriguez et al. (2021), Shavelson & Webb (1991), Henderson et al. (2018), and ordering effects literature. Position contributions clearly against each.
4. **Add 3-4 figures**: at minimum a stacked bar comparison across benchmarks, and a D-study projection curve. The paper is currently 11 tables and 0 figures.

**Important (would strengthen but not alone sufficient)**:
5. Downscope "infrastructure" claims to "numerical precision" throughout, including title consideration.
6. Release analysis code (not just data) to substantiate the "diagnostic tool" contribution.
7. Discuss what the large residual might contain and whether higher-order interactions or additional facets (e.g., batch size, system prompt) could reduce it.
8. Clarify the exact variance estimation method (REML vs Henderson) and justify the choice.

**Desirable (for camera-ready)**:
9. Fine-tuning extension to at least one decoder-only model on a generation task.
10. Sensitivity analysis: split-half reliability of variance decompositions across different 200-item samples.

### Contribution Ranking
1. **Float32 confound discovery** — strongest, standalone, immediately actionable ★★★★
2. **Cross-benchmark variance gradient** — interesting empirical finding, needs CIs ★★★
3. **D-study allocation divergence** — practically useful, well-presented ★★★
4. **Inference-training decorrelation** — novel but limited by RoBERTa scope ★★☆
5. **G-theory as diagnostic tool** — claimed but not delivered (no software) ★★
6. **"No universal recipe" as central thesis** — valid but not constructive enough ★★

### Experiment Coverage Assessment
The paper covers 7 of 8 planned experiments (exp-003 blocked, acknowledged). Coverage is thorough. The main gap is not missing experiments but missing *analyses* on existing data (CIs, model-as-facet, higher-order interactions).

### Venue Fit
The paper fits an evaluation/benchmarking track (e.g., NeurIPS Datasets & Benchmarks, COLM, or an EMNLP evaluation workshop). For a main-track top venue, the negative-result framing needs a stronger constructive component (released tool, lightweight diagnostic protocol, or a concrete evaluation standard proposal).
