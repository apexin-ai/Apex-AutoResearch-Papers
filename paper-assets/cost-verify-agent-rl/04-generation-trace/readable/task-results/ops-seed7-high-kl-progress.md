# ops seed7 high kl progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed7-high-kl-progress_20260521T205140_result.json`
- **Structured JSON:** [`1585a47bef981ed165f7.json`](../../sessions/15/1585a47bef981ed165f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报：

## exp029_seed7_high_kl 状态

- **进程状态**: dead（PID 334159 已退出，EXIT_CODE=0，正常完成）
- **GPU 利用率**: cuda:0 和 cuda:1 均 0%，0 MiB 占用（已释放）
- **当前训练 step**: 7/7（全部完成），总耗时 3h40m

### 关键 Metrics

| 指标 | Step 0 (初始) | Final |
|------|-------------|-------|
| val_success (pass@1, 32ep) | 15.625% | **31.25%** |
| val_response_length | 5,575 | 6,046 |
| val_reward_mean@32 | 1.5625 | 3.125 |
| train_response_length | 5,601 | **12,850** |

**KL 相关**:
- actor/kl_loss (step 1): 0.00128, kl_coef=0.1
- actor/ppo_kl (step 1): 2.71e-05

### 异常情况

1. **W&B BrokenPipeError**: teardown 时 W&B 连接断裂，metrics 可能未完全同步到 W&B（日志里有数据但 registry 之前没收到）
2. **Train response_length 膨胀**: 训练集 response_length 从 5,601 涨到 12,850（+129%），接近 max 16,380。Val response_length 仅温和增长（+8.4%），但 train 端的膨胀说明 **KL=0.1 未能完全抑制 response_length explosion**，只是在 val 端表现更克制
3. **Checkpoint 已保存**: `/root/autodl-tmp/checkpoints/exp029-seed7-high-kl/global_step_7/`

### Hypothesis 评估

假设条件 "step 7 response_length < 2000 and success > 30%"：success 31.25% 达标，但 train response_length 12,850 远超 2000 阈值。高 KL 改善了 val success（15.6% → 31.25%），但未能阻止训练端 response length 膨胀。

---
