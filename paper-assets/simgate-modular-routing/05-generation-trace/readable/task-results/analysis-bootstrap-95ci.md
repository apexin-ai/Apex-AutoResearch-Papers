# analysis bootstrap 95ci

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-95ci_20260514T125452_result.json`
- **Structured JSON:** [`d36782e3bd770705b0f2.json`](../../sessions/d3/d36782e3bd770705b0f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W5 完成。对照表：

| Condition | Mean | 90% CI (old) | 95% CI (new) |
|-----------|------|-------------|-------------|
| always-internal | -39.07 | [-44.89, -33.37] | **[-46.40, -32.27]** |
| always-det | -9.47 | [-13.66, -5.11] | **[-14.71, -4.29]** |
| oracle | -6.58 | [-10.65, -2.43] | **[-11.54, -1.70]** |
| random | -22.38 | [-27.75, -17.09] | **[-28.67, -15.75]** |
| trained-router | -10.70 | [-15.25, -6.38] | **[-16.33, -5.27]** |

修改内容：
- `analysis.py`、`eval_end_to_end.py`、`eval_implicit_router.py` 中 `ci=0.90` → `ci=0.95`，注释/标签中 `90% CI` → `95% CI`
- `death_decomposition.py` 已经是 `BOOTSTRAP_CI = 0.95`，无需修改
- 结果保存：服务器 `results/bootstrap_95ci.json` + 本地 artifacts + registry `plan-003-bootstrap-95ci`

---
