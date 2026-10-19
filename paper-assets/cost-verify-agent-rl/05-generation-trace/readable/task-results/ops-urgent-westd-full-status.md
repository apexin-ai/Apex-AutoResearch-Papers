# ops urgent westd full status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-westd-full-status_20260521T003404_result.json`
- **Structured JSON:** [`4b2e1ba8d378a73c81fc.json`](../../sessions/4b/4b2e1ba8d378a73c81fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-47453 状态汇总

### 实验状态

| 实验 | PID | 状态 | 进度 | 关键指标 |
|------|-----|------|------|----------|
| seed3 OOD (exp029) | 417862 | **CRASHED** | — | `RuntimeError: tensors on cuda:0 and cpu` |
| Cell C v3 | 88226 | **RUNNING** (6h11m) | 2/15 steps (13%) | step0 val: success=0.0, pass@1=0.0, reward=0.5 |

### GPU 占用

| GPU | 利用率 | VRAM | 占用进程 |
|-----|--------|------|----------|
| 0 | 0% | 0 / 98 GB | idle |
| 1 | 0% | 0 / 98 GB | idle |
| 2 | 0% | 45 / 98 GB | PID 95408 (Cell C v3) |
| 3 | 0% | 45 / 98 GB | PID 95409 (Cell C v3) |

### 详情

**seed3 OOD** — 已崩溃，EXIT_CODE=1。根因：`optimizer_offload=True` 导致 Adam optimizer states 在 CPU 上，但 FSDP `_optimizer_step()` 期望所有 tensor 在同一设备。崩溃点：`dp_actor.py:180 self.actor_optimizer.step()`。GPU 0,1 已释放。

**Cell C v3** — 正常运行中，step 2 rollout 阶段（最后日志 06:35，环境交互中所以 GPU util=0%）。step 0 baseline val 全零（符合预期，未训练）。按当前速度 ETA ~32h。无报错。

---
