# research plan 036 growing pains lookup

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_036_growing_pains_lookup_20260521T160331_result.json`
- **Structured JSON:** [`e26eb0e5b46e75786011.json`](../../sessions/e2/e26eb0e5b46e75786011.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/plan_036_growing_pains/plan_036_report.md`。

## 结论

**"Growing Pains"** 论文（Habba et al., arXiv 2604.12843, 2026.04）的 FPC 是 **Fixed Parameter Calibration**，不是 Focal Point Contamination。论文用 IRT anchor items 做高效 benchmark 校准，**不涉及污染检测**，也没有公开的 contamination flag list。因此无法执行 Jaccard overlap 分析。

与我们工作的关联：
- 共享 IRT 基础，验证了 IRT 在 400+ 模型、57 个 MMLU subjects 上的可行性
- 论文在 Limitations 中承认 anchor items 可能随时间被污染——直接支持我们 DIF-based contamination detection 的必要性论点
- 适合在 Related Work 中引用

---
