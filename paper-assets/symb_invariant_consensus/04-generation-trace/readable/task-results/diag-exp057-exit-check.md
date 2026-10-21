# diag exp057 exit check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp057-exit-check_20260519T041402_result.json`
- **Structured JSON:** [`d18ff3aff014b9e3fdfb.json`](../../sessions/d1/d18ff3aff014b9e3fdfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:2 已释放（0 MiB used）。

## 汇总

| 指标 | 值 |
|---|---|
| 状态 | **正常完成** (204/204) |
| SICA accuracy | 56.86% (116/204) |
| SC accuracy | 57.35% (117/204) |
| Delta (SICA - SC) | **-0.49pp** |
| Discordant pairs | b=5, c=6 (total=11) |
| McNemar p | **1.0000** (不显著) |
| cuda:2 | **已释放** |

结论：**Negative**。Mistral-7B T=0.3 上 SICA 与 SC 无显著差异，符合 capability trap 预期。Registry 已更新，tmux sessions 已清理。

---
