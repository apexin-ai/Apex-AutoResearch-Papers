# analysis eval obs only object seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-obs-only-object-seed43_20260516T004714_result.json`
- **Structured JSON:** [`a9b64da6c13b4b0246ae.json`](../../sessions/a9/a9b64da6c13b4b0246ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。以下是完整分析结果：

## eval-obs-only-object-seed43 结果

### 完成状态
**10/10 task 全部完成**，EXIT_CODE=0，正常退出。

### Per-task Success Rate

| Task | SR |
|------|-----|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 10% (1/10) |
| salad_dressing | 10% (1/10) |
| bbq_sauce | 30% (3/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 0% (0/10) |
| butter | 0% (0/10) |
| milk | 10% (1/10) |
| chocolate_pudding | 40% (4/10) |
| orange_juice | 20% (2/10) |

### Overall SR: **12% (12/100)**

### vs Argmin seed=43 对比
- obs_only: **12%** vs argmin: **17%** → **-5pp，obs_only 更差**

### 两个 seed 汇总

| | seed=42 | seed=43 | Pooled |
|--|---------|---------|--------|
| obs_only | 19% | 12% | 31/200 (15.5%) |
| argmin | 12% | 17% | 29/200 (14.5%) |
| diff | +7pp | -5pp | +1pp |

### Fisher Exact Test
- **Pooled one-sided p = 0.4444**（obs_only > argmin）
- Pooled two-sided p = 0.8888
- Odds ratio = 1.08

### 结论：**NEGATIVE**

obs_only 在 object benchmark 上没有显著优于 argmin。seed=42 的+7pp优势在 seed=43 上完全没有复现（反而-5pp），pooled 200 trials 仅差1pp，p=0.44 远未达到显著性。obs_only 对 object benchmark 的改进不成立。

---
