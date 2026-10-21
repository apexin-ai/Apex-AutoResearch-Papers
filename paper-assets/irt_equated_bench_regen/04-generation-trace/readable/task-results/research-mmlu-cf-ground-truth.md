# research mmlu cf ground truth

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_mmlu_cf_ground_truth_20260520T203721_result.json`
- **Structured JSON:** [`89d8090ace1c8d49c705.json`](../../sessions/89/89d8090ace1c8d49c705.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个产出文件全部就绪：

**核心发现**：

1. **MMLU-CF 不可用作 ground truth** — 它是全新构建的数据集，不是 MMLU 的修改版，没有 item-level 映射。

2. **主要 ground truth 来源**: Li et al. (EMNLP 2024 Findings) 的 Contamination_Detector，基于 Bing + Common Crawl web overlap 检测：
   - 9,229 items 有标注（覆盖 METABENCH 12,508 items 的 73.8%）
   - clean: 5,584 (60.5%)，input_and_label: 3,043 (33.0%)，input_only: 602 (6.5%)
   - 已映射到 METABENCH item_id 格式（如 `abstract_algebra.1`）

3. **替代来源**: Hidayat et al. n-gram 检测（46.6% 污染率）、Meta Llama 2 报告（16% 污染率）、Zhu et al. MinKProb 检测

**产出文件** (`artifacts/`):
- `mmlu_cf_ground_truth.csv` — 12,508 items 的 item-level 标签（9,229 有标注）
- `mmlu_cf_analysis.md` — 完整调研报告
- `mmlu_cf_analysis.json` — 机器可读摘要

**主要局限**: Web overlap ≠ training data contamination。这是 proxy ground truth，不是精确标签。适合作为 DIF 验证的初步基准。

---
