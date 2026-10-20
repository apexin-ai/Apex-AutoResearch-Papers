# ops start eval batch1 cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_start-eval-batch1-cuda2_20260518T221718_result.json`
- **Structured JSON:** [`37e0e794ded992fdff00.json`](../../sessions/37/37e0e794ded992fdff00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。

| 项目 | 状态 |
|------|------|
| cuda:2 | 已占用，PID 69890，17672MiB |
| 父进程 PID | 69878 |
| Backend | HF（vllm 不可用，fallback SDPA） |
| 当前进度 | 第 1 个 adapter `Qwen2.5-7B_d000_s42` 模型加载完成，开始 eval (mmlu + arc_challenge) |
| Adapters 队列 | d000_s42 → d000_s123 → d005_s42 → d005_s123 → d025_s42（共 5 个） |
| 日志 | `/root/autodl-tmp/exp001/eval_vllm/batch1.log` |

---
