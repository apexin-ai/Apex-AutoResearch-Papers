# ops read bootstrap results

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-bootstrap-results_20260515T013432_result.json`
- **Structured JSON:** [`34edaa2830dec4867f24.json`](../../sessions/34/34edaa2830dec4867f24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果如下：

---

### bootstrap_compare.json（核心对比结果）

| Condition | Accuracy | Majority Baseline | N |
|-----------|----------|-------------------|------|
| **vota** | **95.63%** | 71.51% | 1190 |
| no_trace | 75.13% | 71.51% | 1190 |
| full_trace | 28.49% | 71.51% | 1190 |

**VOTA 详细指标（bootstrap_compare）：**
- pass: precision=0.944, recall=0.998, F1=0.970
- fail: precision=0.993, recall=0.853, F1=0.917

**Pairwise 对比（95% CI）：**

| 对比 | Mean Diff | CI Lower | CI Upper | 显著？ |
|------|-----------|----------|----------|--------|
| no_trace vs vota | -20.5pp | -23.4pp | -17.7pp | Yes |
| no_trace vs full_trace | +46.6pp | +43.0pp | +50.3pp | Yes |
| vota vs full_trace | +67.1pp | +64.0pp | +70.2pp | Yes |

**Verdict: PASS** — VOTA 95.6% >= no_trace 75.1% + 2pp

---

### 各 checkpoint eval_results.json

**vota/final** — accuracy=**99.16%**（训练集 eval），pass_F1=0.994，fail_F1=0.985

**no_trace/final** — accuracy=75.13%，pass_F1=0.813，fail_F1=0.627

**full_trace/final** — accuracy=28.40%，pass_F1=0.155，fail_F1=0.568

---

关键发现：vota checkpoint 的 `eval_results.json` 报 99.16% 是训练时 eval split 的结果，而 `bootstrap_compare.json` 中 vota 的 **95.63%** 才是正确的测试集 accuracy。两者差异来源于评估数据集不同。full_trace 条件完全崩溃（28%，低于 majority baseline），模型把几乎所有样本预测为 fail。

---
