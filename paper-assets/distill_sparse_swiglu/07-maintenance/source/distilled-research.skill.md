# LLM Activation Sparsity — Research Patterns (25 papers, 2023–2026)

## Evaluation Consensus

**Metrics** (7/8): WikiText-2 PPL + zero-shot accuracy (ARC-C/E, HellaSwag, PIQA, Winogrande, BoolQ) + MMLU 5-shot. Throughput in tok/s for systems papers. Source: TEAL, R-Sparse, SPON, Polar Sparsity. Confidence: high.

**Models** (7/8): Llama-2-7B universal baseline; Llama-3-8B + Mistral-7B standard trio. OPT declining. >13B: TEAL/Polar Sparsity (70B), Compact LM (15B). Confidence: high.

**Reporting** (8/8): Single-run, no std/CI, bold best per group. Field standard. Confidence: high.

**Calibration** (5/8): 10–16 samples from C4/WikiText suffice for training-free methods. Confidence: high.

## Competitive Landscape

**Training-free dominance**: TEAL (ICLR'25 Spotlight) — 40% sparsity, 1.42× speedup, no training. Any training-based method must substantially beat this. R-Sparse adds low-rank for ~1pp extra. 6/25 papers position against TEAL. Confidence: high.

**Predictor overhead fatal**: DejaVu pioneered contextual sparsity but ShadowLLM showed it's *slower* than dense (2981 vs 2609ms, OPT-13B). Source: ShadowLLM, Polar Sparsity. Confidence: high.

**Sweet spot 40–50%**: Below 40% gains too small; above 50% quality degrades sharply (TEAL PPL 9.06 at 65%). Support: 6/8. Confidence: high.

## Gaps Our Work Exploits

**SwiGLU structure unexploited**: SwiGLU only 65% sparsity vs 95% ReLU (ReLU Strikes Back). Training-free methods treat SwiGLU as generic non-ReLU — no paper exploits gate×up structure. Support: 4/8. Confidence: high.

**Batch inference unsolved**: MLP sparsity degrades with batch size (union activation). Polar Sparsity pivoted to attention-only. Static/distilled masks circumvent this. Support: 3/8. Confidence: medium.

**No recovery for training-free**: TEAL/R-Sparse/CATS accept permanent quality loss. Only SPON adds learnable correction (0.016% params). Combining distillation with recovery unexplored. Support: 2/8. Confidence: medium.

**Per-task ≈ per-input masks**: IF-Pruning showed <1% degradation, implying stable domain-level patterns. Lower layers share universally; upper layers specialize. Support: 1/8 strong. Confidence: medium.

## Baselines

Must-have (≥3/8): Dense, TEAL, CATS, ReLUfication-no-retrain (catastrophic failure reference). Strong adds: R-Sparse, GRIFFIN. SPON if recovery comparison needed.
