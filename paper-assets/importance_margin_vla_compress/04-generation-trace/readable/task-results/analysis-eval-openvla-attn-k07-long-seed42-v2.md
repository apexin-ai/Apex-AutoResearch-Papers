# analysis eval openvla attn k07 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_openvla_attn_k07_long_seed42_v2_20260526T035838_result.json`
- **Structured JSON:** [`4bc53f7997f32eb82d69.json`](../../sessions/4b/4bc53f7997f32eb82d69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
实验: eval_openvla_attn_k07_long_seed42_v2
SR: 24.0% (120/500)
对比: Attn k=0.9=44.0%, L2norm k=0.7=31.2%, Random k=0.7=38.8%
conclusion: negative
```

Attention pruning 在 k=0.7 时 cliff 明显：从 k=0.9 的 44.0% 骤降到 24.0%（-20pp）。且 Attn k=0.7 (24.0%) 是三种 scoring 方法在 k=0.7 下表现最差的（L2norm 31.2%, Random 38.8%），说明 attention scoring 在高压缩率下退化最严重，cliff 位置大约在 k=0.7~0.9 之间。

---
