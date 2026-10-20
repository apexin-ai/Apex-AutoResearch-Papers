# eval plan006 scrambled dd

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan006-scrambled-dd_20260517T232936_result.json`
- **Structured JSON:** [`4f8c637934c0d5ebcf63.json`](../../sessions/4f/4f8c637934c0d5ebcf63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。结果：

| K | Scrambled F1 | Treatment F1 | Baseline F1 | Delta(Scr-Bas) |
|---|---|---|---|---|
| full | 0.9809 | 1.0000 | 0.2845 | +0.6964 |
| 1 | 0.9904 | 1.0000 | 0.5752 | +0.4152 |
| 2 | 0.9350 | 0.9904 | 0.4381 | +0.4969 |
| 3 | 0.9350 | 0.9904 | 0.3596 | +0.5754 |
| 5 | 0.9904 | 1.0000 | 0.3105 | +0.6799 |

**结论：Scrambled 和 Treatment 几乎一样好（F1 均 >0.93），远超 Baseline。** 这意味着 DeBERTa multi-task fine-tuning 本身就足以产生 DD 上的跨攻击泛化能力，正确的 persuasion labels 不是关键因素。即使 labels 被打乱，fine-tuning 过程仍然让 DeBERTa 学到了区分 jailbreak 和 benign 的有效特征。

结果已保存到 `results/plan_006_scrambled_dd_eval.json`。

---
