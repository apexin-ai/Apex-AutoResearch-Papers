# 诊断报告: eval_openvla_l2norm_k05_long_seed42

## 结论：误报 — 实验已成功完成

### 根因

实验正常运行并完成，**不是真正的失败**。监控系统误判原因：

1. **无 exit sentinel 文件**: `/tmp/agent-ml-exit/eval_openvla_l2norm_k05_long_seed42.exit` 不存在，说明该实验未通过标准 tmux wrapper 启动（或使用了不同的 job name），监控轮询 5 次未找到 sentinel 文件后判定为 dead
2. **无 W&B 日志**: 实验未配置 W&B，监控无法通过 W&B run 状态确认存活

### 实验结果

- **状态**: 已完成
- **Overall SR**: 16.4% (82/500)
- **耗时**: 666.6 分钟
- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_l2norm_prune_k05_10_seed42.json`
- **完成时间**: 2026-05-27 09:01:58

### 是否需要重试

**不需要**。实验已完整跑完 10 tasks x 50 episodes = 500 episodes，结果已保存。

### 服务器状态 (westd-38929, 2026-05-27 09:15 UTC)

| 资源 | 状态 |
|------|------|
| GPU 0 | RTX PRO 6000, 15.5/97.9 GB, 0% util (空闲) |
| GPU 1 | RTX PRO 6000, 16.2/97.9 GB, 68% util (运行 l2norm k=0.95) |
| GPU 2 | RTX PRO 6000, 15.8/97.9 GB, 56% util (运行 l2norm k=0.75) |
| GPU 3 | RTX PRO 6000, 16.2/97.9 GB, 72% util (运行 attn k=0.95) |
| 磁盘 | /root/autodl-tmp: 179G/250G used (72%), 72G free |

GPU 0 已空闲，可用于新实验。
