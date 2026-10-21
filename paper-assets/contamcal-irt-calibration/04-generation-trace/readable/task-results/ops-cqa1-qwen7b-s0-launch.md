# ops cqa1 qwen7b s0 launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-qwen7b-s0-launch_20260520T023245_result.json`
- **Structured JSON:** [`1a8b5d7a0b45a57d0ff4.json`](../../sessions/1a/1a8b5d7a0b45a57d0ff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已确认启动，模型加载成功，正在 tokenize d000 数据集。

```
cqa1 s0 训练: 已启动
PID: 313418 (GPU process), tmux PID: 313407
tmux session: sft_qwen7b_s0_cqa1
磁盘空间: /root/autodl-tmp 72% (49G free)
参数: batch=1, grad_accum=16, lr=5e-5, lora_r=16, lora_alpha=32, gradient_checkpointing, bf16
预计训练时长: ~10-15h (5 dosages × 50k samples, batch=1 on 4090D 24GB)
```

注意：bitsandbytes 的 `libnvJitLink.so.13` 警告是非关键的（未使用 4bit 量化），不影响训练。

---
