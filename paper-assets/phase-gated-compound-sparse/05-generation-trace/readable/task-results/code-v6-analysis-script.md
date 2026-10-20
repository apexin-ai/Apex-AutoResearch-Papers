# code v6 analysis script

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v6-analysis-script_20260514T043453_result.json`
- **Structured JSON:** [`1764628e8065160e9eb6.json`](../../sessions/17/1764628e8065160e9eb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量运行成功。

**产出：**
1. `/root/autodl-tmp/pacs/analysis/analyze_v6_complete.py` — 可运行
2. `/root/autodl-tmp/pacs/analysis/v6_analysis_results.json` — 结果 JSON

**关键发现：**
- **Table 1**: 所有 sparsity 下 gradient 都显著 >1（p=0.0000），从 s015 的 11.5x 增长到 s030 的 41.9x，确认 importance 策略下 low-phase II 远大于 high-phase
- **Table 3**: s025/s030 出现 crossover（high phase importance wins, mid/low phase random wins），s015/s020 random 全赢——低 sparsity 下 importance 策略反而让所有 phase 的 II 更高

---
