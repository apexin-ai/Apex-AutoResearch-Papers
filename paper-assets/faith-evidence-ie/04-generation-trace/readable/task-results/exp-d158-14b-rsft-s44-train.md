# exp d158 14b rsft s44 train

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_d158_14b_rsft_s44_train_20260525T051132_result.json`
- **Structured JSON:** [`6aee6397d826b13603eb.json`](../../sessions/6a/6aee6397d826b13603eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。

**状态汇总**：
- **PID**: 357577, cuda:1
- **模型加载**: Qwen3-14B 加载完成 → SFT adapter 合并完成 → LoRA 创建完成 (trainable 1.71%, 257M params)
- **数据**: 3016 samples tokenized, CED scores mean=0.691
- **训练进度**: 9/567 steps (~7s/step), 总步数 567 (3016 samples × 3 epochs ÷ 16 effective batch)
- **预计耗时**: ~567 × 7s ≈ 66 min
- **超参数**: 与原始 14B RSFT 一致 (lr=2e-5, rank=64, alpha=128, dropout=0.05, epochs=3, grad_accum=16 for single GPU)
- **wandb**: `freige-rsft / rsft_qwen3_14b_k1_s44`
- **输出**: `/root/autodl-tmp/rsft_output_14b_s44`

---
