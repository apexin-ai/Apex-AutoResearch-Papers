# analysis lconsist cont exit check

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lconsist-cont-exit-check_20260520T000905_result.json`
- **Structured JSON:** [`4e4fe4830e99bc1c47ec.json`](../../sessions/4e/4e4fe4830e99bc1c47ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，cron 不存在（可能已被之前的自动检测清除）。

**汇报：**

| 项目 | 值 |
|------|-----|
| 退出原因 | **磁盘满** — step 5500 保存 checkpoint 时 `OSError: [Errno 28] No space left on device` |
| 时间线 | 原始训练 SIGTERM 杀死 @step 1168 → resumed from checkpoint-1000 → 跑到 step 5500 崩溃 |
| 最终 step | 5500 / 20000 (27.5%) |
| 最终 L_act | ~0.30 (波动范围 0.17-0.40) |
| 最终 L_con | ~1e-5 (已坍缩，符合预期) |
| 最终 hm_ent | 7.05 |
| 最后 checkpoint | checkpoint-1000（checkpoint-5500 未保存成功） |
| GPU 0 显存 | 已释放 (0 MiB) |
| 当前磁盘 | runs 所在 `/dev/md0` 有 197G 可用，根分区 21G 可用 |

注意：`phase1_oft_baseline` 仍在 GPU 2 上运行 (24349 MiB)，它也会写 checkpoint。如果要重跑 `phase1_lconsist_v1_cont`，需确认 save_freq 不会再次撑满磁盘——可能需要清理旧 checkpoint 或加大 save_freq。

---
