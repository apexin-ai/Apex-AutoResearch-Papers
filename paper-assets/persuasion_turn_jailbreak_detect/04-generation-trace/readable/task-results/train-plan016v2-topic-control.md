# train plan016v2 topic control

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan016v2-topic-control_20260518T054507_result.json`
- **Structured JSON:** [`5aa7e7b4436e03fba3eb.json`](../../sessions/5a/5aa7e7b4436e03fba3eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 016v2 Topic Classification Control 实验完成。

## 结果汇总

| K | Topic Control | Persuasion (006) | Vanilla Baseline (006) |
|---|---|---|---|
| K=1 | **0.697** | 1.000 | 0.575 |
| K=2 | **0.716** | 0.990 | 0.438 |
| K=3 | **0.717** | 0.990 | N/A |
| K=5 | **0.750** | 1.000 | N/A |
| Full | **0.727** | 1.000 | 0.285 |

**结论**：Topic control F1=0.727 远低于 persuasion treatment (1.0)，但高于 vanilla baseline (0.285)。

- Topic 分类 fine-tuning 比不 fine-tuning 好（+44pp vs vanilla），说明任何 fine-tuning 都能提供一些帮助
- 但与 persuasion treatment 相比差距巨大（-27pp），证明 **persuasion-specific learning 是 cross-attack 泛化的关键驱动力**，generic classification fine-tuning 不够

标签泄漏检查：Train Cramer's V=0.228（弱），无泄漏。

**产出**：
- `src/models/deberta_topic.py` — 5-class topic model (无 intent head)
- `src/label_topics.py` — 关键词标注 + 交叉表验证
- `src/train_deberta_topic.py` — Stage 1 训练
- `src/plan_016v2_dd_eval.py` — Stage 2 + DD OOD 评估
- `checkpoints/plan_016v2_topic/` — 模型 checkpoint
- `results/plan_016v2_topic_control.json` — 完整结果

---
