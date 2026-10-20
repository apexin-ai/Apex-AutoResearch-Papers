# diagnose grpo random 20 wandb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_random_20_wandb_20260518T020357_result.json`
- **Structured JSON:** [`dc8316f350e7c5777523.json`](../../sessions/dc/dc8316f350e7c5777523.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B run 存在 (state: crashed) 但 **metrics 未同步到 W&B**（timeout 杀进程前未 flush）。Log 文件有完整 9 个 checkpoint 的数据。

汇总结果：

```
W&B data available: no (run exists but metrics not synced before timeout kill)
Log data available: yes
Steps captured: 9 (step 10, 20, 30, 40, 50, 60, 70, 80, 90)
```

**从 log 提取的完整 dynamics：**

| Step | reward | frac_zero_std | entropy | kl |
|------|--------|---------------|---------|------|
| 10   | 0.1606 | 0.300 | 0.2313 | 0.0042 |
| 20   | 0.1419 | 0.325 | 0.2282 | 0.0047 |
| 30   | 0.1663 | 0.325 | 0.2353 | 0.0046 |
| 40   | 0.1450 | 0.400 | 0.2145 | 0.0046 |
| 50   | 0.1750 | 0.300 | 0.2140 | 0.0046 |
| 60   | 0.1844 | 0.350 | 0.2005 | 0.0042 |
| 70   | 0.1900 | 0.300 | 0.2246 | 0.0045 |
| 80   | 0.1419 | 0.375 | 0.2374 | 0.0049 |
| 90   | 0.1725 | 0.325 | 0.2206 | 0.0042 |

**Dynamics pattern: Stable plateau, no collapse.**
- Reward: 振荡 0.14-0.19 (mean ~0.164), 无持续上升趋势
- frac_zero_std: 振荡 0.30-0.40, 高位但未到 collapse (collapse = 0.8+)
- Entropy: 稳定 0.20-0.24, 无崩塌
- KL: 极低 0.004-0.005, 模型几乎未学习

与已知 step 70 数据完全吻合 (reward=0.19, frac_zero_std=0.30)。

**Recommendation: 可直接分析。** 9 个 checkpoint 覆盖 90% 训练过程，pattern 明确且稳定——不需要重跑。"Random = plateau, no collapse" 结论可确认为 success。

是否需要我更新 registry 将此实验标记为 success？

---
