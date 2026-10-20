# research paper materials

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-materials_20260512T172304_result.json`
- **Structured JSON:** [`7f632487e94de3e6bb7a.json`](../../sessions/7f/7f632487e94de3e6bb7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成，产出保存在 `artifacts/_project/report/paper_materials.md`。

关键发现：
- **Claim 2（per-test ≈ trajectory 等价性）证据最充分**，TOST + clustered bootstrap + ICC 齐全，可直接写
- **Claim 1（complexity-dependent advantage）函数级方向正确但统计力度不足**——缺 CLS vs CWM paired bootstrap（数据已有未跑），repo-level 是决胜关键
- **Claim 3（oracle frontier）证据丰富但 oracle 分析基于模拟**，需明确标注
- **最大阻塞项**：repo-level 训练结果（P0），所有其他缺失项（paired bootstrap、effect size、图表）都可立即推进

---
