# prepare seed comparison pipeline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_seed_comparison_pipeline_20260516T001825_result.json`
- **Structured JSON:** [`12a0ea8d5bd49623c6ad.json`](../../sessions/12/12a0ea8d5bd49623c6ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Denominator 修正完毕，显示 3/4 和 2/4。

## 报告

### (1) 脚本状态：就绪 ✓

`/root/autodl-tmp/scripts/seed_comparison.py` 已存在并可正常运行。功能完整：
- 自动读取各 eval 目录的 metrics.json
- 提取 rel_f1, evi_f1, EDCR
- 运行 paired t-test + Cohen's d + 95% CI
- 输出 markdown 表格和 JSON
- 支持 `--watch N` 模式自动轮询

已更新：添加了 s45 支持（CED → `rsft_s45`, flat-NLI → `rsft_flat_nli_s45`），denominator 从 3 改为 4。

### (2) 已有 eval 结果目录

| Method | Seed | Eval Dir | 状态 |
|--------|------|----------|------|
| CED | s42 | `rsft_r2b` | ✅ |
| CED | s43 | `rsft_s43` | ✅ |
| CED | s44 | `rsft_s44` | ✅ |
| CED | s45 | `rsft_s45` | ❌ 不存在 |
| flat-NLI | s42 | `rsft_flat_nli` | ✅ |
| flat-NLI | s43 | `rsft_flat_nli_s43_reeval` | ✅ |
| flat-NLI | s44 | `rsft_flat_nli_s44` | ❌ 空目录 |
| flat-NLI | s45 | `rsft_flat_nli_s45` | ❌ 空目录 |

### (3) CED s42/s43/s44 实际 rel_f1 值

| Seed | rel_f1 | evi_f1 | EDCR |
|------|--------|--------|------|
| s42 | **0.4493** | 0.8128 | 0.6609 |
| s43 | **0.4683** | 0.8156 | 0.6388 |
| s44 | **0.4655** | 0.8087 | 0.6350 |
| mean | 0.4610 ± 0.0102 | 0.8124 ± 0.0035 | 0.6449 ± 0.0140 |

当前可配对 2 seeds (s42, s43)，paired t-test 已可运行但 N=2 统计不可靠。还需等待 flat-NLI s44/s45 和 CED s45 的 eval 完成才能做有效的 4-seed paired comparison。

---
