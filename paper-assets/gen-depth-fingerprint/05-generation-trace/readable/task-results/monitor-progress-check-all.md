# monitor progress check all

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress-check-all_20260515T033916_result.json`
- **Structured JSON:** [`5b200a58302a07a83c28.json`](../../sessions/5b/5b200a58302a07a83c28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常运行，无异常：

| 实验 | 进度 | ETA | GPU |
|------|------|-----|-----|
| **plan-014** (Qwen3-8B) | **815/996 (82%)** | ~49 min | cuda:0 75%, 16.5G/32.6G |
| **plan-005-cont** (Pythia-2.8B continuation) | **78/995 (8%)** | ~1h50m | cuda:1 63%, 6.2G/32.6G |
| **plan-005-elab** (Pythia-2.8B elaboration) | **72/995 (7%)** | ~2h18m | cuda:2 64%, 6.2G/32.6G |
| **plan-005-rewrite** (Pythia-2.8B rewriting) | **72/995 (7%)** | ~2h02m | cuda:3 64%, 6.2G/32.6G |

**plan-014** 即将完成（~50分钟内）。三个 plan-005 实验刚启动约 10 分钟，还需 ~2 小时。

磁盘充足（根分区 25%、数据盘 50%），无 OOM/掉卡。plan-014 有少量 seeds 因空输出被跳过，属正常行为。

报告已保存至 `artifacts/progress_snapshot.md`。

---
