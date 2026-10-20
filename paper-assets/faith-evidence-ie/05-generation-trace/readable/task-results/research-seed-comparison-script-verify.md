# research seed comparison script verify

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed_comparison_script_verify_20260516T034809_result.json`
- **Structured JSON:** [`c8b6bac0921263215667.json`](../../sessions/c8/c8b6bac0921263215667.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本正常工作。汇总如下：

## 脚本状态

### `seed_comparison.py` — 已修复 5 处问题

| # | 问题 | 修改 |
|---|------|------|
| 1 | `ign_f1` 不在 METRICS_KEYS，完全不读 Ign-F1 | 加入 `ign_f1` 到 METRICS_KEYS 和 METRIC_LABELS |
| 2 | METHODS 含旧协议 fallback（`rsft_r2b_maxtok1536`, `rsft_s43`, `rsft_s44`, `rsft_flat_nli` 等），paired t-test 会静默用错误数据 | 移除所有旧协议 fallback，只保留统一协议目录 |
| 3 | `load_metrics` fallback 到 `metrics.json` 时 ign_f1 无效 | fallback 到 `metrics.json` 时自动剥离 `ign_f1` 字段 |
| 4 | Per-seed 表格缺 Ign-F1 列 | 表格首列加入 CED/fNLI Ign-F1 |
| 5 | dry-run 不显示 ign_f1 | dry-run 输出增加 ign_f1 |

### `paired_ttest_analysis.py` — 不存在
功能已内置在 `seed_comparison.py` 的 `paired_ttest` + `cohens_d` + `ci_95` 中，无需单独脚本。

### 当前 eval 完成情况（统一协议）
- **已完成**: flat-NLI s44, flat-NLI s45（均读 metrics_v2.json）
- **待完成**: CED s42/s43/s44/s45, flat-NLI s42/s43（6 个 eval 进行中）

### 脚本输出内容
per-seed Ign-F1/F1/evi_f1/EDCR, mean±std, paired t-test (t, p), Cohen's d, 95% CI — 全部就绪，8 个 eval 出齐后直接 `python scripts/seed_comparison.py` 即可。

---
