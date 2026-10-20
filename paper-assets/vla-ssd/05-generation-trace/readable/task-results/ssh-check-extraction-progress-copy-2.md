# ssh check extraction progress

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-extraction-progress_20260515T173426_result.json`
- **Structured JSON:** [`8d9c21ee56d08cc637ee.json`](../../sessions/8d/8d9c21ee56d08cc637ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## LIBERO-Goal 特征提取进度

### 进程状态
两个进程均在运行，已运行约 49 分钟：

| 进程 | PID | RSS | CPU |
|------|-----|-----|-----|
| lg_extract_trained | 627256 | 2.4 GB | 997% |
| lg_extract_untrained | 627335 | 2.4 GB | 991% |

### 完成进度

**trained** — **9/10 完成**，第 10 个任务 `turn_on_the_stove` 进行中（309/4460, ~7%）
- 已产出 10 个 h5 文件（含正在写入的），总计 25 GB
- 预计剩余 ~3 分钟

**untrained** — **8/10 完成**，第 9 个任务 `put_the_wine_bottle_on_top_of_the_cabinet` 进行中（2633/5394, ~49%）
- 已产出 9 个 h5 文件（含正在写入的），总计 23 GB
- 当前任务剩余 ~1.5 分钟，之后还有 1 个任务（~5-7 分钟）
- 预计总剩余 ~7-9 分钟

### 无错误
两个日志均无报错，正常推进中。trained 即将完成，untrained 预计再跑约 10 分钟。

---
