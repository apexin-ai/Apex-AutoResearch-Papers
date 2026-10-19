# figure fig2 norm sweep v4 final

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig2-norm-sweep-v4-final_20260521T070817_result.json`
- **Structured JSON:** [`a0cb12f26b38bdf08b29.json`](../../sessions/a0/a0cb12f26b38bdf08b29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。v4 已注册为 `art_20260521_aad88d`。

**汇总：**

| ε | n | Mean SR | SEM | vs v3 |
|---|---|---------|-----|-------|
| 0.03 | 13 (was 11) | 14.8% | ±0.4% | +seed66(11.5%), seed67(14%) |
| 0.05 | 16 (was 15) | 13.5% | ±0.4% | +seed66(11%) |
| 0.10 | 20 (was 19) | 15.5% | ±0.5% | +seed66(13.5%), seed67(14%) |
| 0.20 | 12 (unchanged) | 16.8% | ±0.6% | — |

Caption 用: `n=13/16/20/12 for ε=0.03/0.05/0.1/0.2`

脚本已保存到本地 `artifacts/fig2_norm_sweep_v4.py` 和远程 `/root/acr-vla-conformal-refinement/artifacts/`。

---
