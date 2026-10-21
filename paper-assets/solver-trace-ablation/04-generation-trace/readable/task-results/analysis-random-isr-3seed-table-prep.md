# analysis random isr 3seed table prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random-isr-3seed-table-prep_20260515T180802_result.json`
- **Structured JSON:** [`50e9f96d3a65ea648d82.json`](../../sessions/50/50e9f96d3a65ea648d82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入并注册。

**发现一个数据问题**：plan018-additive-random-b01-s42 在 2026-05-15 被重新分类，registry 当前值 (H1=58, H8=4, genuine=18) 与你提供的旧值 (H1=56, H8=3, genuine_strict=12) 不一致。且新值存在内部矛盾：H7+H1+H8+genuine = 80 ≠ n_proved=79，有一个 sample 被重复计数。需要排查。

**核心结论**：
- ISR pooled genuine 6.06% (14/231), dominant failure = H7 tautology (70.6%)
- Random pooled genuine 10.98% (19/173, 2-seed provisional), dominant failure = H1 embedding (65.9%)
- 两种方法的 genuine rate 都远低于 SFT baseline (~93%)，且 inter-seed variance 极大

---
