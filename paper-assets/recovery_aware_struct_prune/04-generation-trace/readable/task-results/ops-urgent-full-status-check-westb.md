# ops urgent full status check westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_full_status_check_westb_20260517T225419_result.json`
- **Structured JSON:** [`931768daa582f2dd2d51.json`](../../sessions/93/931768daa582f2dd2d51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. PID 存活情况
| 任务 | PID | 状态 |
|------|-----|------|
| grpo_cka_only_20 | 725232 (子进程，bash wrapper 725227) | **运行中** |
| grpo_random_20 | 719684 | **运行中** |

### 2. GPU 状态
| GPU | 温度 | 功耗 | 显存占用 | 利用率 |
|-----|------|------|----------|--------|
| cuda:0 | 80°C | 604W/600W | 73549/97887 MiB | 100% |
| cuda:1 | 81°C | 599W/600W | 73165/97887 MiB | 100% |

**无空闲 GPU**，两张卡满载。

### 3. 训练进度

**grpo_cka_only_20** (cuda:0)
- 当前 step: **70/100**
- 已运行: ~7h54m
- 预计剩余: ~3h18m（~395s/step × 30 steps）
- 预计完成: ~2026-05-18 10:12 UTC

**grpo_random_20** (cuda:1)
- 当前 step: **75/100**
- 已运行: ~9h04m
- 预计剩余: ~2h59m（~430s/step × 25 steps）
- 预计完成: ~2026-05-18 09:54 UTC

### 4. 每 10 步指标趋势

**grpo_cka_only_20:**

| Step | Reward | frac_zero_std | grad_norm | KL | Entropy |
|------|--------|---------------|-----------|------|---------|
| 10 | 0.2531 | 0.175 | 1.891 | 0.00121 | 0.0830 |
| 20 | 0.2181 | 0.200 | 1.250 | 0.00123 | 0.0749 |
| 30 | 0.2500 | 0.200 | 1.102 | 0.00167 | — |
| 50 | 0.3544 | 0.150 | 1.977 | 0.00157 | 0.0938 |
| 60 | 0.2994 | 0.200 | 3.750 | 0.00158 | 0.0934 |
| 70 | 0.3075 | 0.125 | 1.164 | 0.00156 | 0.0862 |

趋势: reward 从 0.25→0.35 有上升，frac_zero_std 从 0.2 降到 0.125（好），KL 稳定在 0.0015 左右，entropy 低（0.08-0.09）。训练健康。

**grpo_random_20:**

| Step | Reward | frac_zero_std | grad_norm | KL | Entropy |
|------|--------|---------------|-----------|------|---------|
| 10 | 0.1606 | 0.300 | 3.750 | 0.00418 | 0.2313 |
| 20 | 0.1419 | 0.325 | 8.625 | 0.00470 | 0.2282 |
| 30 | 0.1663 | 0.325 | 3.672 | — | — |
| 50 | 0.1750 | 0.300 | 4.750 | 0.00458 | 0.2140 |
| 60 | 0.1844 | 0.350 | 3.594 | 0.00416 | 0.2005 |
| 70 | 0.1900 | 0.300 | 7.094 | 0.00451 | 0.2246 |

趋势: reward 从 0.16→0.19 缓慢上升，frac_zero_std 持续偏高（0.30-0.35），KL 约 0.0045（比 cka 高 3x），entropy 高（~0.22）。random 剪枝后的模型学习效率明显低于 CKA 剪枝。

### 结论
两个训练均在正常进行，random_20 预计约 3h 后完成，cka_only_20 约 3.3h 后完成。CKA 剪枝在 GRPO 恢复训练中表现明显优于 random 剪枝（reward 高 ~60%，zero-std 比例低）。

---
