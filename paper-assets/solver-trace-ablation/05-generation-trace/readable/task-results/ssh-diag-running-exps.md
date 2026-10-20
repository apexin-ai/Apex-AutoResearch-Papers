# ssh diag running exps

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diag-running-exps_20260516T164207_result.json`
- **Structured JSON:** [`e52959b69347eb6e0013.json`](../../sessions/e5/e52959b69347eb6e0013.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. exec-retrain-for-warmstart-s42 — ✅ 已完成

- **进程**: 无（已结束）
- **步数**: 203/200（已跑过 target，checkpoint-200 已保存）
- **最终 metrics**: reward_mean ~0.62-1.0，prove_rate 高，训练健康
- **checkpoint**: `/root/autodl-tmp/outputs/exec_retrain_v3_s42/checkpoint-200` ✓
- **注**: s43 也已完成（223 steps logged，checkpoint-200 存在）

### 2. gated-isr-warmstart-t02-s42 — ⚠️ 运行中但已崩溃（reward collapse）

- **进程**: PID 890110，cuda:0（94% util, 81GB VRAM）
- **步数**: 78/300
- **问题**: **reward=0.0, loss=0.0, grad_norm=0.0, gate_pass=0.000** 贯穿几乎所有 step
  - ISR gate (threshold=0.2) 完全阻断了 reward signal
  - 模型产出 ISR < 0.2，无法通过 gate，无梯度更新
  - 这是 dead run，继续跑毫无意义
- **额外风险**: 磁盘 **250G/250G 满**，下次 save (step 100) 必定 OOM

### 3. gated-isr-warmstart-t02-s43 — ❌ 已崩溃

- **进程**: 无
- **步数**: 死在 100/300
- **Traceback**:
  ```
  safetensors_rust.SafetensorError: Error while serializing: 
  I/O error: No space left on device (os error 28)
  ```
  在 step 100 保存 checkpoint 时磁盘满崩溃
- **同样的 reward collapse**: gate_pass=0.000 贯穿全程，仅极少数 step 有 reward（step 79: 0.125, step 87: 0.375）

---

## 根因

1. **磁盘满**: exec_retrain 配置 `save_total_limit: 10`（违反 C003），两个 exec_retrain 目录各保留 3 checkpoint = 45GB × 2 = 90GB 不必要占用
2. **ISR gate 过严**: warmstart 模型虽然 prove_rate 不错，但 ISR 几乎全在 0.2 以下 → gate_pass=0 → 无 reward → 无梯度 → 死循环

---

## 需要的操作

| 实验 | 操作 |
|------|------|
| exec-retrain s42/s43 | Registry → `conclusion: success`。清理旧 checkpoint（仅保留 checkpoint-200） |
| gated-isr-warmstart-t02-s42 | **Kill**（reward collapsed + 即将磁盘满崩溃），registry → `conclusion: failed_reward_collapse` |
| gated-isr-warmstart-t02-s43 | Registry → `conclusion: failed_disk_full` |
| **磁盘清理** | 删 `exec_retrain_v3_s{42,43}/checkpoint-{100,150}` → 释放 ~60GB |
| **重新提交前** | 需修复 ISR gate 策略（threshold 0.2 对 warmstart 模型太高，或改为 progressive gating） |

---
