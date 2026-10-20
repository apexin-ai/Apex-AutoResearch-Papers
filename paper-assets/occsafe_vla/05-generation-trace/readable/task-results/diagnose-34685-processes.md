# diagnose 34685 processes

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_34685_processes_20260525T172726_result.json`
- **Structured JSON:** [`2903ba342f2eb7a1a284.json`](../../sessions/29/2903ba342f2eb7a1a284.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 34685 进程诊断

| exp_id | pid | 存活? | 最后step | 目标step | 状态判断 | 最新checkpoint |
|--------|-----|-------|---------|---------|---------|---------------|
| cutoff_15k_s2_v2 | 2475 | **死** | 41215 | 50005 | **崩溃** (82%) | 40000_chkpt |
| cutoff_25k_s2_v3 | 11510 | **死** | 40824 | 50005 | **崩溃** (82%) | 40000_chkpt |
| reverse_cutoff_s2_v3 | 8347 | **死** | 41049 | 50005 | **崩溃** (82%) | 40000_chkpt |

**关键发现：**
- 4 张 GPU 全部空闲（0% 利用率，0 MiB 显存）
- 三个进程在差不多同一时间段（elapsed ~12:25-12:35）全部死亡，日志无 traceback/error，只有进度条戛然而止 → **大概率被系统同时 kill（OOM 或外部干预）**
- 系统 uptime 152 天，非重启
- 三个实验均已保存 40000 checkpoint，需 resume 跑完剩余 ~9000 步

**checkpoint 路径：**
- `cutoff_15k_s2_v2`: `/root/autodl-tmp/checkpoints/cutoff_15k_s2_v2/openvla-7b+..--cutoff_15k_s2_v2--40000_chkpt`
- `cutoff_25k_s2_v3`: `/root/autodl-tmp/checkpoints/cutoff_25k_s2_v3/openvla-7b+..--cutoff_25k_s2_v3--40000_chkpt`
- `reverse_cutoff_s2_v3`: `/root/autodl-tmp/checkpoints/reverse_cutoff_s2_v3/openvla-7b+..--reverse_cutoff_s2_v3--40000_chkpt`

**注意：** C002 约束禁止 cutoff/reverse_cutoff 使用 `--resume`，必须从 pretrained 重头训练。如果要恢复这三个实验，需要确认是否能绕过此约束或重新从头跑。

---
