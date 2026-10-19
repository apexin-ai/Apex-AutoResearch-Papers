# code bootstrap asymmetry

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_asymmetry_20260521T210858_result.json`
- **Structured JSON:** [`fec2075c5ca46406df41.json`](../../sessions/fe/fec2075c5ca46406df41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型都跑完了。结果如下：

## Bootstrap Asymmetry 结果

| | Llama-3.1 | Qwen-3 |
|---|---|---|
| ZH→EN bal_acc | 0.7647 (L15) | 0.6905 (L18) |
| EN→ZH bal_acc | 0.6985 (L5) | 0.6429 (L23) |
| Observed diff | +0.0662 | +0.0476 |
| Bootstrap mean diff | +0.0670 | +0.0455 |
| **95% CI** | **[-0.0095, 0.1392]** | **[-0.0471, 0.1382]** |
| **CI excludes 0** | **No** | **No** |

## 结论

**两个模型的不对称 claim 均未获得统计显著性支撑。** 虽然 ZH→EN 方向在两个模型上都 point estimate 更高（Llama +6.6pp, Qwen +4.8pp），但 95% CI 均包含 0。当前 test set 规模（Llama 272, Qwen 168）下，这一差异无法与随机波动区分开。

如果要 claim 不对称性，需要更大的 test set 或更强的效应量。

---
