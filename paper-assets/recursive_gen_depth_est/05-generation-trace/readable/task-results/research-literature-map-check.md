# research literature map check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_map_check_20260515T050221_result.json`
- **Structured JSON:** [`931dfae914793959e461.json`](../../sessions/93/931dfae914793959e461.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已完成。总结如下：

## literature_map.yaml 更新结果

**从 10 → 33 条条目**，新增 23 篇论文。按类别覆盖：

| 类别 | 条目数 | 状态 |
|------|--------|------|
| Model collapse 理论+实证 | 13 | 充分 (Shumailov, Alemohammad, Dohmatob×3, Gerstgrasser, Drayson, Marchi, +5 recent) |
| Decoding strategies | 5 | 充分 (Holtzman, Finlayson, Garces Arias, Wiher, Basu) |
| Binary detection | 5 | 充分 (Binoculars, Fast-DetectGPT, DivEye, LOKI, GLTR) |
| Adjacent task | 2 | EditLens + DivEye 覆盖核心邻域 |
| Ordinal classification | 2 | CORAL + CLOC（DCOL 基础） |
| Watermarking | 1 | Kirchenbauer |
| Data curation | 2 | DSIR + QuRating |
| Attribution | 2 | Uchendu + Pu |
| Covariate shift | 1 | Sugiyama |
| Detection fragility | 1 | Pudasaini |

**Dream D002 要求 25+ 引用 → 33 条，全部满足。** 2024-2026 论文占 67%。

## 关键发现

1. **无直接竞争者** — 文献扫描确认，ordinal depth estimation from text 是新任务
2. **所有 5 篇 memory.md 指定论文均已入 map** (Garces Arias, Wiher, Holtzman, Shumailov, Basu)
3. **新增重要发现**：Marchi et al. (ICASSP 2025) "Heat Death" — T≠1 导致渐近退化的理论证明，直接支撑 temp09 accelerated convergence 的解释

## 产出文件

- `literature_map.yaml` — 33 条完整引用，含 cite_in 标注
- `artifacts/writing_prep_notes.md` — Related Work 骨架（4 小节）+ 每个 Claim 的支撑引用列表 + 图表 checklist + action items

---
