# ops westd eval progress check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_eval_progress_check_20260519T071445_result.json`
- **Structured JSON:** [`3ab3a654f84cb4db0c8f.json`](../../sessions/3a/3ab3a654f84cb4db0c8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前时间 UTC 15:15（服务器本地约 15:15）。

## 汇总

| GPU | 任务 | PID | 状态 | 进度 | 中间 Acc | 显存占用 | 预估完成 |
|-----|------|-----|------|------|----------|----------|----------|
| cuda:0 | MATH-500 SFT Standard | 56146 | **运行中** | **390/500 (78%)** | 0.2543@350 | 19.3G/97.9G | ~2-3h |
| cuda:1 | HumanEval GRPO CKA-only | 66521 | **运行中** | **150/164 (91%)** | 0.2214@140 | 17.8G/97.9G | ~20-30min |
| cuda:2 | HumanEval GRPO Standard fair v3 | 76392 | **运行中** | **6/164 (4%)** | — | 16.5G/97.9G | ~4-5h |
| cuda:3 | HumanEval GRPO RASP fair | 74303 | **运行中** | **36/164 (22%)** | 0.1500@20 | 17.3G/97.9G | ~2-3h |

**结果文件**：4 个目标 JSON 均未生成。

**已完成参考**：`humaneval_sft_cka_only_20_2048.json` — pass@1 = 0.0（全挂）。

**GPU 利用率**：4 块均 97-98%，满负荷。

**cuda:1 最快完成**（~30min 内），其次 cuda:0（~2-3h），cuda:3（~2-3h），cuda:2 刚启动 12 分钟（~4-5h）。

---
