# ssh cleanup tmux and submit 4b withevi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup-tmux-and-submit-4b-withevi_20260521T090438_result.json`
- **Structured JSON:** [`64055b4dd7f6c2190cc6.json`](../../sessions/64/64055b4dd7f6c2190cc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:3 不空闲，无法提交。** 按 C001 约束（eval 前 GPU 显存须 < 2GB），当前所有卡都被占用：

| GPU | 显存占用 | PID |
|-----|---------|-----|
| cuda:0 | 6159 MiB | 87387 |
| cuda:1 | 11463 MiB | 88992 |
| cuda:2 | 19599 MiB | 87307 |
| cuda:3 | 10739 MiB | 93402 |

tmux session 已清理。需要等某张卡释放后再提交，或者你想先确认这些进程分别在跑什么？

---
