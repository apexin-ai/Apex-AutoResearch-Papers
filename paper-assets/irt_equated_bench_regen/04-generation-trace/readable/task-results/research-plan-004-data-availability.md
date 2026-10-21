# research plan 004 data availability

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_004_data_availability_20260521T000945_result.json`
- **Structured JSON:** [`e2e1eb29976a2f376a89.json`](../../sessions/e2/e2e1eb29976a2f376a89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。核心结论：

**METABENCH 中 GSM8K 数据完整可用** — 1,319 items × 6,702 models 的 per-item binary response matrix，可立即用于 IRT 分析。同时还有 ARC、HellaSwag、TruthfulQA、Winogrande、MMLU(57 subjects) 共 6 个 benchmark 的完整数据。

**GSM1K 题目公开但无大规模 response matrix** — HuggingFace 上有 1,205 道题，论文有 ~30-50 个模型的聚合准确率，但没有类似 METABENCH 的 per-item responses。

**推荐路线：内部交叉验证（方案 A）**，用 METABENCH 内 6 个 benchmark 互相做 cross-benchmark equating 验证，5,000+ 模型重叠，零 GPU 需求，立即可行。GSM1K 论文数据可作为辅助验证（方案 B）。

报告已写入 `artifacts/plan_004_data_availability.md` 并注册。

---
