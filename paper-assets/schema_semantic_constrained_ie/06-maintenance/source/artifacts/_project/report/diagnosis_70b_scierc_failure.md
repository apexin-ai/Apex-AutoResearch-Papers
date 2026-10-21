# 70B SciERC 实验诊断报告

**诊断时间**: 2026-05-18 21:34 UTC
**服务器**: westd-21461

## 结论：两个实验均已成功完成，非失败

### 实验 1: 70b_scierc_constrained
- **状态**: 正常完成
- **日志末尾**: `Done: 551 new samples, success=551, fail=0 (skipped 0 already processed)`
- **输出文件**: `/root/autodl-tmp/schema_outputs/70b_scierc_constrained.jsonl` (1.26 MB, 551 行)
- **进程 PID 24703**: 已退出（正常结束，非异常死亡）

### 实验 2: 70b_scierc_unconstrained
- **状态**: 正常完成
- **日志末尾**: `Done: 551 new samples, success=551, fail=0 (skipped 0 already processed)`
- **输出文件**: `/root/autodl-tmp/schema_outputs/70b_scierc_unconstrained.jsonl` (1.27 MB, 551 行)
- **进程 PID 24552**: 已退出（正常结束，非异常死亡）

### GPU 当前状态
- GPU 0 (NVIDIA RTX PRO 6000 Blackwell): 空闲, 0MiB / 97887MiB, 0% 利用率
- GPU 1 (NVIDIA RTX PRO 6000 Blackwell): 空闲, 0MiB / 97887MiB, 0% 利用率
- 无运行中的 GPU 进程

### 磁盘状态
- overlay `/`: 18G/30G used (57%)
- `/dev/sda2`: 18G/879G used (3%)
- 磁盘空间充裕

### 系统日志
- `dmesg` 无权限读取（容器环境限制），但根据日志和输出判断无 OOM

### 为什么进程看起来像"失败"
两个进程在处理完全部 551 个样本后正常退出，退出码为 0。PID 消失和 GPU 释放是正常完成的表现，不是崩溃。之前的"miss 4/5"心跳丢失可能是因为进程已经跑完退出了。

### 后续行动
- 无需重试，数据已完整
- 可直接用输出文件进行评估分析
