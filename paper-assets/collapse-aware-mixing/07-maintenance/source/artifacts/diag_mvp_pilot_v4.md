# mvp_pilot_v4 诊断报告

**时间**: 2026-05-12 ~23:22  
**退出码**: 129 (SIGHUP)  
**服务器**: cqa1-38874

## 根因

tmux 服务端进程被杀死（`no server running on /tmp/tmux-0/default`），导致 SIGHUP 信号传递给所有子进程。训练进程在 step 775/1373（Generation 0，56% 完成）被终止。

**不是**代码错误、OOM、磁盘满或 GPU 故障。训练本身运行正常：
- 稳定 ~2.07s/it 吞吐
- Loss 正常下降（116.17 → 106.97 → 106.78）
- 磁盘充裕（根分区 24%，数据盘 49%）
- GPU 正常（RTX PRO 6000, 98GB VRAM）

tmux 被杀的可能原因：AutoDL 平台维护/资源调度，或系统 OOM 杀了 tmux 主进程（容器内 dmesg 不可读，无法确认）。

## 关键日志摘录

```
2026-05-12 23:22:18,963 [INFO] train: Checkpoint saved: /root/autodl-tmp/output/G0/training/checkpoint-760 (step 760)
 56%|█████▋| 775/1373 [29:44<22:15, 2.23s/it]Terminated
```

无 traceback、无 Python error——进程被外部信号干净终止。

## 已产出的 Checkpoints

共 5 个 checkpoint，均在 `/root/autodl-tmp/output/G0/training/`：

| Checkpoint | Step | 时间 |
|-----------|------|------|
| checkpoint-152 | 152 | 22:59 |
| checkpoint-304 | 304 | 23:05 |
| checkpoint-456 | 456 | 23:10 |
| checkpoint-608 | 608 | 23:16 |
| checkpoint-760 | 760 | 23:22 |

**checkpoint-760 可用于恢复训练**，只需再跑剩余 613 步（~21 分钟）完成 G0。

## 修复建议

1. **从 checkpoint-760 恢复**，不要从头重跑 G0。训练脚本需支持 `--resume_from_checkpoint` 参数。
2. **替换 tmux 为 nohup + disown**：`nohup python pilot.py ... > /tmp/pilot_v4.log 2>&1 & disown`。nohup 会忽略 SIGHUP，即使终端断开进程也不会被杀。
3. **在脚本中注册信号处理**：捕获 SIGHUP/SIGTERM 时先保存 checkpoint 再退出，避免训练进度丢失。
4. 如果必须用 tmux，启动时设置 `set-option -g remain-on-exit on`，减少 session 意外销毁的影响。
