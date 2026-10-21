# ops 10894 disk cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894_disk_cleanup_20260524T175145_result.json`
- **Structured JSON:** [`a6bb005a33103eebf8e7.json`](../../sessions/a6/a6bb005a33103eebf8e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。**已释放 75G，可用空间从 740K → 75G（71% 使用率）**。

## 当前状态

### 保留的 checkpoints (140G)
| 实验 | 保留内容 | 大小 |
|------|---------|------|
| detach_ln_s0/s1/s2 | 50000 步 (final) | 15G × 3 |
| cutoff_s2_v2 | 50000 步 (final) | 15G |
| ablation_random_occ_s2 | 50000 步 (final) | 15G |
| full_occ_ln_s0 | 30000 步 | 15G |
| full_occ_ln_s1 | 20000 步 + 损坏的 30000 步 (5.5G) | 21G |
| full_occ_ln_s2 | 20000 步 + 损坏的 30000 步 (2.5M) | 15G |
| ablation_occ_detach_s0_retrain | 20000 步 + 损坏的 30000 步 (532K) | 15G |

### 需要你决策的事项

1. **3 个损坏的 30000 步 checkpoint** — full_occ_ln_s1 (5.5G)、full_occ_ln_s2 (2.5M)、ablation_occ_detach_s0_retrain (532K) 均写入不完整，无法用于恢复。这 3 个实验恢复时只能从 **20000 步** 重启。要删除这些损坏文件吗？

2. **`runs/...--100_chkpt`** (15G) — 这是 step 100 的非常早期的 checkpoint，还需要保留吗？删除可再释放 15G。

3. **75G 够用吗？** — full_occ_ln_s0 正在运行（step ~30755），下次保存在 step 40000。3 个崩溃实验恢复后各需约 15G 保存新 checkpoint。75G 可以覆盖约 5 个 checkpoint 的写入。

---
