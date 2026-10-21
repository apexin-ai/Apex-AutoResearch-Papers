# fix 8b k2 dual submit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_8b-k2-dual-submit_20260516T102920_result.json`
- **Structured JSON:** [`38d279177be00954cdb6.json`](../../sessions/38/38d279177be00954cdb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡训练成功启动，汇报如下：

| GPU | 任务 | 显存占用 | 利用率 | 状态 |
|-----|------|----------|--------|------|
| cuda:0 | exec-only | 86,295 / 97,887 MiB (88%) | 94% | step 1/500 完成，~28.6s/it |
| cuda:1 | ISR β=0.1 | 83,707 / 97,887 MiB (85%) | 93% | step 1/500 完成，~28.5s/it |

K=2 未 OOM，训练正常进行。预计总时长约 4 小时。

---
