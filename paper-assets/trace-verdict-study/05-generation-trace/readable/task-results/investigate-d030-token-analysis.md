# investigate d030 token analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_d030_token_analysis_20260515T224517_result.json`
- **Structured JSON:** [`28e1f1ff1693cd07676c.json`](../../sessions/28/28e1f1ff1693cd07676c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析报告已保存到 `/root/trace-verdict-study/artifacts/d030_token_analysis.txt`。

## 结论：Label truncation 假说**未确认**

### 核心发现

| 项目 | 结果 |
|------|------|
| max_length | 2048（SFTConfig + to_chat_text 一致） |
| VOTA >2048 比例 | **91.7%**（4327/4720）|
| exception_only >2048 | 13.3% |
| no_trace >2048 | 0.0% |
| to_chat_text() | **存在** label-preserving truncation |
| 截断后实际长度 | 2049 tokens（off-by-one，encode-decode 往返） |
| 被截掉的 token | **`\n`**（`<|EOT|>` 之后的尾部换行），**不是 label** |

### 为什么不是 label truncation

`to_chat_text()` 从初始 commit 就存在，truncate input content 而非序列右端。虽然有 off-by-one bug（91.7% 的样本 2049 tokens），SFTTrainer 右截断只切掉 `<|EOT|>` 后的 `\n`，label "pass"/"fail" 和 `<|EOT|>` 均完整保留。

### 需要排查的替代原因

1. **评估端 chat template 不匹配**：DeepSeek 推理时 prompt 格式可能与训练不一致
2. **生成参数问题**：DeepSeek 可能需要不同的 decoding 设置
3. **全 trace 输入被截断太多**：91.7% 的 VOTA 样本大量丢失 trace 信息（从 ~2626 截到 ~1976 input tokens），但这只会降低准确率，不应产生 garbage tokens
4. **建议检查 `deepseek_full_trace`** 是否也有类似 garbage 问题，以区分 DeepSeek-specific vs VOTA-specific

---
