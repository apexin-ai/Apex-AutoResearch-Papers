# ops check pythia retrain done

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-pythia-retrain-done_20260519T034431_result.json`
- **Structured JSON:** [`c6c11c41fbed1b8e2269.json`](../../sessions/c6/c6c11c41fbed1b8e2269.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **成功完成**，K*=7。

## 结果汇总

**模型**: Pythia-1.4B (retrain-chain protocol, LoRA r=16)
**Scorer**: Qwen2.5-1.5B
**K* = 7** (threshold AUC > 0.60, 所有 7 个 depth pair 均超阈值)

### Pairwise AUC (5-fold GroupKFold CV)

| Depth Pair | AUC (mean) | 95% CI |
|---|---|---|
| 0 vs 1 | 0.9844 | [0.9829, 0.9858] |
| 1 vs 2 | 0.9470 | [0.9418, 0.9522] |
| 2 vs 3 | 0.8891 | [0.8822, 0.8960] |
| 3 vs 4 | 0.7999 | [0.7951, 0.8047] |
| 4 vs 5 | 0.6907 | [0.6880, 0.6934] |
| 5 vs 6 | 0.6497 | [0.6429, 0.6565] |
| 6 vs 7 | 0.6340 | [0.6275, 0.6406] |

### Pairwise JSD (单调递减)

| Depth Pair | JSD |
|---|---|
| 0 vs 1 | 0.1775 |
| 1 vs 2 | 0.1286 |
| 2 vs 3 | 0.1069 |
| 3 vs 4 | 0.0643 |
| 4 vs 5 | 0.0331 |
| 5 vs 6 | 0.0271 |
| 6 vs 7 | 0.0138 |

### 关键结论

**Pythia retrain K* = 7，与 Qwen retrain K* ≥ 7 一致。** "Retrain artifacts are model-independent" 的 claim 成立：

- 两个架构不同的模型（Pythia GPT-NeoX vs Qwen）在 retrain protocol 下均达到 K*=7
- AUC 衰减曲线形态高度相似：从 ~0.98 单调下降，到 depth 7 仍 >0.63
- JSD 同样单调递减，收敛趋势一致
- 6v7 的 AUC=0.634 和 CI 下界 0.6275 均 >0.60 阈值，说明即使到 depth 7 仍有统计显著的可区分性

分析脚本 `analyze_pythia_retrain_depth7.py` 不存在，以上结果直接从 `summary.json` / `pairwise_auc.json` / `jsd.json` 提取。

---
