# ssh cleanup restart s43 variant

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup-restart-s43-variant_20260516T164656_result.json`
- **Structured JSON:** [`5c61e265a69c72c21dfb.json`](../../sessions/5c/5c61e265a69c72c21dfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 产出

### 1. 磁盘清理
- **释放 ~110GB**（250G→141G used，110G available）
- 删除：exec_retrain_v3 中间 checkpoints (60G) + 失败的 warmstart (35G) + isr_gated_curriculum (15G)

### 2. s43 checkpoint-100 状态
- **不可用**（仅 1/4 safetensors，磁盘满时写入中断）
- 已决定：从 exec_retrain_v3_s43/checkpoint-200 重新开始

### 3. 两个实验 PID
| 实验 | GPU | PID | tmux session |
|------|-----|-----|-------------|
| τ=0.2 s43 r2 | cuda:0 | 896839 | warmstart_t02_s43 |
| τ=0.15 s43 | cuda:1 | 896913 | warmstart_t015_s43 |

### 4. 前 5 步指标对比

| Step | τ=0.2 reward | τ=0.2 gate_pass | τ=0.15 reward | τ=0.15 gate_pass |
|------|-------------|-----------------|---------------|------------------|
| 1 | 1.0 | 1.0 | 1.0 | 1.0 |
| 2 | 0.0 | — | 0.0 | — |
| 3 | 0.25 | 0.286 | 0.25 | 0.286 |
| 4 | 0.0 | — | 0.0 | — |
| 5 | 0.125 | 0.125 | 0.125 | 0.125 |

前 5 步两个 τ 变体表现相同（因为 ISR 值要么远超两个阈值 (0.8, 0.48)，要么远低于两个阈值 (0.117/0.131)）。τ 差异需要更多步数才能体现——在 ISR 介于 0.15~0.2 的 proof 上会产生分化。

τ=0.2 的 grad_norm 正常（step 4: 9.65, step 6: 1.70），确认梯度在流动。τ=0.15 的 step 6-10 全部 reward=0（gate_pass=0），但这在早期训练属正常——数据采样导致的稀疏信号。

---
