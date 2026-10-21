# run exp 003 s2 r3only

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp-003-s2_r3only_20260518T153014_result.json`
- **Structured JSON:** [`6617bad944b7f7f244c8.json`](../../sessions/66/6617bad944b7f7f244c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OOM 原因明确：westd-29046 是 RTX PRO 6000 (96GB VRAM)，westd-28034 是 RTX 5090 (32GB)。8B 模型 + GRPO (num_generations=4) 在 32GB 上放不下。

**选项：**

1. **多 GPU（推荐）**：用 westd-28034 的 2 张 GPU（如 cuda:2,3），通过 accelerate + FSDP 或 DeepSpeed ZeRO 分摊显存。训练超参不变，仅并行方式不同。
2. **QLoRA (4-bit)**：模型从 ~16GB 降到 ~5GB，轻松放进 32GB 单卡。但量化会改变训练动态，不完全等同于 seed 1。
3. **换到 westd-29046 另一张 GPU（cuda:0）**：环境完全一致，配置完全一致。最干净的方案，但需要 westd-29046 的 cuda:0 空闲且不影响其他实验。

哪种方案？

---
