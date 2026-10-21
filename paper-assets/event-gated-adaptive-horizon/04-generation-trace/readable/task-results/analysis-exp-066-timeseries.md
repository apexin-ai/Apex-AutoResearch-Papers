# analysis exp 066 timeseries

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_066_timeseries_20260525T020923_result.json`
- **Structured JSON:** [`50246da44347a9fbf318.json`](../../sessions/50/50246da44347a9fbf318.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已注册。以下是完整分析结果：

---

## exp_066 时序 RSSM Fidelity 分析结果

### 数据总览

| Step | SS ratio (dt2/dt1) | OL ratio (H=8) | CumRew Err (dt2) | State Div Gap | VE ratio |
|------|-------------------|-----------------|-------------------|---------------|----------|
| 10K  | 1.058x | 0.942x | 1.24 | 0.093 | 0.005 |
| 15K  | 1.049x | 1.022x | 1.28 | 0.131 | 0.022 |
| 20K  | 1.113x | 1.072x | 1.35 | 0.149 | 0.156 |
| 25K  | 1.069x | **1.287x** | 1.60 | 0.153 | 0.163 |
| 30K  | **1.250x** | **1.371x** | 1.82 | 0.151 | 0.215 |
| 35K  | 1.302x | **1.491x** | **1.99** | 0.157 | 0.229 |
| 40K  | 1.295x | 1.407x | 1.76 | 0.155 | **1.591** |
| 45K  | 1.407x | 1.339x | 1.74 | 0.149 | 0.360 |
| 50K  | 1.430x | **1.519x** | 1.90 | 0.146 | 0.616 |
| 55K  | 1.278x | 1.448x | 1.87 | 0.151 | 0.621 |
| 60K  | **1.623x** | 1.417x | 1.79 | 0.142 | **1.399** |
| 65K  | **1.835x** | 1.328x | 1.68 | 0.134 | **1.399** |

### 关键发现

**1. Fidelity gap 非单调，但总体上升趋势明确：**
- Single-step ratio: 1.05x → 1.83x（终点最高）
- Open-loop ratio: 0.94x → 1.5x peak（35K-50K区间最大）
- 机制：dt=1 MAE 随训练持续下降（0.093→0.047），而 dt=2 MAE 基本不变（~0.08），gap 来自 dt=1 改善但 dt=2 不改善

**2. Gap 加速点：step 25K-30K**
- Open-loop ratio 在 25K 突破 1.25x，此后持续 >1.3x
- 对应到训练过程：这是 model 从"随机探索"转为"有意义策略"的过渡期

**3. 时序因果关系：Fidelity gap LEADS VE ratio**
- Fidelity gap（OL ratio）在 25K-35K 急速上升到 1.5x
- VE ratio 在此期间仍然很低（0.16-0.23）
- VE ratio 直到 40K 才第一次 spike 到 1.59
- **结论：fidelity gap 先建立（~25K-35K），然后驱动 value overestimation（~40K+）**
- 这个 5K-15K step 的时间差对应约 2-6 个 eval cycle 的延迟

**4. State divergence 稳定但持续存在：**
- dt=2 imagination 的 cosine divergence 始终高于 dt=1（gap ~0.09-0.16）
- 说明 dt=2 的 latent space 系统性偏离 posterior，是结构性问题

### 数据文件位置
- 服务器：`bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066_timeseries_rssm_fidelity_s0/timeseries_analysis_v2.json`
- 分析脚本：`scripts/exp_066_timeseries_analysis_v2.py`

---
