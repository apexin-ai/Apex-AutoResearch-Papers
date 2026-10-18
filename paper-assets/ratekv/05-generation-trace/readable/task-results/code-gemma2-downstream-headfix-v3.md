# code gemma2 downstream headfix v3

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma2_downstream_headfix_v3_20260515T194418_result.json`
- **Structured JSON:** [`427909c6aaa953c55f1d.json`](../../sessions/42/427909c6aaa953c55f1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证清单全部通过：

| 检查项 | 结果 |
|--------|------|
| `orig_attn.head_dim` 返回 256 | ✅ |
| eval_ppl.py 不影响其他模型（try/except fallback） | ✅ |
| CUDA_VISIBLE_DEVICES=1 设置正确 | ✅ |
| dry-run arc_challenge limit=50 通过，无 shape mismatch | ✅ (acc=0.6) |
| registry 已更新修复信息 | ✅ |

修复内容：`eval_ppl.py` 第 32-35 行，`head_dim` 改为优先从 `model.model.layers[0].self_attn.head_dim` 读取（Gemma-2 返回 256），`AttributeError` 时 fallback 到原逻辑，兼容所有其他模型。

---
