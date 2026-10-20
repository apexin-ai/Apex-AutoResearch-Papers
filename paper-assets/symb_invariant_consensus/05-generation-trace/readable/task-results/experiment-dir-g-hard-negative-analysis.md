# experiment dir g hard negative analysis

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-g-hard-negative-analysis_20260520T155439_result.json`
- **Structured JSON:** [`e4823895f772d10346a1.json`](../../sessions/e4/e4823895f772d10346a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成，结果清晰。核心发现：

**四类分布**: both_correct=109, sica_only=12, sc_only=2, both_wrong=81

**both_wrong 最关键的 pattern**:
- **64% (52/81)** 是 gt=False/True 但 SICA 和 SC 都预测 Unknown → 模型倾向"拿不准就说 Unknown"，对需要确定推理的题系统性回避
- gt=False→Unknown 占 32 题（最大单一错误模式），gt=True→Unknown 占 20 题
- 反向的 gt=Unknown 但预测 False/True 占 18 题

**Error Taxonomy**:
| 类别 | 数量 | 特征 |
|------|------|------|
| moderate_error | 34 | 中等共识，泛化推理失败 |
| confident_systematic_error | 24 | 12条trace高度一致+SICA/SC同意，但都错→系统性误推理 |
| ambiguous_reasoning | 13 | trace共识<50%，模型根本不确定 |
| borderline_sica | 6 | SICA margin极小（<10），走向错的一边 |
| insufficient_reasoning | 4 | 低共识+少constraints，pipeline抽取失败 |

**关键 insight**:
- **Gold label skew**: both_wrong 中 False 占 43% vs both_correct 中仅 21% → 模型对"False"判断能力最弱
- both_wrong 中 Unknown 仅 23% vs both_correct 中 42% → 真正该判 Unknown 的题反而容易做对
- Constraint 密度在 both_wrong 反而略高（41.9 vs 37.1）→ 问题不在 constraint 数量而在质量
- confident_systematic_error (24题) 是最值得深挖的：模型高度自信地推出了错误结论

输出文件：
- `/root/symb_invariant_consensus/results/dir_g_hard_negative_analysis/analysis.json` (81KB)
- `/root/symb_invariant_consensus/results/dir_g_hard_negative_analysis/analysis_report.md` (8KB)

---
