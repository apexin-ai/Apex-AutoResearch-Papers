# writing fix drayson framing consistency

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_fix_drayson_framing_consistency_20260514T235736_result.json`
- **Structured JSON:** [`ec5af42b7fd9d5aa952b.json`](../../sessions/ec/ec5af42b7fd9d5aa952b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。总结：

**修改了 6 个文件，共 20 处变更：**

| 文件 | 变更数 | 关键修改 |
|------|--------|----------|
| `paper_framing.md` | 9 | 核心差异从 "unknown proportion" 转为 "adaptive b* without validation-set tuning"；Drayson 污染设置从 "已知比例" 改为 "不假设已知（原文明确声明）"；Claim 3 降级为 Setting |
| `literature_map.yaml` | 2 | differentiation.contamination_setting 修正；our_advantages "Unknown contamination" → "Zero validation cost" |
| `artifacts/literature_diff_drayson.md` | 3 | 核心差异化重排序（#1=adaptive b*, #2=lightweight detector, #3=unknown proportion 降级为辅助）；Angle B 修正 |
| `artifacts/drayson_comparison.md` | 2 | 污染设置表修正；局限性 #2 从 "已知污染比例" 改为 "b 选择依赖 validation set" |
| `artifacts/novelty_drayson_analysis.md` | 2 | 表格修正；推荐叙事中 Angle B 修正 |
| `artifacts/_project/report/*` (2 files) | 6 | 同步以上修正到报告副本 |

**跨文件一致性确认：** 所有文件中 Drayson 相关表述现在统一为——Drayson 不假设已知比例，核心差异是 **adaptive b* without validation-set tuning** vs per-model validation-based empirical selection。"Unknown proportion" 保留为辅助差异点，不再作为 vs Drayson 的核心 claim。

---
