# data snr extended extract

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_snr-extended-extract_20260518T040927_result.json`
- **Structured JSON:** [`c5eb364c8ac934b12833.json`](../../sessions/c5/c5eb364c8ac934b12833.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。JSON 已保存到本地 `artifacts/snr_extended_results.json` 并注册为 artifact `art_20260518_edbba5`。

包含内容：
- 7 个 checkpoint (steps 0-300) 的 KL/BCE SNR mean + 95% CI + std
- 每个 checkpoint 32 层的 per-layer SNR
- KL 和 BCE 完整 loss curve (每 10 步)
- 训练时间 (KL: 641s, BCE: 320s)
- Final ratio KL/BCE at step 300 = 5.14x
- 两个前置实验 (v1, constrained) 的汇总对比

---
