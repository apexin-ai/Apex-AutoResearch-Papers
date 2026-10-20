# code d058 analysis batch

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d058-analysis-batch_20260520T201310_result.json`
- **Structured JSON:** [`9263feed839268173c94.json`](../../sessions/92/9263feed839268173c94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部完成，registry 已更新。

---

**总结**

### exp33: Strategy Prediction (plan_002 checkpoints) → DONE
plan_002 显著优于 exp16 mixed-LLM checkpoints:
- DD OOD 漏检: 31/5/26 → **0/0/1**，jb 策略准确率 14.3% → **25.7%**
- AA OOD 漏检: 63/41/66 → **1/7/1**，jb 策略准确率 6.8% → **50.1%** (+43pp)
- 各攻击策略检测率全面提升 (authority_appeal 28%→96%, emotional_manipulation 52%→95%)

### exp34: Representation t-SNE/UMAP → DONE
- 生成 6 张可视化图 (vanilla/MLM/9-class × t-SNE/UMAP)
- 保存在 `results/exp34_tsne/` (PDF+PNG+NPZ)

### exp35: Cross-Seed Ensemble → DONE
- Majority vote **从不破坏**正确预测 (broke=0 everywhere)
- 9-class ensemble: DD/FITD **F1=1.000**，AA **F1=0.981**
- jb_mlm 从 ensemble 获益最大: DD +8.6pp, AA +6.0pp (修正 30/26 个错误)
- vanilla 太弱，ensemble 无法挽救

---
