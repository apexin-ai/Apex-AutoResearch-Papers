# eval plan 004 v5 routing

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan-004-v5-routing_20260514T082118_result.json`
- **Structured JSON:** [`3a8203eed14420c8a5fe.json`](../../sessions/3a/3a8203eed14420c8a5fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 结果汇总

**plan-004-v5 Generation-based Routing Eval**

| 指标 | plan-004-v5 | ablation-b | 判定 |
|------|------------|-----------|------|
| accuracy | 53.3% | 65.4% | ❌ |
| balanced_accuracy | 41.5% | 59.3% | ❌ |
| **internal_recall** | **26.7%** | 51.5% | **❌ < 30%** |
| det_recall | 56.3% | — | — |
| internal_precision | 6.3% | — | — |

**Confusion Matrix:**
```
             det    int
  det       152    118
  int        22      8
```

**结论：negative**。internal_recall=26.7% 低于 30% 判定线，全面落后 ablation-b。

**关键发现：** Logit-level metrics（训练时 Trainer eval: internal_recall=84.9%）与 generation-based eval（26.7%）严重不一致。模型在 teacher-forcing 下能区分路由，但自回归生成时无法可靠输出 `[SIMULATE]` 前缀。三种 thinking 模式（on/off/strip）结果完全一致，排除 thinking mode 为根因。

这与 plan-002-generative-v1 是相同的失败模式，说明 implicit router 的 generative routing 方案本身存在系统性问题。Registry 已更新（conclusion → negative，metrics 含两级 eval 数据）。

---
