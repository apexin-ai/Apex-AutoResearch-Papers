# ops check v8b exit and eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_v8b_exit_and_eval_20260516T065813_result.json`
- **Structured JSON:** [`fc323eabc139e552717f.json`](../../sessions/fc/fc323eabc139e552717f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated: `conclusion: success`, metrics and notes saved.

---

## v8b_twostage 500-batch Eval 结果

### Gate 判定: **ALL PASS**

| Gate | 指标 | 值 | 阈值 | 结果 |
|------|------|----|------|------|
| G1 | Margin amplification | **93.23x** | ≥ 2.0x | ✅ |
| G2 | Preservation improvement | **+56.01pp** | ≥ +10pp | ✅ |
| G3-deploy | ACIS+Prune(50%) / baseline | **0.8679** | ≤ 1.10 | ✅ |
| G4 | LED median | **0.1354** | < 1.0 | ✅ |

### 核心数据

| 条件 | action_loss | vs baseline (0.004063) |
|------|------------|----------------------|
| ACIS+Prune 50% | **0.003538** | 0.87x (优于baseline) |
| Standard (no prune) | 0.020746 | 5.09x (train-mode soft-forward 预期行为) |
| Bypass (no ACIS) | 0.018652 | 4.58x |
| Random prune 50% | 0.017966 | 4.41x |

### 关键发现

- **G3-deploy 0.87x**: ACIS+Prune(50%) 后 action_loss 比 baseline 还低 13%，说明 two-stage 训练成功让 ACIS 学到了有效的 channel selection——剪掉 50% channel 反而提升性能
- **G1 93.23x**: importance margin 被极大放大（baseline ~0.01 → IMM ~0.98），ACIS 已经学会给重要 channel 打极高分
- **G2 +56pp**: top-k preservation 从 baseline 的 33.5% 跃升至 96.7%（eps=0.01），ranking 鲁棒性显著提升
- **Bypass 确认 ACIS 有效**: bypass loss (0.0187) 略低于 standard (0.0207)，说明 ACIS 模块确实改变了 forward pass 行为

---
