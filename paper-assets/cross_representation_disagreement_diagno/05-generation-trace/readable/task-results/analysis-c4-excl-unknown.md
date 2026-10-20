# analysis c4 excl unknown

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_excl_unknown_20260514T174423_result.json`
- **Structured JSON:** [`a15615093afead185b80.json`](../../sessions/a1/a15615093afead185b80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已写入 `artifacts/c4_excl_unknown_analysis.md`。

**核心发现：**

C4 Excl. Unknown 下降的根因是 **FOL targeted repair 反效果**（-28.6pp），严重拖累了优秀的 code targeted repair（+18.2pp）：

| | Code (N=22) | FOL (N=7) |
|--|---|---|
| Targeted 优于 Blind 的 cases | 4 | 1 |
| Blind 优于 Targeted 的 cases | **0** | **3** |

**机制：** FOL targeted repair 有 60% 的概率锚定在原始错误答案上（vs code 仅 11%）。当 FOL 原始输出为 Unknown 且 GT≠Unknown 时，targeted repair 80% 保持 Unknown 不变——诊断信息反而阻止了结构性重写。

**GT=Unknown 为何掩盖了问题：** Blind repair 在 GT=Unknown 上倾向于输出确定性答案（True/False），只有 44.4% 正确；targeted 因诊断上下文更保守，巧合地有利于 Unknown，达到 66.7%。这 22.2pp 的差距掩盖了 FOL repair 的问题。

**结论：** 主要是 pipeline 问题（FOL targeted prompt 需要从"patch 原始代码"改为"以诊断为线索重写"），同时 error_side=both（0% 成功率）是方法论限制，需要在论文中讨论。

---
