# analysis bootstrap ci extraction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_extraction_20260518T025815_result.json`
- **Structured JSON:** [`f44ca5f24c62bf6272f8.json`](../../sessions/f4/f44ca5f24c62bf6272f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存到 `/root/autodl-tmp/vla-ssd/results/bootstrap_ci_values.json`。

## 汇总（复制到论文用）

| Comparison | Δ | 95% CI | p |
|---|---|---|---|
| Ablation all24 vs baseline (L1) | +0.059 | [0.042, 0.075] | <0.001 |
| Ablation all24 vs control8 (L1, specificity) | +0.042 | [0.029, 0.056] | <0.001 |
| RSA trained vs untrained image_mean (L12) | +0.079 | [0.060, 0.098] | <0.001 |
| RSA trained vs untrained last_preaction (L12) | +0.047 | [0.023, 0.070] | <0.001 |
| Action R² trained vs untrained imgmean peak | +0.015 | [0.004, 0.025] | 0.006 |
| Action R² trained vs untrained lastpre peak | +0.069 | [0.047, 0.090] | <0.001 |
| Action R² trained L19 vs untrained L32 lastpre | +0.045 | [0.032, 0.058] | <0.001 |
| Llama2base vs untrained (L1 imgmean) | +0.082 | [0.062, 0.103] | <0.001 |
| Trained vs llama2base (L1 imgmean) | −0.004 | [−0.013, 0.005] | 0.78 (ns) |
| Trained vs untrained (L1 imgmean) | +0.079 | [0.061, 0.098] | <0.001 |

关键发现：
- llama2base 在 L1 显著高于 untrained（Δ=+0.082），但 trained 与 llama2base 无显著差异（Δ=−0.004, ns）→ L1 action encoding 主要由语言预训练建立
- 所有 ablation 和 RSA 对比的 CI 均不包含 0

---
