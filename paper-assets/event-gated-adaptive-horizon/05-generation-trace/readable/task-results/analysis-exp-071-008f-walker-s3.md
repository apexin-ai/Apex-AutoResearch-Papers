# analysis exp 071 008f walker s3

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_071_008f_walker_s3_20260525T100740_result.json`
- **Structured JSON:** [`74d39a54177cdade8998.json`](../../sessions/74/74d39a54177cdade8998.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 总结

**exp_071_008f_walker_s3: SUCCESS (borderline)**

| 指标 | 值 |
|------|-----|
| eval_return (final/peak) | 311.9 / 457.7 |
| ve_ratio (final/peak) | 0.4 / 0.7 |
| gate_dt_mean | 2.0 (fixed) |
| CIVO | **未出现** (符合预期) |

**轨迹特征**: 55-65K 达峰 (~457)，之后显著下滑至 95K 谷底 (187)，105K 部分恢复到 312。勉强过 300 线。

**008f 四 seed 汇总**:

| Seed | 结论 | final eval |
|------|------|------------|
| s1 | success | 503 |
| s2 | **negative** | 148 |
| s3 | success (borderline) | 312 |
| s4 | success | TBD |

**008f 整体稳定性判断**: 3/4 success (75%)，但方差极大 (148–503)。作为 no-dt_emb control 组，缺乏 dt embedding 的配置在后期训练稳定性上表现不佳——s2 崩溃、s3 勉强存活。这与 dt_emb 有助于训练稳定性的假设一致（尽管机制不是通过 CIVO，control 组无 CIVO 符合预期）。

---
