# research verify 006 35k ve

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_006_35k_ve_20260514T044030_result.json`
- **Structured JSON:** [`4a13854bd04192519f6d.json`](../../sessions/4a/4a13854bd04192519f6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个数据点都拿到了。

---

### 数据点 1：exp_006 (fixed_dt2) @35K

- **来源**: `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt2_v1_s1/metrics.jsonl`
- **value_mean** = 151.097
- **eval_return** = 485.331
- **v/e ratio** = 151.097 / 485.331 = **31.13%**

轨迹：@35K 31.1% → @45K 53.3% → @55K 93.3%（value 追赶 eval 的加速趋势明显）

---

### 数据点 2：exp_008a (no_subsample) @65K

- **来源**: `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample/metrics.jsonl`
- **value_mean** = 226.096
- **eval_return** = 607.981
- **v/e ratio** = 226.096 / 607.981 = **37.19%**

轨迹：@55K 37.6% (183.5/487.9) → @65K 37.2% (226.1/608.0)（v/e ratio 基本持平，value 和 eval 同步增长）

---
