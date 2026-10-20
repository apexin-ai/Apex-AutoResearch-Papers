# diagnose exp 018 019 failures

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_018_019_failures_20260516T063126_result.json`
- **Structured JSON:** [`481aac0806eb3e4dea41.json`](../../sessions/48/481aac0806eb3e4dea41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**结论：exp-018 和 exp-019 均在正常运行，并未失败。**

### exp-018 (LLaMA-3.1-8B, cuda:0)
- **状态**: 运行中 (PID 10403, 13:01 启动)
- **当前进度**: depth 1 生成中，943/1250 batches (75%)，~5.93s/batch
- **已完成数据**: `depth_0.jsonl` (4.4MB)
- **配置**: 5000 samples, max_depth=5, batch_size=4
- **预计 depth 1 完成**: ~30 分钟后

### exp-019 (Mistral-7B-v0.3, cuda:1)
- **状态**: 运行中 (PID 12147, 13:16 启动)
- **当前进度**: depth 2 生成中，21/625 batches (3%)，~6.15s/batch
- **已完成数据**: `depth_0.jsonl` (4.1MB) + `depth_1.jsonl` (4.2MB)
- **配置**: 5000 samples, max_depth=5, batch_size=8
- **预计 depth 2 完成**: ~62 分钟后

### GPU 状态
| GPU | 显存 | 利用率 | 占用进程 |
|-----|------|--------|---------|
| 0 | 16.1/24.6 GB | 96% | exp-018 (LLaMA-8B) |
| 1 | 14.7/24.6 GB | 96% | exp-019 (Mistral-7B) |
| 2 | 16.4/24.6 GB | 100% | exp-020 (Pythia, 3进程) |
| 3 | 0/24.6 GB | 0% | 空闲 |

### 说明
注册表中标记为 `DONE(failed)` 可能是误标。两个实验的进程、日志、GPU 占用都正常，没有任何错误信息。exp-019 进度领先（已完成 depth 1），exp-018 稍慢（batch_size=4 vs 8）。

每个实验需要完成 depth 0-5 共 6 轮生成，按当前速度，完整跑完预计还需 **5-8 小时**。无需修复，等待即可。

---
