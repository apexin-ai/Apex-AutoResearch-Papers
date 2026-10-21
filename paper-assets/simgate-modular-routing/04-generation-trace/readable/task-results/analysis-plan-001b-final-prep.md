# analysis plan 001b final prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-001b-final-prep_20260513T215331_result.json`
- **Structured JSON:** [`e81bfd8bd6722521fe99.json`](../../sessions/e8/e81bfd8bd6722521fe99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇总：

### 预筛最终结果 (25/25 tasks)
| 分类 | 数量 |
|------|------|
| death-dominated | 19 |
| genuine-det | 5 (find-animal, identify-life-stages-1, lifespan-longest-lived, lifespan-longest-lived-then-shortest, measure-melting-point-unknown) |
| internal-preferred | 1 (find-non-living-thing) |

之前待定的 3 个 task 全是 death-dominated，方案 A 直接确认为最终方案。

### Blocking Gates 全部通过
- pipeline-format-fix ✅ — `classify_episode()` 三标签已集成，端到端验证通过
- episodes.jsonl 格式 ✅
- `--reuse_dirs` 支持跳过已完成 episodes ✅
- find-non-living-thing 40 eps 可行（max_variations=300，仅用 13%）

### 产出文件
1. `artifacts/prescreening_final_summary.json` — 25 tasks 分类总表（含 delta_nd、death rate 等完整指标）
2. `artifacts/plan_001b_revised_proposal.md` — 最终提案（15 tasks, 185 new eps, 双卡 ~7h）

**方案可提交 Director 审批。**

---
