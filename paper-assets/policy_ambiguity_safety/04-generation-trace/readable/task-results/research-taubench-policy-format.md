# research taubench policy format

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_taubench_policy_format_20260520T071404_result.json`
- **Structured JSON:** [`12f03f19765a01528eb3.json`](../../sessions/12/12f03f19765a01528eb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

总结文档已写入 `artifacts/taubench_policy_format.md` 并注册为 artifact (`art_20260520_35356d`)。

核心发现：

**策略格式**：两个版本都用 markdown 文档，层级为 "角色定义 → 领域概念 → 具体操作条款"。条款以自然语言描述，嵌入条件逻辑、枚举值、数值约束。τ² 版本更结构化，增加了加粗关键词和独立 subsection。

**注入方式**：τ-bench v1 直接将 wiki.md 全文作为 system prompt；τ² 包裹在 `&lt;policy>` XML 标签中注入。Tool description 也冗余包含部分策略信息。

**评估方式**：核心是 DB state hash 比对 + 子串匹配/NL assertions。τ² 新增了 LLM judge 评估自然语言断言，适合评估歧义场景。

**对我们项目最有价值的点**：
1. 条件逻辑中的精确值（24h、枚举 reason、数字行李配额）是注入歧义的理想目标
2. Tool description 与 policy 的信息冗余可以用来制造不一致
3. 补偿条款本身就有"不主动提供"vs"用户暗示"的天然歧义
4. τ² 的 `nl_assertions` + `reward_basis` 机制可以直接复用来评估安全行为

---
