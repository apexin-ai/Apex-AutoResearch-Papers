# Paper Framing — Embedding Alignment Gap

## Target Venue
EMNLP 2026 ARR (deadline: May 25, 2026) — Findings full paper (8 pages)

## Title (working)
"The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training"

## Core Insight
In iterative self-training (student-as-generator feedback loop), the geometric diversity of a model's internal embeddings becomes systematically misaligned with content diversity (measured by rare n-gram survival). This "alignment gap" worsens monotonically across generations, causing diversity-based data selection using internal representations to **accelerate** rather than prevent model collapse. Frozen external embeddings (e.g., Contriever) are immune to this misalignment.

## Core Claims

### C1: Alignment Gap Exists and Worsens Monotonically
- Internal embedding diversity selection ratio degrades from ~1.04 (Gen 0) to ~0.52 (Gen 7)
- The model increasingly selects vocabulary-poor samples when using its own representations for diversity scoring
- Evidence: Phase 2 RGDS selection diagnostics (GPT2-125M, WikiText-103, self-iterate)

### C2-weak: Frozen External Embeddings Are Immune to the Gap
- Contriever-based selection maintains ratio >1.1 across all generations (1.14→1.28 through Gen 4)
- External embeddings improve model quality (PPL -6.5% vs uncurated) but do NOT improve rare n-gram survival
- This is a comparative claim: external embeddings "don't make the mistake" internal ones make, not a solution to vocabulary collapse
- The dissociation between PPL improvement and rare n-gram stagnation itself is an interesting finding

### C3: The Gap Causes Accelerated Collapse
- RGDS (internal diversity selection) produces PPL 75.07 vs uncurated 50.28 (+49%) and rare n-gram 0.0051 vs 0.0090 (-43%)
- Complete causal chain: embedding space contracts → "geometrically diverse" = "vocabulary-poor" → selection amplifies homogeneity → accelerated collapse

## Secondary Claims

### S1: PPL and Rare N-gram Measure Different Collapse Dimensions
- External selection improves PPL (-6.5%) without improving rare n-gram survival
- Selection ratio >1.1 translates to PPL gains but not vocabulary diversity gains
- Implication: semantic diversity ≠ lexical diversity in the context of iterative distillation

### S2: Representation Quality Metrics Don't Detect Diversity Collapse
- RankMe increases during collapse (280→303, +8%)
- k-NN probe accuracy stable (0.988 throughout)
- These metrics track representation structure, not content diversity — a cautionary finding for monitoring frameworks

## Anticipated Reviewer Concerns

### R1: "GPT2-125M is too small — does this generalize?"
- Response: GPT2-medium (355M) experiments planned; alignment gap mechanism (embedding space contraction under self-iterate) is architecture-general
- If GPT2-medium shows gap: "scales beyond toy models"

### R2: "Only one dataset (WikiText-103)"
- Response: OpenWebText subset planned as P1
- The mechanism is data-agnostic (self-iterate collapse is well-documented across datasets)

### R3: "N=1 seed — is this noise?"
- Response: 3 seeds per configuration planned; the monotonic trend over 8 generations (not a single-point measurement) reduces seed sensitivity concern
- seed=123 already running as replication

### R4: "You only found a problem, not a solution"
- Response: (a) Embedding re-anchoring experiment planned as simple mitigation; (b) the finding itself has immediate practical value — practitioners should avoid internal-embedding-based curation during iterative training
- If re-anchoring works → upgrade to "found + solved"

### R5: "What's the theoretical explanation for the gap?"
- Connect to neural collapse literature (Papyan et al. 2020): self-iterate reduces intra-class variability → embedding effective dimensionality drops → greedy submodular selection in low-dim space favors collapsed mode directions
- Not a formal proof, but a plausible mechanistic intuition with empirical support

### R6: "External embeddings don't improve rare n-gram — how is C2 useful?"
- C2 is comparative: shows the gap is specific to internal embeddings under training feedback, not an inherent property of embedding-based selection
- PPL improvement shows external selection captures meaningful diversity (semantic level), even if not lexical level
- Opens future work: what selection signal DOES preserve lexical diversity?

## Narrative Arc
1. **Setup**: Iterative self-training causes model collapse (established). Diversity-based data curation is a natural mitigation idea.
2. **Surprise**: Using the model's own representations for diversity selection makes collapse WORSE, not better.
3. **Explanation**: The Embedding Alignment Gap — internal representations' notion of "diverse" diverges from content diversity as training progresses.
4. **Contrast**: Frozen external embeddings don't suffer this misalignment (but also don't solve vocabulary collapse).
5. **Implication**: Embedding-based diversity selection is unreliable in iterative settings; the field needs vocabulary-aware alternatives.

## Related Work Positioning
- Model collapse: Shumailov et al. (Nature 2024), Alemohammad et al. (2024), Dohmatob et al. (2024)
- Data selection/curation: SemDeDup (Abbas 2023), D4 (Tirumala 2023), DSIR (Xie 2023) — these use external embeddings for static (non-iterative) curation; we show iterative setting introduces new failure mode
- Neural collapse: Papyan et al. (2020) — theoretical grounding for why embeddings lose diversity signal
- Representation quality metrics: RankMe (Garrido et al. 2023) — we show RankMe doesn't detect diversity collapse
