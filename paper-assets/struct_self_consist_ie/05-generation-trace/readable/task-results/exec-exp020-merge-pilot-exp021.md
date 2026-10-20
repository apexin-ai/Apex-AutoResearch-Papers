# exec exp020 merge pilot exp021

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_exp020_merge_pilot_exp021_20260516T160805_result.json`
- **Structured JSON:** [`62c32d647aab068ba84a.json`](../../sessions/62/62c32d647aab068ba84a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-021 is running. All confirmed.

---

## Summary — 4-Step Pipeline Complete

| Step | Status | Details |
|------|--------|---------|
| **1. exp-020 训练完成** | DONE | 8236/8236 steps, eval_loss=0.031, time=5h54m |
| **2. LoRA merge** | DONE | `checkpoints/qwen3-8b-fewnerd-merged/` (9 shards) |
| **3. Pilot inference** | **PASS** | Greedy F1 = **0.8037** > 0.5 threshold |
| **4. exp-021 4-GPU 训练** | RUNNING | 4x RTX 5090, DDP, 6177 steps, 3 epochs |

**exp-021 运行信息：**
- tmux session: `exp021`
- PIDs: 316742, 316743, 316744, 316745 (4 worker ranks)
- Log: `/tmp/exp021_train.log`
- GPU 利用率: 71-100%, 每卡 ~20 GB
- Config: LoRA r=32/α=64, bs=2×4GPU×8accum=64 effective, lr=2e-4, cosine, 3 epochs
- 总步数: 6177 (vs exp-020 单卡 8236 步，因 4GPU 并行 effective batch size 翻倍)

**注：** DeepSpeed ZeRO-2 因版本兼容问题（DS 0.18.9 vs LlamaFactory 要求 ≤0.16.9 + lr_scheduler bug）回退为 PyTorch DDP。对 LoRA 训练来说 DDP 已足够（87M 可训练参数，显存不是瓶颈）。

---
