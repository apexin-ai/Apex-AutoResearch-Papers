# analysis evidence chain status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_evidence-chain-status_20260514T150201_result.json`
- **Structured JSON:** [`24287ae66924fef9b440.json`](../../sessions/24/24287ae66924fef9b440.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个产出已写入并注册。

**证据链状态摘要**
- **Claim 1** (exec-only ISR 崩塌): ✅ 完整 — FOL 3-seed (s42 partial-genuine, s43 degraded, s44 tautological) + 1000-step 单调恶化确认
- **Claim 2** (ISR β=0.1 + Goodhart): 近完整 — ISR 3/3 ✓, Random 2/3（s43 ALLOCATED 待跑），β=0.3 剂量响应 ✓, hacking taxonomy ✓, SFT 对照 ✓
- **Claim 3** (跨逻辑泛化): 进行中 — Prolog s42 双 condition 完成，s43/s44 共 4 个 cell 运行/排队中

**阻塞项**: 1 个 ALLOCATED (random-b01-s43-r2) + 2 个 RUNNING (prolog-exec s43/s44) + 2 个 PREPARING (prolog-sta s43/s44)

**Artifact IDs**: `art_20260514_8cc22c` (evidence chain), `art_20260514_552b2e` (table drafts)

---
