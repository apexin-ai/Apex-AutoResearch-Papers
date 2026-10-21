# ops plan 013 check and analyze

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan_013_check_and_analyze_20260515T235059_result.json`
- **Structured JSON:** [`8903abee0e909e497f68.json`](../../sessions/89/8903abee0e909e497f68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 完成状态
40/40 runs 全部成功（8 conditions × 5 seeds），两个 GPU 进程均正常退出。

### 2. 统计分析结果

| Condition | PPL (mean±std) | Δ vs unfiltered | p-value | Cohen's d | Sig? | n_samples |
|-----------|---------------|-----------------|---------|-----------|------|-----------|
| **unfiltered** | 15.78±0.07 | (baseline) | — | — | — | 10000 |
| rf_strict | 15.81±0.06 | -0.03 | 0.607 | -0.53 | No | 2496 |
| rf_moderate | 15.76±0.06 | +0.02 | 0.492 | 0.33 | No | 4940 |
| rf_soft | 15.73±0.04 | +0.04 | 0.407 | 0.79 | No | 4422 |
| oracle_strict | 15.88±0.13 | -0.10 | 0.216 | -1.00 | No | 2500 |
| oracle_moderate | 15.81±0.10 | -0.03 | 0.485 | -0.38 | No | ~5000 |
| random_strict | **16.24±0.17** | **-0.46** | **0.013** | -3.67 | **Yes** | 2496 |
| random_moderate | **16.00±0.09** | **-0.22** | **0.028** | -2.81 | **Yes** | ~5000 |

### 3. 结论：**Negative**

- **RF filtering vs unfiltered**：所有 RF 条件均无统计显著差异（p > 0.4）。rf_soft 用 44% 数据达到与全量相当的 PPL（d=0.79 是大效应量，但 n=5 seeds 不足以达到显著性）。
- **Random filtering 显著更差**：random_strict (p=0.013) 和 random_moderate (p=0.028) 均显著差于 unfiltered，确认随机删除数据有害。
- **Oracle 也不帮忙**：即使用真实递归深度做 oracle filtering，PPL 也不优于 unfiltered，说明按递归深度筛选数据这条路本身对下游 PPL 的影响有限。
- RF 的价值在于"不伤害"（不像 random），但不显著提升。

### 4. Registry 更新
- conclusion → `negative`
- metrics → 8 conditions 完整指标
- status → `DONE`
- artifact 已注册 (`art_20260515_3ef4f0`)

---
