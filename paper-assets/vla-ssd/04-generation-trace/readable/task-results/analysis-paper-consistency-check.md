# analysis paper consistency check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_consistency_check_20260518T192717_result.json`
- **Structured JSON:** [`f191f32a46858c76f787.json`](../../sessions/f1/f191f32a46858c76f787.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心发现：

**🔴 高优先级 — 数值不匹配 9 处**
- **L1 heads 24→25**: 系统性错误，出现 4 次 (introduction, experiments×2, discussion)。Registry 记录 `l1_heads_gt50pct.trained=25`，论文全写 24。
- **总帧数 63,228 vs 63,728**: 500 帧差异。
- **Untrained readout L8/L16**: 论文 95.5%/91.1% vs registry 98.6%/92.0%，差距显著，需确认哪组是最终数据。
- **p=0.002 vs 0.0018**: 精度损失，建议用准确值。

**🟡 中优先级 — 措辞 4 处**
- "sole" 出现 3 次、"exclusive" 出现 1 次，与 "graded distributed routing" 叙事矛盾，建议统一改为 "primary"。

**🟡 中优先级 — 5 个附录 figure 有 label 但未被引用**
- `fig:rsa_perlayer_curve`, `fig:random_subset_ablation`, `fig:ood_diagnostics`, `fig:linear_vs_mlp`, `fig:multilayer_attention`

**🟢 低优先级**
- 4 处 -ing 分词句尾 (AI 写作标志)
- 30 个编译 warnings (0 errors, 17 个 float specifier, 3 个 hyperref)
- 交叉引用和 citation 完整性良好 (0 悬空 ref, 0 缺失 cite)

报告路径: `artifacts/paper_consistency_report.md`

---
