# Literature Survey: Dose-Response Thresholds in Data Augmentation

## Landscape Summary

The literature on noise/error tolerance in training data reveals a consistent but under-theorized phenomenon: **nonlinear degradation thresholds** exist, but their location is highly task- and architecture-dependent.

### 1. Noise Tolerance in Classification vs. Sequential Decision-Making

Rolnick et al. (2017) showed DNNs tolerate extreme label noise (100:1 dilution) in image classification. However, this robustness does not transfer to sequential decision tasks. Our finding—that embodied planning collapses between 10-25% error injection—aligns with the general observation that **multi-step reasoning tasks have lower noise tolerance** than single-step classification. The compounding nature of errors in trajectory-level tasks creates a multiplicative failure mode absent in i.i.d. classification.

### 2. Error Injection for Agent Training: Contrastive vs. Direct

Three dominant paradigms exist for using failure data in agent training:
- **Contrastive/DPO** (ETO, Song et al. 2024): Pairs failures with successes; avoids direct noise injection entirely.
- **Recovery-annotated** (PALADIN, 2025): Pairs each failure with a correction demonstration.
- **Direct mixing** (our approach): Injects error trajectories alongside clean data without explicit pairing.

The literature strongly favors the first two approaches. **No prior work reports systematic dose-response curves for direct error injection into agent SFT**, making our negative result novel. The closest is Wang et al. (2024), who show negative examples help—but only with contrastive structure.

### 3. Data Mixing Laws and Phase Transitions

Recent theoretical work (Ye et al. ICLR 2025; Dohmatob & Feng ICLR 2025) establishes that critical mixing proportions exist and are predictable via scaling laws. Dong et al. (ACL 2024) document "ability conflicts" emerging at high mixing amounts—a phenomenon analogous to our degradation. Seddik et al. provide upper bounds on low-quality data proportion, offering theoretical grounding for our observed threshold.

### 4. Our Contribution's Position

Our finding occupies a unique position: we provide **the first empirical dose-response curve for taxonomy-guided error injection in embodied agent SFT**. The 10%→25% cliff is:
- Sharper than classification noise thresholds (gradual degradation)
- Specific to direct mixing (contrastive methods sidestep it)
- Consistent with theoretical predictions but never previously measured in this setting

This positions our work as an empirical anchor point for the theoretical mixing-law literature, with practical implications for the growing error-injection-for-robustness paradigm.
