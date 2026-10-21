# analysis plan 001b gpu1

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-001b-gpu1_20260514T014310_result.json`
- **Structured JSON:** [`e53b7a1042dd697caa6a.json`](../../sessions/e5/e53b7a1042dd697caa6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总结果：

## plan-001b-gpu1 结果

| Task | Eps | Int Mean | Det Mean | Δ(int-det) | Int Deaths | Det Deaths | Det-pref | Int-pref |
|------|-----|----------|----------|------------|------------|------------|----------|----------|
| find-non-living-thing | 20 | 24.90 | 24.95 | **-0.05** | 0 | 0 | 7 | 4 |
| grow-fruit | 20 | -43.65 | -18.55 | **-25.10** | 9 (6 exclusive) | 4 (1 exclusive) | 6 | 1 |
| inclined-plane | 20 | -55.00 | -19.00 | **-36.00** | 11 (7 exclusive) | 4 (0 exclusive) | 7 | 0 |
| identify-life-stages-2 | 20 | -48.40 | -18.40 | **-30.00** | 10 (6 exclusive) | 4 (0 exclusive) | 6 | 0 |

**关键发现**:
1. **find-non-living-thing 预筛信号未复现** — 5 eps 显示 internal-preferred，20 eps 后本质持平（delta=-0.05），且 det-pref 反而多（7 vs 4）。原计划的 follow-up 到 40 eps 可能不再必要。
2. **3 个 death-dominated task 全部确认** — internal router 单侧死亡数远高于 det（exclusive death: 6/6/7 vs 1/0/0），alive 时两者得分都很低且接近。
3. 所有 80 episodes 数据完整，无错误。

---
