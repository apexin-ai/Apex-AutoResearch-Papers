# Ablation Batch Failure Diagnosis — 2026-05-21

## 根因判断

**外部 SIGTERM（平台级 kill）**。4 个进程在完全相同的时刻 `12:52:12 UTC+8`（04:52:12 UTC）收到 SIGTERM signal 15，由 torchrun elastic agent 传播到 worker 后退出。

排除项：
- **非 OOM**：内存 83GB/1TB used，914GB available
- **非重启**：uptime 156 天，`last reboot` 无近期记录
- **非 crontab 定时 kill**：`crontab -l` 为空
- **无内核/系统日志**：`dmesg` 权限不足（容器环境），`journalctl` 无 journal 文件

结论：**SeetaCloud/WestD 平台级进程管理**——最可能是计费配额到期、维护窗口、或平台自动进程清理。建议检查 WestD 控制台的实例计费状态和维护公告。

## 各实验进度和最新 Checkpoint

| 实验 | GPU | 最后 step | 进度 | 运行时间 | Checkpoint |
|------|-----|----------|------|---------|------------|
| ablation_occ_detach_s0 | cuda:0 | 4006/50005 | 8.0% | ~1h07m | **step 2500** ✅ (完整, ~14.5GB) |
| ablation_occ_detach_s1 | cuda:2 | 1546/50005 | 3.1% | ~29m | **无** ❌ (未达首次保存点) |
| ablation_random_occ_s0 | cuda:1 | 3993/50005 | 8.0% | ~1h07m | **step 2500** ✅ (完整, ~14.5GB) |
| ablation_random_occ_s1 | cuda:3 | 1545/50005 | 3.1% | ~29m | **无** ❌ (未达首次保存点) |

Checkpoint 路径：
- `ablation_occ_detach_s0`: `/root/autodl-tmp/checkpoints/ablation_occ_detach_s0/openvla-7b+...--image_aug--2500_chkpt/`
- `ablation_random_occ_s0`: `/root/autodl-tmp/checkpoints/ablation_random_occ_s0/openvla-7b+...--image_aug--2500_chkpt/`

## 环境完整性

- ✅ conda env `occsafe` 完好：torch=2.11.0+cu128, cuda=True
- ✅ 4x RTX PRO 6000 Black (96GB each) 全部空闲可用
- ✅ 数据集 `/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops` 存在
- ✅ 磁盘：156GB/250GB used (63%)，剩余 95GB

## Resume 策略

### 可 resume（有 checkpoint）
- **ablation_occ_detach_s0**：从 step 2500 恢复，损失 ~1506 步计算量（~25 min）
- **ablation_random_occ_s0**：从 step 2500 恢复，损失 ~1493 步计算量（~25 min）

### 需重跑（无 checkpoint）
- **ablation_occ_detach_s1**：从头开始
- **ablation_random_occ_s1**：从头开始

### 建议
1. **先确认计费/配额**：在 WestD 控制台检查实例是否因欠费或到期被平台 kill，确保重跑不会再次中断
2. **降低 save_freq**：当前首次 checkpoint 在 step 2500，建议改为 **1000-2000 步**保存一次，减少被 kill 后的浪费。磁盘空间充足（95GB free），每个 checkpoint ~14.5GB 可以接受
3. **优先重启 s1 实验**：s1 完全没有 checkpoint，需要从头跑；s0 可以 resume 少损失
4. 训练速度约 **1.05-1.09 it/s**（单 GPU），50K steps 预计 ~12.8h/run
