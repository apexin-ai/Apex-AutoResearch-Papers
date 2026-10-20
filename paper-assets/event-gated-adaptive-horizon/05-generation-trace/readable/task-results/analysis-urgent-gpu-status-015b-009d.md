# analysis urgent gpu status 015b 009d

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_urgent_gpu_status_015b_009d_20260515T163803_result.json`
- **Structured JSON:** [`5285dbe9df9562fb7713.json`](../../sessions/52/5285dbe9df9562fb7713.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 9% | 4722 / 97887 MiB |
| 1 | 0% | 2753 / 97887 MiB |

| PID | 实验 | 设备 | 运行时长 | 显存 |
|-----|------|------|----------|------|
| 149708 | **009d** baseline_walker_s0 (500K steps) | cuda:0 | 4h13m | 4156 MiB |
| 149996 | **015b** frozen_dt_emb (105K steps) | cuda:0 | 4h13m | 2744 MiB |
| 389546 | cheetah dryrun (100 steps, CPU) | cpu | 1h45m | 552 MiB |

注意：015b 配置写的 `cuda:0` 但实际挂在 GPU 1 上（2744 MiB 在 GPU 1）。两个实验共享 GPU 0，015b 可能被分配到 GPU 1。

---

## 015b (frozen_dt_emb) — 当前 step ~68K / 105K (65%)

### Eval Return 轨迹
| Step | eval_return |
|------|-------------|
| 5K | 31.0 |
| 15K | **167.9** |
| 25K | 171.8 |
| 35K | **201.6** ← peak |
| 45K | 122.3 ↓ |
| 55K | 105.8 ↓ |
| 65K | 160.3 ↑ partial recovery |

### 关键 metrics @ 65K
- **actor_loss**: -0.0023 — 接近零，持续恶化趋势 (5K: -0.109 → 15K: -0.222 → 35K: -0.014 → 55K: -0.003 → 65K: -0.002)
- **actor_entropy**: -5.12 — 持续下降（策略坍缩）
- **value_mean**: 59.0
- **gate_dt_mean**: 2.0, gate_dt_2_frac = 1.0, empirical_entropy = 0.0 — **gate 完全冻结在 dt=2，从未变化过**
- **fps**: 3.05

### 诊断
- 35K 后 eval_return 崩溃到 ~106-122，65K 有部分回升到 160 但仍远低于 35K peak (201.6)
- actor_loss 趋零 + entropy 持续下降 = 策略探索不足/坍缩
- Gate 完全冻死（frozen_dt_emb 设计如此），不产生任何自适应行为
- 无 checkpoint 文件

---

## 009d (baseline_walker_s0) — 当前 step ~80K / 500K (16%)

### Eval Return 轨迹
| Step | eval_return |
|------|-------------|
| 5K | 35.0 |
| 8K | 36.8 |
| 18K | 126.2 |
| 28K | 183.7 |
| 38K | 264.0 |
| 48K | 293.2 |
| 58K | 325.5 |
| 68K | **402.2** ← peak |
| 78K | **81.0** ↓↓ 崩溃 |

### 诊断
- 68K 前持续上升，非常健康
- **78K 暴跌到 81**（从 402 跌 80%），这是严重异常
- train_return @ 80K 仍有高分 episodes（220-253），也有低分（157），说明表现不稳定
- 目标 500K 还很远，需关注 78K 崩溃是否能自动恢复

---

## 总结

1. **015b**: 65% 进度，eval 在 45K-55K 崩溃后 65K 部分回升(160)，但 actor_loss→0 和 entropy 下降是根本问题。预计还需 ~3h 到 105K
2. **009d**: 16% 进度，68K 达到 402 peak 后 78K 暴跌到 81——需要观察下一个 eval 点(88K)是否回升，如果持续低位可能需要干预
3. **PID 389546** 是个 cheetah dryrun 测试进程（100 steps, CPU），可以清理

---
