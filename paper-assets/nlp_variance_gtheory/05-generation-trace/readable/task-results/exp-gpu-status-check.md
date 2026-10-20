# exp gpu status check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gpu_status_check_20260521T043227_result.json`
- **Structured JSON:** [`ccecbb8edb19c28ce908.json`](../../sessions/cc/ccecbb8edb19c28ce908.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU
4 卡全部 **100% 利用率**，显存 ~90GB/97GB，推理进程活跃。

### Gemma bf16 (`exp001_gemma`) — **已完成**
| Shard | Lines | 状态 |
|-------|-------|------|
| 0 | 23,200 | done |
| 1 | 20,400 | done |
| 2 | 21,400 | done |
| 3 | 21,400 | done |
| **Total** | **86,400** | |

### Gemma fp32 (`exp001_gemma_fp32`) — **已完成**
| Shard | Lines | 状态 |
|-------|-------|------|
| 0-3 | 21,600 × 4 | done |
| **Total** | **86,400** | |

日志确认 `Experiment complete → results/exp001_gemma_fp32/shard_0.jsonl`，完成时间 ~11:49。

### Mistral bf16 (`exp001_mistral`) — **运行中 ~76%**
每 shard 324 conditions，每 condition 200 items：

| Shard | Lines | Conditions Done | Progress |
|-------|-------|----------------|----------|
| 0 | 49,200 | 246/324 | 75.9% |
| 1 | 48,000 | 240/324 | 74.1% |
| 2 | 48,400 | 242/324 | 74.7% |
| 3 | 51,600 | 258/324 | 79.6% |

日志显示正在处理 condition ~4100-4300 区间，每 condition ~42s。剩余 ~80 conditions，**预计 ~1 小时内完成**。

### Qwen (`exp001_qwen`) — **待运行**
4 个 shard CSV 已就绪，无输出文件。

### nohup 链式脚本
未找到 chain log 文件和 nohup.out。该脚本可能已在 Gemma fp32 完成后成功启动 Mistral，自身退出。但 **Mistral 完成后是否会自动启动 Qwen 需要确认**——如果链式脚本已退出，Qwen 可能需要手动启动。

### .done 标记
未找到任何 `.done` 文件。

---
