# ssh autodl small model batch inference

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_small_model_batch_inference_20260522T092638_result.json`
- **Structured JSON:** [`ec2b199af8f56cc94680.json`](../../sessions/ec/ec2b199af8f56cc94680.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态汇总：

**下载进度：**
- **Gemma-2-9b-it**: ModelScope 下载中，4.1GB/17.2GB（~24%），预估 ~55 min 剩余
- **Llama-3.1-8B-Instruct**: 在 gemma 之后顺序下载，预估 gemma 完成后 ~60 min
- **Qwen2.5-7B / Mistral-7B**: 编排脚本会在 gemma 完成后自动启动下载

**编排逻辑（tmux: orchestrator）：**
1. 等 gemma 权重完整 → GPU 0 启动推理 + 启动 Qwen/Mistral 下载
2. 等 llama 权重完整 → GPU 1 启动推理
3. 等 Qwen 权重完整 → GPU 2 启动推理
4. 等 Mistral 权重完整 → GPU 3 启动推理

**脚本修改：**
- `generate_vllm_batch.py`: 加了 `enforce_eager=True`（跳过 Blackwell GPU 上的 torch.compile 卡顿），4 个小模型改用本地路径
- `run_small_models.sh`: 自动编排下载→推理流水线

**预估时间线：**
- ~18:40 gemma 下载完 → 开始推理（~20-30min）+ 启动 Qwen/Mistral 下载
- ~19:40 llama 下载完 → 开始推理
- ~20:00 Qwen 下载完 → 开始推理
- ~20:40 Mistral 下载完 → 开始推理
- ~21:10 全部完成

**磁盘**: 170GB 可用，足够

**问题：**
- Gemma 和 Llama 是 HuggingFace gated repo，无 HF token，使用 ModelScope 下载
- AutoDL 下载带宽 ~4MB/s（ModelScope CDN），是主要瓶颈
- Blackwell GPU (SM 12.x) 的 vLLM torch.compile 有问题，已用 `enforce_eager=True` 绕过

要我定时轮询检查进度，还是你稍后再来查？

---
