# code two sided power

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_two_sided_power_20260520T093308_result.json`
- **Structured JSON:** [`df91cdc7c7a475cdb921.json`](../../sessions/df/df91cdc7c7a475cdb921.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。三个产出文件已生成并注册：

1. **`two_sided_power.csv`** — 55 行检测率数据
2. **`two_sided_power_curves.png`** — 3-panel 图（left/right/two-sided）
3. **`dual_regime_summary.json`** — 所有 benchmark 的 crossover 在 75–90% 之间

核心发现：two-sided 检测弥补了 left-tail 在高污染下的失效——left-tail 在 25–50% 达峰后下降，right-tail 在 90%+ 才起作用，two-sided 在全范围保持高 power。

---
