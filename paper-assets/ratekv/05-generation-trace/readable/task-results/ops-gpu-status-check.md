# ops gpu status check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260515T163433_result.json`
- **Structured JSON:** [`02821f3585458b69ef71.json`](../../sessions/02/02821f3585458b69ef71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 状态
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell (98GB) | **0%** | 0 / 97887 MiB |
| 1 | RTX PRO 6000 Blackwell (98GB) | **84%** | 14903 / 97887 MiB |

### GPU 上的 Python 进程
- PID **350602** 在 GPU 1 上，占用 14894 MiB — 这是 **Mistral k_ablation sweep**

### Llama compounding sweep
**已完成。** 结果保存在 `/root/ratekv/artifacts/llama_compounding_sweep_results.json`

k ablation 结果 (budget=0.25):
| k | PPL | mem ratio |
|---|-----|-----------|
| 0 | 8.0922 | 1.0000 |
| 2 | 8.1243 | 0.9932 |
| 4 | 8.1803 | 0.9863 |
| 8 | 8.2259 | 0.9727 |
| 16 | 8.4378 | 0.9453 |
| 32 | 9.0506 | 0.8906 |
| 64 | 11.9910 | 0.7812 |
| 128 | 40.2067 | 0.5625 |
| 256 | 1519.19 | 0.2480 |

Best k=0 (PPL=8.0922)

### 当前运行中的任务
1. **tmux session**: `gemma2_9b_full_pipeline`（session 存在但 bash 空闲，无活跃 GPU 进程）
2. **PID 350602**: `run_k_ablation.py` — **Mistral** compounding sweep 正在 GPU 1 上运行（刚启动约 30 秒，CPU 174%）

### k_ablation 状态
- **Llama sweep**: 已完成
- **Mistral sweep**: 正在运行（GPU 1, 14.9GB 显存）

---
