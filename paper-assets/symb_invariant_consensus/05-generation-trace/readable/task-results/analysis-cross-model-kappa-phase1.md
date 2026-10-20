# analysis cross model kappa phase1

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-model-kappa-phase1_20260520T060602_result.json`
- **Structured JSON:** [`657de160855eca1e7703.json`](../../sessions/65/657de160855eca1e7703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果汇总：

## 跨模型 Fleiss' κ 分析结果 (Variable-K, FOLIO-204, N=204)

| 组合 | Nom_K | κ | Eff-K | SC Acc |
|---|---|---|---|---|
| Mistral-only (K=4) | 4 | 0.515 | 1.52 | 61.3% |
| LLaMA-only (K=4) | 4 | 0.441 | 1.68 | 62.3% |
| Qwen-only (K=4) | 4 | 0.639 | 1.37 | 74.5% |
| Mistral-only (K=12) | 12 | 0.519 | 1.76 | 54.4% |
| LLaMA-only (K=12) | 12 | 0.471 | 1.92 | 64.7% |
| Qwen-only (K=12) | 12 | 0.649 | 1.47 | 76.0% |
| Mistral+LLaMA (K=8) | 8 | 0.410 | 2.02 | 60.8% |
| Mistral+Qwen (K=8) | 8 | 0.462 | 1.87 | 72.1% |
| LLaMA+Qwen (K=8) | 8 | 0.459 | 1.88 | 74.0% |
| **3-Model Mix (K=12)** | **12** | **0.422** | **2.11** | **74.5%** |

### 关键发现

- **κ 降低 16.5%**: 跨模型 κ 平均 0.444 vs 同模型 κ 平均 0.532 (K=4)
- **Effective-K 增益 26.3%**: 跨模型 1.92 vs 同模型 1.52
- **3-Model Mix Eff-K = 2.11**: 12 条 traces 等效于 2.11 条独立样本（同模型 K=12 最高仅 1.92）
- 跨模型 SC accuracy 普遍优于等 K 的同模型 SC

### 验证
- κ_within(LLaMA, K=4) = 0.441 ≈ 预期 0.41 ✓
- κ_within(Qwen, K=12) = 0.649 ≈ 预期 0.66 ✓  
- κ_within(Mistral, K=12) = 0.519 > 预期 0.44（差异原因：variable-K 方法用 P_i 加权而非简单平均，Mistral 空答案率约 17%）

结果已保存至服务器 `/root/symb_invariant_consensus/results/cross_model_kappa/cross_kappa_results.json` 和本地 artifact。

---
