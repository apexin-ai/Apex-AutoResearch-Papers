# diagnose mvp2 eval ced kl001 r4 multi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp2_eval_ced_kl001_r4_multi_20260514T212003_result.json`
- **Structured JSON:** [`b44bbbbd34352e39730f.json`](../../sessions/b4/b44bbbbd34352e39730f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断摘要：

**失败原因：** 进程在 ckpt-30 eval 完成后按 Director 指令被外部 kill，非异常崩溃。监控检测到 dead process 后 auto-resolved as FAIL。

**已完成 eval 的 6 个 checkpoint：**

| Checkpoint | F1 | Evi-F1 | EDCR |
|---|---|---|---|
| ckpt-10 | 0.003 | 0.720 | 0.998 |
| ckpt-20 | 0.009 | 0.423 | 0.995 |
| ckpt-30 | 0.034 | 0.589 | 0.980 |
| ckpt-50 | 0.156 | 0.564 | 0.886 |
| ckpt-60 | 0.147 | 0.576 | 0.906 |
| ckpt-90 | **0.211** | 0.567 | 0.858 |

**未完成：** ckpt-40（中断，目录为空）、ckpt-70/80（未执行）

F1 整体随 step 单调上升，best = ckpt-90 (F1=0.211)。EDCR 随 step 下降（模型逐步学会过滤 distractor citations）。

---
