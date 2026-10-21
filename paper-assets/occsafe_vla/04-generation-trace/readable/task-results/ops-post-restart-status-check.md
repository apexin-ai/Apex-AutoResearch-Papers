# ops post restart status check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-status-check_20260527T133906_result.json`
- **Structured JSON:** [`760cf2bbb887ead9ff58.json`](../../sessions/76/760cf2bbb887ead9ff58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685

| 实验 | 类型 | GPU | PID 状态 | 进度/Step | 备注 |
|------|------|-----|---------|----------|------|
| detach_ln_v2_s1_35_eval | eval | 0,1 | 735898 alive (S, 13h21m) | T4: 29/50 (58%) | 正常运行 |
| detach_ln_s4_eval | eval | 0,1 | 735898 (同上) | Tasks 2/10, T1: 24/50 (48%) | 正常运行 |
| ablation_occ_detach_s4 | train | 2 | 736253 alive (S, 13h21m) | 48572/50005 (97%) | ETA ~22min, ~1.08it/s |
| mvp_occ_s4 | train | 3 | 736253 (同上) | 48442/50005 (97%) | ETA ~24min, ~1.08it/s |

GPU 使用：0/1 低占用(17GB/98GB, 7-56%)，2/3 满载(62-63GB, 97-99%)

## westd-10894

| 实验 | 类型 | GPU | PID 状态 | 进度/Step | 备注 |
|------|------|-----|---------|----------|------|
| full_occ_ln_v2_s1c | train | 0 | 481426 alive (R, 13h02m) | 44384/50005 (89%) | ETA ~1h27m, chkpt=40000 |
| full_occ_ln_v2_s2 | train | 1 | 481643 alive (R, 13h02m) | 44597/50005 (89%) | ETA ~1h24m, chkpt=40000 |
| detach_ln_v2_s0c_r3 | train | 2 | 543255 alive (S, 4h56m) | 15993/50005 (32%) | ETA ~8h52m, chkpt=10000 |
| full_occ_ln_s4 | train | 3 | 553813 alive (S, 4h26m) | 14163/50005 (28%) | ETA ~9h18m, chkpt=10000 |

GPU 使用：全部满载(62-63GB/98GB, 93-99%)

**异常记录：**
- `detach_ln_v2_s0c_r3` 的旧日志 (`/root/runs/occsafe_vla/detach_ln_v2_s0c.log`) 显示之前崩溃过（exitcode 1, 14:29:15），但已被重启（PID 543255, 4h56m），当前日志在 `/root/autodl-tmp/checkpoints/detach_ln_v2_s0c_r3.log`，正常训练中。

**DDL 风险评估（2026-05-28 12:00 UTC）：**
- westd-34685 两个训练实验 ~30min 内完成，无风险
- westd-10894 的 s1c/s2 ~1.5h 后完成，无风险
- detach_ln_v2_s0c_r3 ETA ~8.9h → 约 UTC 23:30 完成，无风险
- full_occ_ln_s4 ETA ~9.3h → 约 UTC 00:00 May 28 完成，无风险

**全部 8 个实验进程存活，无需干预。**

---
