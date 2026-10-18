# diagnose eval openvla attn k09 object seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_attn_k09_object_seed42_v3_20260524T224910_result.json`
- **Structured JSON:** [`64804814989d3180b6c1.json`](../../sessions/64/64804814989d3180b6c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `eval_openvla_attn_k09_object_seed42_v3` 完成，registry 已更新为 DONE/success，cron 已清除。

**结果汇总：**
- **Overall SR: 61.4%** (307/500)
- Attention pruning 256→230 vision tokens (k=0.9)
- Per-task SR: salad_dressing/ketchup/orange_juice 76% | alphabet_soup/tomato_sauce/chocolate_pudding 74% | milk 52% | cream_cheese 46% | bbq_sauce 38% | butter 28%
- 耗时 260.6 min

注意：结果 JSON 中 `k_ratio` 字段为 null（logging bug），但日志确认 pruning 已生效：`[Attn Pruning] 256 -> 230 vision tokens (k=0.9)`。

---
