# 诊断报告：westd-10894 四实验同时被 SIGTERM

**日期**: 2026-05-21  
**事件时间**: 12:52:12 UTC+8 (04:52:12 UTC)

## 根因判定：平台级外部 SIGTERM（高置信度）

### 判定依据

| 排查项 | 结果 | 说明 |
|--------|------|------|
| SIGTERM 时间戳 | 12:52:12.120 ~ 12:52:12.137 | 4 个进程在 17ms 内全部收到 signal 15 |
| OOM | ❌ 排除 | OOM killer 发 SIGKILL(9)，不是 SIGTERM(15) |
| 实例重启 | ❌ 排除 | /proc/uptime = 156 天，无重启记录 |
| 磁盘满 | ❌ 排除 | root: 11G 可用 (34%), data: 95G 可用 (37%) |
| 手动 kill | ❌ 排除 | bash_history 无 kill 命令，实验由自动化 ssh_execute 启动 |
| 训练异常 | ❌ 排除 | 日志无 error/exception，进度条正常推进至被杀 |
| 系统日志 | 无 | 容器环境无 syslog/kern.log/messages，journal 目录为空 |

**结论**: 17ms 内同时终止 4 个独立进程，只有进程树的公共祖先（容器 init / 平台管理进程）发送 SIGTERM 能做到。最可能是 SeetaCloud 平台的维护操作或资源调度触发了容器级 SIGTERM 广播。

## 各实验进度

| 实验 | GPU | 启动时间(UTC+8) | 终止步数 | 最近 checkpoint | 丢失步数 |
|------|-----|-----------------|---------|----------------|---------|
| ablation_occ_detach_s0 | cuda:0 | 11:44 | ~4006 | step 2500 ✅ | ~1506 |
| ablation_random_occ_s0 | cuda:1 | 11:44 | ~3993 | step 2500 ✅ | ~1493 |
| ablation_occ_detach_s1 | cuda:2 | 12:22 | ~1546 | 无 ❌ | ~1546 |
| ablation_random_occ_s1 | cuda:3 | 12:22 | ~1545 | 无 ❌ | ~1545 |

**Checkpoint 详情**:
- s0 实验: `/root/autodl-tmp/checkpoints/ablation_{occ_detach,random_occ}_s0/...--2500_chkpt/` 完整（含 model shards + action_head + occ_head + proprio_projector + lora_adapter）
- s1 实验: 仅有初始 dataset_statistics.json，无任何模型 checkpoint

## 服务器当前状态

| 项目 | 状态 |
|------|------|
| SSH 连通 | ✅ 正常 |
| GPU | 4× RTX PRO 6000 Black (98GB)，全部空闲，0MiB 占用 |
| 磁盘 | root 20G/30G, data 156G/250G |
| 温度 | 31-37°C，正常 |
| 残留进程 | 无 |

**服务器可立即用于重启实验。**

## 建议

1. **ablation_occ_detach_s0 / ablation_random_occ_s0**: 从 step 2500 checkpoint resume，损失约 25 分钟训练时间
2. **ablation_occ_detach_s1 / ablation_random_occ_s1**: 需从头重启，损失约 29 分钟训练时间
3. 考虑将 save_freq 从当前值降低（如 1000），减少意外中断时的数据丢失
4. 启动后可用 nohup 隔离进程，但对平台级 SIGTERM 无效——建议训练脚本中加入 SIGTERM handler 做紧急 checkpoint save
