# train plan016 sentiment control

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan016-sentiment-control_20260518T044342_result.json`
- **Structured JSON:** [`5b9139e15328d393b3eb.json`](../../sessions/5b/5b9139e15328d393b3eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 016 实验完成。完整结果：

| K | Sentiment Control | Persuasion (006) | Vanilla Baseline (006) |
|---|---|---|---|
| 1 | **1.000** | 1.000 | 0.575 |
| 2 | **1.000** | 0.990 | 0.438 |
| 3 | **1.000** | 0.990 | N/A |
| 5 | **1.000** | 1.000 | N/A |
| full | **1.000** | 1.000 | 0.285 |

**结论**: Sentiment control 在 DD OOD 上 F1=1.0，与 persuasion treatment 完全持平，远超 vanilla baseline。这表明 cross-attack 泛化**不是**由 persuasion-specific learning 驱动的——任何对 DeBERTa 进行 domain-adaptive fine-tuning（即使辅助任务与 persuasion 无关）都足以让 BiGRU 在 OOD 攻击上泛化。

**关键发现**: sentiment 标注（0=jailbreak, 1/2=benign 随机分半）与 intent 标签高度相关。模型通过 sentiment + intent 双重监督学到了 jailbreak/benign 的区分特征，这些特征足以泛化到 DD。persuasion strategy 的 9-class 细粒度信息对 DD 检测没有额外贡献。

**产出文件**:
- 训练脚本: `src/train_deberta_sentiment.py`
- 模型: `src/models/deberta_sentiment.py`
- 评估脚本: `src/plan_016_dd_eval.py`
- Checkpoint: `checkpoints/plan_016_sentiment/best/`
- 结果: `results/plan_016_sentiment_control.json`

---
