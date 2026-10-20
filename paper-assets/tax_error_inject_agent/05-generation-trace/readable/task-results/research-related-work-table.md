# research related work table

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related-work-table_20260514T101016_result.json`
- **Structured JSON:** [`b392a129256450e4e407.json`](../../sessions/b3/b392a129256450e4e407.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `/root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md`（63 行）。

核心对比结论：
- **PALADIN** 只覆盖 tool error，TaxEI 将注入式训练扩展到 planning + context error
- **Agent-R / ETO** 依赖自然产生的错误，TaxEI 用 taxonomy 系统化控制注入
- **Reflexion / AgentRefine** 的 recovery 信号来自 LLM 自省，TaxEI 的 recovery 来自真实环境反馈
- **ReAct** 是纯 prompt baseline，无 error training

所有信息已通过 WebSearch 交叉验证，无 [TBD] 标注。

---
