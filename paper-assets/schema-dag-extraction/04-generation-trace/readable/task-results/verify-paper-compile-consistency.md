# verify paper compile consistency

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_paper_compile_consistency_20260516T023830_result.json`
- **Structured JSON:** [`768fd2d12d04cad42d45.json`](../../sessions/76/768fd2d12d04cad42d45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 1. 编译验证

- **状态**: 通过
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf` (13页, 370KB)
- **错误**: 无
- **Warnings**: 仅 overfull/underfull hbox (可忽略) 和 `h` float → `ht` (可忽略)
- **Table within_pool 渲染**: 左侧 Regression (Slope/CI/r/p)，右侧 Quartile (Δ/CI)，底部 permutation p=0.436 脚注 — 结构正确
- **Caption**: 明确提及 "The full 80-rel condition (n=25) is underpowered for both metrics"

## 2. 交叉一致性检查

| 检查项 | 状态 | 详情 |
|--------|------|------|
| abstract 数值 vs results | 通过 | NER 0.72→0.42, RE 85.7%→50.4%, permutation p=0.44 (0.436 rounded), Δ 31.2/9.1pp, Llama r=0.725/Δ=-27pp |
| introduction 数值 vs results | 通过 | r=0.112–0.129, permutation p=0.44, merge amplification F1=0.32 vs 0.45 |
| main.tex limitations vs results | 通过 | Llama -43pp/r=0.725, CH2 Δ=-27.1/-23.9pp, floor≈0.51, slope -0.401, permutation p=0.436 |
| "3.4×" BCS amplification | 通过 | 所有 .tex 文件中已完全清除 |
| "amplification" 用法 | 通过 | 仅保留 "merge amplification"（SDGD 概念）和 "stable rather than amplifying"（否定形式） |
| 旧 CI "8.62" / "0.16" | 通过 | 无残留 |
| slope 数值一致性 (-0.449, -0.401, p=0.436) | 通过 | table + body text 一致 |
| count_40 描述 (C001约束) | 通过 | 明确标注 "40-relation subsets sampled from the 80-relation pool, not an independent schema" |

## 3. Provenance 更新

已完成以下修改：

- **C010**: 文本从 "amplify with schema scale / 3.4x" 更新为 "robust across schema sizes, slopes consistent (permutation p=0.44)"
- **C013**: 文本从 "amplify $3.4$" 更新为 "consistent across schema sizes (slope permutation p=0.44)"；evidence metric 同步更新
- **C033**: CI 从 [-0.694, -0.057] 更正为 [-0.701, -0.069]（对齐论文表格）
- **C034**: CI 从 [-0.549, -0.345] 更正为 [-0.552, -0.346]（对齐论文表格）
- **T006**: 新增 tab:within_pool 表条目，data source = `artifacts/three_way_comparison/results_unified.json`
- **_completeness.tables**: 5 → 6

---
