# analyze gen gpt2m a100 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_gen_gpt2m_a100_s43_fp32_20260519T151034_result.json`
- **Structured JSON:** [`00af016191ad201ed2ee.json`](../../sessions/00/00af016191ad201ed2ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。

---

## gen_gpt2m_a100_s43_fp32 分析结果

### 结论：**SUCCESS** — GPT-2m 跨 seed canary lead-lag 稳健

### 核心指标

| 指标 | s43 (fp32) | s42 (fp16) | 一致性 |
|------|-----------|-----------|--------|
| **PermG fwd** | **8/8** | 5/8 | s43 更强 |
| **PermG rev** | 5/8 | — | — |
| **DiffXCorr fwd** | 8/8 | — | — |
| **K≥3 robust** | 4/8 | — | — |
| **K≥4 robust** | 1/8 | 6/8 | s43 较弱 |
| **d1_drift** | **-24.9%** | -28.9% | 方向一致，幅度相近 |
| **Threshold Onset** | 0/8 | — | T=11 样本不足 |
| **TY Granger** | 4/8 | — | — |

### 指标轨迹 (gen_0 → gen_10)

| 指标 | gen_0 | gen_10 | 变化 |
|------|-------|--------|------|
| token_entropy | 3.571 | 0.587 | -83.6% |
| distinct_1 | 0.103 | 0.077 | -24.9% |
| distinct_2 | 0.551 | 0.370 | -32.9% |
| distinct_3 | 0.857 | 0.628 | -26.7% |
| perplexity | 32.6 | 15,024 | +460x |
| ece | 0.011 | 0.517 | +46x |
| effective_rank | 2.37 | 33.34 | +14x |

### 与 s42 对比分析

- **PermG 信号更强**：s43 fwd 8/8 > s42 的 5/8，canary→diversity Granger 因果在所有 8 对上显著
- **K≥4 consensus 较弱**：1/8 vs s42 的 6/8。根因是 Threshold Onset 0/8（canary onset 未触发 3σ 阈值，T=11 样本限制），不代表信号缺失
- **d1_drift 方向一致**：-24.9% vs -28.9%，magnitude 接近，confirm diversity 退化是跨 seed 稳定现象
- **fp32 vs fp16**：s43 fp32 满足 D079 合规要求，精度差异未改变定性结论

### 磁盘 & GPU 状态

**GPU (westd-19828)**：
- cuda:0 — **空闲** (0 MiB / 97,887 MiB)
- cuda:1 — **占用** (64,417 MiB / 97,887 MiB)

**磁盘**：
- `/root/autodl-tmp`：224G / 250G (**90% 已用**，剩余 27G)
- 最大目录：`generalize/` 120G, `alpha_sweep/` 20G, `intervention/` 6.2G, `gen_wiki_gpt2m_a100_s43/` 2.8G

**OPT-1.3B 缓存**：未缓存（HF cache 和 local models 均不存在）

---
