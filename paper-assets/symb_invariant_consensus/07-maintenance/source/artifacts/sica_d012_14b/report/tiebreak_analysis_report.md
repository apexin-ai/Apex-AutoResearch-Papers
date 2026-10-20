## Tiebreak Baseline Analysis (D017 Task 3)

**60 题中 5 题出现平局（top-2 候选票数相同）**

### 策略对比

| Method | Accuracy | 95% CI | Correct/Total |
|--------|----------|--------|---------------|
| **SICA (constraint-weighted)** | **80.0%** | — | **4/5** |
| Random (bootstrap 10k) | 50.0% | [0.0, 100.0] | — |
| Alphabetical | 60.0% | — | 3/5 |
| First-seen | 40.0% | — | 2/5 |
| Majority-of-first-6 | 60.0% | — | 3/5 |

### SICA Wins（4题）
- P11: False vs Unknown 各5票，SICA分数 145.5 vs 127.0，margin=18.5 → 选 False ✓
- P29: False vs Unknown 各6票，SICA分数 3.0 vs 33.0，margin=30.0 → 选 Unknown ✓
- P42: Unknown vs False 各6票，SICA分数 45.0 vs 46.0，margin=1.0 → 选 False ✓
- P59: False vs Unknown 各6票，SICA分数 61.0 vs 64.0，margin=3.0 → 选 Unknown ✓

### SICA Loss（1题）
- P03: True vs Unknown 各6票，SICA分数 102.0 vs 105.0，delta=3.0 → 选了 Unknown，实际答案 True

### 关键发现
- SICA 的 margin 分布：30.0 / 18.5 / 3.0 / 1.0（wins）vs 3.0（loss）
- 唯一 loss 的 margin 仅 3.0，属边界情况
- SICA 比 SC 多对 2 题（44/60 vs 42/60 = +3.3pp）

Source: results/tiebreak_analysis.json on westd-32608