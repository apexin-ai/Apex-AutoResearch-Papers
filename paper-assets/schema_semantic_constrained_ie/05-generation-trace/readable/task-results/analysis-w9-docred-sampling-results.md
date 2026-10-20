# analysis w9 docred sampling results

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w9_docred_sampling_results_20260516T195333_result.json`
- **Structured JSON:** [`273df055aba8a57599a8.json`](../../sessions/27/273df055aba8a57599a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**实验失败**，未产生任何输出。

### 失败原因

模型路径错误：脚本尝试加载 `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`，但：
1. 该路径在 westd-21461 上不存在（`/root/autodl-tmp/models/` 下只有 Mistral 相关模型）
2. 即使存在，多层嵌套路径 `Qwen3-8B-ms/Qwen/Qwen3-8B` 会被 transformers 误解为 HuggingFace repo ID 格式

### Greedy baseline 参考（phase2_docred_full_s1，Qwen ZS constrained greedy）

| Metric | Value |
|--------|-------|
| ET_pct | 0% |
| RV_pct | 0.03% |
| DR_pct | 10.21% |
| CF_pct | 2.57% |
| R_F1 | 8.23 |
| E_F1 | 59.37 |

### 修复建议

需要将 Qwen3-8B 模型下载到 westd-21461 上（或修改配置指向正确路径），然后重新运行。当前服务器只有 Mistral-7B 模型。

要我将失败报告写入 `w9_sampling_analysis.md` 并更新 registry 状态为 FAILED 吗？

---
