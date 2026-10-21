# ops harvest3 deploy4 s47

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest3_deploy4_s47_20260529T041242_result.json`
- **Structured JSON:** [`f72dcded7c59dbe0b749.json`](../../sessions/f7/f72dcded7c59dbe0b749.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部仍在运行，无一完成。

## 当前进度

| exp_id | 服务器 | 当前位置 | 累计 SR | 运行时间 |
|--------|--------|---------|---------|---------|
| eval_pi05_attention_k085_long_seed47_w38 | westd-38929 | T6 完成 (6/10) | 171/350 = 48.9% | 111.6min |
| eval_pi05_attention_k050_long_seed47_w41 | westd-41074 | T5 完成 (5/10) | 179/300 = 59.7% | 107.5min |
| eval_pi05_random_k095_long_seed47_cqa1 | cqa1-33015 | T0 进行中 (ep20) | 13/20 = 65% | 刚启动 ~11min |

**w38** 和 **w41** 预计还需 ~60-80min 完成（按当前速率）。**cqa1** 刚开始，预计需 ~3h。

全部 GPU 仍被占用，无法部署新实验。需等当前实验完成后再收割和部署。

---
