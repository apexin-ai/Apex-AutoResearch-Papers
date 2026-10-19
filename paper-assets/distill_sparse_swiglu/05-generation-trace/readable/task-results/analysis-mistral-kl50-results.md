# analysis mistral kl50 results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral_kl50_results_20260516T042015_result.json`
- **Structured JSON:** [`3b99f1b3f0d1b37bdb7d.json`](../../sessions/3b/3b99f1b3f0d1b37bdb7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕，cron 此前已不存在（可能已被自动清理）。

**结果汇总：Mistral-7B KL 50% sparsity downstream eval → negative**

| Benchmark | Sparse | Dense | Retention |
|-----------|--------|-------|-----------|
| ARC-c acc_norm | 0.3183 | 0.6024 | 52.8% |
| WinoGrande | 0.6290 | 0.7869 | 79.9% |
| MMLU | 0.2295 | 0.6244 | 36.8% |
| GSM8K strict | 0.0045 | 0.3654 | 1.2% |

MMLU 和 ARC-c 均未达到 70% retention 阈值（0.437 / 0.422），MMLU 接近随机水平，GSM8K 完全崩溃。崩溃模式与 Llama KL 50% 高度一致，确认 50% unstructured sparsity 对 SwiGLU FFN downstream 的破坏与模型架构无关。

---
