# StructFuse Pilot Results (seed=42, 24 repos, 3282 train / 1148 val)

## Qwen2.5-Coder-3B (m2_embed_verify)

| Strategy | Status | Best Step | val_loss | R@1 | R@5 | R@10 |
|----------|--------|-----------|----------|-----|-----|------|
| random | completed | 500 | 0.4834 | 0.5357 | 0.9808 | 1.0 |
| embedding_distance | completed | 500 | 0.4603 | 0.5557 | 0.9808 | 1.0 |
| dataflow_aware | running | — | — | — | — | — |

## StarCoder2-3B (plan_013_starcoder)

| Strategy | Status | Best Step | val_loss | R@1 | R@5 | R@10 |
|----------|--------|-----------|----------|-----|-----|------|
| random | completed | 500 | 0.5113 | 0.4922 | 0.98 | 1.0 |
| embedding_distance | completed | 1000 | 0.4816 | 0.5078 | 0.9843 | 1.0 |
| dataflow_aware | running | 500 | 0.5257 | 0.4756 | — | — |

## Cross-Encoder Comparison

| Encoder | Strategy | val_loss | R@1 | R@5 |
|---------|----------|----------|-----|-----|
| Qwen2.5-Coder-3B | random | 0.4834 | 0.5357 | 0.9808 |
| Qwen2.5-Coder-3B | embedding | 0.4603 | **0.5557** | 0.9808 |
| StarCoder2-3B | random | 0.5113 | 0.4922 | 0.98 |
| StarCoder2-3B | embedding | 0.4816 | 0.5078 | 0.9843 |
| StarCoder2-3B | dataflow | 0.5257 | 0.4756 | — |

## Key Findings
- Embedding > random for both encoders (Qwen +2.0pp, StarCoder +1.6pp R@1)
- Qwen consistently outperforms StarCoder (~5pp R@1 gap)
- R@5/R@10 near saturation across all configs
- Best overall: Qwen embedding (R@1=55.6%)
- All best checkpoints at step 500 or 1000, subsequent overfitting
