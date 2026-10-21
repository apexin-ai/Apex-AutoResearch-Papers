# code dual ood f1 calc

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dual_ood_f1_calc_20260522T233122_result.json`
- **Structured JSON:** [`1a05e4c4177f82e4ca8b.json`](../../sessions/1a/1a05e4c4177f82e4ca8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。在 `appendix.tex` 的 `\label{app:oasst2}` section 末尾（`tab:benign_summary` 之后）插入了 `\subsection{Estimated Dual-OOD Detection Performance}`（`\label{tab:dual_ood}`），包含：

| Benign condition | DD OOD F1 | AA OOD F1 |
|---|---|---|
| IID (FPR=0) | .994±.009 | .981±.019 |
| WildChat, no adapt | .855±.020 | .842±.012 |
| OASST2, no adapt | .874±.009 | .861±.018 |
| WildChat + 10-shot | .994±.009 | .981±.019 |
| OASST2 + 25-shot | .991±.009 | .978±.018 |

核心结论：无 adaptation 时 dual-OOD F1 下降 12-14pp（由 benign FP 驱动），few-shot adaptation 后恢复到 IID upper bound 的 0.3pp 以内。

---
