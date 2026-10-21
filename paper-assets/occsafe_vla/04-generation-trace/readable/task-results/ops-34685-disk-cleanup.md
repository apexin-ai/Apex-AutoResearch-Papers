# ops 34685 disk cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-disk-cleanup_20260526T205826_result.json`
- **Structured JSON:** [`724bd6057e03c92872fa.json`](../../sessions/72/724bd6057e03c92872fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 4: 清理完成

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 260G (75%) | 200G (58%) |
| 可用 | 91G (25%) | 151G (42%) |

**释放 ~60G，删除项：**
- `full_occ_bn_v2_s1/--40000_chkpt` — 15G（已完成实验中间 checkpoint）
- `cutoff_15k_s1/` — 15G（v1 旧实验整目录）
- `vanilla_retrain_s0/` — 15G（v1 旧实验整目录）
- `full_occ_retrain_s0/` — 15G（v1 旧实验整目录）
- `logs/archive/` — 1G
- `/tmp` 临时文件 — 238M

**4 个运行中实验全部正常**（PID 均存活）。剩余 checkpoint 目录仅含运行中实验和已完成 v2 实验的 50000_chkpt。

4 个新实验（~60G）启动后预计剩余 ~91G (26%)，高于 20% 目标。

---
