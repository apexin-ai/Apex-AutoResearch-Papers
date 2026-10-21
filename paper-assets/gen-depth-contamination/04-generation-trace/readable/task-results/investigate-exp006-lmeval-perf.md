# investigate exp006 lmeval perf

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_exp006-lmeval-perf_20260514T050129_result.json`
- **Structured JSON:** [`55acf39204af23b0c714.json`](../../sessions/55/55acf39204af23b0c714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了 `num_fewshot` 默认为 0（lm-eval evaluator.py:338-342: "if num_fewshot not provided, and the task does not define a default one, default to 0"）。所有数据已收集完毕。

---

```
batch_size: auto (lm-eval 自动寻找最大可用 batch size，已是最优)
device: cuda:0 (hardcoded in exp006_evaluate.py:29)
num_fewshot: 0-shot (MMLU 和 HellaSwag 均为 0-shot，task yaml 和代码均未设 num_fewshot，lm-eval 默认 0)
eval_tasks: ["mmlu", "hellaswag"]（MMLU 展开为 57 个子任务 + 4 个 group 聚合，HellaSwag 1 个，无其他 benchmark）
actual_eval_time: 7.6 min（10 个已完成 run 均值 7m38s，标准差 <5s，极其稳定）
optimization_possible: 否，当前配置已接近最优
99min_explanation: 误算。eval 实测 7.6min 而非 58min，99min 估算中的 eval=58min 是错误的
```

**详细数据**：

| Run | Train (s) | Eval (s) | Total run-to-run |
|-----|-----------|----------|-----------------|
| no-filter_s42 | 2178 (36.3m) | 458 (7.6m) | — |
| no-filter_s123 | ~2196 | 454 | 44m14s |
| no-filter_s456 | ~2196 | 462 | 44m11s |
| no-filter_s789 | ~2196 | 457 | 44m05s |
| no-filter_s1024 | ~2196 | 457 | 44m05s |
| binary-ours_s42 | 2243 (37.4m) | 461 | — |
| binary-ours_s123 | ~2241 | 459 | 45m14s |
| binary-ours_s456 | ~2241 | 455 | 49m04s |
| binary-ours_s789 | 2240 (37.3m) | 460 | 45m15s |
| binary-ours_s1024 | ~2240 | 461 | 45m13s |

**结论**：
- `batch_size=auto` 已是最优，lm-eval 自动搜索 GPU 可容纳的最大 batch
- 0-shot 已是最快 fewshot 设置，无需降
- eval 仅占 run 总时长的 ~17%，训练才是瓶颈
- 99min 估算是错的：真实 pace 约 44-45 min/run，与 Monitor Worker 的 45.2min 估算吻合

---
