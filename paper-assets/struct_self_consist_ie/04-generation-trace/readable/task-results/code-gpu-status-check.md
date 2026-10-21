# code gpu status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu_status_check_20260518T215600_result.json`
- **Structured JSON:** [`d627b17de32e5908cd28.json`](../../sessions/d6/d627b17de32e5908cd28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### autodl-5090（主服务器）

| GPU | 状态 | 显存 | 温度 | 任务 |
|-----|------|------|------|------|
| 0 | 空闲 | 2MiB / 32G | 30°C | - |
| 1 | **满载 94%** | 30878MiB / 32G | 79°C | LLaMA FewNERD LoRA 训练 (PID 137865) |
| 2 | 空闲 | 2MiB / 32G | 28°C | - |
| 3 | 空闲 | 2MiB / 32G | 28°C | - |

**LLaMA FewNERD 训练进度：**
- Step **20000 / 24708**（80.95%），Epoch 2.43 / 3.0
- Loss: 0.0201，LR: 2.13e-5
- 已用时 12h24m，**预计剩余 ~2h55m**（约 08:50 UTC 完成）
- 已保存 checkpoint: 17000, 18000, 19000

**LLaMA CoNLL 训练：已完成** (May 15)
- 最终 adapter: `checkpoints/llama3.1-8b-conll2003-lora/adapter_model.safetensors` (335MB)
- Checkpoints: 3600 → 4390（5个），含 eval results

---

### autodl-5090-b

| GPU | 状态 | 显存 | 温度 | 任务 |
|-----|------|------|------|------|
| 0 | 空闲 | 2MiB / 32G | 28°C | - |
| 1 | **满载 93%** | 30628MiB / 32G | 70°C | FewNERD s789 推理 (vLLM) |
| 2 | 空闲 | 2MiB / 32G | 28°C | - |
| 3 | 空闲 | 2MiB / 32G | 29°C | - |

**FewNERD s789 推理：24550 / 37648**（65%），~5min 剩余

---

### autodl-5090-c

| GPU | 状态 | 显存 | 温度 | 任务 |
|-----|------|------|------|------|
| 0 | 空闲 | 0MiB / 32G | 30°C | - |
| 1 | 空闲 | 0MiB / 32G | 32°C | - |
| 2 | **满载 98%** | 30581MiB / 32G | 72°C | FewNERD s789 推理 (vLLM) |
| 3 | 空闲 | 0MiB / 32G | 33°C | - |

**FewNERD s789 推理：7161 / 37648**（19%），~16min 剩余

---

### 总结
- **3 台服务器全部连通**，各有 1 张 GPU 在工作，其余空闲
- LLaMA FewNERD 训练还剩 ~3h 完成（3 epoch），loss 已收敛到 0.02
- LLaMA CoNLL 训练已完成，adapter 就绪
- FewNERD s789 推理在 5090-b（65%）和 5090-c（19%）上并行跑，5090-b 约 5min 完成，5090-c 约 16min 完成

---
