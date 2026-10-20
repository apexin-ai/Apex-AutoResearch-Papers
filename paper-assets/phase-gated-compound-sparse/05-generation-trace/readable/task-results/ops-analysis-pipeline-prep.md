# ops analysis pipeline prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_analysis_pipeline_prep_20260514T214639_result.json`
- **Structured JSON:** [`b20e1dec21bdbdcba40a.json`](../../sessions/b2/b20e1dec21bdbdcba40a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/analysis_pipeline_audit.md`。

核心结论：

**最佳脚本**: `analyze_c2_n500.py` — 95% 就绪，B=10000 已正确，有 d_z CI。**仅需 1 处修改**：删除 `format_report()` 中的 Imp/Rand ratio 列（lines 285-300），违反 D031/D033。

**实验进度**: 4/16 条件完成（每个模型的 s015），s020 正在跑，s025/s030 排队中。

**发现的约束违规汇总**：
- `analyze_c2_n500.py`: ratio 显示 (D031/D033) — 1 处修改
- `analyze_n500.py`: B=1000 无 d_z CI + d_z 对 random 也算了 (D059) — 3 处修改
- `analyze_n500_unified.py`: B=1000 + d_z 对 random 也算了 — 2 处修改

---
