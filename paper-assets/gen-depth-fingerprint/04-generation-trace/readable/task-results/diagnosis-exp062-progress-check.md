# diagnosis exp062 progress check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp062_progress_check_20260521T115923_result.json`
- **Structured JSON:** [`29f95af365aa8bf8c12a.json`](../../sessions/29/29f95af365aa8bf8c12a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/analysis/exp062_progress_report.txt`。

**当前状态**：4 张 GPU 全部在跑，5/16 combo 已完成，4/16 进行中，7/16 排队。

关键进展：
- **pythia-2.8b** 和 **olmo-2-1b** 的 greedy+topk 全部完成
- **pythia-1b** greedy 完成，topk 在跑（67%，~22min）
- **qwen3-1.7b** greedy 即将完成（97%，~6min），之后开始 topk
- **llama-3.2-3b** 和 **mistral-7b-v0.3** 都在 greedy 阶段（57%，各需 ~1.5h）
- **qwen3-0.6b** 和 **qwen3-8b** 排在 cuda:3 的 chain 队列中，等 pythia-1b 完成后启动

**瓶颈**：cuda:3 任务最重——pythia-1b topk 结束后还要跑 qwen3-0.6b 和 qwen3-8b 各两种策略，预计全部完成需 ~6-7h。其他三张卡各需 ~3-5h 完成剩余的 greedy+topk。

---
