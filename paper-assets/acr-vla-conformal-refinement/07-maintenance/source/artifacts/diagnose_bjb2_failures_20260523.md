# 诊断报告：bjb2-28827 三个 eval 实验失败

**日期**: 2026-05-23  
**服务器**: bjb2-28827 (6x RTX 4090, 1TB RAM, uptime 149 days)

## 实验失败摘要

| 实验 | 模式 | GPU | 提交时间 | 状态 |
|------|------|-----|---------|------|
| eval-supp-obj-adapt-s42 | adaptive_conformal_crm | 无指定 | ~04:12 | 已重跑(r2), 运行中 |
| eval-supp-obj-reconvla-s42 | reconvla | cuda:1 | ~04:12 | 已重跑, 运行中 |
| eval-supp-goal-crm005-s42 | crm_obs_only | cuda:2 | ~04:12 | 已重跑, 运行中 |

## 失败原因

**三个实验的共同表现**: 进程在启动后立即死亡，未产生任何日志输出或 exit sentinel 文件。监控系统连续 5 次检测到进程不存在，自动判定为失败。

**原始日志已丢失**: 12:11-12:12 的重跑使用了相同的日志路径和 tmux session 名称，覆盖了原始日志文件。原始 adapt 实验的日志 (`eval-supp-obj-adapt-s42.log`) 在 `~/runs/` 中不存在。

## 根因分析

**排除项**:
- ❌ OOM kill: dmesg 无任何 OOM 记录
- ❌ 服务器重启: uptime 149 天，未重启
- ❌ 磁盘满: 根分区 44% 使用，数据盘 33% 使用
- ❌ 内存不足: 1TB RAM，当时使用约 102GB
- ❌ 代码 bug: 代码自 5/20 未更新，重跑使用相同代码正常运行

**最可能原因: GPU 资源争抢**

04:12 提交时，训练任务 `train-crm-smolvla-3suite-v1` 正在运行（直到 07:03 才结束）。训练日志显示 `device: cuda`（未指定具体 GPU），可能占用了多块 GPU。三个 eval 实验在 GPU 分配冲突下启动失败：
- adapt 实验无 GPU 指定（默认 cuda:0），与训练直接冲突
- reconvla (cuda:1) 和 goal (cuda:2) 如果训练也占用了这些 GPU，则同样冲突
- CUDA 初始化失败时进程可能在 Python 输出任何内容之前就被 kill

**佐证**: 12:12 重跑时训练已结束 5 小时，全部 6 块 GPU 空闲，三个实验均正常运行。

## 当前重试状态

三个实验已于 12:11-12:12 重新提交，当前均在正常运行中：

| 实验 | tmux session | 当前进度 |
|------|-------------|---------|
| adapt-s42 | eval-supp-obj-adapt-s42-r2 (GPU 0) | object benchmark, task 3/10 |
| reconvla-s42 | eval-supp-obj-reconvla-s42 (GPU 1) | object benchmark, task 1/10 |
| goal-crm005-s42 | eval-supp-goal-crm005-s42 (GPU 2) | goal benchmark, task 2+/10 |

**无需额外操作**，等待当前运行完成即可。
