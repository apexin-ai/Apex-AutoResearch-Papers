# audit ref verify A

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-verify-A_20260526T101601_result.json`
- **Structured JSON:** [`fbb8e483237a85dbea67.json`](../../sessions/fb/fbb8e483237a85dbea67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/artifacts/ref_audit_worker_A.md`。

**核心发现汇总：**

**P0 必须修复（4 条被引用条目有严重错误）：**
1. **ren2024actorattack** — 标题伪造（实际是 "Derail Yourself"），venue 错（ICLR 2025→ACL 2025），缺 arXiv ID
2. **robey2024smoothllm** — venue 错（不在 ICML 2024，应为 arXiv/TMLR 2025）
3. **mehrotra2024tap** — 副标题伪造（"with the Pruning of Candidate Outputs"→"Automatically"）
4. **jiang2024redqueen** — 标题/年份/venue 全错（应为 ACL 2025 Findings，标题已改）

**P1 建议修复（5 条）：** metallamaguard3_2024（无独立论文）、gguard2025/lu2025xboundary（标题已更新）、chao2024jailbreakbench（venue 不完整）、song2026multibreak（ICML 2026 未确认）

**P2 清理：** 18 条未被引用条目，2 对重复（shen2025antidote、hsu2024improved 含伪造作者名）

---
