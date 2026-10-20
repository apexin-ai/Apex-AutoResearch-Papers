# check step 50k

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_step-50k_20260513T042653_result.json`
- **Structured JSON:** [`457828e6b3381ba8721b.json`](../../sessions/45/457828e6b3381ba8721b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告

### 进程 & GPU
- **进程存活**: 5 个 dreamer 相关进程运行中
- **GPU 利用率**: GPU 0: 0%, 4722 MiB | GPU 1: 27%, 4345 MiB

### 训练进度

| 指标 | Baseline | Event-Gated |
|------|----------|-------------|
| **当前 step** | **65,000** | **60,000** |
| 最新 eval_return | 615.86 (step 65K) | 188.46 (step 55K) |
| 最新 train_return | ~808–841 (step 64K) | ~38–208 (step 60K) |
| model_loss | 3.94 | 3.92 |
| fps | 7.58 | 6.66 |

### Gate 指标 (event-gated, step 55K 最新详细记录)

| 指标 | 值 | 说明 |
|------|-----|------|
| **gate_scale** | **0.0** | ⚠️ Phase 2 尚未启动 |
| **gate_loss** | **0.0** | gate 梯度未开放 |
| gate_dt_mean | 1.0 | 完全固定在 dt=1 |
| gate_dt_std | 0.0 | 无变异 |
| gate_dt_1_frac | 1.0 | 100% 选择 dt=1 |
| gate_empirical_entropy | 0.0 | 无多样性 |
| gate_entropy_ratio | 0.0 | — |
| gate_entropy_bonus | 0.095 | 熵奖励在累积但 scale=0 未生效 |

### Eval Return 趋势对比

| Step | Baseline | Event-Gated | 比值 (EG/BL) |
|------|----------|-------------|-------------|
| 5K | 31.8 | 31.0 | 0.98 |
| 15K | 206.6 | 161.5 | 0.78 |
| 25K | 395.3 | 186.6 | 0.47 |
| 35K | 388.5 | 211.9 | 0.55 |
| 45K | 513.8 | 127.9 | 0.25 |
| 55K | 625.7 | 188.5 | 0.30 |

### 关键发现

1. **Phase 2 未启动** — event-gated 已过 50K 步但 `gate_scale` 仍为 0.0，gate 完全锁定在 dt=1。需要确认 Phase 2 的触发条件是否正确配置（可能 gate_scale 的 warmup schedule 设置有问题，或 50K 阈值检查逻辑未触发）。

2. **event-gated 严重落后** — eval return 仅为 baseline 的 30%（188 vs 626）。gate 模块虽然 scale=0，但其存在可能仍在影响梯度流或计算图，增加了学习负担。

3. **GPU 0 利用率 0%** — 可能 baseline 在 GPU 1 上活跃训练，GPU 0 的进程处于空闲或数据收集阶段。

**建议检查**: event-gated 的配置文件中 Phase 2 启动阈值（gate_scale warmup 的起始 step 是否确实设为 50K），以及为什么 55K 步时 gate_scale 仍为 0。

---
