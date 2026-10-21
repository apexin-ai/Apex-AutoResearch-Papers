# analysis codellama13b full trace tail256 seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama13b_full_trace_tail256_seed42_20260518T022429_result.json`
- **Structured JSON:** [`29af7fb845e773e22595.json`](../../sessions/29/29af7fb845e773e22595.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结论：**success**。

**核心结果**: CodeLlama-13B tail-256 accuracy = **77.9%** (CI: 75.7%--80.3%)，pass_f1=0.843，fail_f1=0.626。

**跨模型 tail-256 对比**:

| Model | Params | Accuracy |
|-------|--------|----------|
| Qwen-1.5B | 1.5B | 72.6% |
| DeepSeek-6.7B | 6.7B | 76.4% |
| CodeLlama-13B | 13B | 77.9% |
| Qwen-7B | 7B | 78.9% |

4 个模型（3 个 family，1.5B--13B）全部聚集在 72.6%--78.9%（仅 6.3pp 跨度），确认 **256 tokens 信号不足是 universal 的**。13B 模型并未突破 ~79% 的天花板，甚至低于 Qwen-7B，说明在信号极度匮乏时模型规模的边际收益接近零，模型架构/预训练数据的影响大于参数量。

报告已写入 artifacts 并注册，registry 已更新 conclusion=success、metrics、checkpoint_path、log_path。

---
