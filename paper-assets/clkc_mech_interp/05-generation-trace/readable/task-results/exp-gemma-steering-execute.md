# exp gemma steering execute

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemma-steering-execute_20260524T082115_result.json`
- **Structured JSON:** [`163fae85f169973eed65.json`](../../sessions/16/163fae85f169973eed65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三层全部完成。汇总报告：

---

## Gemma-2-9B-IT Steering 结果（position=last）

**Baseline 分布（所有层共享）**: N=88, neither=24, both=43, contextual=20, parametric=1

---

### Layer 17（probe acc = 66.48%）

| alpha | steer_flip_pct | ctrl_flip_pct | fisher_p |
|-------|---------------|---------------|----------|
| -20 | 0.0% | 0.0% | 1.0000 |
| -10 | 0.0% | 0.0% | 1.0000 |
| -5 | 0.0% | 0.0% | 1.0000 |
| +5 | 0.0% | 0.0% | 1.0000 |
| +10 | 0.0% | 0.0% | 1.0000 |
| +20 | 0.0% | 0.0% | 1.0000 |

Best alpha: 无（全部零 flip）。Bonferroni (k=6, p<0.0083): **不显著**。

---

### Layer 16（probe acc = 59.66%）

| alpha | steer_flip_pct | ctrl_flip_pct | fisher_p |
|-------|---------------|---------------|----------|
| -20 | 0.0% | 0.0% | 1.0000 |
| -10 | 0.0% | 0.0% | 1.0000 |
| -5 | 0.0% | 0.0% | 1.0000 |
| +5 | 1.1% | 0.0% | 1.0000 |
| +10 | 0.0% | 0.0% | 1.0000 |
| +20 | 0.0% | 1.1% | 1.0000 |

Best alpha: +5（1 steering flip vs 0 control），但 p=1.0。Bonferroni: **不显著**。

---

### Layer 18（probe acc = 61.93%）

| alpha | steer_flip_pct | ctrl_flip_pct | fisher_p |
|-------|---------------|---------------|----------|
| -20 | 2.3% | 0.0% | 0.4971 |
| -10 | 2.3% | 0.0% | 0.4971 |
| -5 | 1.1% | 0.0% | 1.0000 |
| +5 | 0.0% | 0.0% | 1.0000 |
| +10 | 0.0% | 0.0% | 1.0000 |
| +20 | 1.1% | 0.0% | 1.0000 |

Best alpha: -20 或 -10（各 2 steering flips vs 0 control，p=0.497）。Bonferroni: **不显著**。

---

### 总结

三层 steering 全部失败。最好情况是 L18 alpha=-20/-10 的 2/88 flips（2.3%），p=0.497，远不及 Bonferroni 阈值 0.0083。注意所有 flip 的 p2c 和 c2p 都是 0——flip 发生在 neither/both 之间，不在 parametric↔contextual 之间。

核心问题：probe accuracy 本身很低（60-66%），说明这些层的线性探针方向可能不足以捕获 parametric vs contextual 的区分信号，导致沿该方向做 steering 无效。加上 baseline 中 parametric 只有 1 个样本，模型几乎不产出 parametric 回答，steering 的上行空间极其有限。

---
