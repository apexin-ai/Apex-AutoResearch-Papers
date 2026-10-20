# code llama70b analysis pipeline

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama70b-analysis-pipeline_20260524T065551_result.json`
- **Structured JSON:** [`ede1070f83e5a6c3f3a7.json`](../../sessions/ed/ede1070f83e5a6c3f3a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出总结：**
- 脚本 `/root/autodl-tmp/simgate-modular-routing/src/analyze_llama70b.py` 已部署
- Dry-run 全部指标精确匹配：delta_full=29.60, delta_nd=2.84, DAF=90.4%, label_fraction=78.9%, labels=86/9/150
- 关键修复：优先读 `episodes.jsonl`（`episode_summary.jsonl` 有重复条目导致少 6 个 episode）；ratio 字段存储全精度避免 rounding 后显示偏差
- Artifact 文档写到 `artifacts/llama70b_analysis_pipeline.md`

---
