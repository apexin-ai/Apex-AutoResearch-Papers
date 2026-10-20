# analysis power and bootstrap

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_power-and-bootstrap_20260517T180833_result.json`
- **Structured JSON:** [`e5afef08a092972ce3b7.json`](../../sessions/e5/e5afef08a092972ce3b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个 JSON 已保存到 `analysis/` 目录。

**Power Analysis 总结：所有 10 个条件均 underpowered。**

| Model | Domain | n | obs Δ(pp) | disc | MDE_80%(pp) | obs_power |
|---|---|---|---|---|---|---|
| Qwen2.5-14B | FOLIO+PW | 804 | +0.25 | 30 | **1.86** | 0.057 |
| Qwen2.5-14B | StrategyQA | 60 | +3.33 | 2 | inf | 0.000 |
| Qwen2.5-14B | ARC-Chall | 60 | -1.67 | 1 | inf | 0.000 |
| Qwen2.5-14B | GSM8K | 30 | 0.00 | 0 | inf | 0.000 |
| Mistral-7B | FOLIO+PW | 60 | 0.00 | 4 | 5.94 | 0.050 |
| LLaMA-3.1-8B | FOLIO+PW | 60 | +6.67 | 6 | 9.27 | 0.335 |
| LLaMA-3.1-8B | StrategyQA | 200 | +2.00 | 14 | 4.64 | 0.206 |
| LLaMA-3.1-8B | FOLIO | 204 | -2.45 | 13 | 4.84 | 0.186 |
| DeepSeek-R1-7B | FOLIO+PW | 60 | -3.33 | 2 | inf | 0.000 |
| Qwen2.5-7B | FOLIO+PW | 60 | 0.00 | 4 | 5.94 | 0.050 |

**Bootstrap CIs：所有条件的 95% CI 均包含 0。**

- 最窄 CI：Qwen14B FOLIO+PW [-1.12, +1.62]（n=804）
- 最宽 CI：LLaMA8B FOLIO+PW [0.00, +15.00]（n=60）
- n_d ≤ 2 的条件 McNemar test 无法在任何 effect size 下拒绝 H0（MDE = inf）

---
