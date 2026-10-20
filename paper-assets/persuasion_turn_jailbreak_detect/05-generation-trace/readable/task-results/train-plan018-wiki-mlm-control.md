# train plan018 wiki mlm control

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan018-wiki-mlm-control_20260518T055948_result.json`
- **Structured JSON:** [`f874ca9b1c32ddf563e1.json`](../../sessions/f8/f874ca9b1c32ddf563e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 018 全部完成。

## 结果总结

**Hypothesis confirmed**: Wikipedia MLM 显著弱于 jailbreak-domain MLM，证明 domain-specific text exposure 是 OOD 泛化的关键因素。

| 方法 | DD OOD F1 (full) | DD OOD F1 (k=1) |
|---|---:|---:|
| Jailbreak MLM (017) | **1.000** | **1.000** |
| Persuasion treatment (006) | **1.000** | **1.000** |
| **Wikipedia MLM (018)** | **0.742** | **0.822** |
| Vanilla baseline (006) | 0.285 | 0.575 |

关键发现：
- Wikipedia MLM（F1=0.74）远低于 jailbreak-domain MLM（F1=1.0），**domain specificity 是必要的**
- Wikipedia MLM 仍高于 vanilla baseline（F1=0.29），说明 generic continued pretraining 提供部分提升
- IID 性能依然高（F1=0.99），说明分类能力本身没受损，问题出在 OOD 域适应

**产出文件**：
- 数据: `data/plan_018_wiki_mlm/{train,val}.jsonl` + `stats.json`
- 训练脚本: `src/train_deberta_mlm_wiki.py`
- 评估脚本: `src/plan_018_wiki_dd_eval.py`
- 结果: `results/plan_018_wiki_mlm_control.json`
- Checkpoint: `checkpoints/plan_018_wiki_mlm/best/`

---
