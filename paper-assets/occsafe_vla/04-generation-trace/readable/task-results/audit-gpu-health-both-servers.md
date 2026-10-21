# audit gpu health both servers

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu_health_both_servers_20260528T013730_result.json`
- **Structured JSON:** [`8afc7602fe163388ea99.json`](../../sessions/8a/8afc7602fe163388ea99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## westd-34685: 全部正常

| GPU | 利用率 | 显存占用 | 实验 | 实际 PID | 预期 PID | 状态 |
|-----|--------|----------|------|----------|----------|------|
| 0 | 99% | 62161/97887 MiB | detach_ln_v2_s2 (resume from 15000) | 29416 | 29334 | **运行中** |
| 1 | 83% | 62223/97887 MiB | vanilla_object_s0 (resume from 10000) | 29629 | 29484 | **运行中** |
| 2 | 92% | 62209/97887 MiB | full_occ_ln_v2_s3 | 7921 | 7850 | **运行中** |
| 3 | 99% | 62203/97887 MiB | detach_ln_v2_s3 | 8269 | 8066 | **运行中** |

PID 与预期有小偏差（实际 PID 是 python worker 子进程，预期 PID 可能是 torchrun 父进程），但 4 个实验全部确认在跑。

---

## westd-10894: 2 个存活，2 个挂掉

| GPU | 利用率 | 显存占用 | 实验 | 实际 PID | 预期 PID | 状态 |
|-----|--------|----------|------|----------|----------|------|
| 0 | 99% | 62971/97887 MiB | vanilla_object_s1 | 798980 | 798980 | **运行中** |
| 1 | 85% | 62243/97887 MiB | detach_ln_v2_s4 | 822480 | 822480 | **运行中** |
| 2 | 0% | 0/97887 MiB | full_occ_bn_object_s0 | — | 930834 | **已挂** |
| 3 | 0% | 0/97887 MiB | detach_bn_object_s0 | — | 931057 | **已挂** |

### 崩溃详情

- **崩溃时间**: 2026-05-28 09:35:41 UTC（北京时间 17:35）
- **崩溃位置**: `save_training_checkpoint()` → `merged_vla.save_pretrained()` → `safe_save_file()`
- **根因**: **`No space left on device (os error 28)`** — 两个实验在保存 step 5000 checkpoint 时同时触发磁盘满错误
- **磁盘状态**: `/root/autodl-tmp` 250GB **已用 100%**（仅剩 400K）
- **GPU 显存**: 已完全释放（0 MiB）
- **进度**: 两个实验都只跑到 ~5000 步（已保存 5000_chkpt），训练到约 step 5000 时尝试保存 checkpoint 写满磁盘崩溃

需要清理 westd-10894 磁盘空间后重启这两个实验（可用 `--resume --resume_step 5000`）。

---
