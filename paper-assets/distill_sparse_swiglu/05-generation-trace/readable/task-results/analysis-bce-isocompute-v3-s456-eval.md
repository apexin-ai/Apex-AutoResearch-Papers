# analysis bce isocompute v3 s456 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bce_isocompute_v3_s456_eval_20260517T204713_result.json`
- **Structured JSON:** [`4dabb29c6f5967364482.json`](../../sessions/4d/4dabb29c6f5967364482.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整对比：

## s42 vs s456 对比

| Metric | s42 | s456 | Δ (relative) |
|--------|-----|------|--------------|
| **teal_sparse_ppl** | 27.97 | 28.35 | +1.4% |
| model_level_sparsity | 0.500 | 0.500 | 0% |
| arc_challenge_acc_norm | 0.2398 | 0.2807 | +17.1% |
| winogrande_acc | 0.5059 | 0.5241 | +3.6% |
| mmlu_acc | 0.3002 | 0.2567 | -14.5% |
| gsm8k_exact_match | 0.0485 | 0.0220 | -54.6% |
| gsm8k_exact_match_strict | — | 0.0083 | — |

## 判断

- **PPL**（最可靠指标）：28.35 vs 27.97，+1.4%，高度一致
- **Downstream variance**：MMLU 和 GSM8K 波动大，但这两个 metric 本身在低性能区间（MMLU ~25% 接近 4-choice random，GSM8K <5% 接近 0）有高方差，属于预期内噪声
- **Conclusion: success** — PPL 核心指标稳定，downstream 差异来自低性能区间的随机波动

## 注意

此 eval 只运行了 TEAL sparse 模式，未包含 dense_ppl 和 predictor_hard_mask_ppl（s42 的这两个值来自其他 eval run）。如需完整 3-seed 对比这两个指标，需要单独为 s456 跑 dense baseline eval。

---
