# analyze mvp kl norm v2 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mvp_kl_norm_v2_s42_20260515T155645_result.json`
- **Structured JSON:** [`2ac0abb83dbb65b231d3.json`](../../sessions/2a/2ac0abb83dbb65b231d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 汇总

| 指标 | KL norm v2 (s42) | BCE baseline (mean) |
|------|------------------|---------------------|
| Dense PPL | 9.21 | 28.16* |
| Sparse PPL | 12.08 | 44.05* |
| Δ | **+31.2%** | +56.4% |
| Model sparsity | 0.498 | ~0.5 |

**Conclusion: success** — KL 蒸馏损失的相对 PPL 增幅 (+31.2%) 显著优于 BCE (+56.4%)。

*注意：dense PPL 差异 (9.21 vs 28.16) 说明 BCE baseline 的"统一 eval"可能使用了不同的 WikiText 版本或评估参数。需要用相同 evaluate.py 重新评估 BCE baseline 做严格对比。

---
