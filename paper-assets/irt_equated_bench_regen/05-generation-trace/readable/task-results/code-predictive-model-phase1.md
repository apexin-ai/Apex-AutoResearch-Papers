# code predictive model phase1

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_predictive_model_phase1_20260522T091330_result.json`
- **Structured JSON:** [`d2295c4b8e674810b9c8.json`](../../sessions/d2/d2295c4b8e674810b9c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 1 完成。输出摘要：

**数据探测**：所有 6 个数据源均可用，包括 MetaBench 57 个 MMLU subject 的 prompts CSV（含完整题目文本），12508 items 文本特征覆盖率 100%。

**特征提取结果**：`artifacts/predictive_model/` 下 3 个文件——

| 文件 | 内容 |
|------|------|
| `features.csv` | 12508 items × 36 列 |
| `target.csv` | 12508 items × dif_c (0/1) |
| `feature_inventory.md` | 特征清单 + 来源 |

**36 个特征分三类**：
- **统计特征 (11)**：difficulty（整体/ref/foc/other）、difficulty_change、item_variance、discrimination_ptbis（整体/ref/foc）、discrimination_change
- **结构特征 (12)**：subject、subject_c_pct/b_pct、subject_mean_diff_change/n_items/mean_difficulty、difficulty_vs_subject、alpha_mh/delta_mh/se/p_value、li_label/li_contamination_type
- **文本特征 (13)**：question_length/word_count、option_count/length_mean/length_std、has_negation、prompt_total_length、qtype_factual/reasoning/statement_eval/other

**Target**：31.3% positive rate（3918 ETS-C / 8590 non-C），中等不平衡。

---
