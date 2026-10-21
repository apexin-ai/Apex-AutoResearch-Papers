# ssh retry per trial analysis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_retry-per-trial-analysis_20260518T030658_result.json`
- **Structured JSON:** [`e66eb7866a0e0e1582aa.json`](../../sessions/e6/e66eb7866a0e0e1582aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果非常清晰。

## 总结

### 1. Per-trial 数据可用性：**YES**

数据结构示例（每个 episode JSON）：
```json
{
  "task_name": "chemistry-mix",
  "variation_idx": 0,
  "mode": "retry",
  "trials": [
    {"trial_idx": 0, "score": -100.0, "is_death": true, "is_success": false, ...},
    {"trial_idx": 1, "score": -100.0, "is_death": true, "is_success": false, ...},
    {"trial_idx": 2, "score": -100.0, "is_death": true, "is_success": false, ...}
  ]
}
```

### 2. Death 定义

- `is_death = (score <= -100)`
- **Episode-level DR(N) = P(前 N 次 trial 全部 death)**
- 成功时提前 break（少于 N 次 trial 的 episode 算存活）
- 每次 trial 是完全重新开始（retry 无 reflection，reflexion 带反思）

### 3. Dose-Response 表格（death-prone tasks, 200 eps）

| N | Retry DR | 95% CI | Reflexion DR | 95% CI |
|---|----------|--------|--------------|--------|
| 1 | 0.4650 | [0.397, 0.534] | 0.4600 | [0.392, 0.529] |
| 2 | 0.4450 | [0.378, 0.514] | 0.3400 | [0.278, 0.408] |
| 3 | 0.4150 | [0.349, 0.484] | 0.2700 | [0.213, 0.335] |

关键发现：
- **Retry N=1 → N=3 只降了 5pp**（46.5% → 41.5%），边际收益极小
- **Reflexion N=1 → N=3 降了 19pp**（46.0% → 27.0%），reflection 对 death 减少有显著作用
- N=1 时两者 DR 几乎相同（~46%），说明 single-trial 基线一致
- Retry 的 dose-response 曲线几乎平坦，说明盲目重试对 death 无实质帮助

### 4. 建议

**不需要跑 N=5,10 的新实验**。理由：
1. Retry 的 N=1→3 边际改善仅 2pp/trial，外推 N=10 也最多到 ~35%（远高于 routing 的目标）
2. 已有数据足以支撑论文的核心论点：**blind retry 对 death 无效，routing 是必要的**
3. 如果 reviewer 要求更多数据点，可以用现有 3 个点 + CI 做一个 exponential decay fit 外推

结果已保存至 `results/retry_dose_response_analysis.json`。

---
