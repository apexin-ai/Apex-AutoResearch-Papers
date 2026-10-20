# code result analysis script

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_result_analysis_script_20260515T140418_result.json`
- **Structured JSON:** [`fcd3b971bf6ca9d219ea.json`](../../sessions/fc/fcd3b971bf6ca9d219ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。3 个已完成实例（black_1, cookiecutter_1, cookiecutter_2）的部分数据全部正确解析，所有 6 个输出模块都正常工作：

- **Per-instance table**: 3×4 格，P/F + judge 分数
- **Condition summary**: 4 条件的 test_pass_rate / avg_judge / diff_apply / tokens
- **Head-to-head**: 4 组对比的 win/tie/loss
- **Statistical tests**: sign test + wilcoxon（n<5 时正确跳过）
- **Oracle baseline**: 检测到 httpie_2 oracle pass，但该实例尚未完成所以 oracle 子表为空
- **Kill criteria C001**: 三条标准全部检测，当前均 FAIL（符合预期，数据不完整）

JSON 已保存到 `pipeline_output/phase3_v2_analysis.json`。脚本自动发现 checkpoint/oracle 文件，无需手动指定路径。等 14 实例全部跑完后直接 `python analyze_phase3_v2.py` 即可。

---
