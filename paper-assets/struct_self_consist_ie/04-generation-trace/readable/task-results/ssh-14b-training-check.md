# ssh 14b training check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-training-check_20260520T141049_result.json`
- **Structured JSON:** [`5d20b28b722581ee550a.json`](../../sessions/5d/5d20b28b722581ee550a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。当前 session 无活跃 cron（监控 cron 来自之前的 session，已自然失效）。

## 结果汇总

**训练成功完成** `exp_qwen25_14b_fewnerd`

| 指标 | 值 |
|------|-----|
| 模型 | Qwen2.5-14B-Instruct QLoRA |
| 总步数 | 41,180 (5 epochs) |
| Train loss | 0.0348 |
| Eval loss | 0.0323 |
| 训练时长 | ~29.8h (2×5090) |

**Checkpoint 位置：**
- QLoRA adapter（最终）: `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-14b-fewnerd-qlora-s42/` (5.2GB)
- 已有 merged（早期 ckpt36000）: `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-14b-fewnerd-merged-ckpt36000/` (28GB)

**后续注意：** 最终 checkpoint 是 QLoRA adapter（step 41180），不是 merged 模型。已有的 merged 版本是 ckpt36000（早期），不是最终版。用于 N∈{1,2,4,8,16} inference 前需要先 merge 最终 adapter 到 base model。

---
