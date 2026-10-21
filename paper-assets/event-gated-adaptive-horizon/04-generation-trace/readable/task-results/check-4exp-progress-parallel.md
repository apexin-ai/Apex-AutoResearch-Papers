# check 4exp progress parallel

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_4exp_progress_parallel_20260523T194210_result.json`
- **Structured JSON:** [`1a4e1d0050b3a9fc36da.json`](../../sessions/1a/1a4e1d0050b3a9fc36da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_ID  | PID    | 步数/210K       | 最新 ve_ratio@step    | eval_return | 状态    | 预估剩余
--------|--------|----------------|-----------------------|-------------|---------|--------
exp_058 | 164830 | 60K (29%)      | 0.081@55K (峰0.231@45K) | 无          | 运行中  | ~3.9h
exp_057 | 157775 | 165K (79%)     | 0.272@165K (峰~0.49@35K)| 无          | 运行中  | ~1.2h
exp_055 | 345223 | 167K (80%)     | 1.173@162.5K           | 无          | 运行中  | ~2.8h
exp_056 | 346430 | 160.4K (76%)   | 2.203@152.5K           | 无          | 运行中  | ~3.3h
```

**补充说明：**

- **4 个实验全部没有 eval/return 指标**，只有 train_return（exp_058: 65.0, exp_055: 5.05, exp_056: 5.45）
- **所有实验 gate 完全卡死在 dt=2**：gate_dt_mean=2.0, gate_dt_2_frac=1.0, gate_empirical_entropy=0.0 — gate 从未学会变化
- bjb1-45299 FPS ~10，bjb1-40020 FPS ~4（PegInsertion 环境更重）
- exp_057 Walker 的 ve_ratio 从 35K 峰值 0.49 一路下降到 165K 的 0.27
- exp_055/056 PegInsertion 的 ve_ratio 显著高于 Cheetah/Walker（frozen 056 > trained 055）

---
