# infra gpu check and fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check-and-fix_20260514T031506_result.json`
- **Structured JSON:** [`587f5eb7034db90202b8.json`](../../sessions/58/587f5eb7034db90202b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 7 个 RUNNING 实验的进程全部存活，exp_001_sft_d005_15B 已更新为 RUNNING。

## 报告

### GPU 状态 (6× RTX 4090D, 24GB each)

| GPU | 显存占用 | 利用率 | 实验 | PID | 运行时间 |
|-----|---------|--------|------|-----|---------|
| 0 | 10055/24564 MiB | 22% | **exp_001_sft_d100_15B_v2** (1.5B d100 SFT) | 251924 | 2h08m |
| 1 | 12620/24564 MiB | 100% | **exp_001_eval_3B_d000_s42** (3B eval) | 249294 | 2h22m |
| 1 | ↑ (共享) | ↑ | **exp_001_eval_05B_d005** (0.5B d005 eval) | 255322 | 1h48m |
| 2 | 7330/24564 MiB | 99% | **exp_001_eval_05B_d000_s42_v5** (0.5B d000 eval) | 266511 | 37m |
| 2 | ↑ (共享) | ↑ | **exp_001_eval_05B_d100_v5** (0.5B d100 eval) | 266780 | 37m |
| 3 | 8957/24564 MiB | 55% | **exp_001_eval_3B_d000_s123** (3B eval) | 242581 | 2h58m |
| 4 | 18545/24564 MiB | 23% | **exp_001_sft_d005_15B** (1.5B d005 SFT) ✅ 已修复→RUNNING | 271916/271921 | ~3m |
| 5 | 5829/24564 MiB | 43% | **exp_001_eval_15B_d000_s123** (1.5B eval) | 250600 | 2h17m |

### exp_001_sft_d005_15B 最终状态
- **RUNNING** (已从 QUEUED 更新)
- PID 271916 (wrapper) / 271921 (python) 均存活
- GPU 4, 18536MiB 显存占用

### 空闲 GPU
**没有空闲 GPU**——6 块全部在跑任务，其中 GPU 1 和 GPU 2 各有 2 个进程共享。

---
