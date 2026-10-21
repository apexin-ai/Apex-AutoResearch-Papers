# ops exp026 metrics hunt

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_metrics_hunt_20260515T122735_result.json`
- **Structured JSON:** [`443dbf8242f761067b33.json`](../../sessions/44/443dbf8242f761067b33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp026 指标报告

### 指标来源
Ray worker stdout：`/root/autodl-tmp/tmp/ray/session_2026-05-15_18-38-45_487055_778562/logs/worker-f5a9c771...781795.out`

控制台日志被大量 `anchor_obs` 警告刷屏，指标被淹没但实际存在。TensorBoard 无数据因为 config 的 logger 列表是 `['console', 'wandb']` 而 WANDB_MODE=disabled，无 tensorboard backend。

---

### Step 0-2 指标趋势

| 指标 | Step 0 (val) | Step 1 (train) | Step 2 (train) | 趋势 |
|------|-------------|----------------|----------------|------|
| **success** | 6.25% | 21.88% | 32.81% | ↑ 显著提升 |
| **entropy** | — | 0.2672 | 0.3170 | ↑ 未 collapse |
| **pg_loss** | — | 0.00732 | 0.00571 | ↓ 正常 |
| **kl_loss** | — | 0.1797 | 0.0974 | ↓ 模型稳定化 |
| **ppo_kl** | — | 0.0670 | 0.0267 | ↓ |
| **reward/score mean** | — | 1.218 | 1.620 | ↑ |
| **grad_norm** | — | 14.43 | 15.62 | 稳定 |
| **action_is_valid** | 63.1% | 68.6% | 60.3% | 波动 |
| **pass@16** | — | 100% | 100% | — |

---

### 关键结论

1. **无 entropy collapse** — entropy 从 0.267 → 0.317（反而上升），与 exp020b/022/023c 的前 5 步崩塌形成鲜明对比
2. **Success rate 快速上升** — 从 baseline 6.25% → 32.8%（2 步内 5× 提升）
3. **当前状态**：Step 3 正在计算 ref log prob（两卡 100% 利用率），~43 min/step
4. **下一个判断点**：Step 5 val（test_freq=5），预计 ~22:50（北京时间）

---

### 为什么控制台看不到指标

tmux 的 `capture-pane` 只保留最后 N 行屏幕缓冲区，而 `anchor_obs` 警告每步产生数百行，把指标行推出了可见范围。实际指标每步结束时输出一行到 worker stdout，需从 Ray logs 目录读取。

---
