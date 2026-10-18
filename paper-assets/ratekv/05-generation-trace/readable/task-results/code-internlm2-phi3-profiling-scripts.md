# code internlm2 phi3 profiling scripts

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_internlm2_phi3_profiling_scripts_20260515T224738_result.json`
- **Structured JSON:** [`98a7fab03b6f35f60f7c.json`](../../sessions/98/98a7fab03b6f35f60f7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建，语法验证通过。

与 CodeLlama 模板的差异汇总：

| | InternLM2 | Phi-3-medium |
|---|---|---|
| model path | `internlm/internlm2-7b` | `microsoft/Phi-3-medium-4k-instruct` |
| GPU | `cuda:0` | `cuda:1` |
| batch_size | 2 | 1 |
| model_name | `"InternLM2-7B"` | `"Phi-3-medium-14B"` |
| output prefix | `internlm2_` | `phi3_medium_` |
| trust_remote_code | `True` | `True` |

注意：两个脚本都加了 `trust_remote_code=True`（InternLM2 和 Phi-3 都需要）。原 phi3 文件使用自定义 `patch_attention_phi3` 的方案已替换为统一的 `eval_ppl.patch_attention`。

---
