# analysis verify fisher pvalue

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify-fisher-pvalue_20260516T155600_result.json`
- **Structured JSON:** [`99f5c4d6dfa8b1f946a4.json`](../../sessions/99/99f5c4d6dfa8b1f946a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果明确了。让我总结。

## 验证结果

### 每 seed 实际 N
所有 JSON 文件确认 `n_rollouts=10`，10 tasks → **每 seed N=100 trials**（非 200）。

验证来源：
- `eval_object_obs_only_norm02.json`: n_rollouts=10, SR=0.22 → 22/100
- `eval_object_obs_only_norm02_seed43_r2.json`: n_rollouts=10, SR=0.16 → 16/100
- ROADMAP seed44: 16/100 (文件不在 bjb1-32546，已在 D040 记录)

### 正确的 pooled counts

| Seed | obs_only | argmin | N |
|------|----------|--------|---|
| 42 | 22/100 (22%) | 12/100 (12%) | 100 |
| 43 | 16/100 (16%) | 17/100 (17%) | 100 |
| 44 | 16/100 (16%) | 13/100 (13%) | 100 |
| **Pooled** | **54/300 (18%)** | **42/300 (14%)** | **300** |

### Fisher exact test (one-sided, obs > argmin)

```
Table: [[54, 246], [42, 258]]
Fisher exact p (one-sided) = 0.1102
```

### 差异解释

| 来源 | p 值 | 原因 |
|------|------|------|
| `pooled_fisher_test.py` | **0.035** | KNOWN_DATA 错误地将所有计数翻倍（N=200/seed），如 22→44, 16→32, 12→24 等。108/600 vs 84/600 |
| ROADMAP "p≈0.091" | **0.091** | 使用了 **chi-square test（无 Yates 校正）** 而非 Fisher exact test。χ²=1.786, p_one=0.0907 |
| Fisher exact（正确） | **0.110** | 正确数据 54/300 vs 42/300，Fisher exact one-sided |

### 根因

`pooled_fisher_test.py` 的 `KNOWN_DATA` 将每个 seed 的 success 和 total 都乘了 2（假设 n_rollouts=20），导致 N 从 300 膨胀到 600。比例不变但样本量翻倍，人为缩小了 p 值。

ROADMAP 的 p≈0.091 则是因为使用了 chi-square 近似而非 Fisher exact test。用 Fisher exact test 计算正确数据得到 p=0.110。

**结论**：3-seed pooled Fisher exact p = 0.110，未达 α=0.05 也未达 α=0.10。等 seed45 做 4-seed pooled 是正确策略。

---
