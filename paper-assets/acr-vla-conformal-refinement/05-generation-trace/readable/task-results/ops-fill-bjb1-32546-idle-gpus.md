# ops fill bjb1 32546 idle gpus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-bjb1-32546-idle-gpus_20260516T071129_result.json`
- **Structured JSON:** [`9ced640082ff1bd3855a.json`](../../sessions/9c/9ced640082ff1bd3855a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断
**scalar-seed44 失败原因**: 日志仅 17 行，在 task 1 rollout 5/10 处截断，无 Python traceback。dmesg 不可访问（容器权限）。几乎确定是系统 OOM SIGKILL——SIGKILL 不给 Python 打印 traceback 的机会。已在 bjb1-32546 重试。

**VLA-only-seed44 (bjb2-40593)**: PID 286989 已死，日志显示 **10/10 tasks 完成，overall 10.0% (10/100)**，EXIT_CODE=0。成功。

## bjb1-32546 GPU 状态
| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| cuda:0 | 22% | 5665/24564 MiB | eval-scalar-object-seed44-r2（已在跑） |
| cuda:1 | 22% | 5165/24564 MiB | 其他任务 |
| cuda:2 | 21% | 5665/24564 MiB | eval-acr-object-v4-obs-only |
| cuda:3 | 24% | 1942/24564 MiB | eval-obs-only-object-norm02-seed43-r2 |
| cuda:4 | 23% | 5665/24564 MiB | eval-obs-only-object-norm01-seed44（已在跑） |
| cuda:5 | 0% | 2/24564 MiB | **空闲 → 已部署** |

## 部署结果
- **cuda:0 → eval-scalar-object-seed44-r2** — 已在运行（另一实例先提交，PID 226878）
- **cuda:4 → eval-obs-only-object-norm01-seed44** — 已在运行（另一实例先提交，PID 227086）
- **cuda:5 → eval-obs-only-object-default-seed44** — 已提交（PID 229742），obs_only default norm (~1.42) seed=44

## 说明
cuda:0 和 cuda:4 的实验已被另一进程提交（GPU 分配与任务计划略有不同：scalar 在 cuda:0 而非 cuda:4，obs-only-norm01 在 cuda:4 而非 cuda:5），但实验内容一致。cuda:5 是唯一剩余空卡，已部署 obs-only-default-seed44（因 VLA-only seed44 已完成）。

## 问题/Blocker
无。6 张卡全部满载。

---
