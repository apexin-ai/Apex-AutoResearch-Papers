# eval occ s1 45K eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_occ-s1-45K-eval_20260521T114827_result.json`
- **Structured JSON:** [`37e666e733bfebbbeb7b.json`](../../sessions/37/37e666e733bfebbbeb7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况与预期不同：

- **当前进度**: step 24851/50005（不是 ~41396）
- **速度**: ~1.08 it/s
- **距 45000 还有**: 20149 步 ≈ **5 小时 11 分钟**（预计约 UTC 01:00，即北京时间明天 09:00）

训练命令是从 17500_chkpt resume 的，`save_freq=5000`，所以 25000 checkpoint 即将在 ~2 分钟内出现。

已有 checkpoint: 17500, 30000, 35000, 40000（后三个应是之前 run 产生的）。

**要继续轮询等 45K 吗？** 约 5 小时后才到。或者你想先用已有的 40K checkpoint 跑 eval？

---
