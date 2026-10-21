# analysis seed comparison prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed_comparison_prep_20260516T021842_result.json`
- **Structured JSON:** [`a5471f66326019e20073.json`](../../sessions/a5/a5471f66326019e20073.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。汇总：

## 脚本修复项（已完成）
1. **CED s42**：`rsft_r2b` → `rsft_r2b_maxtok1536`（f1=0.4504，匹配你给的数据）
2. **CED s43**：添加 fallback `["rsft_ced_s43", "rsft_s43"]`，优先用新 eval
3. **CED s45**：`rsft_s45` → `rsft_ced_s45`
4. **`all_complete`**：`== 3` → `== 4`（4 seeds）
5. **missing 状态**：分开追踪 CED/flat-NLI 缺失的 seeds
6. **Per-seed 表格**：改为 markdown table 格式

## 当前已有 metrics

| 方法 | s42 | s43 | s44 | s45 |
|------|-----|-----|-----|-----|
| CED RSFT | 0.4504 ✓ | 0.4683 ✓ | 0.4655 ✓ | 空（pending） |
| flat-NLI RSFT | 0.4539 ✓ | 0.4523 ✓ | 空（pending） | 空（pending） |

## 还缺什么
- **CED s45** (`rsft_ced_s45`)：目录空，eval 未产出
- **flat-NLI s44** (`rsft_flat_nli_s44`)：目录空
- **flat-NLI s45** (`rsft_flat_nli_s45`)：目录空

5/8 已完成，还差 3 个 eval 结果。当前 2 个 matched pairs 的初步统计 p=0.638，不显著——但 n=2 完全不够，等 4 seeds 齐了才有意义。

---
