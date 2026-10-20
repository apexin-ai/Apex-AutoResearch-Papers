# research data audit full

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-audit-full_20260523T102337_result.json`
- **Structured JSON:** [`dd987deb955bd7794158.json`](../../sessions/dd/dd987deb955bd7794158.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/data_audit_report.md` 并注册。

**结果：127 个定量声明，109 个验证通过，2 个不一致，16 个无法验证。**

### 2 个不一致（不要自行修改论文）：

**D1 (HIGH) — Gemma DAF CI**：论文写 [79.5%, 98.4%]，但服务器原始数据 `gemma analysis.json` 和 registry 都是 [68.79, 100.0]。CI 偏窄，可能高估 Gemma DAF 精度。需要核实 bootstrap 代码来源。

**D2 (MEDIUM) — Table 2 trained router CI**：论文写 [-16.33, -5.27]，provenance C248/C249 记录的是 [-15.25, -6.38]。点估计 -10.70 一致，定性结论不变（均未超过 always-det），但 CI 数值有偏差。

### 其他发现：
- Provenance 中 C152/C200/C233/C234 仍引用旧值 "98.2% step tie rate"，论文已正确更新为 97.4%
- §3.1 "independent seed replication ($N{=}220$) yields DAF=89.7%" 的 89.7% 精确匹配 Gemma-2-9B-it 结果，可能是 cross-model 结果被误标为 "seed replication"
- Provenance C256 (55.4±5.2%) 与论文当前文本 (54.1±5.4%) 不符，建议废弃
- C320 (partial r=0.02) 已从论文中删除但 provenance 未清理
- C323/C324 为空条目

---
