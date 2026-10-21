# diag temp progress check v3

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_temp-progress-check-v3_20260518T164951_result.json`
- **Structured JSON:** [`7d0ff59f2b75c3aeb5d8.json`](../../sessions/7d/7d0ff59f2b75c3aeb5d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU
| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 3625/32607 MiB | 50% | OLMo t=0.5 生成 |
| 1 | 1825/32607 MiB | 32% | Qwen t=0.5 生成 |
| 2 | 空闲 | 0% | - |
| 3 | 空闲 | 0% | - |

### 生成进度（截至 00:49 monitor 日志）

| 任务 | Seeds | 速率 | 预计剩余 |
|------|-------|------|---------|
| OLMo t=0.5 | **827**/990 | ~7 seeds/min | ~23 min |
| Qwen t=0.5 | **554**/990 | ~4.7 seeds/min | ~93 min |
| OLMo t=0.9 | 0 (未开始) | - | - |
| Qwen t=0.9 | 0 (未开始) | - | - |

### 进程状态
- `tmux` session `temp_olmo` 运行中，包含两个生成进程 + monitor 脚本
- Monitor 脚本 (`scripts/monitor_temp_pipeline.py`) 正常运行，每 120s 轮询
- 无报错

### Feature extraction
- 尚未触发（seeds 未达阈值）
- 已有的 feature CSV 中，`features_pythia-2.8b-t05.csv` 和 `features_pythia-2.8b-t09.csv`（5/18 14:03）说明 Pythia 温度实验已完成 feature extraction
- 最新结果文件：`tost_per_generator.json`（23:11）、`instruct_analysis_summary.json`（23:12）

### 结论
两个 t=0.5 生成任务正在跑，OLMo 约 23 分钟完成，Qwen 约 1.5 小时。t=0.9 尚未启动（应该在 t=0.5 完成后排队）。Monitor 正常，无需干预。

---
