# analysis decoupling data pipeline verify

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_decoupling-data-pipeline-verify_20260520T010609_result.json`
- **Structured JSON:** [`34894b075f3b867bfc78.json`](../../sessions/34/34894b075f3b867bfc78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/paper_data/decoupling_pipeline_audit.md`。

**核心结论：**

1. **管道一致**：decoupling_data.csv 中所有数据（σ 和 Jaccard）均来自 lm-eval `--log_samples`，没有混入 `results_1.3b/logprob/` 自定义管道。

2. **轻微差异**：GDN 的 h24-1/h6-1/h3-1 存在两次 lm-eval 运行 — 第一次无 `--log_samples`（产出 root `_results.json`，用于 `summary_all_1.3b.csv` → `cross_arch_std`），第二次带 `--log_samples`（产出 JSONL，用于 Jaccard 计算）。最大差异 7/5153 = 0.14%（h6-1），对结论无影响。

3. **§4.4 可靠性**：σ trajectory 和 Jaccard trajectory 引用的数据来源一致，定性结论不受影响。

---
