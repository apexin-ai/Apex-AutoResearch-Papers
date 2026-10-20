# eval plan002 sta

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan002-sta_20260514T032542_result.json`
- **Structured JSON:** [`f099a481ce474cff3692.json`](../../sessions/f0/f099a481ce474cff3692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 完成，registry 和 artifact 均已更新。

## 结果汇总

### plan002-additive-b03-s42 eval_sta.py 评估结果

| 指标 | 值 |
|------|-----|
| **prove_rate** | 18.0% (18/100) |
| **mean_isr** | 0.0257 |
| **isr_std** | 0.0742 |
| **median_isr** | 0.0 |
| **proved_only_isr** | 0.1427 |
| **max_isr** | 0.375 |
| **isr/pr ratio** | 0.1427 |

### By answer type
| Type | n | proved | prove_rate | mean_isr |
|------|---|--------|------------|----------|
| true | 34 | 7 | 20.6% | 0.0172 |
| unknown | 41 | 8 | 19.5% | 0.0422 |
| false | 25 | 3 | 12.0% | 0.0102 |

### 组件数统计（仅 proved 的 18 个样本）
| 指标 | n_components | n_necessary |
|------|-------------|-------------|
| mean | 10.67 | 1.39 |
| median | 9.0 | 2.0 |
| std | 4.49 | 1.04 |
| range | 5–24 | — |

注意：训练日志的 last100 prove_rate 是 55.3%，但 eval_sta.py 在独立测试集上仅 18%，差距很大。这可能是训练集 vs 测试集的泛化差异，或训练时 binary ISR 近似与 full STA 评估方式的差异所致。

---
