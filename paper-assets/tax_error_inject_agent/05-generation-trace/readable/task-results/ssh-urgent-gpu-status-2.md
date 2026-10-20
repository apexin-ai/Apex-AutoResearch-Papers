# ssh urgent gpu status 2

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-gpu-status-2_20260514T141239_result.json`
- **Structured JSON:** [`feac924737e8edcc12b6.json`](../../sessions/fe/feac924737e8edcc12b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 全景状态汇总

### 1. v3 评估（已完成）

| 实验 | GPU | 结果 |
|------|-----|------|
| v3-taxei-eval | cuda:0 (已释放) | **66.0%** (31/47) ✅ |
| v3-random-eval | cuda:1 (已释放) | **51.1%** (24/47) ✅ |

v3-taxei 按任务类型：look_at_obj 83.3%, pick_clean 72.7%, pick_heat 75.0%, pick_and_place 62.5%, pick_two 57.1%, pick_cool 42.9%

### 2. v4 训练（r3 已 OOM 崩溃，r2 重试中）

v4-taxei-sft-r3 和 v4-random-sft-r3（PID 58741/58826）均已 **CUDA OOM 崩溃**。

当前有新进程在跑（log 文件名 r2）：

| 实验 | GPU | PID | 进度 | Loss | Token Acc | VRAM | ETA |
|------|-----|-----|------|------|-----------|------|-----|
| v4-taxei-sft (r2) | cuda:2 | 58034 | **1313/3387 (38.8%)** | 0.35 | 0.88 | 18.48 GiB | ~1h5m |
| v4-random-sft (r2) | cuda:3 | 58163 | **1304/3387 (38.5%)** | 0.35 | 0.88 | 18.48 GiB | ~1h6m |

训练参数：Qwen3-8B + LoRA (rank=16, alpha=32), bs=1, grad_accum=8, 3 epochs, lr=1e-4, ~1.9s/it

### 3. GPU 汇总

| GPU | 状态 | 实验 | VRAM |
|-----|------|------|------|
| cuda:0 | **空闲** | v3-taxei-eval 已完成 | 0 / 32 GiB |
| cuda:1 | **空闲** | v3-random-eval 已完成 | 0 / 32 GiB |
| cuda:2 | **训练中** | v4-taxei-sft r2 (38.8%) | 19.5 / 32 GiB |
| cuda:3 | **训练中** | v4-random-sft r2 (38.5%) | 19.5 / 32 GiB |

**cuda:0 和 cuda:1 当前空闲可用。** v4 训练预计约 1h5m 后完成（epoch 1.1/3）。

---
