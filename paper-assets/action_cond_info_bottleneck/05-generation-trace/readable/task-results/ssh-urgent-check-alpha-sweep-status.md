# ssh urgent check alpha sweep status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-check-alpha-sweep-status_20260517T040422_result.json`
- **Structured JSON:** [`531c65010efa604fc075.json`](../../sessions/53/531c65010efa604fc075.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. 进程存活状态
| PID | 状态 | 运行时间 | GPU | 任务 |
|-----|------|----------|-----|------|
| 837180 | **存活** | 1h06m | GPU 0 (3745 MiB) | alpha=0.0, 全 4 suites |
| 872669 | **存活** | 44m | GPU 1 (4076 MiB) | alpha=0.3, libero_spatial only |

### 2. GPU 状态
- GPU 0: 3211 MiB used, 0% util（eval 间歇期）
- GPU 1: 4636 MiB used, 1% util（eval 间歇期）

### 3. eval_info.json
- **alpha=0.0**: 无 eval_info.json（尚未完成任何 suite）
- **alpha=0.3**: 无 eval_info.json（尚未完成）

### 4. 进度估算
- **alpha=0.0** (PID 837180): libero_spatial 目录有 7/10 task videos → 约 70% spatial 完成，之后还有 object/goal/10 三个 suite
- **alpha=0.3** (PID 872669): libero_spatial 目录有 5/10 task videos → 约 50% spatial 完成

两个进程都在正常运行中，无异常。alpha=0.0 预计还需 ~2-3h 完成全部 4 suites，alpha=0.3 spatial 预计 ~40min 完成。

---
