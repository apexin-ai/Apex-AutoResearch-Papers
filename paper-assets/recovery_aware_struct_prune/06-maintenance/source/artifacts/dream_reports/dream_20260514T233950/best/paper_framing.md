# Paper Framing — recovery_aware_struct_prune

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25 submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026

## Core Insight (Redundancy Paradox)
Traditional structured pruning removes "redundant" structures (high functional overlap with others) to minimize immediate accuracy loss. We show this logic inverts for RLVR recovery: structures with high functional overlap are precisely the most RLVR-recoverable, because RLVR's global exploration can redistribute their function across retained structures. This creates a **Redundancy Paradox** — what's safe to prune for immediate accuracy is different from what's safe to prune for post-recovery accuracy.

RASP exploits this by protecting structures that are both important AND functionally unique (low CKA overlap = irreplaceable reasoning scaffolding), while allowing removal of structures whose function can be recovered through RLVR's path compression mechanism ("RL Squeezes, SFT Expands", ICLR 2026).

## Core Claims (3)

1. **CKA-aware pruning preserves reasoning ability**: At matched sparsity and parameter count, RASP preserves significantly more post-prune reasoning accuracy than importance-only pruning (MVP evidence: 29% vs 1% GSM8K at 20% sparsity, p<0.0001), and this gap enables qualitatively different recovery outcomes (RASP-pruned models can be recovered via RLVR; standard-pruned models cannot).

2. **Functional overlap predicts per-structure recoverability**: Per-structure CKA functional overlap F(h) is a stronger predictor of post-recovery accuracy restoration than standard importance metrics alone. Validated via mixed-effects regression (layer as random effect) on N=224+ attention heads, controlling for weight norm, gradient importance, and activation magnitude.

3. **Recovery method conditions optimal pruning order**: The relative ranking of pruning strategies changes depending on recovery method (RLVR vs SFT). Structures expendable under RLVR recovery may be critical under SFT recovery, consistent with the "RL Squeezes, SFT Expands" mechanism — RLVR compresses incorrect paths (tolerates removal of overlapping structures) while SFT expands correct paths (needs preserved trajectory-encoding structures).

## Story Spine

- **Problem**: Structured pruning for reasoning LLMs optimizes for immediate post-pruning accuracy, treating subsequent recovery as independent. At moderate sparsity (20-35%), this disconnect can be catastrophic: standard importance-based pruning collapses reasoning ability to near-zero, making recovery impossible regardless of method. The choice of what to prune determines whether recovery can succeed at all.

- **Existing approaches & gaps**: Self-Healing (2025) shows RLVR recovers pruned reasoning models to 95%+ at 25% compression but uses standard pruning and tests only one ratio. GRASPrune (ACL 2026) provides SOTA budgeted structural pruning but doesn't study reasoning-specific recovery. RESP (Dec 2025) uses reasoning-trace calibration but has no recovery phase. No work studies how the pruning structure choice interacts with RLVR recovery quality, or whether optimal pruning differs for RLVR vs SFT recovery.

- **Our framing**: We introduce Recovery-Aware Structured Pruning (RASP), reframing structural redundancy from a flaw to eliminate into a signal of RLVR recoverability. RASP scores structures by S(h) = I(h) × (1 - F(h))^α, protecting functionally unique reasoning scaffolding while allowing removal of structures whose function can be redistributed through RLVR. This connects to the Lottery Ticket Hypothesis at a new level: LTH asks "which subnetwork trains well" (binary); RASP asks "which structures to remove so the remainder recovers well under a specific training paradigm" (paradigm-conditioned trainability).

- **Headline result template**: "At 20% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, RASP preserves 29% GSM8K accuracy (vs 1% for standard pruning), enabling RLVR recovery to X% while standard-pruned models remain unrecoverable. Per-structure CKA overlap explains Y% of variance in recovery outcomes (mixed-effects β = Z, p < 0.001)."

## Venue Fit
- EMNLP Efficient Methods track: natural fit for structured pruning + reasoning model recovery
- Reasoning model compression is timely (DeepSeek-R1, QwQ, etc. driving demand)
- Empirical rigor + mechanistic analysis aligns with EMNLP's preference for thorough experimentation

## Venue Fit Risks
- **"Just another pruning metric"**: Mitigate with Redundancy Paradox framing, LTH generalization (paradigm-conditioned trainability), and mechanistic analysis showing WHY it works
- **"Single model"**: DeepSeek-R1-Distill-Qwen-7B is the most widely-used open reasoning model; multi-sparsity + multi-method comparison compensates
- **"MPruner already uses CKA"**: Different granularity (intra-layer per-head vs inter-layer), different objective (recoverability prediction vs redundancy removal), different domain (reasoning LLM vs CNN/general transformer)

## Anticipated Reviewer Concerns & Experimental Responses

| Concern | Response | Supporting Experiment |
|---------|----------|----------------------|
| Incremental over importance-only pruning | 28pp post-prune gap is qualitative, not incremental; enables vs prevents recovery | exp-001, exp-002 |
| CKA overlap might correlate with simpler metrics | Scoring ablation: CKA vs magnitude/gradient/random | exp-007 |
| Single model generalization | Multi-sparsity (20%, 25%, 30%) + multi-method (Standard, GRASPrune, RASP) | exp-003, exp-005 |
| RLVR vs SFT claim needs controlled comparison | Same pruned models, same data budget, different recovery method | exp-006 |
| Statistical rigor of correlation claim | Mixed-effects regression with covariates at structure level (N=224+ heads) | exp-008 |
| Recovery might just reflect post-prune accuracy | Include GRASPrune (different post-prune accuracy profile) to break correlation | exp-005 |

## Key Differentiations
- **vs MPruner (2024)**: inter-layer CKA for depth pruning in CNNs → RASP uses intra-layer CKA between individual heads for width pruning in reasoning LLMs, optimizing for post-recovery (not immediate) performance
- **vs Self-Healing (2025)**: tests RLVR recovery with standard pruning → RASP optimizes the pruning decision FOR recovery
- **vs RESP (Dec 2025)**: reasoning-trace calibration without recovery → RASP includes recovery-awareness in the pruning score
- **vs GRASPrune (ACL 2026)**: SOTA budgeted pruning without recovery study → GRASPrune is our primary baseline
- **vs PASER (2025)**: optimizes recovery DATA → RASP optimizes pruning STRUCTURE (complementary)
