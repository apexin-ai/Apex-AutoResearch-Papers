# code exp002v3 gs8 dryrun

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002v3-gs8-dryrun_20260522T153430_result.json`
- **Structured JSON:** [`5af55099c535bc00ceef.json`](../../sessions/5a/5af55099c535bc00ceef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果：OOM

**RTX 5090 32GB 无法支撑 Qwen3-8B + num_generations=8。**

### 详情

| 指标 | 数值 |
|------|------|
| GPU 总显存 | 31.36 GiB |
| PyTorch allocated | 26.26 GiB |
| PyTorch reserved | 2.72 GiB |
| OOM 时 free | 1.77 GiB |
| OOM 时请求 | 2.32 GiB |
| 缺口 | ~0.55 GiB |

### 失败点
- **Generation forward pass**（lm_head 投影层），还没到 backward
- Accelerate 已自动做了部分 CPU offload（`Some parameters on meta device because offloaded to cpu`），仍然不够
- 瓶颈是 8 个 generation 的 KV cache + logits 同时在 GPU 上

### 可能的解决路径（待 Director 决策）
1. **降 num_generations 到 4** — 介于 2 和 8 之间的折中
2. **降 max_completion_length**（256→128）— 减少 KV cache
3. **用双卡**（cuda:0+3 都空闲）+ DeepSpeed ZeRO-2（跟原 exp-002v3 一样）
4. **4-bit 量化推理**（QLoRA 方式）— 但会改变实验条件

脚本已创建在 `/root/contrastive_entrain_calib/training/run_exp002v3_gs8_cosine.py`，max_steps 仍为 2（dry-run 状态），等你定方案后我改参数启动。

---
