# ops urgent westd21461 check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_westd21461_check_20260516T060700_result.json`
- **Structured JSON:** [`ae3d5c3b2d2484c68daf.json`](../../sessions/ae/ae3d5c3b2d2484c68daf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验**仍在运行**，无需提取 metrics。

## 状态汇总

| 实验 | 服务器 | 进度 | 运行时间 | 预估剩余 |
|------|--------|------|----------|----------|
| w6_mistral_docred_unconstrained | westd-21461 GPU:0 | 203/998 | ~37min | ~2.4h |
| w6_mistral_docred_constrained | westd-21461 GPU:1 | 150/998 | ~31min | ~2.9h |
| w5_qwen_docred_lora_constrained_eval | westd-16980 GPU:1 | 685/998 | ~4.2h | ~1.9h |
| w6_mistral_scierc_constrained | westd-16980 | **死进程** | — | 需处理 |

## GPU 状态

| 服务器 | GPU 0 | GPU 1 |
|--------|-------|-------|
| westd-21461 | 90%, 15GB (unconstrained) | 86%, 15GB (constrained) |
| westd-16980 | **空闲 0%, 0MB** | 85%, 17GB (qwen eval) |

## 问题

`w6_mistral_scierc_constrained` registry 仍标记 RUNNING，但 westd-16980 上无对应进程（之前 xgrammar 错误崩溃）。westd-16980 GPU:0 完全空闲，可以提交新实验。

需要：
1. 将 w6_mistral_scierc_constrained 标记为 FAILED（或重新提交到 westd-21461/westd-16980）？
2. 三个运行中实验等完成后再提取 metrics。

---
