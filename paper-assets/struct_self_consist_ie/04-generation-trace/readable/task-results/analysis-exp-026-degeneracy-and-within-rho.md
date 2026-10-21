# analysis exp 026 degeneracy and within rho

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_026_degeneracy_and_within_rho_20260517T100239_result.json`
- **Structured JSON:** [`f337c22219e49cf45382.json`](../../sessions/f3/f337c22219e49cf45382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 任务 1: Degeneracy 定义修正

之前脚本用的是 **KeySet exact match**（所有 8 samples 的 `frozenset((text, type))` 完全相同），不是正确定义。

正确定义 **Constant F1 gold-filtered** 的修正值：

| T | Old (KeySet) | New (Constant F1) | Delta |
|---|---|---|---|
| T=0.5 | 0.3285 | **0.4026** | +0.074 |
| T=0.8 | 0.1960 | **0.2722** | +0.076 |
| T=1.0 | 0.1270 | **0.1758** | +0.049 |
| T=1.2 | 0.0799 | **0.1248** | +0.045 |

新定义下 degeneracy 更高（预期：不同 entity 集合可以产生相同 F1）。Gold-filtered 总数=529（排除了 22 个无 gold entity 的 instances）。趋势不变：低温 degeneracy 更严重。

### 任务 2: Within-instance ρ(LP, F1)

| T | mean ρ | median ρ | std | valid% |
|---|--------|----------|-----|--------|
| T=0.5 | 0.1306 | 0.2182 | 0.5422 | 59.7% |
| T=0.8 | 0.1701 | 0.2635 | 0.4951 | 72.8% |
| T=1.0 | 0.1449 | 0.2474 | 0.5000 | 82.4% |
| T=1.2 | **0.2245** | **0.3152** | 0.4554 | 87.5% |

解读：
- LP-F1 alignment 整体偏弱（mean ρ ≈ 0.13–0.22），方差极大（std ~0.5）
- T=1.2 alignment 最好（mean=0.22, median=0.32），因为高温下 LP 分布更分散，discriminability 增强
- Valid fraction 随温度升高：低温下太多 instance 的 F1 或 LP 方差为 0（degenerate），无法计算 ρ
- Median 显著高于 mean，说明分布左偏（部分 instance 有强负相关拉低均值）

JSON 已保存到 `artifacts/exp_026_T_ablation/within_instance_rho.json`。

---
