# paper claim strength audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_claim-strength-audit_20260516T075150_result.json`
- **Structured JSON:** [`c77ebada0e0f497cbb1c.json`](../../sessions/c7/c77ebada0e0f497cbb1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件在 `artifacts/claim_strength_audit.md`，已注册 (`art_20260516_0b4bf1`)。

核心发现：
- 10/13 阴性实验已被 results.tex 引用，叙事角色清晰
- **关键缺口**：exp_016e（梯度分解 + reward-only SGS = no-op）完全未写入论文，是 Framing B 最强机制证据
- 未验证假说：obs decoder 梯度通路是 CIVO 驱动源（exp_018 QUEUED）；跨环境泛化（exp_010a RUNNING）

---
