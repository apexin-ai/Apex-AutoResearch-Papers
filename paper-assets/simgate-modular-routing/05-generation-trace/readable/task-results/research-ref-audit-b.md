# research ref audit B

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-B_20260526T101527_result.json`
- **Structured JSON:** [`fecee9ee48593c9e156f.json`](../../sessions/fe/fecee9ee48593c9e156f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审核完成。报告已写入 `artifacts/ref-audit/audit_worker_B.md`。

68 条引用中发现 10 个问题：

**严重（需修复）：**
- `toolace-2025`: 第一作者姓错误 (Zhang → **Liu**)
- `agent-safetybench-2024`: 多个作者名错误 + 2 个虚构作者
- `automix-2024`: 多个作者名错误 + 缺少 7 位共同作者
- `amitai2024explaining`: 第二作者名错误 (Guy → **Yael** Septon)
- `reflexion-2023`: 缺少作者 Edward Berman
- `salt-2026`: 第三作者名错误 (David → **Qiaojing** Yan)

**轻微：**
- `dagger-2011`: 作者昵称 vs 正式名 (Drew → J. Andrew Bagnell)
- `switch-transformer-2022`: 页码 1-39 → 1-40
- `bonagiri2025check`: 作者顺序与 arXiv 不一致
- `axis-2026`: cite key 标 2026 但实际年份为 2025

**无 hallucinated paper**，所有 68 篇论文均真实存在。正文引用上下文全部正确，未发现张冠李戴。

---
