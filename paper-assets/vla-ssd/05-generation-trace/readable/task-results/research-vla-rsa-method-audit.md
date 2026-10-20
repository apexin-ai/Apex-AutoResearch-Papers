# research vla rsa method audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vla_rsa_method_audit_20260516T024305_result.json`
- **Structured JSON:** [`c4be255983e87770f057.json`](../../sessions/c4/c4be255983e87770f057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/vla_rsa_method_audit.md`。

**核心结论**：

5 个脚本中，4 个使用方法 A（cross-task global + cosine + 3-phase），唯一的例外是 `rsa_siglip_only.py` 使用方法 B（within-task + euclidean + 全轨迹）。

**🔴 论文关键风险确认**：Claim 2 ("LLM degrades from 0.615 to 0.488") 是无效比较。SigLIP+Projector RSA=0.615（方法B）与 VLA RSA=0.4876（方法A）存在 3 个方法论差异（配对方式、距离度量、时序处理），0.127 的差值无法归因于 LLM。

修复：用方法 A 重算 SigLIP+Projector RSA，成本最低（只需改一个脚本）。

---
