# analysis dose response 25pct 5seed stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dose-response-25pct-5seed-stats_20260515T235641_result.json`
- **Structured JSON:** [`7004f395ca168a230da4.json`](../../sessions/70/7004f395ca168a230da4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存至 `artifacts/dose_response_25pct_stats.json`。核心结果：

**描述统计**
| Condition | Mean | SD | Range |
|-----------|------|----|-------|
| Vanilla (0%) | 67.2% | 3.9 | 61.7–72.3 |
| TaxEI 25% | 52.7% | 7.6 | 46.8–63.8 |
| Random 25% | 60.0% | 8.0 | 51.1–72.3 |

**Pairwise 比较（paired t-test）**
| Comparison | Δ | p | Cohen's d | Sig? |
|------------|---|---|-----------|------|
| Vanilla vs TaxEI 25% | **14.5pp** | **0.0042** | **2.63** | **YES** |
| Vanilla vs Random 25% | 7.2pp | **0.039** | 1.36 | **YES** |
| TaxEI 25% vs Random 25% | -7.3pp | **0.029** | -1.49 | **YES** |
| TaxEI 25% vs TaxEI 10% | -8.5pp | 0.221 | -0.65 | no |
| Random 25% vs Random 10% | -3.8pp | 0.231 | -0.63 | no |

**关键发现**

1. **TaxEI 25% 显著差于 Vanilla**（p=0.004, d=2.63，极大效应量），10% 时不显著（p=0.249）—— 25% 剂量把效应放大到了统计显著。

2. **TaxEI 25% 显著差于 Random 25%**（p=0.029, d=1.49）—— 首次证明 targeted injection 比 random 更有效，10% 时无差异。

3. **Dose-response 单调递减**：TaxEI 67.2→61.3→52.7%，Random 67.2→63.8→60.0%。Page's trend test: TaxEI p=0.004, Random p=0.044。

4. **TaxEI 斜率是 Random 的 2 倍**：0.58 vs 0.29 pp/1% injection。Targeted injection 的 dose-response 更陡。

5. **Power**：Vanilla vs TaxEI 25% power=0.989（n=5 已充分）；Vanilla vs Random 25% power=0.629（需 n=7）；TaxEI vs Random 25% power=0.705（需 n=6）。

6. **Bootstrap 95% CI**：Vanilla vs TaxEI 25% = [6.54, 21.52]pp；TaxEI vs Random 25% = [-14.04, -1.28]pp（不含零，与 t-test 一致）。

---
