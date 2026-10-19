# analyze eval loss mse object seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-loss-mse-object-seed42_20260522T102512_result.json`
- **Structured JSON:** [`9c43a29e0d8a54a1c9b1.json`](../../sessions/9c/9c43a29e0d8a54a1c9b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

## 结果报告

### 总体成绩
**Average success rate: 7.0% (14/200)**

### 每个 Task 的 Success Rate

| Task | Success Rate | Successes/Total |
|------|-------------|----------------|
| alphabet_soup | 0.0% | 0/20 |
| cream_cheese | 0.0% | 0/20 |
| salad_dressing | 10.0% | 2/20 |
| bbq_sauce | 10.0% | 2/20 |
| ketchup | 5.0% | 1/20 |
| tomato_sauce | **15.0%** | 3/20 |
| butter | 10.0% | 2/20 |
| milk | **15.0%** | 3/20 |
| chocolate_pudding | 5.0% | 1/20 |
| orange_juice | 0.0% | 0/20 |

### 与已知 Baseline 对比

| Method | LIBERO-Object Avg SR |
|--------|---------------------|
| VLA-only (SmolVLA) | 10.8% ± 1.3% |
| **MSE CRM (本实验)** | **7.0%** |
| Plan A obs-only CRM (K=2) | 18.3% ± 2.1% |

### 关键发现

1. **MSE CRM 甚至低于 VLA-only baseline (7.0% vs 10.8%)**——说明 MSE-trained CRM 的 correction 信号不仅没有帮助，反而在干扰 VLA 的原始动作。这是 negative result。

2. 与 Plan A obs-only CRM (18.3%) 差距巨大（-11.3pp），说明 loss function 的选择对 CRM 质量影响极大。Plan A 使用的 loss（可能是 conformal/ranking-based）远优于纯 MSE。

3. 3 个 task 完全失败 (0%)，最好的 task 也只有 15%，说明 MSE CRM 的 correction 质量普遍较差，不存在某些 task 表现好但被平均拉低的情况。

4. 无 W&B run 关联，无错误/异常，评估正常完成（EXIT_CODE=0）。

---
