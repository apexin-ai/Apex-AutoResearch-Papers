# research ref audit C

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-C_20260526T101534_result.json`
- **Structured JSON:** [`04566c635b0cf9b40f69.json`](../../sessions/04/04566c635b0cf9b40f69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审核完成。报告已写入 `artifacts/ref-audit/audit_worker_C.md`。

68 条 bib entry 中发现 9 条有问题：

**硬错误（5）：**
- `toolace-2025`：第一作者 "Zhang, Weiwen" → **Liu, Weiwen**
- `automix-2024`：作者列表严重错误（3 个名字拼错 + 缺少 7 位作者 + 含 1 位非作者）
- `agent-safetybench-2024`：作者列表错误（"Junhao Yang" → "Junxiao Yang"，含 3 名非作者，缺 "Hongning Wang"）
- `salt-2026`：第三作者 "David Yan" → **Qiaojing Yan**
- `reflexion-2023`：缺少作者 Edward Berman

**中等问题（2）：**
- `kadavath2022language`：作者 "Eli Tran-Geesaman" → **Eli Tran-Johnson**
- `gajcin2023counterfactual`：实为 AAMAS 2023 Doctoral Consortium 论文，非正式论文

**Venue 升级建议（2）：**
- `routellm-2024`：arXiv → 已被 ICLR 2025 接收
- `pona2025abstract`：arXiv → 已被 NeurIPS 2025 接收

无 hallucinated paper，无引用上下文错配。

---
