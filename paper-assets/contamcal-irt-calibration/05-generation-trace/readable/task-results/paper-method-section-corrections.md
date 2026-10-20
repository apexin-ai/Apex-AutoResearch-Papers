# paper method section corrections

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method-section-corrections_20260516T043244_result.json`
- **Structured JSON:** [`05d26f309fb575e5bb4f.json`](../../sessions/05/05d26f309fb575e5bb4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无残留。修改汇总：

### method.md (2 处)

| 位置 | 旧 | 新 |
|------|----|----|
| L65 | `144-condition simulation sweep` + structural/practical threshold 双分类 + `AUC ≥ 0.70` | `24-condition simulation sweep (240 runs across 10 seeds)` + data-supported 语句：AUC=0.55 lowest tested, J≥50 满足标准；AUC=0.65 small J fails；lower bound open |
| L67 | `$J = 8$--$20$ models per benchmark, far below the $J \geq 50$ threshold` | `evaluates models individually or in small cohorts, yielding effective sample sizes well below the $J \geq 50$` |

### writing_plan.yaml (6 处)

| 位置 | 旧 | 新 |
|------|----|----|
| C3.summary | `structural (AUC≥0.55) vs practical (AUC≥0.70, N≥50) thresholds. LLM eval N=8-20` | `recovery successful at AUC=0.55 (lowest tested, J≥50); lower bound open. LLM eval small cohorts` |
| abstract.key_numbers | `"AUC≥0.70 threshold"` | `"AUC=0.55 recovery (lowest tested)"` |
| method 3.3 content | `a_i(θ_j - b_i + γ_k·e_{ij})` | `a_i(θ_j - b_i) + γ_k·e_{ij}` |
| method 3.4 content | `Structural vs practical thresholds` | `Recovery boundaries from sim sweep (24 conditions, 240 runs)` |
| fig_identifiability.description | `structural identifiability (AUC≥0.55), practical identifiability (AUC≥0.70, N≥50)` | `successful recovery region (AUC≥0.55, all tested N≥20). Lower bound open.` |
| results 5.3 content | `N=8-20 in LLM eval` + 无 AUC=0.55 数据 | `AUC=0.55 J≥50 meets all criteria. AUC=0.65 systematically fails at small J. LLM eval small cohorts` |

---
