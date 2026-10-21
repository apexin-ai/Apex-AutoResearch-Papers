# w7_qwen_scierc_ft_grammar_only 诊断报告

## 失败根因

**误报。** 实验已成功完成，cron 监控因检测不到 W&B metrics 且进程已退出（正常结束）而误判为 failed。

## 证据

- 日志末尾：`Done: 551 new samples, success=551, fail=0 (skipped 0 already processed)`
- 输出文件完整：`outputs/w7_qwen_scierc_ft_grammar_only.jsonl`，551 行，998KB，写入时间 2026-05-16 14:33
- 日志无 traceback、OOM、CUDA error
- 全部 551 个样本逐条处理成功，平均每条 2-3 秒

## 监控误判原因

1. **无 W&B metrics**：grammar_only 模式是纯 inference，不上报 W&B，监控以"无 metrics"判定失败
2. **进程死亡 5 次**：进程正常退出后 PID 不存在，监控轮询 5 次均检测不到 PID，累计计为"死亡 5 次"

## 建议修复

- 监控逻辑需区分 training run（需要 W&B metrics）和 inference run（只看 exit code + output 文件是否产出）
- 对 inference 任务，应检查输出文件是否存在且非空作为成功判据
