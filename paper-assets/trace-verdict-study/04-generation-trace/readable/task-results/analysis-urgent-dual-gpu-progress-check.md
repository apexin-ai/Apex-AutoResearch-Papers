# analysis urgent dual gpu progress check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_urgent_dual_gpu_progress_check_20260519T174506_result.json`
- **Structured JSON:** [`9f78d6664869b75ee6cf.json`](../../sessions/9f/9f78d6664869b75ee6cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. CodeLlama-13B `loop_only_seed42`

| 项目 | 状态 |
|------|------|
| 进程 | PID 517775, **存活**, 100% CPU |
| GPU | GPU 0, **100%** 利用率, 86155 / 97887 MiB |
| 进度 | **325 / 444 steps (73%)**, 已运行 2h44m |
| 速度 | ~29s/step |
| 剩余 | ~119 steps ≈ **57 分钟** |
| Loss | 正常下降中（eval 298/298 刚完成） |
| Checkpoint | checkpoint-148, checkpoint-296 已保存 |
| Eval | 未完成，final/ 目录不存在 |

### 2. DeepSeek-6.7B `loop_only_seed42`

| 项目 | 状态 |
|------|------|
| 进程 | PID 525732, **存活**, 107% CPU |
| GPU | GPU 1, **98%** 利用率, 23383 / 97887 MiB |
| 进度 | **46 / 444 steps (10%)**, 已运行 14m |
| 速度 | ~18.8s/step |
| 剩余 | ~398 steps ≈ **2h05m** |
| Loss | 0.6116 → 0.1267（4 个 log 点，下降正常） |
| Token Acc | 88.8% → 96.8%（快速收敛） |
| Checkpoint | 尚无 |
| Eval | 未完成 |

### 总结

两个实验均正常运行，训练命令链中已包含 `&& eval`，训练结束后会自动执行评估。

- **CodeLlama** 预计 **~1 小时后**完成训练+eval
- **DeepSeek** 预计 **~2.5 小时后**完成训练+eval

无需人工干预。

---
