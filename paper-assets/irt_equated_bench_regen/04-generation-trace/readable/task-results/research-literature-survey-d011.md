# research literature survey d011

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_survey_d011_20260520T232511_result.json`
- **Structured JSON:** [`0edca4936d965340b3a5.json`](../../sessions/0e/0edca4936d965340b3a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调查已完成，写入 `artifacts/literature_survey_d011.md` 并注册。

覆盖 19 篇文献，5 个类别：

1. **DIF 经典** (4篇): Shealy & Stout 1993 (SIBTEST), Clauser & Mazor 1998 (方法综述), Zumbo 1999 (logistic regression 框架), Holland & Wainer 1993 (教科书)
2. **IRT in NLP** (5篇): Lalor et al. 2016/2019, Vania et al. 2021, Rodriguez et al. 2021, Polo et al. 2024 (tinyBenchmarks)
3. **污染检测** (6篇): Shi et al. 2024 (Min-K%), Zhang et al. 2024 (Min-K%++), Balloccu et al. 2024, Golchin & Surdeanu 2024, Oren et al. 2024, Deng et al. 2024
4. **动态 Benchmark** (5篇): DyVal 1/2, LiveBench, MMLU-Pro, MMLU-Redux
5. **关键对标** (2篇): Growing Pains (详细技术对比表) 和 METABENCH

Growing Pains 关键发现：他们用 MIRT-2PL + Fixed Parameter Calibration 做高效评估，但**不做 DIF 分析、不检测污染**。他们在 limitations 中承认 "anchors may become contaminated over time" 但没有解决方案——这恰好是我们论文的核心贡献点。

---
