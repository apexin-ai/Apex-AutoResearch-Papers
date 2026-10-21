# 诊断：mvp2_grpo_flatnli_r3 — 误报，进程正常运行

## 结论
**进程未死，正在正常训练。** 监控系统误判。

## 证据
- PID 53292 存活，CPU 752%，GPU 13056 MiB（cuda:3, RTX 5090）
- 服务器当前时间 2026-05-14 23:14，进程已运行 ~2h43m
- 训练进度：step 94/756（12%），epoch 0.11
- stdout/stderr 均指向日志文件，日志正在被写入
- 无任何 error/exception/OOM/killed 记录

## 误报原因分析
监控系统报 "process dead 5× with no sentinel/W&B — auto-resolved as failed"。可能原因：
1. **W&B 未连接**：训练命令指定了 `--wandb_run_name` 但可能未成功连接 W&B（AutoDL 网络问题），导致监控找不到 W&B heartbeat
2. **无 sentinel 文件**：训练脚本可能未写入监控系统期望的 sentinel 文件
3. **日志行数少**：进度条用 `\r` 覆写，日志文件仅 41 行，可能被误判为无输出

## 训练健康度
| 指标 | 值 | 状态 |
|------|-----|------|
| reward | 0.33-0.74 | 正常波动 |
| flat_nli_reward | 0.22-0.52 | 正常 |
| f1_reward | 0→0.038（step 84起） | 开始上升 |
| entropy | 0.046-0.057 | 偏低但非零 |
| grad_norm | 0.25-0.37 | 健康 |
| step_time | 88-126s | 正常 |
| clipped_ratio | 0.41-0.73 | 偏高，注意长度趋势 |

**非 mode collapse**——reward 有变化，f1 开始出现，completions 长度有分布。

## Checkpoint
4 个已保存：step 20, 40, 60, 80（`/root/autodl-tmp/grpo_flatnli_r3/`，每个 772MB）

## 建议
| 字段 | 值 |
|------|-----|
| error_type | **false_alarm**（监控误报） |
| can_auto_fix | **N/A**（无需修复，正在运行） |
| action | 标记为 running，修复监控检测逻辑（检查 PID 存活而非仅依赖 sentinel/W&B） |
| 关注点 | clipped_ratio 偏高（0.41-0.73），后续观察是否 completions 全部达到 max_length |
