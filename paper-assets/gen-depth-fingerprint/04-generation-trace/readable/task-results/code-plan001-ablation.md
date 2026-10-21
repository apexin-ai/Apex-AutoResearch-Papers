# code plan001 ablation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-ablation_20260514T181555_result.json`
- **Structured JSON:** [`0228b794280e5041dcb7.json`](../../sessions/02/0228b794280e5041dcb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Dry-run 结果摘要：**

| Part | 状态 | 关键结果 |
|------|------|----------|
| A | ✅ | full (0.693) > surface_only (0.589) > reference_only (0.455)；full vs ref 显著 (p=0.022) |
| B | ✅ | entropy_mean/ttr/hapax_ratio 有 moderate trend (R²=0.35-0.39)；其余特征 H1 attractor |
| C | ✅ | PPL 随 depth 单调递减 (13.1→1.3)；Kruskal-Wallis p=0.0047 显著 |

脚本位于 `/root/gen-depth-fingerprint/ablation_analysis.py`，dry-run 产物已清理，results/ 目录只剩 `mvp_results.json`。正式运行去掉 `--dry-run` 即可。

---
