# diagnose exp 008d s4 exit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_008d_s4_exit_20260518T051555_result.json`
- **Structured JSON:** [`a92c38c43875a1495f0e.json`](../../sessions/a9/a92c38c43875a1495f0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## exp_008d_civo_trigger_s4 — SUCCESS ✓

| 指标 | 值 |
|---|---|
| 最终 step | 112K (目标 105K) |
| 错误 | 无 |
| CIVO 触发 | **确认** (ve_ratio=3.03, alert=1.0) |
| Checkpoint | latest.pt (231MB) |

**Eval return 轨迹**:
```
 5K:  30.9
15K: 171.4
25K: 189.5
35K: 153.8
45K: 158.2
55K: 229.3
65K: 333.6
75K: 302.4
85K: 383.3  ← peak
95K: 240.3  ← 开始下降
105K:  63.6  ← 崩塌，CIVO alert 触发
```

**CIVO 特征**: eval_return 从峰值 383.3 崩塌至 63.6 (跌幅 83%)，同时 value_mean 仍高达 192.65，NVE (ve_ratio) = 3.03 >> 1.5× 阈值。经典 value overestimation 导致策略崩塌。

**Seed 4 与前序 seeds 一致**，Walker CIVO 现象在 4 个 seed 上全部复现。

---
