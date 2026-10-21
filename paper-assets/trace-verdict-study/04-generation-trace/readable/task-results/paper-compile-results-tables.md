# paper compile results tables

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_results_tables_20260516T001056_result.json`
- **Structured JSON:** [`f7b8f9db49eb0d4aeb15.json`](../../sessions/f7/f7b8f9db49eb0d4aeb15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张表格已生成并注册，保存在 `artifacts/paper_tables/main_results_tables.tex`。

**数据校验摘要**：

| 表格 | 内容 | 数据源 |
|------|------|--------|
| Table 1 | Qwen 9 条件主结果 | 全部来自 registry（v5 系列 + 组件实验） |
| Table 2 | DeepSeek 4 条件 + 跨模型 gap | deepseek_* registry 条目 |
| Table 3 | 种子鲁棒性（Qwen 3 seed + DeepSeek 3 seed + VOTA 2 seed） | exception_only_seed{42,123,456} + deepseek 对应条目 |
| Table 4 | 校准指标 ECE/MCE/Brier | calibration_analysis_seed42 registry 条目 |

**注意事项**：
- ae_only 的 F1 值（标注 †）是从混淆矩阵推导的（registry 无显式 F1），1 个错误 / 1190 样本
- exception_only MCE=0.8355 已加脚注说明是低样本 bin 导致的膨胀（2 个 GeneratorExit 不可约误差）
- Table 2 脚注标注 DeepSeek 用 unpaired bootstrap，且 VOTA gap 部分归因于训练时 trace content 截断（非 label 截断，符合 v3.0 framing）
- DeepSeek full_trace 使用 v3（label-preserving truncation fix），脚注已标注

---
