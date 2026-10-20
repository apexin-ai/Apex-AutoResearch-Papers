# analysis death stats and prescreening enhance

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_death-stats-and-prescreening-enhance_20260513T184738_result.json`
- **Structured JSON:** [`16dfe125796e93d83aab.json`](../../sessions/16/16dfe125796e93d83aab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整结果

### Prescreening (8 tasks, 37 episodes)

| Task | I_mean | D_mean | Δ(D-I) | I_death | D_death | I_nd | D_nd | Δ_nd | Signal |
|------|--------|--------|--------|---------|---------|------|------|------|--------|
| chemistry-mix | -55.8 | 4.2 | **+60.0** | 3/5 | 0/5 | 10.5 | 4.2 | -6.3 | STRONG_DET |
| chemistry-mix-paint-tertiary | -37.4 | -17.4 | +20.0 | 2/5 | 1/5 | 4.3 | 3.2 | -1.1 | STRONG_DET |
| find-animal | -58.4 | 8.2 | **+66.6** | 3/5 | 0/5 | 4.0 | 8.2 | **+4.2** | STRONG_DET |
| find-living-thing | -58.4 | -16.6 | +41.8 | 3/5 | 1/5 | 4.0 | 4.2 | +0.2 | STRONG_DET |
| find-non-living-thing | 31.6 | 24.8 | -6.8 | 0/5 | 0/5 | 31.6 | 24.8 | -6.8 | NEUTRAL |
| find-plant | -58.4 | 3.2 | +61.6 | 3/5 | 0/5 | 4.0 | 3.2 | -0.8 | STRONG_DET |
| freeze | -60.0 | 2.0 | +62.0 | 3/5 | 0/5 | 0.0 | 2.0 | +2.0 | STRONG_DET |
| grow-fruit | -50.0 | 0.0 | +50.0 | 1/2 | 0/2 | 0.0 | 0.0 | 0.0 | STRONG_DET |
| **AGGREGATE** | **-42.8** | **1.1** | **+43.9** | **18/37 (48.6%)** | **2/37 (5.4%)** | **11.4** | **6.9** | **-4.5** | |

### MVP (5 tasks, 100 episodes)

| Task | I_mean | D_mean | Δ(D-I) | I_death | D_death | I_nd | D_nd | Δ_nd | Signal |
|------|--------|--------|--------|---------|---------|------|------|------|--------|
| boil | -49.8 | -19.7 | +30.1 | 10/20 | 4/20 | 0.5 | 0.4 | -0.1 | STRONG_DET |
| change-state-of-matter | -54.7 | -14.5 | +40.2 | 11/20 | 3/20 | 0.7 | 0.6 | -0.1 | STRONG_DET |
| chem-mix-secondary | -41.0 | -5.5 | +35.5 | 9/20 | 2/20 | 7.3 | 5.0 | -2.3 | STRONG_DET |
| grow-plant | 0.5 | 0.5 | 0.0 | 0/20 | 0/20 | 0.5 | 0.5 | 0.0 | NEUTRAL |
| melt | -54.7 | -14.6 | +40.2 | 11/20 | 3/20 | 0.7 | 0.5 | -0.1 | STRONG_DET |
| **AGGREGATE** | **-39.9** | **-10.8** | **+29.2** | **41/100 (41.0%)** | **12/100 (12.0%)** | **1.8** | **1.4** | **-0.4** | |

### 关键结论

**Det 优势几乎完全来自死亡回避。**

- **Death rate 差距巨大**: Internal 48.6%/41.0% vs Det 5.4%/12.0% — death filter 有效将致死率压低 ~4x
- **No-death Δ(D-I) 为负**: Prescreening **-4.5**, MVP **-0.4** — 排除死亡后，det 不仅没有优势，反而略差
- 唯一 no-death 正向的 task 是 find-animal (+4.2)，其余全部中性或负
- `find-non-living-thing` 无死亡发生，det 反而比 internal 低 6.8 分

**任务 2 确认**: 预筛脚本在 candidate 级别记录了 `lethal` 字段（line 155），但 episode 级别没有 `death_count` — 不影响分析，从 `final_score <= -100` 即可判定。

---
