# V2 LoRA 训练失败诊断报告

**日期**: 2026-05-16  
**服务器**: westd-34142 (4× RTX PRO 6000 96GB)

## 结论

两个实验被外部 session 断开同时 kill，**不是** OOM / CUDA error / 代码 bug。

## 详细分析

### v2_lora_universal_r16
- **退出信号**: SIGTERM (EXIT_CODE=143)
- **失败 step**: 9300 / 10000（完成 93%）
- **最后 loss**: 0.6798
- **最后时间戳**: 23:48:51
- **最新 checkpoint**: step_9000

### v2_lora_spatial_r16
- **退出信号**: SIGHUP (EXIT_CODE=129)
- **失败 step**: 6300 / 10000（完成 63%）
- **最后 loss**: 0.6840
- **最后时间戳**: 23:49:03
- **最新 checkpoint**: step_6000

### 时间线对比

| 实验 | 结束时间 | 状态 |
|------|----------|------|
| v2_lora_physical_r16 | 23:26:26 | 正常完成 (EXIT_CODE=0) |
| v2_lora_visual_r16 | 23:31:41 | 正常完成 (EXIT_CODE=0) |
| v2_lora_universal_r16 | 23:48:51 | **被 kill** (SIGTERM) |
| v2_lora_spatial_r16 | 23:49:03 | **被 kill** (SIGHUP) |

### 根因

两个失败实验在几乎相同时刻被 kill（23:48:51 和 23:49:03）。spatial 收到 SIGHUP（终端挂断信号），universal 收到 SIGTERM。这表明 **tmux session 被关闭或 SSH 连接断开**，导致正在运行的进程收到信号终止。

成功实验因为从更靠后的 checkpoint 恢复（需要的步数更少），在 session 断开前已经完成。

日志中无 OOM/CUDA error/Python traceback，磁盘空间充足（170GB avail）。

## 可否 Resume

**两个都可以直接 resume：**

| 实验 | 从 checkpoint 恢复 | 剩余步数 | 预计耗时 |
|------|-------------------|----------|----------|
| universal_r16 | step_9000 | ~1000 steps | ~17 min |
| spatial_r16 | step_6000 | ~4000 steps | ~57 min |

## 建议修复

1. 用 `nohup` 或确保 tmux session detach-proof 方式重启两个实验
2. universal 从 step_9000 恢复，spatial 从 step_6000 恢复
3. 启动命令加 `nohup ... &` 避免 session 断开再次杀死进程
