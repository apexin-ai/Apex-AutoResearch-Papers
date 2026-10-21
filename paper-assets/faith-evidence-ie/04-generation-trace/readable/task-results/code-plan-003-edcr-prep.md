# code plan 003 edcr prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_003_edcr_prep_20260515T221504_result.json`
- **Structured JSON:** [`834dd1dfe2f18c128fe0.json`](../../sessions/83/834dd1dfe2f18c128fe0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，结果如下：

**plan_003 EDCR 代码状态: ✅ 就绪**

两个脚本存在且完整：
- `scripts/edcr_diagnostic.py` — 主诊断工具（347行），含 per-relation / per-document EDCR 分析 + LaTeX 输出
- `eval/cross_method_table.py` — 简版跨方法汇总表

依赖链完整：`evaluator.py` 提供 `compute_edcr`/`compute_f1`/`compute_evi_f1`/`_triple_key`，全部 14 个 AUTO_METHODS 的 predictions.json 已在磁盘上，数据格式匹配。

**阻塞项：flat-NLI s44 + s45**
- 目前只有 flat-NLI s42 和 s43 的 eval 结果
- s44/s45 训练+eval 完成后需要：
  1. 产出 predictions.json
  2. 在 `edcr_diagnostic.py` 的 `AUTO_METHODS` 列表中添加这两个条目
  3. 然后跑 `python -m freige.scripts.edcr_diagnostic --auto-discover`

除了补充 s44/s45 条目（两行代码），不需要其他开发工作。

---
