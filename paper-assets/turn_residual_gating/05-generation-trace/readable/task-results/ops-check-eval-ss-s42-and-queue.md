# ops check eval ss s42 and queue

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_eval_ss_s42_and_queue_20260522T225520_result.json`
- **Structured JSON:** [`b3e24cb2116156e8a2e4.json`](../../sessions/b3/b3e24cb2116156e8a2e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Eval 状态：**RUNNING** (AR 阶段进行中)

PID 48241 (wrapper, 3h28m), PID 49165 (AR gen, 1h45m elapsed)

### 2. TF 结果（已完成 4/4）

| 条件 | turn1_gar | mid_gar | avg_ppl | ntp_loss | recovery |
|------|-----------|---------|---------|----------|----------|
| Base+GAR-ours | 0.0495 | 0.0128 | 4.34 | 1.40 | +0.06pp |
| Base+GAR-dongre | 0.0111 | 0.0031 | 4.34 | 1.40 | -0.91pp |
| **TG+GAR-ours** | **0.5272** | **0.5025** | **2.78** | **0.98** | **+49.04pp** |
| **TG+GAR-dongre** | **0.4434** | **0.3890** | **2.78** | **0.98** | **+37.68pp** |

- baseline_mid_gar = 0.0122

### 3. AR 阶段进度

- **AR 1/2 (ours, beta=0,3,5)**：模型已加载完毕，正在生成中（PID 49165, 1h45m, 26.7 GB GPU）
- **AR 2/2 (dongre)**：尚未开始
- 预计 AR 总时长：还需 ~1-2h（取决于剩余生成速度 + dongre variant）

### 4. Queue Runner 状态

不存在 `/root/turn_residual_gating/runs/d048_queue_runner.log`，queue_runner **未启动**。

### 5. GPU 占用

PID 49165 占用 **26,692 MiB**，单卡跑满。

---
