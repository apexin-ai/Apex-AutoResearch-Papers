# check all gpu status urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_gpu_status_urgent_20260516T224752_result.json`
- **Structured JSON:** [`467b10b8bfd9bdb0822f.json`](../../sessions/46/467b10b8bfd9bdb0822f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU STATUS REPORT ===

[cqa1-33015] — 4x RTX 4090 D (24GB)
cuda:0 | Full FT seed=1    | step 18450/100K | loss=0.063 | sps=4.2 | 2.7GB VRAM
cuda:1 | IMM Full FT 100K  | step 9500/10K   | Stage 1    | margin_loss=0.058 | sps=4.2 | 2.9GB VRAM
cuda:2 | LoRA seed=0       | ✅ DONE (06:44 完成)
cuda:3 | Full FT seed=0    | ✅ DONE (06:47 完成)

[westd-27271] — 2x RTX PRO 6000 Blackwell (98GB)
cuda:0 | IMM v2 (50K base) | step 15550/20K | Stage 2 | total=0.151 action=0.061 | sps=2.9 | 4.7GB VRAM
cuda:1 | 空闲 (0 MiB, 0% util)

空闲 GPU: cqa1 cuda:2, cqa1 cuda:3, westd cuda:1
```

**注意事项：**
- cqa1 cuda:1 的 IMM Stage 1 即将完成（9500/10000），约 10 分钟后进入 Stage 2
- cqa1 cuda:2/3 已完成训练，可分配新任务
- westd cuda:1 完全空闲，98GB 大卡可用

---
