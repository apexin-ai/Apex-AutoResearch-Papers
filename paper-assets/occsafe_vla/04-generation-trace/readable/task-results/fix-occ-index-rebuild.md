# fix occ index rebuild

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_occ_index_rebuild_20260520T164721_result.json`
- **Structured JSON:** [`373518d017bdd3663093.json`](../../sessions/37/373518d017bdd3663093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

**occ_index.json 格式已正确**，无需修复：
- 格式：`{task_name: {file: path, demos: {demo_key: traj_len}}}` — 与 datasets.py 期望一致
- 9 个 task，每个 50 demos，共 450 demos

**HDF5 结构正确**：
- 路径 `data/{demo_key}/bev_binary`，shape `(traj_len, 64, 64)`，dtype bool
- `traj_len` 与 occ_index.json 中记录的一致（LenOK 全部 True）

**非零验证通过**：
- 所有 9 个 task 的 bev_binary 非零率 34%~46%
- 每帧约 1500~2000 个非零像素（共 4096），远非全零

occ_index.json 可能在之前已被修复过（服务器上已是正确格式）。当前数据状态可以直接用于训练。

---
