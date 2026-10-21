# analysis kl35 kl45 eval teal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl35_kl45_eval_teal_20260518T175653_result.json`
- **Structured JSON:** [`a00f213f6993deb23953.json`](../../sessions/a0/a00f213f6993deb23953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。两个实验都标记为 `conclusion=negative`。

## 汇总表

| Metric | kl_sparsity35_s42_eval_teal | kl_sparsity45_s42_eval_teal |
|--------|---------------------------|---------------------------|
| PPL | **9.31** | **10.80** |
| ARC (acc_norm) | **38.91%** | **39.16%** |
| WinoGrande | **67.64%** | **64.64%** |
| MMLU | **40.41%** | **30.37%** |
| GSM8K | **7.73%** | **2.96%** |
| Actual Sparsity | 33.6% | 44.9% |
| Errors | None | None |

## 严重异常：Downstream 指标崩塌

PPL 完全符合预期（35%→9.31，45%→10.80，与 30%/40%/50% 单调递增），**但 downstream 全部崩塌**：

| Metric | KL 30% (参考) | KL 35% (本次) | KL 45% (本次) | KL 50% (参考) |
|--------|------------|------------|------------|------------|
| ARC | 51.19% | 38.91% | 39.16% | 46.42% |
| WinoGrande | 71.98% | 67.64% | 64.64% | 67.40% |
| MMLU | 62.68% | 40.41% | 30.37% | 51.05% |
| GSM8K | 38.06% | 7.73% | 2.96% | 19.94% |

35% 和 45% 的 downstream **比 50% 还差**，这在 PPL 单调递增的前提下不可能。特别是：
- MMLU 35%=40.41% vs 50%=51.05% (低 10pp)
- GSM8K 35%=7.73% vs 50%=19.94% (低 12pp)
- GSM8K 45%=2.96% 接近随机

**最可能的原因**：eval 脚本中 lm-eval 的 few-shot 配置或 mask 应用方式与之前 30%/50% 的 eval 不一致。PPL 用自定义 eval loop 所以正常，downstream 走 lm-eval harness 可能在 mask 传递上有 bug。建议对比本次和 30%/50% eval 的 lm-eval 调用方式差异。

---
