# ops t20 progress check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_t20_progress_check_20260520T125247_result.json`
- **Structured JSON:** [`fabd2f290fbe0cbd0564.json`](../../sessions/fa/fabd2f290fbe0cbd0564.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
t20_a045: [存活] gen  3/20 — gen 3 生成数据中   (运行 1h02m, ~20min/gen, ETA ~5h40m)
t20_a050: [存活] gen 11/20 — gen 11 训练中 76%  (运行 4h29m, ~23min/gen, ETA ~3h20m)
t20_a060: [存活] gen  9/20 — gen 9 生成数据中   (运行 3h36m, ~24min/gen, ETA ~4h24m)
t20_a075: [存活] gen  6/20 — gen 6 计算 MAUVE   (运行 2h34m, ~24min/gen, ETA ~5h20m)
t20_a100: [存活] gen 11/20 — gen 11 生成数据中  (运行 4h29m, ~24min/gen, ETA ~3h40m)
```

5 个进程全部存活，无异常。a045 进度最慢（3/20），因为 pid 显示它只运行了 1h（被修复重启过）。a050 和 a100 进度最快（11/20），预计最先完成。按当前速率，全部实验预计 **~5h40m 内** 跑完。

---
