# research literature gap fill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-gap-fill_20260514T090847_result.json`
- **Structured JSON:** [`c522d7737adf45f31fa9.json`](../../sessions/c5/c522d7737adf45f31fa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献搜索完成。产出写入 `artifacts/paper_draft/literature_gaps.md`。

**找到 14 篇文献，其中 11 篇需新增到 references.bib：**

**Gap 1 — Exposure-ability collinearity (P0, 3篇)**
- San Martín et al. 2015 — 固定效应 3PL 不可识别性的形式化证明，直接支撑 gamma 在高 collinearity 下被低估的理论解释
- Mislevy 1987 — person covariate 与 ability 共线时，辅助信息反而引入 confounding
- Wainer, Bradlow & Wang 2007 — testlet 局部依赖导致参数相关性膨胀，类比 contamination 诱导的局部依赖

**Gap 2 — Measurement error attenuation (P0, 6篇)**
- Carroll et al. 2006 — 非线性模型测量误差的权威教材
- Fuller 1987 — errors-in-variables 经典，reliability ratio 衰减公式
- Stefanski & Carroll 1985 — logistic 回归中协变量测量误差导致渐近偏差（直接对应 ICC logistic 形式）
- Battauz & Bellio 2011 — IRT ability estimates 作为协变量时的异方差测量误差建模（精确对应我们的场景）
- Westfall & Yarkoni 2016 — 测量误差下残差混淆，Type I error 趋近 100%
- Jerzak & Jessee 2026 — latent predictor 的衰减偏差，标准校正方法本身也有偏

**Gap 3 — IRT power/information (P1, 2篇):** Embretson & Reise 2000, Thissen & Wainer 2001

**Gap 4 — 4PL identifiability (P2, 3篇):** Barton & Lord 1981 (原始 4PL), Culpepper 2016 (Bayesian 4PL), Liao et al. 2012 (4PL 鲁棒性)

每篇均附完整 BibTeX entry 和与 ContamCal 的关联说明，可直接复制到 `references.bib`。

---
