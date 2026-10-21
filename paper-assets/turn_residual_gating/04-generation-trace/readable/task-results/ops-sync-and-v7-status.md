# ops sync and v7 status

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync_and_v7_status_20260518T204116_result.json`
- **Structured JSON:** [`ad4047892b77395b23b3.json`](../../sessions/ad/ad4047892b77395b23b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete report:

---

## 任务 1: 代码同步结果

3 个文件已成功同步到 `westd-20861:/root/turn_residual_gating/src/`:

| 文件 | 大小 | 关键验证 |
|------|------|----------|
| `threadgate.py` | 6,740B | `gate_type=="none"` 分支: L88, L115, L163 |
| `train_phase2.py` | 14,935B | |
| `eval_phase2_gar.py` | 22,913B (519行) | `--gate-profile` flag: L321 |

注意: eval_phase2_gar.py 头部注释从中文改为英文（避免 heredoc 编码问题），功能代码完全一致。

---

## 任务 2: v7 训练进度

**当前位置**: Epoch 1, data step 1850 → **global_step ≈ 1231 / 3000 (41%)**

**Epoch 0 已完成**: Avg Loss=0.9757, Avg NTP=0.9499, Avg GAR=0.0255, Avg DIV=0.0003
Checkpoint saved → `/root/turn_residual_gating/runs/phase2_tg_s42_v7/epoch_0`

**最新指标** (Epoch 1 Step 1850):
- L_NTP=0.5583, L_GAR=0.0023, L_DIV=0.0000, Loss=0.5607
- Gate mean=0.9516

**Gate 统计** (global step 1200):
- mean=0.9570, std=0.0540, min=0.7891, max=0.9961
- 相比 step 950 (mean=0.9672), gate mean 略有下降，说明 gate 正在学习抑制部分层

**Gate Profile** (step 1200, 最活跃的抑制层):
- **L3=0.789** (最低), L4=0.797, L0=0.863, L5=0.918
- 高层保持接近 1.0: L26=0.996, L27=0.996

**进度估算**:
- Epoch 0: 完成 (1000 global steps)
- Epoch 1: 23% (1850/8000 data steps → ~231 global steps done)
- 剩余: ~1769 global steps (epoch 1 剩余 + 全部 epoch 2)

---
