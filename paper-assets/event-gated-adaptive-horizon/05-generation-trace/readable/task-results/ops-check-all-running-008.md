# ops check all running 008

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_running_008_20260514T041806_result.json`
- **Structured JSON:** [`a2ba9d313169774ee4da.json`](../../sessions/a2/a2ba9d313169774ee4da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. 进程存活状态

| PID | 实验 | 状态 | 运行时间 |
|-----|------|------|----------|
| 106942 | exp_008a_no_subsample_dt2 | **存活** | 2h40m |
| 109519 | exp_008d_subsample_on_h8 | **存活** | 1h56m |
| 122038 | exp_008e_subsample_on_dt1_h15 | **存活** | 7m44s |
| 121636 | exp_008e_subsample_on_fixed_dt1 | **存活** | 8m08s |

全部存活。

### 2. 008e 两个实验是否重复

**是的，命令完全相同。** 两个 PID 的命令行参数一模一样：
- `--gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15`
- `--logdir logdir/exp_008e_subsample_on_fixed_dt1_h15`

两者共享同一个 logdir，只是 exit file 名字不同（`exp_008e_subsample_on_dt1_h15.exit` vs `exp_008e_subsample_on_fixed_dt1.exit`）。logdir 里有 **两个** tfevents 文件（PID 121641 和 122043），说明两个进程在同时写同一目录。目前都在 step=5000，eval_return=31.0。

**这是个问题**——两个相同实验共写一个 logdir 会互相干扰 metrics。应该 kill 掉一个。

### 3. gate_dt_embed_dim 参数

**存在。** 定义位置：
- `configs.yaml:102` — 默认值 32
- `models.py:94` — 使用 `config.gate_dt_embed_dim`

### 4. 008a eval 结果

| Step | eval_return |
|------|-------------|
| 5K | 31.0 |
| 15K | 167.2 |
| 25K | 230.8 |
| 35K | 500.8 |
| 45K | 563.4 |
| 55K | 487.9 |
| **65K** | **608.0** |

当前已到 68K（train_return ~550）。趋势向好，65K 创新高 608.0。

### 5. 008d eval 结果

| Step | eval_return |
|------|-------------|
| 5K | 31.0 |
| 15K | 153.7 |
| 25K | 167.2 |
| 35K | 146.3 |

当前到 step=45000，45K eval 尚未完成（刚进入 eval 阶段）。008d 表现明显落后于 008a——35K 时 146 vs 008a 的 501。

### 6. GPU 使用情况

| GPU | 利用率 | 显存使用 | 总显存 |
|-----|--------|----------|--------|
| GPU 0 | 39% | 6914 MiB | 97887 MiB |
| GPU 1 | 72% | 11073 MiB | 97887 MiB |

GPU 0 上有 2 个进程（008a: 4158 MiB, 008d: 2742 MiB）。
GPU 1 上有 3 个进程（一个未知 PID 107026: 2744 MiB, 008e×2: 4156+4154 MiB）。GPU 1 利用率较高因为跑了 3 个进程。

**注意**：PID 107026 在 GPU 1 上占 2744 MiB，但不在你列的 4 个 PID 中，可能是之前的残留进程。

---
