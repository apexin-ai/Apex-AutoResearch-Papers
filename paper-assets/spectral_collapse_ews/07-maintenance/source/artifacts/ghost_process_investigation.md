# Ghost Process Investigation Report

**Date**: 2026-05-25  
**PID**: 986901  
**Server**: rtx6000-diagprobe

## 1. Kill 结果

`kill -9 986901` 成功，exit code 0。

## 2. GPU 释放确认

GPU 已完全释放。两块 NVIDIA RTX PRO 6000 均显示 0MiB 占用，无运行进程。

## 3. 进程来源分析

### 身份

该进程是 **exp_024**：Phase 1 fixed_mix 实验，pythia-410m，seed=44，gpu=0。

### 启动时间

- log 文件 birth time: `2026-05-26 03:32:26 +0800`（即 UTC 2026-05-25 19:32）
- 被 kill 时 log 最后修改: `2026-05-26 04:39:46 +0800`
- 运行时长约 **67 分钟**

### 启动方式

- **bash_history**: 无 `run_phase1` 相关记录
- **tmux**: 无活跃 session
- **crontab**: 无
- **nohup/restart 文件**: runs 目录下仅有 `exp_024.log`，无 restart/nohup 残留

**结论**: 该进程由 agent worker 通过 `ssh_execute` 的 nohup 方式启动（stdout 重定向到 `~/runs/spectral_collapse_ews/exp_024.log`），但未在本地 registry 中注册。属于 worker 启动后失去追踪的幽灵进程。

### 运行状态（被 kill 时）

- Gen 0 已完成：eff_rank=417.55, ppl=9.55, distinct4=0.7305
- Gen 1 正在生成合成样本：进度 ~20160/25000（约 80%）
- 模型加载时遇到 HuggingFace 网络不可达，但成功从本地缓存加载

## 4. 输出文件

- `~/spectral_collapse_ews/results/`: **无** seed44 相关的新输出文件（最新结果文件是 May 25 01:17 的 r025_seed42）
- `~/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_seed44/`: Gen 0 checkpoint 已保存，Gen 1 未完成无输出
- 进程被 kill 时 Gen 1 尚未完成，无最终 results JSON 产生

## 5. 其他异常进程

`ps aux | grep python.*run_phase1|python.*train` 返回空——**无其他训练进程**。

## 6. Audit Worker 关联

runs 目录下无 `verify` 或 `audit` 相关文件，audit worker 失败与此进程无直接关联。

## 7. 总结

| 项目 | 状态 |
|------|------|
| Kill | 成功 |
| GPU 释放 | 已确认（0MiB） |
| 来源 | agent worker ssh_execute 启动，未注册到 registry |
| 输出文件 | Gen 0 checkpoint 已存，Gen 1 未完成无输出 |
| 其他异常 | 无 |
