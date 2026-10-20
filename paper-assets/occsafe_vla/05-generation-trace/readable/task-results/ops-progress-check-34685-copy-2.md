# ops progress check 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress_check_34685_20260524T190233_result.json`
- **Structured JSON:** [`fe93d5d2bfb714f28906.json`](../../sessions/fe/fe93d5d2bfb714f28906.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

| 实验 | GPU | 当前 Step | 进度 | 速度 | 剩余步数 | 预估完成 (UTC) |
|------|-----|-----------|------|------|----------|---------------|
| cutoff_45k_s1 | cuda:0 | 21703 | 43% | ~1.08 it/s | 28302 | **May 25 ~06:05** |
| cutoff_15k_s1 | cuda:1 | — | — | — | — | **日志不存在** |
| cutoff_25k_s2 | cuda:2 | 7200 | 14% | ~1.06 it/s | 42805 | **May 25 ~10:00** |
| reverse_cutoff_s2 | cuda:3 | 7162 | 14% | ~1.07 it/s | 42843 | **May 25 ~09:56** |

**补充发现：**
- `cutoff_15k_s1.log` 不存在。目录下没有任何 `*15k*s1*` 文件。
- GPU 1 上刚完成的是 **cutoff_25k_s1**（50005/50005，22:48 结束）和 **reverse_cutoff_s1**（50005/50005，22:47 结束）。
- 4 块 GPU 利用率：99% / 80% / 99% / 82%，显存均 ~62GB。GPU 1 的 80% 可能是刚完成任务的残留。

需要确认 cutoff_15k_s1 是否已在 cuda:1 上启动，或者任务名/日志路径有误。

---
