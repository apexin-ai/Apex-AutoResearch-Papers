# harvest ov attn k07 long v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_ov_attn_k07_long_v2_20260527T100425_result.json`
- **Structured JSON:** [`588d9390fd63f4442014.json`](../../sessions/58/588d9390fd63f4442014.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。实验已在 registry 中，之前被 hook 自动 harvest 过，我做了两处更新：

- **hypothesis** → 补充了与 k=0.85/k=0.9 的对比上下文
- **conclusion** → negative → **success**（24.0% 是 k=0.7 极端压缩点的预期结果）

Registry 最终状态：
| 字段 | 值 |
|---|---|
| status | DONE |
| conclusion | success |
| overall_sr | **24.0%** (120/500) |
| per_task_sr | T1:38, T2:24, T3:38, T4:14, T5:4, T6:50, T7:20, T8:40, T9:6, T10:6 |
| server | westd-38929 |
| gpu_hours | 9.79h |
| log_path | `~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log` |
| results_json | `/root/autodl-tmp/importance_margin_vla_compress/results/openvla_attention_prune_k07_long_seed42.json` |

无活跃 cron 需要清理。

---
