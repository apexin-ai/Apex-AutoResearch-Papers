# debug check dose response final

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_check_dose_response_final_20260518T162658_result.json`
- **Structured JSON:** [`84155f5e16a26981aaf3.json`](../../sessions/84/84155f5e16a26981aaf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**实验仍在运行，未完成。**

| | GPU 0 (dose0) | GPU 1 (dose1) |
|---|---|---|
| 条件 | top-4, 8, 12, 16 | top-20, 24, 28, 32 |
| 已完成 | top4 ✅, top8 ✅ | （无） |
| 当前进度 | top12: 7100/7500 (ETA ~1min) | top20: 6500/7500 (ETA ~3min) |
| 剩余条件 | top16 | top24, top28, top32 |
| 速度 | 6.7 calls/s | 6.1 calls/s |

**已产出文件：**
- `dose_response_top4.json` — paired_mse=0.071, token_div=0.5, KL=2.46
- `dose_response_top8.json` — paired_mse=0.071, token_div=0.5, KL=2.44

**ETA 估算：** 每个条件约 19-20 min。GPU 0 还需 ~20 min（1个条件），GPU 1 还需 ~63 min（3个条件）。瓶颈在 GPU 1，预计约 **65 分钟后全部完成**（~01:32 服务器时间）。

**注意：** top4 和 top8 的 paired_mse 完全相同（0.0710），token_divergence_rate 也一样（0.5），KL 仅微降（2.46→2.44）。n_samples 只有 2，样本量很小。需要等全部 8 个条件跑完后看完整曲线。

---
