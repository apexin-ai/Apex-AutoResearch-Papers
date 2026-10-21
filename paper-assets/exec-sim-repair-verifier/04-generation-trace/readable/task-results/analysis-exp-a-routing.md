# analysis exp a routing

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-a-routing_20260519T030014_result.json`
- **Structured JSON:** [`113bfb0eb753243c665b.json`](../../sessions/11/113bfb0eb753243c665b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**Oracle routing = 100%**（7个CLS config覆盖全部48 variant），但实用routing策略受限于N=48样本量，最佳实用结果是 test-count heuristic 85.42% (+4.17pp)。

| Strategy | Acc | vs Best |
|---|---|---|
| Best single CLS | 81.25% | baseline |
| Oracle (7 CLS) | 100.00% | +18.75pp |
| Oracle (best pair) | 95.83% | +14.58pp |
| Test-count heuristic | **85.42%** | **+4.17pp** |
| Agreement confidence | 83.33% | +2.08pp |
| Majority/weighted vote | 75-79% | negative |

**缺失数据**: TRAJ per-variant 预测不存在（eval脚本未保存，需GPU重跑），无法做CLS+TRAJ跨formulation routing。CWM repo-level 太弱(45-52%)，仅比best CLS多救回1个variant。

**结论**: Routing的oracle potential很大（+18.75pp），但在N=48上难以实现可靠的practical routing。建议在paper中作为analysis/discussion point呈现互补性发现，而非核心贡献。如要强化routing故事，需先重跑TRAJ eval保存per-variant数据。

---
