# code 3 label labeling update

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_3-label-labeling-update_20260513T202829_result.json`
- **Structured JSON:** [`414182c63e43f70a6b47.json`](../../sessions/41/414182c63e43f70a6b47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 结果

**`death_aware_labeling.py`** — 三标签方案完成：
- `classify_episode()` 返回 `(label, reason, signal_source)`，不再有 discard
- 标签：`det-preferred` / `internal-preferred` / `no-preference`
- `signal_source` 四种值：`death_asymmetry` / `both_dead` / `score_comparison` / `tied_alive`
- `labeling_summary.json` 包含 `episode_labels`、`signal_sources`、`step_labels` 三维分布

**`episode_level_collection.py`** — 两处 `steps.append` 均已添加 `is_dead: score_after <= DEATH_THRESHOLD`（line 91, 181）

**Dry-run (find-non-living-thing)**：
| 标签 | Episodes | Steps |
|---|---|---|
| det-preferred | 2 | 60 |
| internal-preferred | 1 | 30 |
| no-preference | 2 | 60 |

5 episodes 全部有 label，无 discard，signal_source 全部正确（2x `score_comparison` + 2x `tied_alive` + 1x `score_comparison`）。符合预期。

---
