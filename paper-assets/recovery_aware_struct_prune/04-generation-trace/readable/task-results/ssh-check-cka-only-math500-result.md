# ssh check cka only math500 result

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_cka_only_math500_result_20260522T235757_result.json`
- **Structured JSON:** [`cda96f290e7f2724f3b3.json`](../../sessions/cd/cda96f290e7f2724f3b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果找到了，文件在 autodl-tmp 下，名为 `math500_sft_cka_only_20_v4.json`（May 19 完成）。

**CKA-only SFT MATH-500 评估结果：**

| 指标 | 值 |
|------|-----|
| **Accuracy** | **29.0%** (145/500) |
| Stderr | ±2.03% |
| Natural EOS | 76.8% (384/500) |
| Truncated | 23.2% (116/500) |
| Avg response length | 673.3 tokens |
| Median response length | 242.5 tokens |

**状态：**
- 评估已完成（500/500），进程 75284 已退出
- 旧日志（`eval_math500_sft_cka_only_20.log`）只跑到 43/500 是 May 18 的早期失败尝试，`v4` 是后来成功跑完的版本
- **westd:1 GPU 空闲**：0 MiB 显存，0% 利用率

---
