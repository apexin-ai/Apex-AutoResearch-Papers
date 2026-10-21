# ssh autodl model inference launch

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_model_inference_launch_20260522T163718_result.json`
- **Structured JSON:** [`7a9e8c092fd1c76f0f50.json`](../../sessions/7a/7a9e8c092fd1c76f0f50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务前提与服务器实际状态不符。汇报如下：

---

## autodl-8gpu 实际状态

### 没有小模型
服务器上 **不存在** Llama-3.1-8B / Qwen2.5-7B / Mistral-7B。之前下载的是大模型 AWQ 量化版：
- Llama-3.3-70B-Instruct-AWQ (37 GiB)
- Qwen2.5-72B-Instruct-AWQ (39 GiB)
- Mistral-Large-Instruct-2407-AWQ (60 GiB)

### 4 张 GPU 全部占满

| GPU | 用途 | 端口 | 显存占用 |
|-----|------|------|---------|
| cuda:0 | exp-003 MCMC | - | 74.3 / 97.9 GB |
| cuda:1 | vLLM: Mistral-Large-AWQ | 8003 | 90.1 / 97.9 GB |
| cuda:2 | vLLM: Llama-3.3-70B-AWQ | 8001 | 91.0 / 97.9 GB |
| cuda:3 | vLLM: Qwen2.5-72B-AWQ | 8002 | 90.1 / 97.9 GB |

### Arena-Hard 流水线已推进到 judge 阶段

Response 生成已基本完成（monitor 最后记录: llama=489, qwen=448, mistral=65）。

当前三个 vLLM 正在服务 **pairwise judge 评估**：

| Target Model | 判评进度 | 完成度 |
|-------------|---------|-------|
| Llama-3.3-70B | 2074 / 3000 | 69% |
| Qwen2.5-72B | 2045 / 3000 | 68% |
| Mistral-Large | 1382 / 3000 | 46% |

### 结论
cuda:1/2/3 不是空闲的——正在用大模型 AWQ 跑 judge 评估，不能中断。如果仍需要小模型 response，需要等当前 judge 完成后释放 GPU，或者用另一台机器。

---
