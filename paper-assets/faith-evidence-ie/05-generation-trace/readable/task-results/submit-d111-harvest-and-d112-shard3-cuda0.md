# submit d111 harvest and d112 shard3 cuda0

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_d111_harvest_and_d112_shard3_cuda0_20260519T000710_result.json`
- **Structured JSON:** [`1c4a98a125d2df2f525b.json`](../../sessions/1c/1c4a98a125d2df2f525b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

### D111 eval 结果

| 指标 | 值 |
|---|---|
| ign_f1 | **0.3974** |
| f1 | 0.4049 |
| evi_f1 (TP) | 0.7986 |
| evi_f1_joint | 0.3147 |
| edcr | 0.6982 |
| format_ok | 983/985 |
| truncated | 288/985 |

s42 的 D076 标准化 re-eval ign_f1 = 0.3974，与之前一致。三 seed 对比：s42 (0.3974) < s43 (0.4365) < s44 (0.4734)。

### D112 shard 3

已启动，tmux session `d112_shard3`，python PID 590568，运行在 cuda:0（15029MiB）。

### 当前 4 卡占用

| GPU | 显存 | 进程 |
|---|---|---|
| cuda:0 | 15029MiB | D112 shard 3 (PID 590568) |
| cuda:1 | 18739MiB | D112 shard 1 (PID 587729) |
| cuda:2 | 17883MiB | D112 shard 2 (PID 587819) |
| cuda:3 | 11045MiB | D112 shard 0 (PID 590423) |

4 卡满载，D112 四个 shard 并行运行。

---
