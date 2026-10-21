# code pipeline format fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pipeline-format-fix_20260513T214210_result.json`
- **Structured JSON:** [`d38c669e5416139fa1b5.json`](../../sessions/d3/d38c669e5416139fa1b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

### 变更摘要

**`episode_level_collection.py` 修改（11 处）：**

1. **`label_episode()` → `classify_episode_labels()`** — 替换为与 `death_aware_labeling.classify_episode()` 一致的 3-label 方案，返回 `(label, reason, signal_source)`
2. **新增 `episodes.jsonl` 输出** — `run_task_collection()` 每个 episode 写入 prescreening 兼容格式 `{episode_idx, variation_idx, always_internal, always_deterministic}`
3. **标签统一** — 全部使用 `"det-preferred"/"internal-preferred"/"no-preference"` + `signal_source`
4. **向后兼容** — `labeled_steps.jsonl` 和 `episode_summary.jsonl` 保留，内容更新为 3-label

**端到端验证通过：**
- prescreening `episodes.jsonl`(5 episodes） → `death_aware_labeling.py` → 150 条 `sft_triples.jsonl`
- 标签分布：det-preferred=2, internal-preferred=1, no-preference=2
- `scan_reuse_episodes()` 正确识别旧格式数据
- SFT triples 包含 `signal_source` 字段

---
