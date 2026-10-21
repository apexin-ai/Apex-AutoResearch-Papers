# eval sim rollout temp08

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_sim_rollout_temp08_20260516T113930_result.json`
- **Structured JSON:** [`1d76a9ce118b2fe77660.json`](../../sessions/1d/1d76a9ce118b2fe77660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

```
cuda:0 temp=0.8: success_rate = 0/50 (0.0%)
Mean episode length: 400.0 steps (all episodes hit max)
95% Wilson CI: [0.0%, 7.1%]
Mean reward: 0.0000
```

Temperature=0.8 修复了 flow matching ODE 的 diversity（noise_diversity_std=0.052 PASS），但在 closed-loop sim rollout 中 **0% 成功率**。所有 50 个 episode 均跑满 400 步，reward 全为 0。

行为分析：
- 每个 episode 稳定跑满 400 步（不是几步内崩溃），说明模型在输出 action，但 action 质量不足以完成 peg insertion 任务
- reward 全部为 0.000，没有任何 episode 有部分进展
- 3.4s/episode（400 steps），说明每步推理正常运行

**结论**：Temperature scaling 恢复了 action 分布的 diversity，但 LoRA fine-tuning 导致的 action quality 退化（不仅仅是 mode collapse）无法通过推理时 temperature 调整来修复。问题不只是 ODE trajectory 过于集中，而是学到的 velocity field 本身就偏离了正确的 action 空间。

---
