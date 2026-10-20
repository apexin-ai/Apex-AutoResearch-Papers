# urgent re selection reconcile

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_re_selection_reconcile_20260515T034532_result.json`
- **Structured JSON:** [`d9f7badfff98c8d52709.json`](../../sessions/d9/d9f7badfff98c8d52709.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已出。关键发现整理如下：

---

## RE Selection F1 Reconciliation 结果

### 数据概况
- 总实例数: 551
- 有 gold relations 的实例: **397**
- gold relations 为空的实例: **154**（这些实例的 greedy 和 logprob selection F1 均为 0.000）

### 三子集对比

| 子集 | n | Greedy F1 (mean) | Logprob Sel F1 (mean) | Δ |
|------|---|---|---|---|
| A: 全集 | 551 | 0.2913 | 0.2845 | -0.0068 |
| **B: Gold-nonempty** | **397** | **0.4042** | **0.3948** | **-0.0094** |
| C: Greedy-F1>0 | 238 | 0.6743 | 0.5995 | -0.0748 |

### Micro-averaged F1（论文报表级别）

| 子集 | Greedy micro-F1 | Logprob micro-F1 | Δ |
|------|---|---|---|
| A: 全集 | 0.4289 | **0.3941** | -0.0349 |
| B: Gold-nonempty | 0.4436 | **0.4156** | -0.0280 |
| C: Greedy-F1>0 | 0.6229 | 0.5498 | -0.0731 |

### 0.395 vs 0.410 根因

从 raw data 重算，最接近的两个值是：
- **0.3948** ≈ 0.395 → gold-nonempty 子集的 **mean per-instance** logprob selection F1
- **0.4156** ≈ 0.416 → gold-nonempty 子集的 **micro-averaged** logprob selection F1

两个数来自**同一子集，不同的 F1 聚合方式**（instance-mean vs micro-average）。两种算法下 logprob selection **都输给 greedy**（greedy mean=0.4042, micro=0.4436），不存在 logprob 赢 greedy 的场景。

如果论文中某处报出 0.410 且声称赢了 greedy，可能的来源：
1. 使用了不同子集（如漏掉了部分 gold-empty instance 导致 n 偏移）
2. F1 聚合方式混用（一处用 mean per-instance，另一处用 micro-averaged）
3. greedy baseline 本身也因子集不同而变化（mean=0.404 vs micro=0.444）

### 5-Signal 完整结果表（Gold-nonempty, n=397, mean per-instance F1）

| Signal | Selection F1 | Δ vs Greedy | Wins | Losses | Ties |
|--------|-------------|-------------|------|--------|------|
| SJ-Best | 0.3855 | -0.0188 | 29 | 49 | 319 |
| FK-Best | 0.3872 | -0.0171 | 34 | 50 | 313 |
| EM-Best | 0.3727 | -0.0316 | 27 | 62 | 308 |
| **Logprob-Best** | **0.3948** | **-0.0094** | **36** | **59** | **302** |
| Voting-Best | 0.3660 | -0.0382 | 39 | 65 | 293 |

### Logprob vs Greedy 详细统计（Gold-nonempty）
- Wins: 36, Losses: 59, Ties: 302
- 所有 5 个 signal 的 selection 都**低于** greedy，logprob 是损失最小的

**结论：论文中两组值的矛盾根因是 F1 聚合方式不一致。从 raw data 重算，无论用哪种聚合，logprob selection 都不优于 greedy。建议统一用 mean per-instance F1 = 0.395（与 greedy 0.404 对比）。**

---
