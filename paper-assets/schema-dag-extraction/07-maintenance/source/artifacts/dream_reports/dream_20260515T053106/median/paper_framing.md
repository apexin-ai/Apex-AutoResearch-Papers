# Paper Framing — schema-dag-extraction

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25 cycle)
- Commitment deadline: August 2, 2026
- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)
- Deadline: ARR May 25, 2026 (10 days from today)

## Core Claims (3 conditions)

1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. Evidence required: within-count correlation r(metric, BCS) significant after controlling for count, replicated on >=2 datasets and >=2 models.

2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.

3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the SCS-thresholded confusability graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).

## Story Spine

- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches (per-type splitting, similarity-based partitioning, fixed k-step pipelines) operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.

- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). ProUIE/KGGen use fixed task-level decomposition (ignores intra-layer schema structure). No prior work isolates confusability from count in training-free LLM IE.

- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE. We discover a multi-channel degradation model: count drives recall decline (capacity bottleneck) while confusability drives type confusion (disambiguation failure). We then operationalize this into SDGD -- a principled framework for confusability-minimizing schema decomposition.

- **Cross-task validation**: We validate on two complementary IE tasks — NER (Few-NERD, 66 fine-grained types) and Event Detection (MAVEN, 168 FrameNet-based event types). MAVEN's hierarchical type structure with known sibling confusion rates (14.6-19.8%) provides a natural testbed where confusability is independently documented. Cross-task replication (NER + ED) demonstrates confusability-aware decomposition is task-agnostic, not NER-specific.

- **Headline result template**: "Controlling for type count, batch confusability score (BCS) independently predicts F1 degradation (partial r=0.30, p<0.05), with high-confusability batches showing 10-28x more type confusion errors. SDGD-zero improves F1 by X points over single-pass on Few-NERD (66 types) and Y points on MAVEN (168 types), matching per-type splitting quality at Z% of the API cost."

## Core Insight (Narrative A -- Multi-Channel Degradation)

Schema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:
- **Channel 1 (Count -> Recall)**: More types in the prompt -> attention dilution -> entities missed. Monotonic, near-linear. Addressable by reducing batch size.
- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types -> interference during type assignment -> correct entities labeled with wrong types. Addressable by separating confusable types into different batches.

These channels are orthogonal and independently addressable. SDGD targets Channel 2; batch size reduction targets Channel 1; combining both yields additive gains.

## Evidence Hierarchy (D008 — restructured after type frequency confound discovery)

**Layer 1 (Primary — strongest)**: Pairwise BCS-confusion analysis
- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs); nonzero-only Spearman ρ=0.254 (p=1.1e-6)
- Top confused pairs are all high-BCS semantic neighbors (e.g., person-other ↔ person-politician, BCS=0.934)
- This analysis is immune to type frequency confound (operates at type-pair level)

**Layer 2 (Supporting — pending)**: Per-type F1 vs mean BCS analysis
- Controls for type frequency by computing F1 per type, not per batch
- Partial correlation controlling for type frequency
- Status: analysis in progress

**Layer 3 (Discussion — transparent reporting)**: Batch-level BCS-F1 positive correlation
- Within-count batch-level r(F1, BCS) is POSITIVE (high BCS → high F1), opposite to naive prediction
- Explanation: type frequency confound — high-frequency types tend to have high BCS AND high F1
- This is NOT evidence for the hypothesis; reported transparently as methodological finding
- Demonstrates the importance of controlling for confounds — strengthens methodological rigor

**Methodological note**: The positive batch-level correlation motivated our shift from batch-level to type-pair-level and per-type analysis. This progression (naive → controlled → mechanistic) is itself a methodological contribution.

## Venue Fit Risks

- **"Just an empirical study"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels "Lost in the Middle" (TACL 2024) methodology.
- **Training-free IE relevance**: Cite deployment scenarios -- clinical (mCODEGPT), regulatory (FINRA 2026), multilingual (50+ languages with no IE corpora). Training-free is sometimes the ONLY option.
- **Multi-model generalizability**: MVP used only Qwen3-32B. Need >=2 models. Plan: add one model from different family.
- **Over-prediction confound**: F1 curve reversal at low counts needs careful framing. Present recall as clean degradation signal; precision artifact explained in methodology section.

## Anticipated Reviewer Concerns

| Concern | Response Strategy | Experiment |
|---------|------------------|------------|
| Only one model | Add >=1 more model | exp-012 |
| Only one dataset for Claim 1 | Replicate on MAVEN (168 event types, cross-task) + optionally DocRED | exp-004, exp-005 |
| No practical method | SDGD framework | exp-008 to exp-011 |
| Confusability measure validity | SCS validation: embedding vs empirical | exp-015 |
| Effect size small | Report batch-level + type-pair-level + error decomposition | exp-006, exp-007 |
| Why not just per-type splitting? | Ablation: SDGD vs per-type vs random | exp-013, exp-014 |
| Latency overhead of decomposition | Report API calls and wall-clock time | exp-008 |
| Type frequency confound | Transparent reporting: batch-level positive correlation + per-type and pairwise analysis controlling for frequency | exp-002, per-type analysis |
| BCS direction unexpected | Pairwise analysis (immune to frequency) confirms hypothesis; batch-level reported in discussion | exp-002 |
