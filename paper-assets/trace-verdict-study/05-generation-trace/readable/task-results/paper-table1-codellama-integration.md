# paper table1 codellama integration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table1-codellama-integration_20260516T183059_result.json`
- **Structured JSON:** [`e9ba9208428669c501ec.json`](../../sessions/e9/e9ba9208428669c501ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件已创建并注册：

**`table1_final.json`** (`art_20260516_1dd26b`) — 21 行数据，覆盖 4 个模型家族 + DebugBench，每行含 accuracy、95% CI、n=1190/426、lift over majority baseline (0.7151)、exp_id。

**`cross_family_analysis_draft.md`** (`art_20260516_e5caef`) — 4 段：
1. 主结论：exception_only 在 4 家族均 ≥99.33%
2. Scale effects：no_trace 随 scale 单调上升（67→76%），signal-rich conditions scale-invariant
3. DeepSeek seed123 离群值（91.09%）归因于训练不稳定而非架构缺陷
4. DebugBench 跨任务迁移（exception_only=100%）

**一个 discrepancy 需注意**：task 描述的 label_only=86.22% 与 registry 2-seed mean (86.48%) 不符。Registry 中只找到 seed123 (87.06%) 和 seed456 (85.90%)，未找到第三个 seed。表格中使用了 registry 的 86.48%。如需修正请确认是否存在未提取的 label_only seed42 实验。

---
