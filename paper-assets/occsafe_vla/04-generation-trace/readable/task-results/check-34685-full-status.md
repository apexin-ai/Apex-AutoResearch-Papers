# check 34685 full status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_34685_full_status_20260525T172455_result.json`
- **Structured JSON:** [`982cd267dc00802e20fb.json`](../../sessions/98/982cd267dc00802e20fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 状态报告

### 系统
- **服务器重启过**：PID 1 启动于今天 01:18，所有训练进程被杀
- **GPU 全部空闲**：4 卡均 0 MiB / 0% 利用率 / 27-28°C
- **无任何 python/torchrun 进程**

### finetune.py 修复
`occ_norm_type` 已在 line 98（定义）和 line 1018（使用）—— 修复确认。

### 实验状态

| 实验 | GPU | PID 存活 | 最终 step | 50K checkpoint | 状态 |
|------|-----|---------|-----------|---------------|------|
| cutoff_25k_s2_v3 | cuda:0 | 死 | ~40824 (82%) | 无 | **中断** |
| reverse_cutoff_s2_v3 | cuda:1 | 死 | ~41049 (82%) | 无 | **中断** |
| cutoff_45k_s1_v3 | cuda:2 | 死 | ~41147 (82%) | 无 | **中断** |
| cutoff_15k_s2_v2 | cuda:3 | 死 | ~41215 (82%) | 无 | **中断** |

每个实验的最新 checkpoint 都是 **40000_chkpt**（另有 20000、30000）。

### 最后一条 AUX 日志

| 实验 | step | occ_loss | action_loss |
|------|------|----------|-------------|
| cutoff_25k_s2_v3 | 40800 | 0.0141 | 0.0708 |
| reverse_cutoff_s2_v3 | 41000 | 0.0127 | 0.0591 |
| cutoff_45k_s1_v3 | 41100 | 0.0136 | 0.0806 |
| cutoff_15k_s2_v2 | 41200 | 0.0152 | 0.0520 |

### 关键问题
4 个实验全部因服务器重启在 ~82% 处中断。按 **C002 约束**（cutoff/reverse_cutoff 禁止 --resume），需要从 pretrained 权重重新训练，每个约 12.7h。4 卡当前全部空闲，可立即使用。

---
