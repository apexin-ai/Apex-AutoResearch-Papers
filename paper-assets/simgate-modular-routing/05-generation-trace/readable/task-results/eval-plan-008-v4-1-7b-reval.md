# eval plan 008 v4 1 7b reval

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan-008-v4-1_7b-reval_20260515T204715_result.json`
- **Structured JSON:** [`8e9c946963be4da82e39.json`](../../sessions/8e/8e9c946963be4da82e39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。结果如下：

```
=== 1.7B Re-eval (unified pipeline, tokenizer-default thinking + strip_thinking) ===
Seed 42: balanced_acc=0.3870, internal_recall=0.1667, eval_loss=0.24 (from trainer)
Seed 43: balanced_acc=0.3981, internal_recall=0.2000, eval_loss=0.4363 (from trainer)
Mean: balanced_acc=0.3926±0.0055

=== 对比（旧 vs 新 pipeline）===
Seed 42: old=0.5761 → new=0.3870 (Δ=-0.1891)
Seed 43: old=0.4852 → new=0.3981 (Δ=-0.0871)
Mean: old=0.5307±0.0643 → new=0.3926±0.0055
```

**关键发现**：

1. 用与 0.6B/4B 完全相同的 generation-based eval pipeline 后，1.7B balanced_acc 从 0.5307 大幅下降到 0.3926。

2. **旧值的 confound 不止 enable_thinking** — 旧 1.7B 数据来自 Trainer 的 logit-based eval（直接检查 next-token logits），而 0.6B/4B 用的是 generation-based eval（`eval_routing_metrics.py`，自回归生成 + strip_thinking）。这是两种完全不同的 eval 方法，logit-based 天然偏高。

3. **统一 pipeline 下的 router-size 对比**：
   | Model | Seed 42 | Seed 43 | Mean |
   |-------|---------|---------|------|
   | 0.6B  | 0.6296  | 0.5593  | 0.5945 |
   | **1.7B** | **0.3870** | **0.3981** | **0.3926** |
   | 4B    | 0.5889  | 0.5352  | 0.5621 |

   1.7B 在 generation-based eval 下表现最差，远低于 0.6B 和 4B。Internal recall 极低（16.7%-20%），说明模型在生成时几乎无法产出 non-[SIMULATE] 的 internal routing 信号。

4. `eval_loss` 来自 Trainer eval（logit-based），不受 enable_thinking 影响，因此保留原值。

结果文件已保存到 `results/plan-008-v4/1_7b_seed42_reeval.json` 和 `1_7b_seed43_reeval.json`。

---
