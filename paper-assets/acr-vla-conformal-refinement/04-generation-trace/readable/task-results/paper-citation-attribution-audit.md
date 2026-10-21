# paper citation attribution audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_citation-attribution-audit_20260515T201532_result.json`
- **Structured JSON:** [`80cb54e78e019885c9d2.json`](../../sessions/80/80cb54e78e019885c9d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/citation_attribution_audit.md` 并注册。

## 结果摘要

**27 引用中：7 INCORRECT / 5 NEEDS_REVIEW / 15 CORRECT**

### 最严重的问题（Blocking）

| 引用 | 错误性质 |
|---|---|
| **chen2026reconvla** | 核心机制完全错误——论文说"多样本选择"，实际是 CQR 单流不确定性量化。三个章节都有 |
| **a2c2_2025** | 训练方式说反了——论文说"jointly with VLA"，实际 base VLA 是 frozen 的 |
| **silver2018residual** | "bounded corrections" 不存在于原文，只有 zero-initialization |
| **digflow2025** | "regularizes denoising trajectory" 错误——实际是 representation-level gating |
| **pan2025drc** | decay 机制描述完全错误（不是 episode-level 衰减） |
| **zhou2025acp_cbf** | bib 作者错误 (Zetian Zhou → Hao Zhou) |
| **zollo2025vla_calibration** | bib 作者名错误 (Matteo → Thomas) |

chen2026reconvla 和 a2c2_2025 是最高优先级修正项，因为它们影响论文的 positioning 叙事。

---
