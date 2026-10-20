# paper diagnosis text fixes

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_diagnosis-text-fixes_20260524T115254_result.json`
- **Structured JSON:** [`25d5ab43000729468a29.json`](../../sessions/25/25d5ab43000729468a29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修正已完成：

**修正 1 (L51)** — 选择方案 B：
- 原文：`Among instruction-tuned models, $\kappa$ ranges from 0.19 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.94$.`
- 新文：`Among non-thinking instruction-tuned models, $\kappa$ ranges from 0.19 to 0.82 ($K_{\text{eff}} = 1.20\text{--}3.94$); thinking-mode Qwen3 reaches $\kappa = 0.91$ ($K_{\text{eff}} = 1.09$).`

选 B 的理由：下一句 "K_eff ≤ 1.30 never improves" 正好覆盖 thinking-mode 的 1.09 案例，显式标注使论证链更清晰。

**修正 2 (L139)** — 移除 "gradient" 和 "weaker models suffer more"：
- 原文：`The bias ratio gradient ($4.97\times$ Mistral $> 3.85\times$ Qwen $> 2.88\times$ LLaMA) suggests weaker models suffer more severe confirmation bias; all models exceed $1.0$, a pattern that persists from 7B open-source to frontier closed-source (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb}).`
- 新文：`Bias ratios exceed $1.0$ across all three families ($4.97\times$ Mistral-7B, $3.85\times$ Qwen2.5-14B, $2.88\times$ LLaMA-3.1-8B); the ordering does not follow a strict capability gradient (LLaMA-3.1-8B shows lower BR than Qwen2.5-14B despite lower SC accuracy). This pattern persists from 7B open-source to frontier closed-source (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb}).`

---
