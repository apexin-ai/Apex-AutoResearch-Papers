# hotfix kill cuda2 qwen

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_hotfix_kill_cuda2_qwen_20260521T071542_result.json`
- **Structured JSON:** [`84b954fb19e51ec68702.json`](../../sessions/84/84b954fb19e51ec68702.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终状态

| GPU | 状态 | 进程 |
|-----|------|------|
| cuda:0 | pythia-2.8b greedy+topk | PID 283041，运行中 |
| cuda:1 | olmo-2-1b greedy+topk | PID 283607，greedy 进度 ~33%（324/995） |
| cuda:2 | **空闲** ✓ | 3MiB |
| cuda:3 | **空闲** ✓ | 3MiB |

**已完成：**
1. 已 kill cuda:2 上的 qwen3-1.7b 违规进程（PID 338751 及其父进程链）
2. 已修复 `cross_model_chains.py`、`detector_baseline.py`、`sampling_ablation.py` 中所有 cuda:2/3 默认值 → cuda:0
3. `start_qwen_after_olmo.sh` 本身无问题（已使用 cuda:1），已重新启动等待链
4. 无 crontab 自动触发

**OLMo 预计完成时间：** greedy 剩余 ~671 条 × 8.6s ≈ 96 min，之后还有 topk ~995 条 × 8.6s ≈ 143 min。**OLMo 总计约 4 小时后完成**（~19:15 CST），届时 Qwen3-1.7B 自动在 cuda:1 启动。

**Qwen3-1.7B 已完成的进度（80/996 greedy）丢失**，重启后将从头开始。

---
