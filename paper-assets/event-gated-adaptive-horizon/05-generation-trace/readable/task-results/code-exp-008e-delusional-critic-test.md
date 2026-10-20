# code exp 008e delusional critic test

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_008e_delusional_critic_test_20260514T033809_result.json`
- **Structured JSON:** [`796cd5483a1ff0661bd2.json`](../../sessions/79/796cd5483a1ff0661bd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Dry-run 结果

step=5000 的关键指标：

| 指标 | 值 | 验证 |
|------|-----|------|
| **gate_dt_mean** | **1.0** | ✓ imagination 全部使用 dt=1 |
| gate_dt_1_frac | 1.0 | ✓ 100% dt=1 |
| gate_dt_2_frac | 0.0 | ✓ imagination 不使用 dt=2 |
| **value_mean** | 0.00177 | ✓ 正常输出 |
| model_loss | 20.96 | ✓ RSSM 正常训练（含 dt=2 subsample 数据） |
| kl | 8.19 | ✓ 与 008d (8.08) 接近，world model 正常 |

## 总结

1. **无需代码改动** — `--gate_subsample_max_dt 2 --gate_fixed_dt 1 --imag_horizon 15` 完美实现：
   - RSSM 通过 subsample 训练 dt_embedding[2]
   - actor/critic 仅在 dt=1 imagination 上训练

2. **value_mean 已有** — `tools.tensorstats(value.mode(), "value")` 自动输出

3. **008e 完整启动命令**：
```bash
python dreamer.py --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 \
  --steps 105000 --seed 1 --compile False \
  --device cuda:1 \
  --gate_enabled True \
  --gate_fixed_dt 1 \
  --gate_subsample_max_dt 2 \
  --imag_horizon 15
```

4. **监控要点**：追踪 `value_mean / eval_return` 比率。如果该比率随训练加速上升（类似 008d，而非保持低位如 008a），则支持 Reviewer 的 delusional critic 假说。

---
