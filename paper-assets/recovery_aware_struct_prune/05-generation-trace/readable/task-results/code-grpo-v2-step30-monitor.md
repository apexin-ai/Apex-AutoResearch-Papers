# code grpo v2 step30 monitor

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-v2-step30-monitor_20260515T073628_result.json`
- **Structured JSON:** [`dc1e8fc2d60e18a27361.json`](../../sessions/dc/dc1e8fc2d60e18a27361.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部获取。

```
RASP (pid 274151):
- 当前 step: 32/250 (13%)
- reward_mean: 0.0375 → 0.0125 → 0.0125 (趋势: ↓ 后停滞)
- clipped_ratio: 0.981 → 0.988 → 0.981
- frac_reward_zero_std: 0.90 → 0.95 → 0.95
- mean_completion_length: 1006 → 1013 → 1007 (趋近 max 1024)
- loss: 0.003 → ~0 → ~0
- grad_norm: 0.44 → 0.25 → 0 (已归零)
- entropy: 0.084 → 0.080 → 0.087 (极低)
- 判断: COLLAPSE
  理由: reward 趋零、grad_norm 归零、loss 归零、生成内容为
  "#### 3*2*60" 无限重复、mean_length 贴近 max。
  frac_reward_zero_std=0.95 虽未过 0.98 阈值，但其余指标
  已全面崩溃，模型已停止学习。

Standard (pid 276973):
- 当前 step: 30/250 (12%)
- reward_mean: 0.075 → 0.019 → 0.031 (趋势: ↓ 后微回升)
- clipped_ratio: 0.731 → 0.819 → 0.769
- frac_reward_zero_std: 0.825 → 0.925 → 0.900
- mean_completion_length: 811 → 874 → 844
- loss: 0.031 → -0.003 → 0.027 (波动)
- grad_norm: 0.31 → 0.38 → 0 (step 30 归零)
- entropy: 0.138 → 0.150 → 0.146 (高于 RASP)
- 判断: PRE-COLLAPSE / UNCERTAIN
  理由: 指标整体优于 RASP（mean_length 未贴顶、clipped_ratio ~77%、
  entropy 更高），但 grad_norm 已在 step 30 归零，生成内容出现
  "#### 7248" 大量重复。frac_reward_zero_std=0.9 还未过 0.98，
  有微弱回升迹象但趋势不乐观。

磁盘: /root 30G 总量，已用 8.6G (29%)，剩余 22G — 健康。

总体结论: 
- RASP 已确认 collapse，继续训练无意义。
- Standard 处于 pre-collapse 边缘，grad_norm 归零是强烈警告信号，
  大概率在 step 40-50 前完全 collapse。
- 建议启动 v3 应急方案。两个实验的 lr=1e-6 + max_completion_length=1024
  组合在当前模型规模下 reward signal 太稀疏，
  核心问题是几乎所有 completion 都 hit length limit 且拿不到 reward。
```

---
