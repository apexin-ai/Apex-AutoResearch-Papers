# infra plan007 status check

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan007-status-check_20260520T204547_result.json`
- **Structured JSON:** [`3a4f11ffbb44bebc30ae.json`](../../sessions/3a/3a4f11ffbb44bebc30ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量运行完成，210 条记录全齐。以下是完整结果。

---

## 1. 进程状态

**已正常完成。** PID 500791 已终止，42/42 combos 全部执行，总耗时 2792s (~46min)。无异常退出。

**结果文件：** `/home/sonny/causal_annot_error_attrib/artifacts/plan007/correction_guidance_results.json` (87.9 KB, 210 records)

---

## 2. Bias Reduction % (7 topo × 5 method，均值 over 6 C structures)

| Topology | naive_plugin | dsl | **ppi** | mcsimex | mla |
|---|---|---|---|---|---|
| confounding | -0.0% | 49.8% | **99.3%** | 35.9% | 0.0% |
| mediation | -0.0% | 70.3% | **98.8%** | 42.4% | 0.0% |
| collider | 0.0% | -89.2% | **97.0%** | 37.1% | -0.0% |
| exposure | -45.6% | -59.6% | **98.8%** | -3.8% | -89.9% |
| mbias | 0.0% | -768.0% | **63.7%** | 25.7% | 0.0% |
| iv | -40.9% | -187.4% | **99.5%** | 64.7% | -59.2% |
| frontdoor | -53.5% | -29.2% | **99.3%** | -55.7% | -112.5% |
| **GRAND MEAN** | -20.0% | -144.8% | **93.8%** | 20.9% | -37.4% |

## 3. Coverage 95% (均值 over 6 C structures)

| Topology | naive_plugin | dsl | **ppi** | mcsimex | mla |
|---|---|---|---|---|---|
| confounding | 0.0% | 6.1% | **98.6%** | 0.8% | 0.0% |
| mediation | 2.0% | 27.6% | **96.8%** | 22.2% | 2.0% |
| collider | 8.3% | 1.3% | **99.2%** | 32.1% | 8.3% |
| exposure | 0.0% | 0.0% | **95.0%** | 37.4% | 0.0% |
| mbias | 92.1% | 10.8% | **98.5%** | 92.6% | 92.1% |
| iv | 0.0% | 0.0% | **94.7%** | 36.8% | 0.0% |
| frontdoor | 0.0% | 0.0% | **94.8%** | 41.1% | 0.0% |
| **GRAND MEAN** | 14.6% | 6.5% | **96.8%** | 37.6% | 14.6% |

## 4. DSL 详细分析

DSL 仅在 **confounding** 和 **mediation** 下有效（分别 49.8%、70.3%），且效果随误差严重程度递增（mild → severe 从 16.5% → 94.5%）。在其他 5 种拓扑下**系统性失败**：

- **mbias**: 灾难性恶化 -768%（最差 realistic_llm 达 -2537%）
- **iv**: -187.4%
- **collider**: -89.2%
- **exposure**: -59.6%
- **frontdoor**: -29.2%

DSL 失败不是个别 C 结构的问题，而是**拓扑结构性的**——在 collider/mbias/iv/frontdoor 下几乎所有 C 结构都恶化。

## 5. Frisch-Waugh-Lovell 验证

**验证通过。** naive_plugin 和 mla 在经典 OLS 拓扑（confounding/mediation/collider/mbias）下 bias_reduction 精确为 0.0%，确认标签噪声沿 FWL 投影不变性消除。

但在 exposure/iv/frontdoor 下，两者都**显著恶化**：
- naive_plugin: exposure -45.6%, iv -40.9%, frontdoor -53.5%
- mla: exposure -89.9%, iv -59.2%, frontdoor -112.5%

这说明 FWL 不变性**仅限于 T→Y 直接效应的 OLS 估计**，不适用于需要 2SLS / front-door 等多步骤估计量的拓扑。

## 6. PPI 弱点分析

PPI 在 40/42 scenarios 最优（win rate 95.2%），但在 **mbias** 下表现明显弱化：

| Topology | C Structure | Bias Reduction | Coverage | RMSE |
|---|---|---|---|---|
| mbias | realistic_llm | **-25.1%** | 99.0% | 0.0283 |
| mbias | mild_uniform | 62.5% | 98.3% | 0.0299 |
| mbias | near_permutation | 69.9% | 98.6% | 0.0301 |
| mbias | asymmetric | 82.9% | 98.7% | 0.0296 |
| mbias | severe_uniform | 93.3% | 98.1% | 0.0308 |
| collider | near_permutation | 92.5% | 98.6% | 0.0310 |

注意 mbias+realistic_llm 场景 PPI bias reduction 为 **-25.1%**（恶化），但 coverage 仍 99%——这意味着 PPI 的置信区间正确反映了校正后增大的不确定性，只是 bias 校正本身失效。

## 7. 关键发现总结

1. **PPI++ 全面碾压**：93.8% 平均 bias reduction、96.8% coverage，在 40/42 场景最优
2. **MC-SIMEX 次优但不稳定**：grand mean 20.9%，在 iv (64.7%) 尚可但 frontdoor (-55.7%) 崩溃
3. **DSL 拓扑敏感**：仅在 confounding/mediation 有效，其余拓扑系统性失败
4. **naive_plugin/mla 在 OLS 拓扑下 FWL 不变性成立**（bias_red ≈ 0），在 2SLS/frontdoor 拓扑下恶化
5. **mbias 是 PPI 的阿喀琉斯之踵**：6 个 C 结构中 4 个 < 95%，1 个恶化

---
