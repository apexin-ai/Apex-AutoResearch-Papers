# ops verify checkpoints and gpu model

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-checkpoints-and-gpu-model_20260518T202751_result.json`
- **Structured JSON:** [`0b7bde83deae79033b4f.json`](../../sessions/0b/0b7bde83deae79033b4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

1. **s123 checkpoint**: 存在，两个路径均有
   - `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt`
   - `/root/distill_sparse_swiglu/checkpoints/kl_30pct_s123/predictor_kl_normalized.pt`

2. **s456 checkpoint**: 存在，两个路径均有
   - `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt`
   - `/root/distill_sparse_swiglu/checkpoints/kl_30pct_s456/predictor_kl_normalized.pt`

3. **westd-34887**: NVIDIA RTX PRO 6000 Blackwell Server Edition × 2, 每卡 97887 MiB (~96 GB)

4. **westd-41718**: NVIDIA RTX PRO 6000 Blackwell Server Edition × 2, 每卡 97887 MiB (~96 GB)

两台服务器 GPU 型号和显存完全一致，4 个 checkpoint 文件全部存在（注意 s123/s456 各有两份，分别在 `kl_sparsity30_*` 和 `kl_30pct_*` 目录下）。

---
