# paper number audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_number-audit_20260514T132335_result.json`
- **Structured JSON:** [`d53e36f6a1db33de7aa6.json`](../../sessions/d5/d53e36f6a1db33de7aa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/_project/report/number_audit_final.md`。

**发现 3 个不一致：**

1. **❌ Cohen's d_z 数据源冲突**（高优先级）：`cohens_d_6point_paired_dz.txt` 和 `cohens_d_6point_paired_info.txt` 给出的 d_z 值完全不同（如 DS s015: 0.442 vs 0.607）。论文使用前者，与 `cross_model_analysis_summary.json` 一致，但后者引用了 `regen` 脚本，可能是更新版本。需确认哪组为正。

2. **❌ 百分位/p_Bonf 算术矛盾**（中优先级，results.tex:115）：99.68th percentile 对应 raw p=0.0032，Bonferroni 校正后应为 0.0128 而非 0.0032。或者若 p_Bonf=0.0032 正确（raw p=0.0008），百分位应为 99.92th。不影响显著性结论。

3. **❌ 熵变区间记号反写**（低优先级，analysis.tex:43）：`[-0.040, -0.047]` 应为 `[-0.047, -0.040]`。

其余约 95 个数字/声明全部通过验证，跨文件一致性良好。6 类数值因原始数据不在提供的文件中无法交叉验证（置换检验详情、bootstrap CI、判别崩溃指标等）。

---
