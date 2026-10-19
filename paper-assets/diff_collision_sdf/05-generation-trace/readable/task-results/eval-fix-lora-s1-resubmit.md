# eval fix lora s1 resubmit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_fix-lora-s1-resubmit_20260528T101832_result.json`
- **Structured JSON:** [`4ade0ca6b9e38c159576.json`](../../sessions/4a/4ade0ca6b9e38c159576.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

磁盘 350G 已满，需腾出 ~8G 空间才能拷贝 LoRA s1 checkpoint。

以下 `29999` step 的 checkpoint 可以安全删除（都有对应的 `30000` step），每个 7.2G：

| 可删目录 | 大小 |
|---|---|
| `seed1_l005/29999/` | 7.2G |
| `seed1_l01/29999/` | 7.2G |
| `seed2_l005/29999/` | 7.2G |
| `seed2_l01/29999/` | 7.2G |

删除任意 1 个就够。建议删 `seed1_l005/29999/` 或 `seed1_l01/29999/`。

另外，`pi05_lora_baseline_object_pudding_seed1/` 下有 1.6M 的残留文件（刚才传输失败留下的），也需清理。

确认删除哪个？

---
