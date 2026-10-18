# ops check v8 1 exit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_v8_1_exit_20260516T055533_result.json`
- **Structured JSON:** [`696bbba3f7911709c813.json`](../../sessions/69/696bbba3f7911709c813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the final report:

---

## v8.1 实验报告 (`mvp_imm_anchor_v8_1`)

### 1. 训练退出原因

**正常完成。** 30K steps 全部跑完，无异常退出。

- 日志末行：`2026-05-16 13:54:38 [INFO] Training complete.`
- W&B summary：`train/action_loss=0.00245`, `gate/lipschitz_estimate=1.00031`, `margin/mean=1.4944`
- PID 121326 已退出

### 2. 最终 step 数和 checkpoint 状态

- **最终 step**: 29950/30000（checkpoint 保存在 step_029999）
- **Checkpoint 目录**: `checkpoints/imm_anchor_v8_1/`，共 15 个 checkpoint（step_002000 ~ step_029999，每 2000 步）
- **latest 软链接** → `step_029999`

### 3. Eval 结果

**OVERALL VERDICT: FAIL** — G3-deploy 未通过

#### Gate 评估

| Gate | 指标 | 值 | 阈值 | 结果 |
|------|------|-----|------|------|
| G1 | Δ_k margin ratio | **86.5x** | ≥ 2.0 | **PASS** |
| G2 | Preservation rate diff | **+59.2pp** | ≥ 10pp | **PASS** |
| G3-deploy | ACIS+Prune(50%) loss / baseline | **2.53x** | ≤ 1.10 | **FAIL** |
| G4 | LED ratio median | **0.084** | < 1.0 | **PASS** |

#### Standard Eval (ACIS, 500 batches, train mode)

| Condition | action_loss | preservation |
|-----------|-------------|--------------|
| eps0.0, prune=F | 0.0374 | 1.000 |
| eps0.0, prune=T (50%) | **0.0103** | 1.000 |
| eps0.01, prune=F | 0.0378 | 0.978 |
| eps0.01, prune=T | 0.0121 | 0.977 |
| eps0.02, prune=F | 0.0390 | 0.953 |
| eps0.02, prune=T | 0.0159 | 0.952 |
| eps0.05, prune=F | 0.0521 | 0.855 |
| eps0.05, prune=T | 0.0200 | 0.856 |

**Baseline**: 0.004077

#### Bypass-ACIS (random prune baseline)

| Condition | action_loss |
|-----------|-------------|
| eps0.0, prune=F | 0.0380 |
| eps0.0, prune=T | 0.0183 |

Bypass vs Standard 几乎一致（G3a-bypass=9.32x vs G3-standard=9.17x），**排除 ACIS selection overhead 为 G3 失败的主因**。

#### 关键观察

- **Margin 和 preservation 极佳**（G1 86.5x, G2 +59pp），说明 IMM 成功地拉开了重要/不重要 token 的 margin
- **LED certified bound 很低**（0.084），理论保证很强
- **但 action_loss 绝对值仍远高于 baseline**：最佳条件（eps0.0, prune=T）的 0.0103 是 baseline 的 2.53 倍
- 降低 λ_margin 从 0.5→0.2 + gradient isolation 未解决核心问题：**模型在 IMM 训练后 action 预测质量本身下降了**

---
