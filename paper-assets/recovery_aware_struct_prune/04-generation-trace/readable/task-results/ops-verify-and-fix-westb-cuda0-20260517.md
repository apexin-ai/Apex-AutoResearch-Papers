# ops verify and fix westb cuda0 20260517

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_and_fix_westb_cuda0_20260517_20260517T143930_result.json`
- **Structured JSON:** [`b2262bc6c8b1e044a730.json`](../../sessions/b2/b2262bc6c8b1e044a730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**PID 723605 仍然存活** — eval_sft_cka_only_20 正在运行中，当前进度 176/200 (88%)，中间 accuracy = 0.6600。

**cuda:0 状态**：活跃，GPU-Util 99%，14.6GB 显存占用（PID 723610 python 进程）。

**cuda:1 状态**：grpo_random_20 (PID 719684) 仍在跑，GPU-Util 100%，73GB 显存占用。

**结果文件**：尚未生成（评估未完成）。

### 总结

| 项目 | 状态 |
|------|------|
| PID 723605 (eval_sft_cka_only_20) | ✅ 运行中，88% (176/200)，预计 ~2 分钟内完成 |
| cuda:0 | 活跃 99% — 不空闲 |
| cuda:1 / grpo_random_20 (PID 719679→719684) | ✅ 正常运行 |
| 中间 accuracy | 66.0% (150 samples 时) |

无需重新提交。eval 即将自然完成。

---
