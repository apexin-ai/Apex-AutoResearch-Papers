# ops fix sft unpruned gpu

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-sft-unpruned-gpu_20260515T223411_result.json`
- **Structured JSON:** [`072d318b54d654c4cb00.json`](../../sessions/07/072d318b54d654c4cb00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态总结和问题：

**已完成：**
- PID 66994 (sft_unpruned_baseline) 已成功 kill
- 根因确认：`sft_recovery.py` 第 19-22 行在 import torch 前解析 `--gpu` 参数并覆盖 `CUDA_VISIBLE_DEVICES`，default=0。所以即使外层设 `CUDA_VISIBLE_DEVICES=1`，脚本内部 `--gpu 0` 仍会覆盖为 GPU 0

**当前 GPU 状态变化：**
- PID 66075 (原 eval) 已不存在
- **GPU 0** (13GB/97GB): PID 560362 — `eval_gsm8k.py` 评估 `pruned_rasp_alpha_0.5`
- **GPU 1** (71GB/97GB): PID 534667 — `train_grpo_v5.py` GRPO stage2 训练
- 无活跃 tmux session

**模型路径**: `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/`

**GPU 冲突**：原计划把 SFT 放 GPU 1，但 GPU 1 现在被 GRPO 占用 71GB（仅剩 ~26GB，7B SFT 需要 ~14-18GB，很紧张）。

**可选方案：**
1. **GPU 0**：剩余 ~84GB，eval 只占 13GB，SFT 完全可以共存。用 `--gpu 0` 即可（eval 结束后 GPU 0 完全空闲）
2. **GPU 1**：与 GRPO 共存，剩余 ~26GB，可能刚好够但有 OOM 风险
3. **等 GPU 1 GRPO 结束后再启动**

修正后的启动命令（以方案 A 为例，`--gpu 0`）：
```bash
CUDA_VISIBLE_DEVICES=0 python sft_recovery.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --gpu 0 ...
```

由于 `--gpu` 参数会覆盖 `CUDA_VISIBLE_DEVICES`，正确做法是**直接传 `--gpu N`**，不需要外层 `CUDA_VISIBLE_DEVICES`。

选哪个方案？

---
