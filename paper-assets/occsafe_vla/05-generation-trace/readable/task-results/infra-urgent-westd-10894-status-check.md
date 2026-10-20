# infra urgent westd 10894 status check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-westd-10894-status-check_20260521T091253_result.json`
- **Structured JSON:** [`88484a8d8ff27eb09f52.json`](../../sessions/88/88484a8d8ff27eb09f52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894 状态

**误报 — 4/4 实验全部正常运行。**

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| 0 | 99% | 63037 / 97887 MiB |
| 1 | 99% | 62203 / 97887 MiB |
| 2 | 21% | 62209 / 97887 MiB |
| 3 | 39% | 62203 / 97887 MiB |

### 各实验状态
| 实验 | GPU | 状态 | 当前步数 | 最新 checkpoint | 速度 |
|------|-----|------|---------|----------------|------|
| ablation_occ_detach_s0 | cuda:0 | **running** | ~8554/50005 (17%) | 10000_chkpt | ~1.07 it/s |
| ablation_random_occ_s0 | cuda:1 | **running** | ~8574/50005 (17%) | 10000_chkpt | ~1.08 it/s |
| ablation_occ_detach_s1 | cuda:2 | **running** | ~2919/50005 (6%) | 5000_chkpt | ~1.01 it/s |
| ablation_random_occ_s1 | cuda:3 | **running** | ~2911/50005 (6%) | 5000_chkpt | ~1.03 it/s |

s0 组（14:24 启动）比 s1 组（16:07 启动）早约 1.7 小时，进度差异合理。

### 磁盘
`/root/autodl-tmp`: 230G / 250G (92%), 剩余 21G — 偏高但暂时够用，checkpoint rotation 脚本在控制。

### Rotation 脚本
PID 504685 — **alive**

### 修复动作
无需修复，所有实验正常运行中。System 报告 "0/4 GPU 在用" 是误报。

---
