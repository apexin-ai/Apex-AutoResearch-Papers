# analysis rsft ced s43 train r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rsft_ced_s43_train_r3_20260516T021246_result.json`
- **Structured JSON:** [`0b7bb2dbf2bb7f791237.json`](../../sessions/0b/0b7bb2dbf2bb7f791237.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练结果摘要

- **状态**: success (EXIT_CODE=0, "RSFT training complete.")
- **最终 train_loss**: 0.6151
- **最终 eval_loss**: 0.7618
- **总步数**: 510
- **Epoch**: 3.0
- **训练耗时**: 1h 49m (08:21 → 10:10)
- **Checkpoint 路径**: `/root/autodl-tmp/rsft_output_ced_s43/` (adapter_model.safetensors, 504MB)
- **W&B run ID**: 无（未启用 W&B）
- **基座模型**: Qwen3-4B + SFT adapter merged
- **数据**: 2718 samples, CED scores mean=0.668
- **可训练参数**: 132M / 4.15B (3.18%)

### Task Eval 指标

| Step | F1 | Ign-F1 | Evi-F1 | EDCR | Preds |
|------|-----|--------|--------|------|-------|
| 170 | 0.4601 | 0.4548 | 0.7004 | 0.6205 | 899 |
| 510 (final) | **0.5026** | **0.4932** | **0.7624** | **0.6516** | 795 |

### Eval Metrics (final)
- eval_entropy: 0.6722
- eval_mean_token_accuracy: 0.8291

### 对比前次
- r1: 失败
- r2: 被 kill (SIGTERM)
- **r3: 正常完成**，训练收敛正常，F1 从 step 170 的 0.46 提升到 final 的 0.50

## 建议
- 可以进入 eval 阶段。提交 eval 前需按 C001 约束先 `nvidia-smi` 确认目标 GPU 显存空闲 < 2GB。
- 注意模型保存路径是 `/root/autodl-tmp/rsft_output_ced_s43/`（不在 `freige/` 子目录下）。

---
