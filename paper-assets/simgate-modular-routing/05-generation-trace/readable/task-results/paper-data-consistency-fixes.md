# paper data consistency fixes

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_data-consistency-fixes_20260521T094505_result.json`
- **Structured JSON:** [`2dbee96b728ae25e5cda.json`](../../sessions/2d/2dbee96b728ae25e5cda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功（24 pages, 无错误）。旧数字已全部清除。

---

## 修复结果汇总

### Fix 1 (MATH label 分布) — 已修复
- **来源**: `analysis_n800.json` (N=795)
- **旧值**: Det%=12.0, Int%=13.5, NoPref%=74.6
- **新值**: Det%=7.3, Int%=8.3, NoPref%=84.4
- **修改位置**:
  - `main.tex` L509 (Table L.1)
  - `experiments.tex` L80 (§5.4 MATH 段落)
  - `figures/gen_signal_reversal.py` L27-29 (图表数据)

### Fix 2 (Gemma DAF CI) — 无需修改
- `unified_episode_bootstrap.json` (B=10000) 给出 CI = [79.5%, 98.4%]，**与论文完全一致**
- `gemma_scienceworld_counterfactual/analysis.json` 中的 [68.8%, 100.0%] 是用不同 bootstrap 方法独立计算的结果，非权威来源

### Fix 3 (Step counts) — 已修复
- **来源**: 245-episode `episodes.jsonl`, 逐 episode 计算 aligned step comparison
- **旧值**: 5,726/5,878 (97.4%)
- **新值**: 5,667/6,094 (93.0%)
- **原因**: 245 vs 194 episodes; `find-non-living-thing` (40 ep, 76.9% tie rate) 拉低整体——该 task 无死亡，策略间中间分数差异较大
- **修改位置**:
  - `method.tex` L14 (§3.2 主段落)
  - `method.tex` L75 (§3.5 scope 段落)
  - `introduction.tex` L10, L15 (两处引用)
  - `main.tex` L121 (Appendix B labeling audit)

---
