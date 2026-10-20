# research paper update prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_update_prep_20260515T013953_result.json`
- **Structured JSON:** [`147b37fde61278b3c5d9.json`](../../sessions/14/147b37fde61278b3c5d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清单已保存到 `artifacts/paper_update_checklist.md`。

汇总：

**P0（10项）**：abstract/intro/results/conclusion/discussion 中的核心数字——样本量 50→500、DeepSeek Δ 四个值（0.39→14.59）、d_z（0.44→0.80）、severity gradient G（69×→274×）、crossover 数字、3 张主表（aggregate-ii、main-results、cohens-d）全部需替换。

**P1（10项）**：Qwen cross-model 段落+表格、permutation test 表格+段落、crossover reversal magnitudes、appendix 所有数字、4 张图重新生成。

**P2（4项条件分支）**：QW s015 CI 是否仍跨零（决定 onset threshold 叙事）、QW imp-vs-rand 是否终于显著（D058）、QW rand s030 是否仍 negligible（影响"7/8 FAIL"叙事）、24 个 `\placeholder{}` 待填充。

**P3（5项一致性）**：LLaMA 仍 n=50、c4 机制分析仍 n=30——需在 abstract/methodology/limitations 显式声明不同 n；appendix_results.tex 是冗余文件建议清理；C8 限定语和 C5b future_work 标注已合格无需改动。

---
