# ops gemma2 d100 eval launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gemma2-d100-eval-launch_20260521T021441_result.json`
- **Structured JSON:** [`aab6259f9dd30dc32f20.json`](../../sessions/aa/aab6259f9dd30dc32f20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已成功启动并占用 GPU。

**汇总：**

| 项目 | 状态 |
|---|---|
| **Adapter 完整性** | ✅ `adapter_model.safetensors` 216MB, `lora_alpha=32`, `.done` 标记存在 |
| **ARC 脚本修复** | ✅ `CUDA_VISIBLE_DEVICES` 从 0 改为 2 |
| **MMLU eval (cuda:0)** | ✅ PID 461706, 19344 MiB, GPU-Util 88% |
| **ARC eval (cuda:2)** | ✅ PID 461784, 19680 MiB, GPU-Util 75% |
| **tmux sessions** | `eval_gemma2_d100_mmlu_s0`, `eval_gemma2_d100_arc_s0` |
| **Registry** | 两个实验均为 RUNNING 状态 |

**预估完成时间**：Gemma-2 9B eval 单 benchmark 约 30-60 分钟，预计 ~11:15-11:30 完成。cuda:1 上运行的是 `qwen14b_d050_retrain`，不受影响。

---
