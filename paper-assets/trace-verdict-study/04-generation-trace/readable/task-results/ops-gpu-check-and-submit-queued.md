# ops gpu check and submit queued

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_and_submit_queued_20260521T144833_result.json`
- **Structured JSON:** [`302110bc4fccce584c44.json`](../../sessions/30/302110bc4fccce584c44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常训练，GPU 隔离正确。

## 汇总

### 1. GPU 初始状态
| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| cuda:0 | 49175/97887 MiB | 0% | 无（孤儿显存） |
| cuda:1 | 0/97887 MiB | 0% | 无 |

### 2. codellama_exception_only_seed42 (cuda:1)
- **PID**: 706833
- **显存**: 39078 MiB on GPU-48463d2b (GPU 1)
- **进度**: 2/444 步, ~16s/step, 预计 ~2 小时
- **注**: 首次因 `--model_name`（应为 `--model_path`）参数错误失败；第二次无 `--gradient_checkpointing` OOM；第三次加上后正常运行

### 3. qwen1.5b_no_trace_seed42 (cuda:0)
- **PID**: 706059
- **显存**: 35984 MiB on GPU-ade8d9bb (GPU 0)
- **进度**: 已跑 ~40 步/444, ~1.1s/step, 预计 ~8 分钟完成

### 4. GPU 隔离验证
| PID | GPU UUID | 显存 |
|-----|----------|------|
| 706059 (Qwen-1.5B) | GPU-ade8d9bb (GPU 0) | 35984 MiB |
| 706833 (CodeLlama-13B) | GPU-48463d2b (GPU 1) | 39078 MiB |

隔离正确，两进程分别独占各自 GPU。

---
