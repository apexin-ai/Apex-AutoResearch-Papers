# analysis gold set deep

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gold-set-deep_20260516T050354_result.json`
- **Structured JSON:** [`585b07814d127fcf99c4.json`](../../sessions/58/585b07814d127fcf99c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

## Gold Set Deep Analysis Results

**(a) Stagnation Prevalence**
| Set | N | Stagnation | Progress |
|-----|---|-----------|----------|
| Gold (conf≥2) | 505 | 133 (26.3%) | 372 (73.7%) |
| Silver (all) | 205,461 | 47,040 (22.9%) | 158,421 (77.1%) |
| Silver (conf≥2) | 58,777 | 14,472 (24.6%) | 44,305 (75.4%) |

Gold set 略微富集 stagnation（26.3% vs 22.9%），分布与 silver 一致。

**(b) Silver-Gold Agreement by Confidence Strata**
| Stratum | N | Agreement | Cohen's κ |
|---------|---|-----------|-----------|
| conf=1 | 282 | 0.762 | 0.312 |
| conf=2 | 163 | **0.963** | **0.909** |
| conf=3 | 47 | 0.851 | 0.695 |
| conf≥2 | 210 | 0.938 | 0.865 |

conf=2 一致率最高（96.3%），conf=3 的 7 个 disagreement 可能是 3 LFs 系统性偏差的 edge cases。

**(c) Trajectory Position**
| Position | N | Agreement | Stag % |
|----------|---|-----------|--------|
| First half | 232 | 0.810 | 23.7% |
| Second half | 260 | 0.862 | 28.5% |
| Early 1/3 | 144 | 0.764 | 19.4% |
| Mid 1/3 | 176 | 0.864 | 32.4% |
| Late 1/3 | 172 | 0.872 | 25.6% |

Stagnation 在 mid-trajectory 最集中（32.4%）。Agreement 在 late windows 更高。

**(d) Bootstrap CI (10,000 resamples)**
- MV macro-F1: **0.798 [0.758, 0.837]** (N=492, width=0.079)
- GB macro-F1: 0.721 [0.663, 0.775] (N=279 subset with trajectory data)

注：既有 canonical eval 的 GB 全量结果为 0.839（N=491），CI 更窄。

**(e) Inter-annotator κ (Bootstrap CI)**
- Fleiss' κ (3-cat, 3 LFs): **−0.017 [−0.058, 0.023]** — LFs 有意设计为 diverse/complementary，低 agreement 符合预期
- Cohen's κ (MV vs gold): **0.596 [0.513, 0.673]** — moderate-to-substantial agreement

脚本 + 结果保存在 `artifacts/gold_deep_analysis.json`，已注册 artifact `art_20260516_e9d19e`。

---
