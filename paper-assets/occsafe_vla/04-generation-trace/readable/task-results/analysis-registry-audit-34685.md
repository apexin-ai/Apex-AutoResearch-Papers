# analysis registry audit 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_registry_audit_34685_20260525T102859_result.json`
- **Structured JSON:** [`dc7e2b7030c373333c8e.json`](../../sessions/dc/dc7e2b7030c373333c8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-34685 全部 4 张 GPU 的进程均与 registry 一一对应，无遗漏、无多余进程。

| GPU | nvidia-smi PID | Registry exp_id | Registry PID | 当前 step | 进度 | 速度 | 预计完成 |
|-----|---------------|-----------------|-------------|----------|------|------|---------|
| 0 | 11510 | cutoff_25k_s2_v3 | 11510 ✓ | ~17606/50005 | 35% | ~1.06 it/s | ~03:00 May 26 |
| 1 | 8347 | reverse_cutoff_s2_v3 | 8347 ✓ | ~17732/50005 | 35% | ~1.04 it/s | ~02:58 May 26 |
| 2 | 2186 | cutoff_45k_s1_v3 | 2112 (父进程) ✓ | ~18031/50005 | 36% | ~1.08 it/s | ~02:42 May 26 |
| 3 | 2617 | cutoff_15k_s2_v2 | 2475 (父进程) ✓ | ~18080/50005 | 36% | ~1.08 it/s | ~02:40 May 26 |

**状态：一切正常。** GPU 2/3 的 PID 差异是 nohup bash wrapper（registry 记录）vs 子 python 进程（nvidia-smi 显示），属正常行为。4 个实验均已训练约 5h55min，预计明天凌晨 ~03:00 前全部完成。

---
