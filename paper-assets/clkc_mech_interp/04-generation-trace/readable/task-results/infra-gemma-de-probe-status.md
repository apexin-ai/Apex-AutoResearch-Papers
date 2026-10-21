# infra gemma de probe status

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gemma-de-probe-status_20260522T173654_result.json`
- **Structured JSON:** [`8626aef461ce661a408f.json`](../../sessions/86/8626aef461ce661a408f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. Gemma Probe n=2000 — 已完成

| 方向 | peak_layer | peak_acc | 95% CI |
|------|-----------|----------|--------|
| en→en | layer_24 | 0.7617 | [0.731, 0.791] |
| zh→zh | layer_24 | 0.7097 | [0.674, 0.744] |
| en→zh | layer_22 | 0.6290 | [0.573, 0.680] |
| zh→en | layer_24 | 0.7023 | [0.627, 0.750] |

**Asymmetry (peak layer):**
- `asymmetry_diff` = 0.0662
- `asymmetry_ci` = [0.019, 0.1108]
- `asymmetry_p_value` = 0.006 (显著)
- `n_seeds` = 2000

### 2. DE Probe Training — 仍在运行

进度 856/2000（~43%），输出文件尚未生成。

---
