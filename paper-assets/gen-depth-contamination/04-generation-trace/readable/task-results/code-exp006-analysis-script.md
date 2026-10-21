# code exp006 analysis script

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006-analysis-script_20260514T060214_result.json`
- **Structured JSON:** [`5b9cb95275f97c542b9a.json`](../../sessions/5b/5b9cb95275f97c542b9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已写好：

**`scripts/exp006_analyze_results.py`** — 完整分析脚本：
- 扫描 `outputs/exp006/*/eval_results.json`，解析实际格式（`scores.mmlu["acc,none"]`, `scores.hellaswag["acc_norm,none"]`）
- 处理 `graduated_a{alpha}_s{seed}` 命名的 alpha sweep，自动选最优 α
- 输出 `summary.json` + `summary.csv` + `latex_table.tex`（含主表和 α 敏感性表）
- Paired t-test + Wilcoxon signed-rank，覆盖所有策略对
- 相对 base_model 和 no-filter 的改进量
- 缺失 run 报 warning，不崩溃

**`scripts/exp006_fill_discussion.py`** — 讨论段落生成：
- 读 `summary.json`，根据 graduated vs binary 的对比结果自动选择三种叙述模板（positive/neutral/negative）
- Negative result 只输出注释，不生成正文，触发手动审查
- 输出到 `artifacts/exp006_results/discussion_graduated_paragraph.tex`
- 不直接修改 `discussion.tex`

与实际数据的差异说明：任务描述中的 `runs/exp006_graduated_filtering/` 路径和 `graduated-soft/hard/curriculum` 策略名与服务器实际不符。实际是 `outputs/exp006/`，6 个策略为 `no-filter, binary-ours, binary-drayson, graduated, surprisal, dsir`，graduated 通过 α∈{0.1,0.3,0.5,0.7,0.9} sweep 实现。脚本按实际格式编写。

---
