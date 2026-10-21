# analysis wilson ci complete

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wilson-ci-complete_20260515T081720_result.json`
- **Structured JSON:** [`2fbdfe2e376a4ec6062f.json`](../../sessions/2f/2fbdfe2e376a4ec6062f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 补全的分类数据
| Experiment | n | H7 | H1 | Genuine | 方法 |
|---|---|---|---|---|---|
| ISR b01 s43 | 61 | 59 | 0 | 2 | 从 registry 推导 |
| ISR b01 s44 | 89 | 77 | 0 | 12 | classify_h7.py |
| Random b01 s42 | 79 | 0 | 56 | 23 | classify_h7.py |
| Random b01 s44 | — | — | — | — | **数据丢失**（eval JSON + checkpoint 均被磁盘清理删除）|

## Registry 修正
- `plan002-additive-b01-s42`: genuine_count 25→26（原值不满足 h7+h1+gen=n）
- `plan001-exec-only-s44`: h7_count 97→98
- `exp1-random-b03-s43-r4`: h7=7→0, h1=90→89, genuine=2→3（原值和=99≠92）

## 关键统计发现

**Pooled genuine rate (Wilson 95% CI)**:
- ISR β=0.1: 17.3% [0.130, 0.227] — 3 seeds
- Random β=0.1: 17.4% [0.124, 0.238] — 2 seeds only
- Exec-only: 5.9% [0.034, 0.100]
- SFT: 93.1% [0.780, 0.981]

**Fisher exact**: ISR b01 vs Random b01 genuine rate 无显著差异 (p=1.0, OR=0.997)。ISR b01 vs SFT / Exec-only 均显著 (p<0.001)。ISR b03 vs Random b03 genuine 差异显著 (p=0.001)。

**异质性警告**: ISR β=0.1 和 Exec-only 的 H7 rate seed 间 range=0.81~1.0, variance 极高 — s44 总是 collapse 成 H7 tautology 而 s42 不会，pooled 数据掩盖了 seed 间质变。

输出文件：`artifacts/wilson_ci_complete.csv` + `artifacts/wilson_ci_complete.json`

---
