# analysis dose response 10pct 5seed stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dose-response-10pct-5seed-stats_20260515T221749_result.json`
- **Structured JSON:** [`3f2c58a38bacfa5f4abf.json`](../../sessions/3f/3f2c58a38bacfa5f4abf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 10% Dose-Response 统计结果

### 描述统计
| 条件 | Mean | SD |
|------|------|----|
| Vanilla | 67.2% | 3.9 |
| TaxEI 10% | 61.3% | 8.1 |
| Random 10% | 63.8% | 5.4 |

### 两两对比 — 全部不显著

| 对比 | Δ | paired-t p | Welch p | Bootstrap 95% CI | Cohen's d |
|------|---|-----------|---------|-------------------|-----------|
| Vanilla vs TaxEI-10% | +6.0pp | **0.249** | 0.192 | [−0.8, 14.4] | 0.60 (medium) |
| Vanilla vs Random-10% | +3.4pp | **0.296** | 0.291 | [−1.7, 7.7] | 0.54 (medium) |
| TaxEI-10% vs Random-10% | −2.6pp | **0.577** | 0.578 | [−10.2, 4.2] | −0.27 (small) |

CI 均跨零，无显著差异。

### 方差检验
- **Levene's test** (三组): F=1.41, p=0.281 — 方差无显著差异
- **F-test** (TaxEI-10% SD=8.15 vs Random-10% SD=5.44): F=2.24, p=0.453 — 不显著

TaxEI 10% 的 SD（8.15）是 Vanilla（3.85）的 2 倍，但样本量不足以达到统计显著。

### Dose-Response 趋势
两种注入方式均呈**单调递减**：

| 条件 | 0% → 10% → 100% | d(0→10) | d(0→100) |
|------|------------------|---------|----------|
| TaxEI | 67.2 → 61.3 → 58.3 | 0.60 | **1.12** |
| Random | 67.2 → 63.8 → 58.3 | 0.54 | 0.73 |

- **10% vs full-dose 无显著差异**: TaxEI p=0.664, Random p=0.377
- 10% 剂量的效果约为 full-dose 的 2/3（TaxEI: 6.0pp vs 9.0pp），但 n=5 下无法区分

### Power Analysis
| 对比 | observed d | Power (n=5) | n for 80% power |
|------|-----------|-------------|-----------------|
| Vanilla vs TaxEI-10% | 0.60 | **18.2%** | **24 seeds** |
| Vanilla vs Random-10% | 0.54 | 15.4% | 30 seeds |
| TaxEI-10% vs Random-10% | 0.27 | 7.6% | 109 seeds |
| 10% vs full (TaxEI) | 0.21 | 6.6% | 181 seeds |
| 10% vs full (Random) | 0.44 | 12.1% | 42 seeds |

### 关键结论

1. **10% 剂量下无统计显著差异**，但 effect size 为 medium（d≈0.5–0.6），方向与 full-dose 一致
2. **Dose-response 单调**：两种注入方式的性能均随剂量递增而单调下降（0% > 10% > 100%）
3. **10% 与 100% 之间无法区分**（p>0.37），说明 10% 剂量已产生可观效果，额外 90% 的注入边际收益有限
4. **n=5 严重 underpowered**：最大 power 仅 18.2%，检测 medium effect 需要约 24–30 seeds

---
