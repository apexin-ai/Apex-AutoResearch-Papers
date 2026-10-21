# code exp empirical null

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-empirical-null_20260520T095529_result.json`
- **Structured JSON:** [`197ca73854a17b6bf134.json`](../../sessions/19/197ca73854a17b6bf134.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结论是 **negative** — 假设被推翻。

**关键发现**: Bootstrap null 校准良好，bias 不是 95% flagging 的原因。

| 指标 | 期望值 | 实际值 |
|------|--------|--------|
| Mean null bias | 0 | 0.0925 (小) |
| Mean null std | 1 | 1.0021 (近乎完美) |
| KS reject rate | ~5% | 40% (24/60 cells) |

按 benchmark 分解：
- **hellaswag/mmlu** (大 benchmark, 10K+/14K+ items): KS reject rate 仅 8.3%, null 非常接近 N(0,1)
- **humaneval** (164 items): KS reject rate 75%, bias=0.16 — 有限样本效应显著
- **arc_c** (295 items): KS reject rate 58%, bias=0.15

结论：95% flagging rate 不是因为 null 分布 miscalibrated，而是 LLM response pattern 在真实数据上产生了极端的 lz* 值（远超 bootstrap null 能解释的范围）。小 benchmark 的 null 偏离 N(0,1) 更多，但偏离幅度（bias≈0.1）远不足以解释 |lz*|>>3 的观测值。

**产出**: `artifacts/empirical_null_analysis/` 下 6 个文件（2 图 + 2 CSV + 1 JSON + 1 MD），已全部注册。

---
