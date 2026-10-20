# code d048 phase b prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d048_phase_b_prep_20260522T091503_result.json`
- **Structured JSON:** [`ae85a9fc304832b792a2.json`](../../sessions/ae/ae85a9fc304832b792a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。

## 子任务 1: v9_pcgrad.py 参数

- **--min-gate-std**: 支持, 默认值=`MIN_GATE_STD`=**0.05** (from config.py)
- **--max-seq-len**: 支持, 默认值=`MAX_SEQ_LEN`=**2048** (from config.py)
- **argparse 差异**: 无。两个文件的 argparse 定义完全一致（20 个参数相同），差异仅在训练循环（PCGrad 双 backward + 梯度投影 vs 标准 combined loss）
- **PCGrad s42 复用判断**: **可复用**。未传 `--min-gate-std` 和 `--max-seq-len` 时默认值分别是 0.05 和 2048，符合要求。

## 子任务 2: Base dry-run

- **结果**: 成功，2 步完成（12.5s）
- **loss 组分**: 只有 NTP。`L_NTP=1.3786 L_GAR=0.2294 L_DIV=0.0000 Loss=1.3786`——GAR 被计算但乘以 λ=0 后未计入总 loss（Loss == L_NTP）
- **gate 行为**: gate_type=none → Gate=1.0000, std=0.0000, 所有 28 层固定 1.0, Gate params=0, 无梯度
- **问题**: 无。`/tmp/d048_base_dryrun` 已清理。

## 子任务 3: LO s42 验证

- **实际 gate_type**: `"none"` (train_config.json 确认)
- **gate 行为**: fixed 1.0（gate_type=none → 无 gate 参数，Gate params=0）
- **训练配置**: lambda_gar=1.0, gar_loss_mode=mse_target, gar_target=0.5, max_seq_len=2048, seed=42, epochs=3
- **min_gate_std 差异**: 保存值为 0.0（非当前默认 0.05），但因 gate_type=none 无 gate 参数，该值不影响训练行为
- **复用判断**: **可复用**。gate_type=none + lambda_gar=1.0 + GAR loss 活跃，等价于 D048 LO 配置。

---
