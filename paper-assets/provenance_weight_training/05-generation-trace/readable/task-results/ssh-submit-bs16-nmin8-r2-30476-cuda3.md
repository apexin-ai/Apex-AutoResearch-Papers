# ssh submit bs16 nmin8 r2 30476 cuda3

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_bs16_nmin8_r2_30476_cuda3_20260517T190645_result.json`
- **Structured JSON:** [`cb579ae74198a62d093f.json`](../../sessions/cb/cb579ae74198a62d093f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动成功。

- **PID**: 46446
- **GPU**: cuda:3 (NVIDIA RTX PRO 6000 Blackwell, 95GB)
- **tmux session**: `batchsize16_nmin8_r2`
- **日志**: `~/runs/provenance_weight_training/batchsize16_nmin8_r2.log`
- **配置**: batch_size=4 × grad_accum=4 = 有效 batch_size 16, n_min=8, tau=0.8, adaptive, max_steps=6103
- **预计时长**: ~4h (2.3s/step × 6103 steps)

注意：原始 batch_size=16 直接 OOM（Qwen3 词表 151k，logits 需 18.5GB），已改为 batch_size=4 + gradient_accumulation_steps=4，数学等效。

---
