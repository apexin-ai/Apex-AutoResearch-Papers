# ssh urgent status check 41718

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_status_check_41718_20260520T205243_result.json`
- **Structured JSON:** [`9dae19accb3b1e8023bf.json`](../../sessions/9d/9dae19accb3b1e8023bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41718 状态报告

### GPU
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 0% | 0 / 97887 MiB (空闲) |
| 1 | 96% | 95690 / 97887 MiB |

### JSD 30% uniform eval — ✅ 已完成

| Metric | Value |
|--------|-------|
| WikiText-2 PPL | **8.8848** |
| ARC-c (acc_norm) | **0.4437** |
| WinoGrande | **0.6977** |
| MMLU | **0.3857** |
| GSM8K | **0.0857** |
| HellaSwag (acc_norm) | **0.7063** |
| PIQA (acc_norm) | **0.7519** |

### RevKL 30% uniform eval — 🔄 运行中

- PID 280143 (tmux, exp_id=`revkl_30_s42_uniform_eval`): alive, 运行 1h01m, GSM8K generate_until **77%** (1017/1319)
- PID 279686 (nohup, exp_id=`reverse_kl_30_s42_uniform_eval`): alive, GSM8K generate_until **93%** (1225/1319)
- 完成 GSM8K 后还有 hellaswag + piqa (loglikelihood，速度快)，预计 **~15-20 分钟**全部完成

### ⚠️ 问题：两个 RevKL eval 进程重复跑

同一个 checkpoint (`predictor_reverse_kl.pt`)、同一个配置，被用不同 exp_id 启动了两次，都在 cuda:1 上。两个都会产出结果，取先完成的那个即可（nohup 那个更快）。不影响正确性，但浪费了一半 GPU 算力。

---
