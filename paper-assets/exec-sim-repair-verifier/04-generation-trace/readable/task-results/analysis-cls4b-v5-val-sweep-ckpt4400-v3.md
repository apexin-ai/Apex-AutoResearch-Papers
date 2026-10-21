# analysis cls4b v5 val sweep ckpt4400 v3

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls4b-v5-val-sweep-ckpt4400-v3_20260515T032054_result.json`
- **Structured JSON:** [`81ac40fc38bfa06e254e.json`](../../sessions/81/81ac40fc38bfa06e254e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。总结如下：

---

## cls4b-v5-val-sweep-ckpt4400-v3 结果

**状态**: 成功完成，EXIT_CODE=0，运行 ~70 分钟 (4217s batch time, 1.24 GPU-hours)

### 关键指标

| 指标 | 值 |
|------|-----|
| Accuracy | **89.96%** |
| F1 macro | **84.94%** |
| F1 fail | 76.25% (P=88.8%, R=66.8%) |
| F1 pass | 93.64% (P=90.2%, R=97.3%) |
| Majority baseline | 75.88% |
| Gap vs majority | +14.09pp |
| Samples | 9335 (pass=7083, fail=2252) |
| Truncated | 234/9335, Unparseable: 0 |

### Val Sweep 对比 (cls4b-v5, val@5120)

| Checkpoint | Accuracy | F1 macro | F1 fail | F1 pass |
|-----------|----------|----------|---------|---------|
| ckpt-600 | 82.82 | 79.81 | 72.03 | 87.60 |
| ckpt-4000 | 89.84 | 84.25 | 74.85 | 93.64 |
| **ckpt-4400** | **89.96** | **84.94** | **76.25** | **93.64** |

ckpt-4400 在所有指标上优于 ckpt-4000：accuracy +0.12pp, f1_macro +0.69pp, f1_fail +1.40pp。提升主要来自 fail 类的 recall 改善。f1_pass 持平。

### 关于 v1/v2 CUDA hang

v3 未修改 watchdog，使用完全相同的代码和参数，顺利跑完 9335 个 sample，**确认 v1/v2 的 CUDA hang 是低概率间歇性事件**，而非代码/数据层面的系统性问题。RTX 5090 驱动稳定性仍需关注，但不阻塞实验。

### 对 D063 val sweep 的影响

ckpt-4400 是目前 val sweep 中的 **best checkpoint**（acc 和 f1_macro 均最高）。训练从 ckpt-600 → ckpt-4000 → ckpt-4400 持续改善，尚未出现过拟合迹象。ckpt-4200 和 ckpt-4600 仍在 QUEUED，跑完后可确认曲线趋势——如果 ckpt-4600 继续提升，val-best 可能还会后移。

---
