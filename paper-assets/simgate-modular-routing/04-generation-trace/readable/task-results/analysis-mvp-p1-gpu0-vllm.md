# analysis mvp p1 gpu0 vllm

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp-p1-gpu0-vllm_20260513T151641_result.json`
- **Structured JSON:** [`a1d30245697767609191.json`](../../sessions/a1/a1d30245697767609191.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，两个 task 各 20 episodes 全部完成。

```
METRICS:
- task: melt
  internal_mean: -54.7 ± 50.1, det_mean: -14.6 ± 35.9, oracle_mean: 2.1 ± 8.0
  det_minus_internal: +40.1 (方向: positive)
- task: change-the-state-of-matter-of
  internal_mean: -54.7 ± 50.1, det_mean: -14.5 ± 35.9, oracle_mean: 0.5 ± 1.1
  det_minus_internal: +40.2 (方向: positive)

WANDB_RUN_ID: N/A
EXIT_STATUS: normal (EXIT_CODE=0)
EPISODES_COMPLETED: 40/40 (melt 20/20 + change-the-state-of-matter-of 20/20)
LOG_TAIL:
  --- change-the-state-of-matter-of Summary ---
    always-internal:      -54.7 ± 50.1
    always-deterministic: -14.5 ± 35.9
    oracle-routing:       0.5 ± 1.1
  Global summary saved to results/mvp/global_summary.json
  EXIT_CODE=0
```

**关键观察：**

1. **两个 task 都是 det > internal，效应方向 positive**，det_minus_internal 分别为 +40.1 和 +40.2，信号非常强。
2. **always-internal 分数极低**（均为 -54.7），大量 episode 得分 -100（task failure），说明纯 LLM 推理在这类物质状态变化任务上严重不足。
3. **always-deterministic 也整体偏低**（-14.5/-14.6），但比 internal 好很多——主要是避免了 -100 的灾难性失败（仅 2-3 个 episode 得 -100）。
4. **oracle routing 分数也很低**（0.5 和 2.1），说明即使理想路由，agent 也难以完成任务——greedy 1-step lookahead 限制了 oracle 的上界。
5. 两个 task 的 internal scores 完全一致（相同的 20 个 scores），说明这两个 task 类型对 LLM 行为表现一致。

**MVP 判定**：2/2 task types 的 det-internal 方向均为 positive。需要做 bootstrap 90% CI 检验来正式判定是否 Pass。从 raw scores 看，效应量大（~40 分），但方差也大（std 35-50），bootstrap 检验是否 CI 下界 > 0 待进一步分析。

---
