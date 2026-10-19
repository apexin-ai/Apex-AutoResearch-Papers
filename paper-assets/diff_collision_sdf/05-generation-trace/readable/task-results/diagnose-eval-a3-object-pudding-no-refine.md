# diagnose eval a3 object pudding no refine

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_a3_object_pudding_no_refine_20260521T202157_result.json`
- **Structured JSON:** [`75b10e8ca18af722eba2.json`](../../sessions/75/75b10e8ca18af722eba2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败根因**：Eval进程未在tmux中运行，SSH会话超时后进程被SIGHUP静默杀死。训练任务 `a3_spatial_bowl` 正确地在tmux session中，但所有eval重试都是裸SSH启动，无持久化保护。dmesg无OOM记录，日志无任何错误——纯粹是进程管理问题。

**次要问题**：eval默认跑GPU 0（与训练争抢），GPU 1完全空闲。

**修复**：用tmux启动eval + `CUDA_VISIBLE_DEVICES=1` 指向空闲GPU。产出已写入 `artifacts/worker_output.md`。

---
