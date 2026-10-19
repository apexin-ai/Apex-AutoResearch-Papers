# infra server setup

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_server_setup_20260516T185938_result.json`
- **Structured JSON:** [`395eb38919fcf817508e.json`](../../sessions/39/395eb38919fcf817508e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。汇总如下：

---

**环境状态**
- Python 3.12.3（conda base）
- PyTorch 2.10.0+cu128，CUDA 可用
- 所有依赖已就绪：transformers 4.57.6, datasets 4.8.4, accelerate 1.13.0, einops 0.8.2, scikit-learn 1.8.0, modelscope 1.35.4

**GPU 信息**
- 2× NVIDIA RTX PRO 6000 Blackwell Server Edition，每卡 94GB 显存

**模型路径**
- `/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Llama-8B/`（2 个 safetensors shard）

**数据集**
- HarmThoughts：56,931 行，缓存于 `/root/autodl-tmp/.hf_cache/datasets/`

**项目目录**
- `/root/autodl-tmp/contrastive_trace_safety/`（含 `artifacts/hidden_states/` 和 `src/`）

**磁盘剩余**
- `/root/autodl-tmp/`：35GB 可用（250GB 中已用 216GB）

---
