# 诊断报告: eval_xvla_l2norm_k03_goal_seed42 v2/v3 反复失败

**日期**: 2026-05-24  
**服务器**: westd-38929  
**GPU**: cuda:3 (CUDA_VISIBLE_DEVICES=3), NVIDIA RTX PRO 6000 (98GB)

## 失败根因

### 原因 1: 首次运行 argparse 错误 (exit code 2)

原始运行 (`eval_xvla_l2norm_k03_goal_seed42.log`, 02:18 停止) 因参数拼写错误立即退出:

```
eval_xvla_pruning_libero.py: error: argument --mode: invalid choice: 'l2norm' (choose from 'l2_norm', 'random')
EXIT_CODE=2
```

`--mode l2norm` → 应为 `--mode l2_norm`（缺少下划线）。此错误已在 v2/v3 中修正。

### 原因 2: v2/v3 被监控系统误杀 (核心问题)

v2 和 v3 启动后**运行正常**，日志显示持续产出评估结果，无任何错误/异常/OOM:

| 版本 | 启动时间 | 运行时长 | 最后日志 | 进展 |
|------|---------|---------|---------|------|
| v2 | 02:39:36 | ~22 min | Task 2 Ep 46/50 | Task 0 完成, Task 1 94.0% |
| v3 | 02:46:06 | ~16 min | Task 2 Ep 10/50 | Task 0 42.0%, Task 1 92.0% |

两者均在 ~03:01 被同时终止，特征如下:

1. **日志无错误**: 最后一行是正常的 Ep 输出，无 traceback/exception/error
2. **无 .exit 文件**: `/tmp/agent-ml-exit/` 中不存在 v2.exit 和 v3.exit，说明 bash EXIT trap 未触发 → 进程收到了 SIGKILL（不可捕获）
3. **tmux session 消失**: v2/v3 的 tmux session 不存在，被 v4 替代
4. **v4 立即启动**: 03:02:34 创建，接管 GPU 3

**结论**: 监控系统（agent-ml-research job manager）因检测不到 W&B metrics 或 sentinel 文件，将正在运行的 v2/v3 判定为 "process dead"，执行 kill + restart。**这不是实验代码的 bug，而是监控系统的误判。**

## 系统资源状态（排除硬件问题）

| 指标 | 状态 |
|------|------|
| GPU 显存 | ~5GB/98GB (5%), 充裕 |
| 系统内存 | 150GB/1TB used, 851GB available |
| 磁盘 | 199GB/250GB (80%), 52GB 剩余 |
| GPU 温度 | 47°C, 正常 |
| CUDA 错误 | 无（dmesg 无权限，但 GPU util 正常） |

## 当前状态

- **v4 正在运行**: PID 367660, GPU 3, Task 0 Ep 14/50 进行中 (03:05)
- **风险**: v4 可能再次被监控系统误杀

## 建议修复方案

### 短期（防止 v4 再被杀）

调整监控系统对该实验的健康检查策略，改为检测日志文件的最后修改时间（`stat -c %Y logfile`）而非 W&B/sentinel markers。只要日志在最近 N 分钟内有更新，就视为存活。

### 长期（在 eval 脚本中添加 sentinel）

在 `eval_xvla_pruning_libero.py` 的主循环中周期性写入 sentinel 文件或 W&B heartbeat，使监控系统能正确检测存活状态。

### 不需要修改的

- 评估代码本身无 bug（v2/v3 运行正常）
- GPU/内存/磁盘资源充足
- `--mode l2_norm` 参数已在重试中修正
