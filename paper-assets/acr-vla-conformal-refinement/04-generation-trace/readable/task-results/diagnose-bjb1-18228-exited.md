# diagnose bjb1 18228 exited

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-18228-exited_20260515T050149_result.json`
- **Structured JSON:** [`fec6cc2807990fecd60b.json`](../../sessions/fe/fec6cc2807990fecd60b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断报告：

---

## 诊断报告

### 实验 1: eval-acr-spatial-v4-small (D018: perdof, max_correction_norm=0.1)
- **结论**: FAILED — 未完成
- **完成进度**: 7/10 tasks，部分 SR = **42.9% (30/70)**
- **退出原因**: Hung on task 8 env init（无 error/traceback），进程被 kill
- **Per-task SR**:

| Task | SR |
|---|---|
| between_plate_and_ramekin | 60% (6/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 10% (1/10) |
| on_cookie_box | 40% (4/10) |
| in_top_drawer | 0% (0/10) |
| on_ramekin | 0% (0/10) |
| next_to_cookie_box | **90%** (9/10) |
| tasks 8-10 | ❌ 未运行 |

### 实验 2: eval-acr-spatial-v4-obs-only-r2 (D020: obs_only, max_correction_norm=0.1)
- **结论**: FAILED — 未完成
- **完成进度**: 6/10 tasks 完成 + task 7 进行中 (5/5 at rollout 5/10)，部分 SR = **40.0% (24/60)**
- **退出原因**: 同样 hung 后被 kill，LIBERO env init hang bug
- **Per-task SR**:

| Task | SR |
|---|---|
| between_plate_and_ramekin | **90%** (9/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 40% (4/10) |
| in_top_drawer | 10% (1/10) |
| on_ramekin | 0% (0/10) |
| tasks 7-10 | ❌ 未完成 |

**共同根因**: bjb1-18228 上 LIBERO 环境初始化 hang bug，多个实验均受影响。两个实验都需要在其他服务器上 restart 补完剩余 tasks。

---
