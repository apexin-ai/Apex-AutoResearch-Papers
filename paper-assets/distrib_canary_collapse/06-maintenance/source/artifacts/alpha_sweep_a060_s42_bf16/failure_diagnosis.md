# alpha_sweep_a060_s42_bf16 诊断报告

**结论：实验已成功完成，EXIT_CODE=129 是误报。**

## 失败原因

进程退出码 129 (SIGHUP) 来自 tmux session 销毁。该 tmux session 已不存在于 `tmux ls` 列表中。但 SIGHUP 到达时，Python 脚本已完成所有工作并正常退出。

证据：
- EXIT_CODE sentinel 文件内容为 `0`（脚本自身的退出码）
- shell wrapper 层面捕获到 129（128 + SIGHUP），打印到日志
- 日志无任何 Traceback / Error / Exception
- dmesg 和 journalctl 无 OOM / kill 记录

## 进度

**10/10 generation 全部完成。** gen_0 至 gen_10（含最终评估）均已执行。

时间线（从 output 目录时间戳）：
- gen_0: 01:40
- gen_1: 02:34 (~54min)
- gen_2: 02:53 (~19min)
- gen_3-gen_8: 每个约 19-20min
- gen_9: 04:30
- gen_10 (final eval): 04:49
- 总耗时约 3h09min

## 已有产出

- `config.json` — 实验配置
- `gen_0/` 至 `gen_10/` — 全部 11 个 generation 目录
  - 每个含 checkpoint/, synthetic_data/, trainer/, metrics.json
  - 旧 checkpoint 已按策略清理（gen_1-gen_8 的 checkpoint 被滚动删除，gen_9/gen_10 保留）
- `all_metrics.json` — 全部 11 个 generation 的汇总指标
- `EXIT_CODE` — 内容为 `0`

## 关键指标摘要 (from all_metrics.json)

| Gen | PPL   | Entropy | Eff Rank | MAUVE   | Distinct-3 |
|-----|-------|---------|----------|---------|------------|
| 0   | 27.68 | 3.257   | 48.33    | 0.0288  | 0.833      |
| 5   | 19.71 | 2.590   | 60.77    | 0.0170  | 0.623      |
| 10  | 20.27 | 2.640   | 65.93    | 0.0146  | 0.571      |

趋势：PPL 先降后稳，effective_rank 持续上升，MAUVE 和 distinct-3 持续下降，符合 model collapse 预期。

## 是否可恢复

不需要恢复。实验已完整完成，数据完好。

## 建议

**无需重跑。** 直接使用 `all_metrics.json` 进行后续分析。EXIT_CODE=129 在日志层面是 tmux 清理的副作用，不影响实验结果的完整性和正确性。
