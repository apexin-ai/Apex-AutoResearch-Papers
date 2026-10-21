# research paper update checklist

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-update-checklist_20260519T220548_result.json`
- **Structured JSON:** [`3fbdda7ae0a4be545df2.json`](../../sessions/3f/3fbdda7ae0a4be545df2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成并注册。

**清单概要**：~35 项改动，覆盖 abstract 到 appendix 全部 section。

**P0（15 项，提交前必须完成）**：
- V-recovery 双种子确认 → abstract、Table 1、discussion 三处同步更新
- GSM8K 结果整合（待 eval）→ results 加 negative control 段 + abstract 一句
- Algorithm 1 v2 伪代码与 profile_classifier.py 一致性验证
- experimental_setup seed/checkpoint 数更新
- 所有 Figure 数据源确认（aligned evaluate.py 版本）
- Sensitivity 描述 30→180 更新
- DiD 数据版本确认

**P1（20 项，锦上添花）**：s123 cross-family 数据扩展、domain decomposition 图表、Fisher Info 推导、reference audit 等。

---
