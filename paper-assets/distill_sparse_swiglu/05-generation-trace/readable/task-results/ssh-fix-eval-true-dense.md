# ssh fix eval true dense

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-eval-true-dense_20260515T162544_result.json`
- **Structured JSON:** [`fdca5d92062ccdeec7cf.json`](../../sessions/fd/fdca5d92062ccdeec7cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 已释放，cuda:1 训练进程正常运行。evaluate.py md5: `f4086818bb55dc354ea4c6fe8ed8899a`。

---

## 结果汇总

| exp_id | True Dense | Pred Hard Mask | TEAL Sparse | Sparsity | PPL↑ vs True Dense |
|--------|-----------|----------------|-------------|----------|-------------------|
| mvp_bce_s42 | 6.12 | 27.96 | 44.54 | 0.496 | +628% |
| mvp_bce_s123 | 6.12 | 28.38 | 44.59 | 0.496 | +629% |
| mvp_bce_s456 | 6.12 | 28.14 | 43.03 | 0.496 | +603% |
| mvp_kl_norm_v2_s42 | 6.12 | 9.21 | 12.08 | 0.498 | +97% |
| mvp_kl_norm_v2_s123 | 6.12 | 9.25 | 11.91 | 0.498 | +95% |
| mvp_kl_norm_v2_s456 | — | — | — | — | (训练中) |

### 修复内容
- **Bug**: `evaluate_perplexity(model, ...)` 传入的 `model` 已被 `PredictorWrapper._patch_mlps()` monkey-patch，"dense" 实际走 predictor hard mask 路径
- **Fix**: 添加 `evaluate_true_dense()` 函数，临时用 `_make_original_fwd()` 还原所有 MLP forward，评估后恢复 patch
- **影响**: 之前报告的 PPL 增幅（BCE ~58%, KL ~31%）严重低估。实际对比 true dense，BCE TEAL sparse PPL 增幅 ~620%，KL 增幅 ~97%

### KL vs BCE 差距的新解读
KL predictor hard mask PPL (9.2) 接近 true dense (6.12)，说明 KL predictor 精准识别了不重要 neuron。BCE predictor hard mask PPL (28.0) 远离 true dense，说明 BCE predictor 大量误杀重要 neuron。

---
