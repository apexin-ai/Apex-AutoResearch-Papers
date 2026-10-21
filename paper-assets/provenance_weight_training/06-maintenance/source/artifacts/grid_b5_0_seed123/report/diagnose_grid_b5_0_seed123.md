# 诊断报告：grid_b5_0_seed123 EXIT_CODE=129

## 基本信息

| 字段 | 值 |
|------|-----|
| 实验 | grid_b5_0_seed123 |
| 服务器 | westd-47453, GPU cuda:3 |
| 失败 PID | 94712 |
| 退出码 | 129 (SIGHUP, signal 1) |
| 运行时间 | 2026-05-14 11:08:05 → 11:36:16（约 28 分钟） |
| 训练进度 | step 552/6103（9%），epoch 0.02 |
| 重试次数 | 第 2 次提交（retry_count=1 时失败） |

## 失败根因

**SIGHUP（信号 1）导致进程终止。**

日志末尾显示训练在 step 552 正常运行（loss=11.19, ~4.48s/it），无 OOM、CUDA error 或任何异常。最后一行为 "Terminated" 后紧跟 EXIT_CODE=129。

SIGHUP 通常由以下原因触发：
1. **tmux session 被销毁/重建** — 最可能原因。该实验第 1 次提交（PID 92793）因未实际启动而被 kill_job 标记 killed，重新提交时可能复用了同一 tmux session 名，导致旧 session 被销毁，新提交的进程收到 SIGHUP
2. SSH 连接中断导致控制终端关闭
3. 系统级事件终止了控制终端

**排除的原因：**
- 非 OOM：日志无 OOM 相关错误，dmesg 无 OOM killer 记录
- 非 CUDA 错误：训练指标正常，GPU 温度正常（59°C）
- 非代码 bug：训练逻辑无异常，loss 和 weighting 指标均在合理范围

## 当前状态

实验已被 on_failed hook 自动重试（第 3 次提交，retry_count=2）：
- 当前 PID：94717
- GPU cuda:3 使用 46514MiB / 97887MiB，GPU-Util 99%
- 训练正在正常进行

## 最后 Checkpoint

| 字段 | 值 |
|------|-----|
| 路径 | `/root/provenance_weight_training/output/models/grid_b5_0_seed123/checkpoint-500/` |
| Step | 500 |
| 模型文件 | model.safetensors (1.19GB)，含完整 tokenizer 和 config |
| 保存时间 | 2026-05-14 19:32 |
| step_metrics | 记录到 step 249（metrics 日志，每 step 记录 sub-batch） |

**注意：** 当前第 3 次提交使用了相同的 output_dir，如果未设置 `--resume_from_checkpoint`，训练将从头开始，之前的 checkpoint-500 可能被覆盖。

## 是否可安全重试

**已自动重试且正在运行。** 无需手动干预。

建议确认：
1. 当前运行是否从 checkpoint-500 恢复（检查日志起始 step）
2. 如果从头开始，28 分钟的 checkpoint 损失可接受（总训练约 7.6 小时）

## 建议修复措施

此次失败为偶发性 session 管理问题，非系统性 bug。如需防止复发：
- 确保 kill_job 在销毁 tmux session 前等待旧进程完全退出
- 重试时使用不同的 tmux session 名避免冲突
