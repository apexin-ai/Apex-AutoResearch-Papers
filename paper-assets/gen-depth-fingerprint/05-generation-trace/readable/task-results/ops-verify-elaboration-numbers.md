# ops verify elaboration numbers

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-elaboration-numbers_20260516T130654_result.json`
- **Structured JSON:** [`4ab1effc500263e71f73.json`](../../sessions/4a/4ab1effc500263e71f73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report.

---

## 报告：elaboration/rewriting 数字来源验证

### 来源文件

论文中 elaboration/rewriting 相关数字**全部来自 `data/prompt_type_results.json`**，而非 plan006。

### 逐条验证

| 论文数字 | 出处位置 | 来源文件中的值 | 匹配？ |
|----------|---------|--------------|--------|
| elaboration F1 = 0.730 | limitations.tex:15, discussion.tex:30 | `prompt_type_results.json` → `per_prompt_cv_f1.elaboration.mean = 0.73` | ✓ |
| rewriting F1 = 0.737 | limitations.tex:15 | `prompt_type_results.json` → `per_prompt_cv_f1.inspired_rewriting.mean = 0.7368` → 四舍五入 0.737 | ✓ |
| continuation F1 = 0.781 | limitations.tex:15, discussion.tex:30 | `prompt_type_results.json` → `per_prompt_cv_f1.continuation.mean = 0.7806` → 四舍五入 0.781 | ✓ |
| LOPTO F1 = 0.753 | discussion.tex:30 | `prompt_type_results.json` → `lopto_f1.avg = 0.7525` → 四舍五入 0.753 | ✓ |
| elaboration retains 98.6% | discussion.tex:29 | `prompt_type_results.json` → `depth_decay.elaboration.retention_d4_pct = 98.6` | ✓ |
| continuation 16.9% loss | discussion.tex:29 | `prompt_type_results.json` → `depth_decay.continuation.retention_d4_pct = 83.1` → 100-83.1=16.9 | ✓ |
| elaboration drift 1.4% | appendix_prompt_type.tex:7 | `prompt_type_results.json` → 100-98.6=1.4 | ✓ |
| rewriting drift 6.1% | appendix_prompt_type.tex:7 | `prompt_type_results.json` → 100-93.9=6.1 | ✓ |
| binary F1 0.671 vs 0.749 | limitations.tex:15 | `plan006_paraphrastic_comparison.json` → paraphrase 0.6711, continuation 0.7491 | ✓（这组来自 plan006）|

### plan006 vs prompt_type_results 的关系

- **`data/prompt_type_results.json`**：prompt type 实验（continuation / elaboration / inspired_rewriting，3 种 prompt 类型），是 elaboration/rewriting 相关数字的**权威来源**
- **`results/plan006_paraphrastic_comparison.json`**：paraphrastic comparison 实验（paraphrase vs continuation），只提供 binary F1（0.671 vs 0.749）和 paraphrase 相关数字

两个文件中 continuation 的数值略有差异（plan006 的 CV F1=0.7876 vs prompt_type 的 0.7806；retention 82.6% vs 83.1%），因为它们是独立实验运行，使用不同的数据子集。论文统一使用 prompt_type_results 中的 continuation 数字（0.781, 83.1%）。

### 注意事项

appendix_prompt_type.tex:7 写的是 "16.9% **per depth step**"，但实际是 4 步的总损失（不是每步损失率）。rewriting 6.1% 和 elaboration 1.4% 同理。措辞可能需要修正为 "over the full 4-step chain" 或 "total retention loss"。

---
