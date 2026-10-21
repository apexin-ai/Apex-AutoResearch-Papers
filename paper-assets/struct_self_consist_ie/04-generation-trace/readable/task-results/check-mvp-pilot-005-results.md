# check mvp pilot 005 results

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mvp_pilot_005_results_20260514T094607_result.json`
- **Structured JSON:** [`20ba7cf0ffbc5a4b9d36.json`](../../sessions/20/20ba7cf0ffbc5a4b9d36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成 (DONE/negative)。

---

## mvp_pilot_005 结果汇总

**Verdict: FAIL** — RE full ρ_sj = 0.234 < 0.30 硬截止线

### NER 指标

| 指标 | pilot_005 (T=0.7) | pilot_004 (T=1.0) | 变化 |
|------|-------|-------|------|
| greedy_f1 | 0.662 | 0.667 | -0.005 |
| oracle_f1 | 0.759 | 0.776 | -0.017 |
| headroom | 9.7pp | 10.9pp | -1.2pp |
| ρ_sj (full) | **0.388** | 0.383 | +0.005 |
| ρ_fk (full) | 0.321 | 0.259 | +0.062 |
| ρ_sj (cond) | **0.387** | 0.376 | +0.011 |
| SJ > FK | ✅ both | ✅ both | — |
| pct_zero | 11.2% | 12.2% | -1.0pp |
| soft_jaccard_mean | 0.776 | 0.701 | +0.075 |

### RE 指标

| 指标 | pilot_005 (T=0.7) | pilot_004 (T=1.0) | 变化 |
|------|-------|-------|------|
| greedy_f1 | 0.422 | 0.421 | +0.001 |
| oracle_f1 | 0.553 | 0.588 | -0.035 |
| headroom | 13.1pp | 16.7pp | **-3.6pp** |
| ρ_sj (full) | **0.234** | 0.244 | **-0.010 ↓** |
| ρ_fk (full) | 0.184 | 0.278 | -0.094 |
| ρ_sj (cond) | **0.372** | 0.316 | **+0.056 ↑** |
| ρ_fk (cond) | 0.253 | 0.307 | -0.054 |
| SJ > FK | ✅ both | ❌full/✅cond | **改善** |
| pct_zero | 42.4% | 44.3% | -1.9pp |
| soft_jaccard_mean | 0.687 | 0.611 | +0.076 |

### 关键发现

1. **RE full ρ_sj = 0.234 < 0.30**：Director 硬截止线未通过，甚至比 pilot_004 (0.244) 更差
2. **RE cond ρ_sj 显著提升**：0.316 → 0.372 (+0.056)，T=0.7 在非零子集上有效
3. **RE zero rate 几乎没变**：44.3% → 42.4%，降温未能实质性解决零值问题
4. **SJ > FK 全面恢复**：T=0.7 下 RE full set 也 SJ > FK（pilot_004 full set 是 FK > SJ）
5. **NER 稳定**：ρ_sj 略升至 0.388，T=0.7 对 NER 无负面影响
6. **Oracle headroom 收窄**：T=0.7 降低了多样性，RE oracle F1 从 0.588 降到 0.553

---
