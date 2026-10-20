# ssh mvp v2 full status

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mvp_v2_full_status_20260516T031753_result.json`
- **Structured JSON:** [`9dbcfe48115d45a202d5.json`](../../sessions/9d/9dbcfe48115d45a202d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。以下是完整汇报。

---

## 当前状态

**阶段**：Gen3 合成数据生成中（seed45 ~23%, seed140 ~24%），ETA ~1.5h

**进程**：正常运行。pipeline 从 tmux `mvp_collapse_decoupling` 启动，`run_pipeline.py --seeds 42,137 --start_gen 1`。两张 GPU 都在用（cuda:0 + cuda:1 各 ~10.6GB / 97.9GB）。

**已完成**：Gen0 信号 → Gen1 训练 → Gen1 信号 → Gen2 训练 → Gen2 信号 → Gen3 合成生成中

---

## 每代完整 Metrics 表

| Metric | Gen0 seed42 | Gen0 seed137 | Gen1 seed42 | Gen1 seed137 | Gen2 seed42 | Gen2 seed137 |
|--------|------------|-------------|------------|-------------|------------|-------------|
| **entropy_mean** | 3.1564 | 3.1564 | 3.0437 | 3.0472 | 3.0770 | 3.0795 |
| entropy_std | 0.4432 | 0.4432 | 0.4513 | 0.4521 | 0.4670 | 0.4663 |
| **loss_mean** | 3.1565 | 3.1565 | 3.1118 | 3.1115 | 3.1064 | 3.1063 |
| loss_std | 0.5186 | 0.5186 | 0.5208 | 0.5209 | 0.5205 | 0.5207 |
| **spectral_rank_mean** | 163.72 | 163.72 | 165.00 | 164.80 | 160.92 | 160.93 |
| spectral_rank_std | 8.65 | 8.65 | 8.93 | 8.93 | 8.93 | 8.98 |
| **σ_spectral_rank** | 4.42 | 4.42 | 4.68 | 4.68 | 4.47 | 4.43 |
| **distinct_1** | 0.0387 | 0.0386 | 0.0382 | 0.0384 | 0.0384 | 0.0387 |
| **distinct_2** | 0.3412 | 0.3414 | 0.3385 | 0.3399 | 0.3395 | 0.3421 |
| **distinct_3** | 0.6871 | 0.6870 | 0.6793 | 0.6817 | 0.6767 | 0.6813 |

---

## ρ 值（重点）

| Correlation | Gen0 | Gen1 | Gen2 | Δ(Gen0→1) | Δ(Gen1→2) |
|-------------|------|------|------|-----------|-----------|
| **ρ_loss_entropy (seed42)** | 0.9292 | 0.9118 | **0.9125** | -0.0174 | **+0.0007** |
| **ρ_loss_entropy (seed137)** | 0.9292 | 0.9119 | **0.9127** | -0.0173 | **+0.0008** |
| **ρ_loss_spectral (seed42)** | -0.211 | -0.205 | **-0.2384** | +0.006 | **-0.0334** |
| **ρ_loss_spectral (seed137)** | -0.211 | -0.2036 | **-0.2303** | +0.0074 | **-0.0267** |

**关键发现**：
- **ρ_loss_entropy**：Gen0→Gen1 下降 ~0.017（decoupling 方向），但 Gen1→Gen2 **微弱回升** +0.0007/0.0008，几乎持平。decoupling 趋势在 Gen2 **停滞/反弹**。
- **ρ_loss_spectral**：Gen0→Gen1 略减弱（绝对值变小），但 Gen1→Gen2 **绝对值显著增大**（从 -0.205 → -0.238），方向反转——spectral rank 与 loss 的耦合在 Gen2 反而**加强**了。
- spectral_rank_mean 在 Gen2 大幅下降（165→161），与 Gen0→Gen1 的上升趋势反转。

---

## Bootstrap 分析（仅 Gen0→Gen1）

**ρ_loss_entropy**：
- Δρ = -0.0174 (seed42), -0.0173 (seed137)
- Effect size: **-5.8 / -5.77**（非常大）
- 95% CI 不重叠（Gen0: [0.924, 0.934], Gen1: [0.906, 0.918]）
- **但** permutation test p = 0.496（不显著，因为只有 2 个 gen 点做 slope 检验）

**ρ_loss_spectral**：
- Δρ = +0.006 (seed42), +0.007 (seed137)
- Effect size: 0.41 / 0.50（小到中等）
- permutation test p = 1.0（不显著）

---

## 总结

- Gen0–Gen2 已完成，Gen3 合成数据生成中，预计 ~1.5h 后完成，之后还需 Gen3 训练 + Gen3 信号采集
- **correlation_analysis.json 和 bootstrap_analysis.json 只包含 Gen0→Gen1 数据**，Gen2 的 ρ 值已经在 signal 文件里但还没被纳入汇总分析
- Gen2 的 ρ 变化模式**不符合单调 decoupling 假说**：entropy-loss 相关性停止下降，spectral-loss 相关性反而增强
- 进程正常运行中，无报错

---
