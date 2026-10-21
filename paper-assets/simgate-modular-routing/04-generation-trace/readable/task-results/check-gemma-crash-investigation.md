# check gemma crash investigation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gemma-crash-investigation_20260520T103037_result.json`
- **Structured JSON:** [`ff1f6c9687b3099d502f.json`](../../sessions/ff/ff1f6c9687b3099d502f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. Gemma — **正常运行中，未崩溃**

| 指标 | 状态 |
|------|------|
| GPU 1 | RTX 5090, 28GB/32GB VRAM, vLLM::EngineCore (PID 881524) |
| 进程 | `episode_level_collection.py --task_types freeze` 活跃 (PID 881100) |
| tmux | `gemma-11tasks` session 存在 |
| 日志 | 无 error/exception，正常输出推理进度 |

**已完成数据：**

| 任务 | episodes | 状态 |
|------|----------|------|
| identify-life-stages-1 | 20/20 | ✅ 完成 |
| freeze | 6/20 | 🔄 运行中 |
| 剩余 9 个任务 | 0 | 排队中 |

总进度：**~26/220 episodes**（boil=20, melt=2 是之前遗留数据，不在当前脚本任务列表中）

### 2. ALFWorld — **即将完成**

**132/135 episodes** — GPU 0 利用率 96%，正常推理中。

### 3. 无需重启

两个实验都在正常运行，不需要干预。

---
