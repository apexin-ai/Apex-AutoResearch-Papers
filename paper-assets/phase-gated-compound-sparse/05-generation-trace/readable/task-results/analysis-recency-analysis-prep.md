# analysis recency analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_recency_analysis_prep_20260516T230743_result.json`
- **Structured JSON:** [`5bb1985f639784212b08.json`](../../sessions/5b/5bb1985f639784212b08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 总结

脚本已就绪：`/root/autodl-tmp/pacs/scripts/analyze_recency_results.py`

**用法：**
```bash
/root/miniconda3/bin/python3 scripts/analyze_recency_results.py --dry-run     # 仅检查数据可用性
/root/miniconda3/bin/python3 scripts/analyze_recency_results.py               # 运行完整分析
/root/miniconda3/bin/python3 scripts/analyze_recency_results.py --output analysis_output/recency_comparison.json  # 保存 JSON
```

**当前状态：** recency_s015 已完成，s025/s030 仍在运行。

**初步结果（s015）：**
- Recency phase gradient: median_diff = -0.0026, d_z = +0.083 (negligible), p = 0.77 (NS)
- Importance phase gradient (n500 s015): median_diff = +0.39, d_z = +0.574 (medium), p < 1e-70
- Random phase gradient (n500 s015): median_diff = +0.014, d_z = -0.045 (negligible), p = 0.86 (NS)

**初步判断：好消息。** Recency gradient 不显著，行为与 random 一致，远弱于 importance。支持 "phase-dependent severity 是 attention-score-based eviction 特有交互效应" 的假设。等 s025/s030 完成后重跑确认 dose-response 一致性。

---
