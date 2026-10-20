# ops check westd gpu processes

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westd_gpu_processes_20260517T132852_result.json`
- **Structured JSON:** [`ca263987ff4bc214b4f6.json`](../../sessions/ca/ca263987ff4bc214b4f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 GPU 状态汇报

| GPU | PID | 任务 | 进度 | 当前指标 | 预计完成 |
|-----|-----|------|------|---------|---------|
| **cuda:0** | 23707 | `eval_humaneval` unpruned (2048 tokens) | **119/164** (73%) | Pass@1: 0.53~0.60 | **~21:50 今晚** |
| **cuda:1** | 14556 | `eval_math500` grpo_standard_20 (v8/ckpt-50) | **96/500** (19%) | Acc@50: 0.3600 | **~明天 14:00** |
| **cuda:2** | — | **空闲** | — | — | — |
| **cuda:3** | 11896 | `eval_math500` grpo_rasp_20 (v9) | **152/500** (30%) | Acc@150: 0.3067 | **~明天 08:40** |

**关键信息：**
- **PID 校正**：rasp_20_v2 的实际 PID 是 11896（不是 11891），standard_20 的 PID 14556 正确
- **结果文件**：两个 math500 eval 都未生成最终 JSON（仅完成后写入）
- **速度**：standard_20 约 2.5 min/problem，rasp_20 约 1.9 min/problem（rasp 模型更小所以更快）
- **cuda:2 完全空闲**，可立即使用

---
