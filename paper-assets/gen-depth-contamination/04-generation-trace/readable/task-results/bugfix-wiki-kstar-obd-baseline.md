# bugfix wiki kstar obd baseline

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_wiki-kstar-obd-baseline_20260519T215703_result.json`
- **Structured JSON:** [`863d1b123b1e3c7c5b4f.json`](../../sessions/86/863d1b123b1e3c7c5b4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务全部完成。

---

## 报告

### 任务 2：K* 修正

所有5个 wiki JSON 的 kstar 原为 0-indexed，已全部修正为 1-indexed：

| Config | 修正前 | 修正后 |
|--------|--------|--------|
| wiki_pythia | 2 | **3** |
| wiki_olmo | 0 | **1** |
| wiki_qwen7b | 2 | **3** |
| wiki_llama8b | 2 | **3** |
| wiki_mistral7b | 2 | **3** |

### 任务 3：OBD baseline bug

**根因**：`results/exp_wiki_olmo/` 的全部5个文件（pairwise_auc.json、feature_importance.json、jsd.json、ordinal_results.json、summary.txt）与 `results/exp_wiki_pythia/` 完全一致（md5 相同）。是整个目录被复制过去的，OBD pipeline 从未在 wiki_olmo 数据上运行过。注意：`data/exp_wiki_olmo/features.csv` 与 `data/exp_wiki_pythia/features.csv` md5 不同，数据源本身是正确的。

**修复**：调用 `run_pipeline.run_analysis()` 在 wiki_olmo 的 features.csv 上重新运行了 OBD 分析。

**修复后 wiki_olmo OBD baseline**：
- 0v1: 0.9961 → **0.9933**
- 1v2: 0.6193 → **0.4983**（从 >0.6 变为 ~随机）
- 2v3: 0.5498 → **0.5041**
- 3v4: 0.5231 → **0.4986**
- 4v5: 0.5141 → **0.5089**

OLMo 的 OBD baseline 现在显示 depth 1+ 几乎不可区分（AUC ≈ 0.5），与 DeBERTa 的 kstar=1 一致。summary.json 已同步更新。

---
