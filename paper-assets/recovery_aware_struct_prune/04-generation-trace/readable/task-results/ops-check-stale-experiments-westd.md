# ops check stale experiments westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_stale_experiments_westd_20260519T101704_result.json`
- **Structured JSON:** [`c159929038e38da8626b.json`](../../sessions/c1/c159929038e38da8626b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

| # | PID | 实验名 | 进程状态 | 结果文件 | 结果 |
|---|-----|--------|---------|---------|------|
| 1 | 63783 | eval_humaneval_sft_cka_only_20_2048 | **DEAD** | 存在 | **pass@1 = 0.00%** (PATH bug，全部 `No such file or directory: 'python'`) |
| 2 | 66521 | eval_humaneval_grpo_cka_only_20_2048 | **DEAD** | 存在 | **pass@1 = 20.12%** (33/164) |
| 3 | 72393 | eval_humaneval_grpo_standard_20_fair_2048 | **DEAD** | 不存在 (.json 无, .log 停在 0%) | 旧版无结果。**替代 v3 (PID 76392) 仍在运行**，已跑 3h14m，进度 129/164，当前 pass@1 约 10% |
| 4 | 56146 | eval_math500_sft_standard_20_2048_v2 | **DEAD** | 存在 | **accuracy = 25.8%** (129/500) |

关键发现：
- 4 个旧 PID 全部已死，可安全标记为非 RUNNING
- PID 63783 的结果是废数据（v1 PATH bug），需要 v2 重跑
- PID 76392 (v3 替代) 还活着，预计还需约 30 分钟完成

---
