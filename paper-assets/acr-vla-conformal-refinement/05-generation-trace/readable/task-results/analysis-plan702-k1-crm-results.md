# analysis plan702 k1 crm results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan702-k1-crm-results_20260520T143123_result.json`
- **Structured JSON:** [`1706fda35eada72cd640.json`](../../sessions/17/1706fda35eada72cd640.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

**plan_702 的三个原始 seed 全部失败**，没有产出任何评估结果。

### 失败原因
三个 seed 都在 `src/evaluate.py:466` 崩溃，报错一致：
```
UnboundLocalError: cannot access local variable 'unc_dim' where it is not associated with a value
```
模型加载成功，但在构建评估环境时 `unc_dim` 变量未定义就被引用。

### 当前状态
代码已修复，**r2 重试已启动**（三个 seed 都在跑）：
- `eval-crm-k1-object-seed42-plan702-r2` — GPU 0, 已加载模型, 10 tasks loaded
- `eval-crm-k1-object-seed43-plan702-r2` — GPU 1, 已加载模型, 10 tasks loaded  
- `eval-crm-k1-object-seed44-plan702-r2` — GPU 2(?), 已加载模型, 10 tasks loaded

三个 r2 run 都在 ~22:32 启动，刚开始执行 rollouts，尚无结果输出（output buffer 未 flush）。10 tasks × 10 rollouts = 100 episodes/seed，预计需要 1-2 小时完成。

### 结论
**现在无法提取 metrics**——原始 run 全部 crash，r2 retry 刚开始跑。需要等 r2 完成后再分析。建议 1-2 小时后回来检查 `logs/eval_crm_k1_object_seed4{2,3,4}_plan702_r2.json`。

---
