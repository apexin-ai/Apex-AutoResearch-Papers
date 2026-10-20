# research literature linkage exp004

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-linkage-exp004_20260518T102211_result.json`
- **Structured JSON:** [`b29ff90ba9b0d17094f2.json`](../../sessions/b2/b29ff90ba9b0d17094f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，写报告。

---

## 文献调研报告：Spectral vs Diversity Metrics Divergence

### A) 文献中是否已有关于 spectral vs diversity divergence 的讨论

**No — 没有论文直接报告过 spectral metrics（effective rank, SLV）在 real-data mixing 下保持健康而 diversity metrics（distinct-n）同时崩溃的现象。**

最接近的是：

- **SIGMA (gu2026sigma, 2601.03385)**：报告了 distinct-2 和 hashed n-gram HHI 作为"operational sanity check"，但将其定位为 spectral bounds 的**验证手段**，暗含假设两者相关。论文未研究 data mixing 场景，也未报告两类指标的 divergence。
- **"Where does output diversity collapse in post-training?" (arXiv 2604.16027, Apr 2026)**：发现 post-training 中 semantic diversity 与 lexical diversity 可以反向运动（semantic diversity 从 0.54 降到 0.20，而 lexical diversity 从 0.23 升到 0.80）。概念上相关，但场景完全不同（RLHF post-training，非 recursive synthetic training）。

### B) 与我们发现的对比

- **Gerstgrasser et al. (2404.01413)**：证明 data accumulation 能稳定 test error，但**未报告 diversity metrics**。我们的 exp_004 补充了关键一环：固定 r=0.5 mixing 虽然保住了 spectral health，但 distinct-4 暴跌 86%，说明 test error 稳定 ≠ output diversity 稳定。
- **Dohmatob et al. (2410.04840)**：纯理论分析，用 operator-valued free probability 推导 test error scaling，**无 diversity 讨论**。
- **Briesch et al. (2311.16822)**：报告了 self-consuming loop 中 diversity 下降，但**无 spectral 分析**。正好是我们发现的反面视角。

### C) 是否可作为额外 contribution

**是的。** 这是一个有价值的 novel observation：

> Spectral metrics (effective rank, log determinant) can be "blind" to diversity collapse when real data mixing stabilizes the representation geometry but fails to prevent mode narrowing in output space.

这直接挑战了 SIGMA 等工作中 spectral metrics 作为 collapse 充分检测器的隐含假设。可以作为论文 Discussion 中的重要 finding，论证 spectral EWS 需要与 output-level diversity metrics 配合使用。

### D) 建议补充到 literature_map.yaml 的论文

1. **"Where does output diversity collapse in post-training?"** — arXiv 2604.16027 (Apr 2026), 研究 diversity metrics 之间的 divergence，概念上与我们的 spectral-diversity divergence 发现互补。建议加入 `synthetic_data_quality` cluster。

其余搜索未发现需要新增的直接相关论文。现有 literature_map 覆盖已较完整。

---

需要我将这个发现更新到 `literature_map.yaml` 或 `report.md` 中吗？

---
