# analyze plan014 downstream nli s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan014-downstream-nli-s42_20260514T042736_result.json`
- **Structured JSON:** [`f71f0b5e0897185d913a.json`](../../sessions/f7/f71f0b5e0897185d913a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验成功完成（EXIT_CODE=0）。以下是完整结果：

## plan014 Downstream NLI 结果

### 配置
- Checkpoint: plan001_exec_only_s42
- 100 samples, K=8 generations, T=0.7
- Solver: prover9
- 推理耗时 408.8s，评估 13.6s

### 核心指标

| 指标 | 值 |
|------|-----|
| Overall accuracy | **34.1%** |
| Proved rate | 732/800 (91.5%) |
| Parse errors | 0 |

### 按 gold label 分解 — 严重 true bias

| Gold Label | Accuracy | 分布 |
|------------|----------|------|
| true | **91.2%** (248/272) | 34% of data |
| unknown | 7.6% (25/328) | 41% of data |
| false | **0.0%** (0/200) | 25% of data |

模型几乎总是预测 "true"（entailment），完全无法预测 "false"。

### ISR 与 NLI 准确率的关系

**ISR bucket:**

| Bucket | μ(ISR) | Accuracy | n |
|--------|--------|----------|---|
| high | 0.94 | 75.0% | 12 |
| mid | 0.48 | 37.7% | 69 |
| low | 0.08 | 32.7% | 651 |

Bucket 层面有单调趋势，但 high bucket 仅 12 个样本。

**ISR quartile（等分）:**

| Quartile | Range | Accuracy | n |
|----------|-------|----------|---|
| Q1 | [0.00, 0.00] | 30.6% | 183 |
| Q2 | [0.00, 0.11] | **43.2%** | 183 |
| Q3 | [0.11, 0.17] | 28.4% | 183 |
| Q4 | [0.17, 1.00] | 33.3% | 183 |

Quartile 层面**非单调**（Q2 最高，Q3 最低），无清晰趋势。

### Best-of-N 选择

| 策略 | Accuracy |
|------|----------|
| oracle | 44.0% |
| isr_best | 35.0% |
| prove_first | 35.0% |
| random | 34.1% |

ISR-best 仅比 random 高 +0.9 pp，与 prove_first 持平。

### 统计检验 — 全部不显著

| Test | Statistic | p-value |
|------|-----------|---------|
| Spearman ρ(ISR, correct) | **-0.049** | 0.187 |
| Mann-Whitney Q4>Q1 | U=17202 | 0.288 |
| Bootstrap BoN (ISR vs random) | diff=0.009 | 95% CI [-0.015, +0.037] |

### 结论

**ISR 作为 downstream NLI quality proxy 的结果是阴性的。** Spearman ρ 接近零且不显著，Best-of-N ISR 选择无实质提升，quartile 分析非单调。主要原因：模型存在严重的 "true" prediction bias（false accuracy = 0%），NLI 任务本身的 accuracy 天花板很低（overall 34.1%），ISR 的区分度在此基础上没有空间发挥。

---
