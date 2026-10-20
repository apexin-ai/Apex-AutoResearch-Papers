# check all gpu progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_gpu_progress_20260519T075735_result.json`
- **Structured JSON:** [`c5cec311113f4849b9c0.json`](../../sessions/c5/c5cec311113f4849b9c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张卡全部在跑 eval，所有 PID 存活。汇总：

| GPU | 任务 | PID | 显存占用 | 进度 | 运行时间 | 预估剩余 |
|-----|------|-----|----------|------|----------|----------|
| cuda:0 | D112 RSFT s44 eval (4B) | 627505 | 10,888 MiB / 32,607 MiB | 27/247 (11%) | 22 min | ~3h |
| cuda:1 | 14B SFT eval | 626093 | 14,244 MiB / 32,607 MiB | 23/247 (9%) | 34 min | ~5h 57min |
| cuda:2 | 14B SFT no-evidence eval | 626175 | 14,244 MiB / 32,607 MiB | 25/247 (10%) | 34 min | ~5h |
| cuda:3 | 1.7B RSFT s43_r2 eval | 620725 | 5,492 MiB / 32,607 MiB | 177/247 (72%) | 1h 42min | ~43min |

cuda:3 的 1.7B eval 最快完成，预计约 40 分钟后结束。两个 14B eval（cuda:1/2）最慢，预计还需 5-6 小时。cuda:0 的 4B eval 预计约 3 小时。

---
