# 诊断报告: eval-random-selection-object-k5-seed44-r2

## 结论：假阳性，实验已正常完成

**失败原因**: 非实际失败。实验正常运行完毕并输出了结果 JSON，但 CRON 监控系统报 "Process exited without valid W&B metrics"——因为 `random_selection` 模式的 evaluate.py 不向 W&B 写入 metrics，只输出本地 JSON 文件。CRON 的检测逻辑与该实验类型不匹配。

## 服务器状态 (bjb1-32546, 检查时间 2026-05-19T00:28Z)

- **进程**: seed44 的 random_selection 进程已退出（正常结束），无残留进程
- **GPU2**: 空闲 (2 MiB / 24564 MiB, 0% utilization)
- **输出文件**: `/root/acr-vla-conformal-refinement/logs/eval_object_random_selection_k5_seed44.json` 存在，1493 bytes，写入时间 May 19 23:50
- **当前运行实验**: 仅 `eval-obs-only-spatial-norm02-seed47` 在 GPU1 上运行中

## 实验结果

| 指标 | 值 |
|------|-----|
| mode | random_selection |
| benchmark | object |
| seed | 44 |
| K | 5 |
| n_rollouts | 10 per task |
| **overall_success_rate** | **10.0% (10/100)** |

### Per-task 结果

| Task | Success Rate |
|------|-------------|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 10% (1/10) |
| salad_dressing | 10% (1/10) |
| bbq_sauce | 20% (2/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 10% (1/10) |
| butter | 0% (0/10) |
| milk | 10% (1/10) |
| chocolate_pudding | 20% (2/10) |
| orange_juice | 20% (2/10) |

## 日志关键片段

```
Overall success rate (random_selection): 10.0% (10/100)
[eval] Results saved to logs/eval_object_random_selection_k5_seed44.json
```

日志从加载模型到完成全部 10 tasks × 10 rollouts，无任何错误或异常。

## 同批实验推断

同批 6 个 r2 实验很可能都是同一问题（CRON 不识别纯 JSON 输出的实验为成功）。应检查其他 5 个实验的日志和 JSON 输出，预计也已正常完成。

## 建议修复方案

1. **无需重跑此实验** — 结果已完整
2. **收集其他 5 个 r2 实验的 JSON 结果**，确认是否也已完成
3. **CRON 监控逻辑需适配**: 对不使用 W&B 的实验，应改为检查 output JSON 文件是否存在且非空，或检查日志中是否包含 "Results saved" 字样作为成功标志
