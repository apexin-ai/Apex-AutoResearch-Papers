# infra get current occ pids

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_get_current_occ_pids_20260521T052059_result.json`
- **Structured JSON:** [`dc3d4e7fa6ea4d19ff17.json`](../../sessions/dc/dc3d4e7fa6ea4d19ff17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态

| GPU | 利用率 | 显存占用 | PID |
|-----|--------|----------|-----|
| 0 | 99% | 62203 MiB | 76998 |
| 1 | 99% | 62209 MiB | 80898 |
| 2 | 99% | 62203 MiB | 78171 |
| 3 | 100% | 0 MiB | — |

### finetune.py 进程详情

#### s0 (cuda:0) — PID 76998
- **当前 step**: ~1064/50005
- `--vla_path .../occ_s0/...-42500_chkpt`
- `--resume True --resume_step 42500`
- `--save_freq 2500 --seed 42`
- 日志: `occ_s0_resume2.log`
- 速度: ~1.07 it/s

#### s1 (cuda:1) — PID 80898
- **当前 step**: ~1517/50005
- `--vla_path .../occ_s1/...-17500_chkpt`
- `--resume True --resume_step 17500`
- `--save_freq 5000 --seed 43`
- 日志: `occ_s1_resume3.log`（resume2 已被 kill，signal 15）
- 速度: ~1.08 it/s

#### s2 (cuda:2) — PID 78171
- **当前 step**: ~1483/50005
- `--vla_path .../occ_s2/...-42500_chkpt`
- `--resume True --resume_step 42500`
- `--save_freq 2500 --seed 44`
- 日志: `occ_s2_resume2.log`
- 速度: ~1.09 it/s

### checkpoint_rotation.sh
运行中，PID 71055。

### 关键发现
- s1 的 vla_path 指向 **17500_chkpt**（不是 42500），resume_step 也是 17500，save_freq 是 5000（s0/s2 是 2500）
- s1_resume2 已被 kill（SignalException signal 15），当前跑的是 s1_resume3，从同一个 17500 checkpoint 重新 resume
- GPU 3 显示 100% 利用率但 0 MiB 显存，无进程占用

---
