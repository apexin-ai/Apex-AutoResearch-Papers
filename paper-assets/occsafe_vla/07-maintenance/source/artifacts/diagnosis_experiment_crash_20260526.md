# 实验批量死亡诊断报告

**时间**: 2026-05-26 01:10 (所有实验同一时刻停止)
**影响范围**: 2 台服务器，共 8 个实验

---

## 结论：统一失败原因

**外部进程强制 kill（SIGKILL）**，非代码 crash、非 OOM、非服务器重启。

证据：
1. 两台服务器 8 个实验在 **完全相同的时间戳**（May 26 01:10）停止
2. 所有日志无任何错误信息/stack trace，仅进度条中断
3. 服务器未重启（westd-34685 uptime 152 天，westd-10894 uptime 161 天）
4. 部分实验在死亡前几步出现短暂速度下降（1.08it/s → 2-5s/it），可能是其他进程抢占 GPU 或 checkpoint 保存

**最可能原因**：集群管理系统/调度器批量终止 GPU 进程，或定时维护脚本在 01:10 执行了 kill。

---

## 各实验进度与 checkpoint 状况

### westd-34685（4 个实验）

| 实验 | 最后 step | 进度 | 最新 checkpoint | 丢失 steps | 可恢复 |
|------|-----------|------|-----------------|------------|--------|
| reverse_cutoff_s2_v3 | 41049/50005 | 82% | step 40000 | ~1049 | ⚠️ C002 约束 |
| cutoff_25k_s2_v3 | 40824/50005 | 82% | step 40000 | ~824 | ⚠️ C002 约束 |
| cutoff_45k_s1_v3 | 41215/50005 | 82% | step 40000 | ~1215 | ⚠️ C002 约束 |
| cutoff_15k_s2_v2 | 41147/50005 | 82% | step 40000 | ~1147 | ⚠️ C002 约束 |

### westd-10894（4 个实验）

| 实验 | 最后 step | 进度 | 最新 checkpoint | 丢失 steps | 可恢复 |
|------|-----------|------|-----------------|------------|--------|
| full_occ_ln_s3 | 20398/50005 | 41% | step 20000 | ~398 | ✅ 可 resume |
| ablation_occ_detach_s3 | 20376/50005 | 41% | step 20000 | ~376 | ✅ 可 resume |
| cutoff_45k_s2 | 26480/50005 | 53% | step 20000 | ~6480 | ⚠️ C002 约束 |
| mvp_occ_s3 | ~20k+/50005 | ~41% | step 20000 | 少量 | ✅ 可 resume |

### Checkpoint 存储位置

- westd-34685: `/root/autodl-tmp/checkpoints/{experiment_name}/`
- westd-10894: `/root/autodl-tmp/checkpoints/{experiment_name}/`

---

## 恢复策略说明

**可直接 resume 的实验**（3 个）：
- `full_occ_ln_s3`：从 step 20000 resume，丢失约 398 步（~6 分钟训练量）
- `ablation_occ_detach_s3`：从 step 20000 resume，丢失约 376 步
- `mvp_occ_s3`：从 step 20000 resume

**受 C002 约束的实验**（5 个 cutoff/reverse_cutoff）：
- C002 禁止 cutoff/reverse_cutoff 实验使用 `--resume`（原因：resume 后 batch_idx 从 0 重计，导致 cutoff 阈值触发时机错误）
- 其中 `cutoff_25k_s2_v3`、`cutoff_15k_s2_v2`、`reverse_cutoff_s2_v3` 已过 cutoff 点，cutoff 机制已生效，理论上 resume 不会再次触发 cutoff 问题——但需确认代码行为
- `cutoff_45k_s1_v3`（cutoff=45k, 当前 step=41215）尚未到达 cutoff 点，resume 会导致 batch_idx 重置，**不可 resume**
- `cutoff_45k_s2`（cutoff=45k, 当前 step=26480）同理，**不可 resume**

---

## 系统层面排查结果

| 检查项 | westd-34685 | westd-10894 |
|--------|-------------|-------------|
| 服务器重启 | ❌ 未重启（uptime 152天） | ❌ 未重启（uptime 161天） |
| OOM kill | 日志无 OOM 迹象 | 日志无 OOM 迹象 |
| 磁盘满 | 未见相关错误 | 未见相关错误 |
| 代码 crash | 无 error/traceback | 无 error/traceback |
| 日志最后修改 | May 26 01:10 | May 26 01:10 |

---

## 建议行动

1. **查明 kill 来源**：联系集群管理员确认 01:10 是否有计划内维护或自动 kill 策略
2. **优先 resume 可恢复实验**：full_occ_ln_s3、ablation_occ_detach_s3、mvp_occ_s3
3. **cutoff 实验决策**：确认已过 cutoff 点的实验 resume 后 batch_idx 行为，判断是否安全 resume
4. **cutoff_45k 系列需从头训练**：cutoff_45k_s1_v3 和 cutoff_45k_s2 因未到达 cutoff 点，必须从 pretrained 重新开始
