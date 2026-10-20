# ssh phi4 eval result collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_phi4-eval-result-collect_20260519T070309_result.json`
- **Structured JSON:** [`b61904bdb2d364f07cf6.json`](../../sessions/b6/b61904bdb2d364f07cf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### d000 结果（已完成，14:36→14:59，耗时 ~23 min）

| Benchmark | Accuracy |
|-----------|----------|
| MMLU | **77.47%** |
| ARC Challenge | **93.94%** |

### 其他 dosage 状态

| Dosage | 状态 |
|--------|------|
| d005 | 🔄 运行中 — MMLU 进度 21% (2935/14042)，~14 it/s，约 13 min 完成 MMLU + ARC |
| d025 | 未开始 |
| d050 | 未开始 |

按 d000 的 23 min/dosage 估算，全部完成预计 **~16:10 CST**（还需约 1 小时）。

### GPU 状态

4 块 GPU 全部在用：
- cuda:0: 37.3 GB, 81% util (PID 111720)
- cuda:1: 52.1 GB, 56% util (PID 110298)
- cuda:2: 38.2 GB, 84% util (PID 114344)
- cuda:3: 31.7 GB, 96% util (PID 118080) — 正在跑 phi4_eval

cuda:3 **不空闲**，正在执行当前 eval 批量任务。tmux session `phi4_eval` 存活。

---
