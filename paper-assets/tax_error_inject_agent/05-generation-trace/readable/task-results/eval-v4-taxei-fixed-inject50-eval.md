# eval v4 taxei fixed inject50 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v4-taxei-fixed-inject50-eval_20260515T012509_result.json`
- **Structured JSON:** [`b8d5df7fe6527925b9b9.json`](../../sessions/b8/b8d5df7fe6527925b9b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 结果

**TaxEI 50% injection eval: 24/47 = 51.1%** (negative，低于 59% 阈值)

### Dose-response 完整曲线

| Injection Rate | Success Rate | Δ vs Baseline |
|---|---|---|
| 0% (vanilla) | 61.7% | — |
| 10% | 61.7% | 0pp |
| 25% | 48.9% | -12.8pp |
| **50%** | **51.1%** | **-10.6pp** |

### 关键发现

50% injection (51.1%) 与 25% (48.9%) 基本持平（差异仅 2.2pp，在噪声范围内）。Dose-response 曲线呈现 **阈值效应**，而非线性下降：

- 10% 以下：无损害（recovery 数据被吸收）
- 10%→25%：急剧下降 ~13pp，突破阈值
- 25%→50%：**plateau**，不再进一步恶化

这说明 clean task performance 的下降不是因为"错误样本越多越差"，而是一旦 injection 比例超过某个阈值（~15-20%），模型就开始学到 injection 带来的行为偏差，之后继续增加 injection 不会显著加剧损害。

---
