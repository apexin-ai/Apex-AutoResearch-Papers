# fix experiments ece advantages

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_experiments_ece_advantages_20260517T065121_result.json`
- **Structured JSON:** [`8bbd794dd69d84c2704f.json`](../../sessions/8b/8bbd794dd69d84c2704f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改已完成，验证通过。

**1. ECE 段删除（原 lines 62-68，共 7 行 + 1 空行）**

删除内容：
- `\paragraph{Expected Calibration Error (ECE).}` 及其完整定义（公式、bins 说明、`\cite{calibration2025}` 引用）
- 上下文衔接正常：HellaSwag 段 → 空行 → `\subsection{Experimental Conditions}` 直接过渡
- grep "ECE" 返回空，确认清除干净

**2. Spectral advantages 修正（现 line 186）**

原文三条合并为两条：
- 原 (1) "no labeled evaluation set or external benchmark" + 原 (2) "no held-out evaluation set or text generation" → 新 **(1)** "they require no text generation, labeled benchmarks, or external evaluation sets, only a single forward pass through a small unlabeled probe set ($\sim$1K sequences)"
- 原 (3) → 新 **(2)** "they provide a geometric interpretation..."
- "three" → "two"

消除了与 setup 中 "1,000 held-out sequences" 的矛盾（现在明确说的是 "unlabeled probe set"，不再声称 "no held-out evaluation set"）。

---
