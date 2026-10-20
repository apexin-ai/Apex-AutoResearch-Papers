# ssh pipeline status gen2

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_pipeline_status_gen2_20260516T024324_result.json`
- **Structured JSON:** [`c5a88f2314e4683a1639.json`](../../sessions/c5/c5a88f2314e4683a1639.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pipeline Status Report

### 当前阶段：Gen2 信号计算中 (2/3 Distinct-n)

**Pipeline 进度**：

| 阶段 | 状态 |
|------|------|
| Gen0 signals | ✅ |
| Gen1 training + signals | ✅ |
| Gen0→Gen1 分析 + bootstrap + 绘图 | ✅ |
| Gen2 training (6103 steps) | ✅ checkpoints saved |
| Gen2 compute_signals | 🔄 **运行中** |
| Gen3 | ❌ 未开始 |

**Gen2 信号计算进度**（两个进程并行 on cuda:0）：
- seed42: per-example signals 100%, distinct-n ~46% (143/313)
- seed137: per-example signals 100%, distinct-n ~17% (52/313)

### GPU 利用率
| GPU | Util | VRAM |
|-----|------|------|
| cuda:0 | 39% | 2525 MiB |
| cuda:1 | 33% | 2525 MiB |

### Gen0→Gen1 Metrics (已完成分析)

| Metric | seed42 | seed137 |
|--------|--------|---------|
| ρ(loss,entropy) Gen0 | 0.9292 | 0.9292 |
| ρ(loss,entropy) Gen1 | 0.9118 | 0.9119 |
| **Δρ entropy** | **-0.0174** | **-0.0173** |
| ρ(loss,spectral) Gen0 | -0.211 | -0.211 |
| ρ(loss,spectral) Gen1 | -0.205 | -0.2036 |
| **Δρ spectral** | **+0.006** | **+0.0074** |
| entropy_mean Gen0→1 | 3.156→3.044 | 3.156→3.047 |
| spectral_rank_mean Gen0→1 | 163.7→165.0 | 163.7→164.8 |

**Bootstrap 显著性**：
- entropy Δρ: effect size = -5.8 (强), 但 permutation p = 0.50（仅2代数据点不显著）
- spectral Δρ: effect size = 0.41-0.50, p = 1.0（无变化）

**Gen0→Gen1 Verdict**: FAIL（两个 seed 均未通过）

### 预估

Gen2 distinct-n 按当前速率（~1s/item）预计 **30-50 分钟内完成**，之后 pipeline 会自动进入 Gen2 分析 → Gen3 训练。

---
