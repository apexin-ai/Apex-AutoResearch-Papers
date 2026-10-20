# diag medium rgds seed456 exit

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_medium_rgds_seed456_exit_20260514T125126_result.json`
- **Structured JSON:** [`eef51c6cd7d5a4715c66.json`](../../sessions/ee/eef51c6cd7d5a4715c66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 诊断结果

**退出原因**: ✅ **success** — 实验正常完成，gen_0 到 gen_7 全部跑完。

**Gen7 Metrics**:

| 指标 | 值 |
|------|-----|
| PPL | 86.03 |
| RankMe | 432.02 |
| kNN | 0.988 |
| Rare n-gram | 0.01502 |
| Rank corr | -0.0386 |
| **Ratio** | **0.7899** |

**Registry + Cron**: conclusion=success, metrics 已写入, status=DONE, cron 已删除。

**GPU 状态**: GPU 0 占用 49175 MiB（进程残留显存，未释放），GPU 1 空闲。两卡利用率均 0%。

355M 3-seed RGDS 系列（seed 42/123/456）现已全部完成，可触发全量统计。

---
