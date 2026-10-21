# diagnose exp029 episode level

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_episode_level_20260516T192139_result.json`
- **Structured JSON:** [`c872789ac2fed65db417.json`](../../sessions/c8/c872789ac2fed65db417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论: CUDA OOM** — `loss.backward()` 在 Step 2 崩溃。

- GPU 0 上训练进程占 55.4 GiB + Ray worker (ref model) 占 35.7 GiB = 91 GiB / 95 GiB，backward 需额外 9.3 GiB 无法分配
- Step 1 完成 (30min, success 18%, pass@8 56%)，Step 2 update_actor 阶段 OOM
- **无 checkpoint 可恢复**，必须从头重训
- 服务器有残留 Ray 进程 (PID 899940, 899941) 需清理

**修复方案**: `ray stop --force` 清理残留 → 启用 `optimizer_offload: True` + 设置 `PYTORCH_ALLOC_CONF=expandable_segments:True`，可释放 ~6-10 GiB 显存覆盖峰值需求。

报告已写入 `artifacts/exp029_episode_level/diagnose_attempt4.md`。

---
