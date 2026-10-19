# infra libero smolvla setup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_libero-smolvla-setup_20260513T023758_result.json`
- **Structured JSON:** [`f89277aa06d3273644cb.json`](../../sessions/f8/f89277aa06d3273644cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。核心结果：

**LIBERO**: ✅ robosuite 1.4.0 + libero 0.1.1 + mujoco 3.8.1。5 个 benchmark 可用（spatial/object/goal/90/10，各 10-90 tasks）。数据集 demo 文件需单独下载。

**SmolVLA** (`lerobot/smolvla_base`):
- 450M 参数，865MB 磁盘，**0.86GB VRAM**
- VLM backbone: SmolVLM2-500M-Video-Instruct (16 layers, cross_attn)
- Flow matching num_steps=10, chunk_size=50, action_dim=6

**K=10 推理**:
- K=1: **380ms**
- K=10 sequential: 3931ms (393ms/sample)
- **K=10 batched: 450ms**（8.7x 加速，仅多用 0.4GB VRAM → 1.33GB，远低于 24GB 上限）

**修复了 6 个环境问题**（EGL、HF 503、版本冲突、groot patch、num2words、attention_mask dtype）。详见报告。

---
