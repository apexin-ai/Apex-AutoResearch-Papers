# ssh quick diag opus mistral

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_quick_diag_opus_mistral_20260522T042954_result.json`
- **Structured JSON:** [`d3431412b7235116c370.json`](../../sessions/d3/d3431412b7235116c370.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 模型响应时间对比

| 模型 | 延迟 |
|------|------|
| deepseek-v4-pro | 1.4s |
| gpt-5.5 | 2.2s |
| **claude-opus-4-7** | **4.5s** |
| claude-sonnet-4 | 6.6s |

curl 测试 Opus 耗时 17.4s（含连接开销），**无 rate-limit headers 返回**（grep 无匹配）。

**结论**：Opus 延迟 4.5s 属于模型本身 TTFT 较高，不是代理限速（无 rate-limit/retry-after headers）。Sonnet 反而更慢（6.6s），可能是偶发波动。整体看代理侧无明显限流。

### 2. Mistral 下载进度

- **Mistral-Large-Instruct-2407-AWQ**: 51GB, 8 个 safetensors 文件
- AWQ 量化版完整大小约 50-52GB → **已下载完成 (100%)**

### 3. Judge 收集进度

| Judge | 条数 |
|-------|------|
| gpt-5.5-proxy | 38 |
| qwen3-235b-proxy | 30 |
| gemini-2.5-pro-proxy | 21 |
| deepseek-v4-pro-proxy | 14 |
| claude-sonnet-4.6-proxy | 12 |
| claude-opus-4.7-proxy | 11 |

总计 126 条，进度较早期。Opus/Sonnet 条数最少，与其较高延迟一致——单位时间吞吐低。

---
