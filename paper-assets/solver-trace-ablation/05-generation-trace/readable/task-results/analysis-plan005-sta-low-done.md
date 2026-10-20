# analysis plan005 sta low done

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan005-sta-low-done_20260513T235649_result.json`
- **Structured JSON:** [`4f06a93634d7492546df.json`](../../sessions/4f/4f06a93634d7492546df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整分析报告。

---

## plan005-sta-low-s42 分析报告

### 1. 完整 Metrics 表

| 指标 | 值 |
|------|-----|
| 总步数 | 500 |
| 训练时长 | ~71 min |
| parse_rate | 1.0000 |
| **overall prove_rate** | **0.5657** |
| **overall ISR** | **0.1682** |
| **last-50 prove_rate** | **0.7700** |
| **last-50 ISR** | **0.2559** |
| **last-100 prove_rate** | **0.7725** |
| **last-100 ISR** | **0.2299** |
| last-100 loss | 0.022752 |
| last-100 ISR/PR ratio | 0.298 |
| last-100 ISR < PR 步数 | 99/100 |
| rolling-10 PR ≥ 0.8 首达 | step 178 |
| rolling-10 PR ≥ 0.9 首达 | step 439 |
| max rolling-10 PR | 0.9375 |
| max rolling-10 ISR | 0.3282 |

**分窗口变化：**

| 窗口 | prove_rate | ISR |
|------|-----------|-----|
| 1-50 | 0.178 | 0.091 |
| 51-100 | 0.178 | 0.084 |
| 101-200 | 0.506 | 0.146 |
| 201-300 | 0.671 | 0.179 |
| 301-400 | 0.701 | 0.198 |
| 401-500 | 0.773 | 0.230 |

### 2. 与 plan001-r2 (exec-only 500步) 对比

| 指标 | plan005 (α=0.9 β=0.1) | plan001-r2 (exec-only) | Δ |
|------|----------------------|---------------------|---|
| last-100 prove_rate | 0.7725 | **0.8650** | **-10.7%** |
| last-100 ISR | 0.2299 | **0.8612** | **-73.3%** |
| last-100 ISR/PR ratio | 0.298 | 0.996 | -0.698 |
| last-100 ISR<PR count | 99/100 | 2/100 | — |
| rolling-10 PR≥0.8 | step 178 | step 142 | +36 步更慢 |
| rolling-10 PR≥0.9 | step 439 | step 269 | +170 步更慢 |
| last-100 loss | 0.0228 | 0.0055 | 4.2× 更高 |

### 3. 结论: **NEGATIVE**

即使 STA 权重降到 0.1（exec 占 0.9），依然有严重负面影响：

1. **prove_rate 下降 10.7%** (0.7725 vs 0.865) — STA 信号拖慢了 exec 任务的学习
2. **ISR 灾难性崩塌 73.3%** (0.2299 vs 0.861) — 这是核心发现。模型学会了 prove，但 solver trace 质量极差。exec-only 的 ISR/PR ≈ 1.0（trace 自然好），加 STA 后 ISR/PR = 0.30（trace 被严重破坏）
3. **收敛更慢** — PR≥0.9 需要 439 步 vs exec-only 的 269 步，慢 63%
4. **loss 4× 更高** — STA 产生了 noisy gradients

与 50/50 STA 对比：

| 配置 | prove_rate | ISR | 结论 |
|------|-----------|-----|------|
| exec-only (plan001-r2) | 0.865 | 0.861 | baseline |
| STA 50/50 (r5, 100步) | 0.10 | 0.043 | 灾难退化 |
| **STA 0.1 (plan005, 500步)** | **0.773** | **0.230** | **严重退化** |

退化程度随 STA 权重降低而减轻，但 0.1 仍远不够低。STA reward 的 penalty effect 在当前实现下是 **系统性的**，不是权重调参能解决的问题。

### 4. 建议下一步

STA 作为 additive reward 的方向已被两组实验否定（0.5 和 0.1 权重）。继续降权重（如 0.01）意义不大——要么效果为零，要么仍然是 penalty。

应转向替代方案：
- **Curriculum 方案 (plan002)**：先 exec-only 训练到收敛（~300步），再切换到 exec+STA fine-tune。这避免了早期 STA 干扰 exec 学习
- **STA 作为 filter 而非 reward**：不用 STA 计算 reward，而是用 STA 筛选好的 traces 做 rejection sampling
- **Post-hoc STA**：先用 exec-only 训练，然后用 STA 评分对 checkpoint 做 best-of-N 选择

---
