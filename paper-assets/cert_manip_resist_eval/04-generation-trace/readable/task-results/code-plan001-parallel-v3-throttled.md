# code plan001 parallel v3 throttled

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-parallel-v3-throttled_20260522T100712_result.json`
- **Structured JSON:** [`5cb69255742b79dc5b4a.json`](../../sessions/5c/5cb69255742b79dc5b4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本于 18:26:40 启动，运行中。当前状态：
- **6 个偶发 503** warning（全部 retry 1/5，可恢复）
- **23/126** checkpoint 已有（之前跑的）
- **103** remaining conditions
- **进程稳定**，无崩溃

预计首个新 checkpoint 在 **~19:00-19:10** 出现（10 并发共享 8 模型需约 30-40 分钟完成 300 样本的单个 condition）。

关键改进点（vs 之前崩溃的版本）：
1. **Semaphore 在 retry 间释放**：失败的模型不再阻塞其他模型
2. **全局 10 并发上限 + 15 RPS 限速**：防止 proxy 过载
3. **指数退避 retry**（2/4/8/16/32s），最多 5 次

需要我过一会儿再检查进展吗？

---
