# infra verify processes

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_processes_20260516T052048_result.json`
- **Structured JSON:** [`907bc03155d2484c9b77.json`](../../sessions/90/907bc03155d2484c9b77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/process_verify_loop6.md`。核心发现：

| 进程 | 状态 | 关键信息 |
|------|------|----------|
| **bce_isocompute_v3_s42** | ✅ RUNNING | 2400/2700 步，~5 min 完成 |
| **bench_mistral_kl50_s42** | ✅ RUNNING (PID 207962) | Registry 标记 DONE(killed) 有误；MMLU 进行中 (~6%)，还需 ~30-40 min |
| **bench_dense** | ❌ FAILED | 参数解析错误：`--sparsity_mode dense` 无效，应用 `--dense` 标志。需修正后重新提交 |

**bench_dense** 立即崩溃，需修正命令重新提交。bce_isocompute_v3_s42 即将完成，届时 cuda:1 可用于 bench_dense。

---
