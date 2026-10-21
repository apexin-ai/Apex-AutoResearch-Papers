# behavioral_pilot_w4 失败诊断

## 失败直接原因

进程被 **SIGTERM** 终止（日志记录 EXIT_CODE=143），harness 报告 EXIT_CODE=129 (SIGHUP)。两个信号的组合指向 **SSH 连接断开导致的级联终止**：SSH 断开 → SIGHUP 传递到 tmux → tmux 向子进程发送 SIGTERM。当前无残留 tmux 会话（`no server running`），印证了 tmux 会话已完全销毁。

不是 OOM（GPU 状态正常、无进程残留）。不是脚本 bug（无 Python traceback）。

## 脚本执行进度

| 阶段 | 状态 |
|------|------|
| 模型加载 | 完成（3/3 shards） |
| Task 0 baseline ep 0-5 | 完成（6/10 episodes，全部 fail，R=0.000） |
| Task 0 baseline ep 6-9 | 未开始（正要启动 ep 6 时被杀） |
| Task 0 ablated | 未开始 |
| Task 3, Task 7 | 未开始 |

总进度：6/60 episodes（10%）。每个 episode 约 85s，已运行约 508s。预计总运行时间约 85 分钟。

## 无 W&B metrics 的原因

脚本本身 **没有 wandb 集成**。结果仅写入 JSON 文件 (`/root/autodl-tmp/vla-ssd/results/behavioral_pilot.json`)。因进程中途被杀，JSON 文件也未生成。

## 环境完整性

- GPU：2x NVIDIA RTX PRO 6000 Blackwell (98GB)，空闲健康
- 模型：`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b` 完整（~15GB safetensors）
- 脚本：`/root/vla-ssd/scripts/behavioral_pilot.py` 存在（11611 bytes，May 18 18:21）
- 结果目录：`/root/autodl-tmp/vla-ssd/results/` 存在
- 依赖：robosuite/LIBERO/transformers 均已安装

**可以直接重跑，无需修复环境。**

## 额外观察

日志第 16 行（模型加载完成后）出现一次 "Terminated"，可能是启动时杀掉了先前残留的进程。

所有 6 个已完成 episode 的 baseline 成绩均为 fail (R=0.000, steps=300)，说明在 `open_the_middle_drawer_of_the_cabinet` 任务上 baseline 表现为零。这本身值得关注：如果 baseline 成功率为 0，ablation 实验的对比价值有限。

## 建议

1. **重跑时使用 nohup 或确保 tmux 持久化**：`tmux new -d -s pilot 'nohup python ...'`，避免 SSH 断连杀死进程
2. **考虑 baseline 全失败的问题**：在投入 85 分钟完整运行之前，先排查 baseline 成功率为 0 的原因（可能是 unnorm_key 不匹配、action space 问题、或任务本身对 OpenVLA 太难）
3. **如需 W&B tracking**：需要在脚本中添加 wandb 集成
