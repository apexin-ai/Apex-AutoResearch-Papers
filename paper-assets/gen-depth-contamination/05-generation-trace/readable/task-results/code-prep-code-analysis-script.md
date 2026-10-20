# code prep code analysis script

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-code-analysis-script_20260519T025101_result.json`
- **Structured JSON:** [`89fbba5eff66b5ceee1a.json`](../../sessions/89/89fbba5eff66b5ceee1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证通过：

- **Qwen2.5-1.5B**: K\*=2, 0v1 AUC=0.9388 ✓
- 其他三个模型的实验目录为空，脚本正确输出 `[WARN]` 并在表格中填 TBD ✓
- 1v2 的 AUC (0.7382) 被正确 underline（K\* boundary）✓
- LaTeX 表格和 JSON 已写入 `artifacts/` 目录

脚本位置：`/root/autodl-tmp/gen-depth-contamination/scripts/analyze_code_crossmodel.py`

功能：
1. 读取 4 个模型的 `results/exp_code_*/pairwise_auc.json`
2. 计算 5-fold CV 的 95% CI（mean ± 1.96 * std / sqrt(5)）
3. 确定 K\*（max k where AUC > 0.60）
4. 输出 LaTeX 表格到 `artifacts/code_crossmodel_table.tex`，JSON 到 `artifacts/code_crossmodel_results.json`
5. 缺失实验 gracefully skip，表格填 TBD

实验完成后重新运行 `python3 scripts/analyze_code_crossmodel.py` 即可更新表格。

---
