# Experimental Setup: Negatives per Query (K) and Checkpoint Selection

## Registry Analysis

### K (negatives per query)
**K = 7** (`num_negatives=7`) for all main experiments: m2_full_qwen, m2_full_starcoder, m2_embed_verify, plan_013_starcoder. Earlier MVP experiments (p2b series) used K=3 but are superseded.

### Dual Checkpoint Comparison

| Run | Encoder | Strategy | Best by val_loss | Best by R@1 | Same? |
|-----|---------|----------|-----------------|-------------|-------|
| m2_full_qwen / random_s42 | Qwen | random | step 1000 (0.4651) | step 1000 (0.553) | Yes |
| m2_full_qwen / random_s43 | Qwen | random | step 500 | step 1500 (0.5501) | **No** (Δ=1000) |
| m2_embed_verify / random | Qwen | random | step 500 (0.4834) | step 500 (0.5357) | Yes |
| m2_embed_verify / embedding | Qwen | embedding | step 500 (0.4603) | step 500 (0.5557) | Yes |
| m2_embed_verify / dataflow | Qwen | dataflow | step 500 (0.5602) | step 500 (0.5436) | Yes |
| m2_full_starcoder / random_s42 | StarCoder | random | step 1000 (0.6134) | step 2500 (0.4604) | **No** (Δ=1500) |
| plan_013_starcoder / embedding | StarCoder | embedding | step 1000 (0.4816) | final (0.5174 > 0.5078@1000) | **No** |
| plan_013_starcoder / dataflow | StarCoder | dataflow | step 1000 (0.5255) | final (0.5078 > 0.4869@1000) | **No** |

- plan_013_starcoder / random: data not available (post-hoc eval, no per-step tracking)
- Remaining m2_full runs (7 Qwen + 8 StarCoder): not yet completed

**Pattern**: 4 of 5 Qwen runs agree (both criteria select same checkpoint); 1 Qwen run (random_s43) diverges (Δ=1000 steps). All 3 evaluable StarCoder runs disagree (R@1 improves after val_loss overfits). This is consistent with StarCoder's flatter loss landscape and weaker pretrained separability (neg_difficulty_analysis: StarCoder margin 2.6-4.1x Qwen).

**Totals**: 8 evaluable runs — 4/8 (50%) same, 4/8 (50%) different. By encoder: Qwen 4/5 same, StarCoder 0/3 same.

---

## Paper Paragraph (Experimental Setup)

**Training and Evaluation Protocol.**
For contrastive training, each query is paired with K=7 negative candidates sampled according to the respective strategy (random, embedding-distance, or dataflow-aware), consistent across all strategies and encoder architectures. We adopt a dual checkpoint selection protocol: during training, we independently track the best checkpoint by validation loss and the best by Recall@1 on a held-out validation set (evaluated every 500 steps). When reporting retrieval metrics, we select the checkpoint that maximizes Recall@1 directly, as validation loss and retrieval performance do not always agree—particularly for StarCoder2, where Recall@1 continues to improve after validation loss begins to overfit. Across 8 completed training runs spanning two encoders and three strategies, both criteria selected the same checkpoint in 4 runs; in the remaining 4 runs (1 Qwen2.5-Coder, 3 StarCoder2), the best-by-Recall@1 checkpoint was selected 500–1500 steps later than the best-by-loss checkpoint. Checkpoint divergence is more prevalent for StarCoder2 (0/3 agreement) than Qwen2.5-Coder (4/5 agreement), consistent with StarCoder2's flatter loss landscape. This dual protocol ensures that reported results reflect the model's best retrieval capability rather than a proxy metric.
