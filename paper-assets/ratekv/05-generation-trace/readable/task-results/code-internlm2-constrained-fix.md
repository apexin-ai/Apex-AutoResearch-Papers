# code internlm2 constrained fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_internlm2_constrained_fix_20260516T030739_result.json`
- **Structured JSON:** [`c255effd100f790cb5bc.json`](../../sessions/c2/c255effd100f790cb5bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Running successfully — model loaded, profiles synthesized, allocations solved, now evaluating PPL on WikiText-2. No import errors.

修复完成并已提交：
- **修复内容**：从 profiling 脚本移植了 `patch_attention_internlm2` + `restore_attention_internlm2`（处理 InternLM2 的 fused `wqkv` + einops rearrange），替换了通用 `eval_ppl.patch_attention` 调用
- **实验 ID**：`internlm2_constrained_mckp_v2`，在 `westd-37397` cuda:0 运行中
- **日志**：`~/runs/ratekv/internlm2_constrained_mckp_v2.log`

---
