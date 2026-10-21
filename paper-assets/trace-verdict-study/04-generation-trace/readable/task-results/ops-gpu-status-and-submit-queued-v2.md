# ops gpu status and submit queued v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_and_submit_queued_v2_20260521T151003_result.json`
- **Structured JSON:** [`f9f05f53945d9cde97b5.json`](../../sessions/f9/f9f05f53945d9cde97b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| GPU 0 | 49175 / 97887 MiB (50%) | 0% | **无 compute 进程 — 僵尸显存** |
| GPU 1 | 39091 / 97887 MiB (40%) | 100% | PID 706833 (训练中) |

**GPU 0 异常**: 50GB 显存被占用但没有任何 compute 进程，是之前被 kill 的训练残留的僵尸 VRAM。需要 `nvidia-smi --gpu-reset -i 0` 或重启释放。

### 2. 当前运行的进程

**PID 706833** — `codellama_exception_only_seed42`（GPU 1, tmux session `codellama_exc`）
- 进度: **56/444 steps (~13%)**，已运行 ~19 分钟，预计还需 ~2 小时
- 输出目录: `codellama_exception_only_seed42`（注意：没有 "13b" 前缀）
- **问题**: `codellama13b_exception_only_seed42`（带 "13b" 前缀）**已经完成**，accuracy = **99.83%**。当前运行本质上是同一实验的重复训练（同样用 CodeLlama-13b-Instruct-hf 模型）

### 3. 实验完成状态 — 全部已完成

**优先级 1（exception_only, C1 核心）:**
| 实验 | 状态 |
|------|------|
| `codellama13b_exception_only_seed42` | ✅ DONE (accuracy 99.83%) |
| `deepseek_exception_only_seed123_v2` | ✅ DONE |

**优先级 2（跨模型覆盖）:**
| 实验 | 状态 |
|------|------|
| `codellama13b_no_trace_seed42` | ✅ DONE |
| `codellama13b_vota_seed42` | ✅ DONE |

**优先级 3（scale validation）:**
| 实验 | 状态 |
|------|------|
| `qwen15b_loop_only_seed42` | ✅ DONE |
| `qwen15b_full_trace_seed42` | ✅ DONE |

**Qwen-1.5B 全系列:**
| 实验 | 状态 |
|------|------|
| `qwen15b_exception_only_seed42` | ✅ DONE |
| `qwen15b_vota_seed42` | ✅ DONE |
| `qwen15b_no_trace_seed42` | ✅ DONE |

**其他:**
| 实验 | 状态 |
|------|------|
| `codellama13b_loop_only_seed42` | ✅ DONE |

### 4. 建议

1. **当前运行的 `codellama_exception_only_seed42` 是重复实验** — `codellama13b_exception_only_seed42` 已有 99.83% 的结果。建议 kill PID 706833 释放 GPU 1。
2. **GPU 0 僵尸显存** — 需要 reset 释放 ~49GB VRAM。
3. **所有用户指定的候选实验均已完成**，无需提交新实验。
4. 释放两张卡后，可以用于其他待跑实验（如果有的话）。

---
