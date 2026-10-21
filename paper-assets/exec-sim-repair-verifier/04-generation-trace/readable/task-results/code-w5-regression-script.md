# code w5 regression script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w5-regression-script_20260520T070509_result.json`
- **Structured JSON:** [`d676e6aae2d1acd14f7c.json`](../../sessions/d6/d676e6aae2d1acd14f7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 正常。脚本已写到本地和服务器 `/home/sonny/exec-sim-repair-verifier/w5_mixed_effects_v2.py`。

相比 v1 的改进：
- **参数化输入**：`--eval_dirs` 逗号分隔目录，`--data_dir` 加载 mutation_type 元数据，`--output_dir` 指定输出
- **自动推断**：从目录名提取 formulation (cls/cwm/traj)、model (qwen/deepseek)、seed (sNNN)、complexity (repo/func)
- **两个模型**：cross-complexity (`formulation * complexity/mutation_type`) 和 cross-model (`formulation * model`)，均用 MixedLM + `(1|problem_id)`
- **统计输出**：fixed effects 系数表 + joint Wald χ² ANOVA + 经验 odds ratio（bootstrap 95% CI）
- **保存格式**：JSON (`w5_mixed_effects_results.json`) + LaTeX 表格片段 (`w5_latex_tables.tex`)

---
