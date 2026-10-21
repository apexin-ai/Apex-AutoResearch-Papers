# ops exp026 step progress check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_step_progress_check_20260515T133507_result.json`
- **Structured JSON:** [`781e0ca58a84c7c56b1e.json`](../../sessions/78/781e0ca58a84c7c56b1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp026 训练进度

**当前状态：Step 4 训练中（已完成 3 个训练步 + 1 次初始 val）**

两个进程均存活：
- Worker PID 781795：运行 2h56m，RSS 8.8GB
- Ray PID 778562：运行 2h56m，RSS 1.1GB

### 指标表格

| 指标 | Step 0 (val) | Step 1 | Step 2 | Step 3 |
|---|---|---|---|---|
| **success** | 0.0625 | 0.2188 | **0.3281** | 0.1719 ⚠️ |
| **pass@16** | — | 1.0 | 1.0 | 0.75 ⚠️ |
| **action_is_valid** | 0.6313 | 0.6865 | 0.6035 | 0.6413 |
| **action_is_effective** | 0.8788 | 0.9184 | 0.8256 | 0.8918 |
| **entropy** | — | 0.2672 | 0.3170 | 0.3870 |
| **kl_loss** | — | 0.1797 | 0.0974 | 0.2617 |
| **ppo_kl** | — | 0.0670 | 0.0267 | 0.0208 |
| **pg_loss** | — | 0.00732 | 0.00571 | 0.00632 |
| **grad_norm** | — | 14.43 | 15.62 | 15.65 |
| **critic/score/mean** | — | 1.218 | 1.620 | 1.079 |
| **num_actions** | 42.38 | 40.59 | 31.84 | 41.06 |
| **response_length/mean** | — | 762 | 1022 | 992 |
| **step 耗时 (s)** | 506 (val) | 2278 | 2561 | 3021 |

### GPU 与磁盘

| GPU | 利用率 | 显存 |
|---|---|---|
| cuda:0 | 100% | 49429/97887 MiB (50.5%) |
| cuda:1 | 100% | 49429/97887 MiB (50.5%) |

磁盘：`/root/autodl-tmp/` 139G/250G 已用 (56%)，空间充足。

### 异常检测

1. **success 从 step 2 → step 3 骤降：0.328 → 0.172（-47.6%）** ⚠️ 配合 pass@16 从 1.0 → 0.75 同步下降，说明不是纯方差问题。critic/score/mean 也从 1.62 回落到 1.08。需要观察 step 4-5 是否恢复。
2. **entropy 单调递增：0.267 → 0.317 → 0.387**。策略在变得更 exploratory，目前幅度可接受（未超 30% 单步跳变）。
3. **kl_loss 在 step 3 跳高（0.097 → 0.262）**，但 ppo_kl 反而继续下降（0.027 → 0.021），说明 KL penalty 在约束策略偏移，尚在控制范围内。
4. GPU 利用率 100%、无 OOM、无 abort，运行正常。

### 预估 Step 5 Val Eval 时间

- 平均 step 耗时：~2620s（步骤间有增长趋势，step 3 已达 3021s）
- Step 4 已运行约 ~2200s，预计还剩 ~800-1000s（~15 min）
- Step 5 = 训练（~2800-3000s）+ val eval（~506s）
- **预计 step 5 val eval 完成时间：约 55-60 分钟后**（~北京时间 22:55 左右）

---
