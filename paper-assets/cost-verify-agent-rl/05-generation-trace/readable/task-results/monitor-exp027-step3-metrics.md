# monitor exp027 step3 metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp027_step3_metrics_20260515T190559_result.json`
- **Structured JSON:** [`ebf95d2ef49f665ffefa.json`](../../sessions/eb/ebf95d2ef49f665ffefa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. The grep shows the structured step:3 line with the actual metrics.

```
Step 3 状态: 完成 (3/50, 4:08:46 elapsed, Step 4 rollout 进行中)

指标:
  success:     10.16%  (0.1015625)
  KL:          0.248   (actor/kl_loss)
  entropy:     0.385   (actor/entropy)
  pass@16:     50%     (0.5)
  grad_norm:   21.31   (actor/grad_norm)
  reward_mean: 0.483   (critic/rewards/mean)

判定: 绿区 ✓
  success ≥10%:   10.16% ✓
  KL < 0.3:       0.248  ✓
  entropy > 0.15: 0.385  ✓
  pass@16 ≥ 0.5:  0.5    ✓ (刚好在边界)

趋势分析 (Step 2 → Step 3):
  success:  10.16% → 10.16%  持平
  KL:       0.413  → 0.248   ↓40% 显著下降，从黄区回到绿区
  entropy:  0.360  → 0.385   ↑7%  多样性增加
  pass@16:  62.5%  → 50%     ↓    下降但仍在绿区阈值
  batch:    6144   → 6048    略减
  step时间: 5886s  → 4689s   ↓20% 加速
```

**关键发现**: Step 3 从黄区升级到绿区。KL 从 0.413 大幅回落到 0.248，说明 Step 2 的 KL 飙升是暂态而非趋势性发散。entropy 同步上升表明策略探索性在恢复。success 稳定在 10.16%（连续两步 13/128 trajectories 成功）。

Step 4 rollout 已在进行中（02:58 UTC 开始），按当前 ~4700s/step 速率，预计 ~04:15 UTC 完成。

---
