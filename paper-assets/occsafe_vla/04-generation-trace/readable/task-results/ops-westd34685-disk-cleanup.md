# ops westd34685 disk cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd34685_disk_cleanup_20260523T141255_result.json`
- **Structured JSON:** [`f2280fcfee61a3067d87.json`](../../sessions/f2/f2280fcfee61a3067d87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **4 个旧实验全部删除成功** — cutoff_s0, cutoff_s1, depth_s0, depth_s1 均已不存在
2. **清理后磁盘可用 121G**（350G 总量，已用 230G，66%）
3. **不需要删除中间 checkpoint** — 可用 121G > 80G 阈值，空间充足
4. **注意**：`save_latest_checkpoint_only=False`，训练会保留所有 checkpoint（每个 ~15G）。当前 121G 余量足够支撑 40K step 写入，但如果后续训练持续产出多个 checkpoint，需关注空间

---
