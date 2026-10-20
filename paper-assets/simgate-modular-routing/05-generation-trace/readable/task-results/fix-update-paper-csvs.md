# fix update paper csvs

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_update-paper-csvs_20260514T063526_result.json`
- **Structured JSON:** [`5c335bedb171bee59720.json`](../../sessions/5c/5c335bedb171bee59720.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。验证汇总：

**death_decomposition_preliminary.csv**
- 旧文件已重命名为 `_OLD.csv`
- 新文件 11 tasks / 245 eps（chemistry-mix 10→20 eps）
- label_dist: det_pref=86, int_pref=9, no_pref=150 — 与 registry plan-012-full 一致

**heatmap_data.csv find-non-living-thing 行**
- n: 25→40
- signal_category: `internal-preferred`→`genuine-det`
- delta_DI: -1.32→+9.58（方向反转）
- int_mean: 26.24→18.9, det_mean: 24.92→28.48
- death_rate_int=0, death_rate_det=0（不变）

两个文件已注册为 artifacts（`art_20260514_f69db2`, `art_20260514_5ea537`）。

---
