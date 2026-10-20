# train phase b pilot

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_phase-b-pilot_20260517T161130_result.json`
- **Structured JSON:** [`b458570de3d87ead58e5.json`](../../sessions/b4/b458570de3d87ead58e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase B Mini Pilot 端到端 pipeline 验证完成。

---

### 结果汇总

```
=== Phase B Pilot Results (N=270, test=41) ===

Full Conversation:
  Treatment (DeBERTa-FT + GRU): F1=1.000, FPR@95TPR=0.000
  Baseline (DeBERTa-vanilla + GRU): F1=0.737, FPR@95TPR=0.000
  TF-IDF + LR:                      F1=1.000

Early Detection:
  K=2: Treatment=1.000, Baseline=0.737, TF-IDF=0.894
  K=3: Treatment=1.000, Baseline=0.894, TF-IDF=0.894
  K=5: Treatment=1.000, Baseline=0.894, TF-IDF=0.894
```

### 关键发现

1. **Pipeline 端到端跑通** — DeBERTa multi-task → embedding extraction → GRU classifier 全链路正常
2. **DeBERTa Stage 1** — 5 epoch 后 persuasion acc 0.718, intent acc 0.984 (best at epoch 4)
3. **Treatment 完美分类** — 小数据集上 F1=1.0，包括 K=2（仅前 2 轮）
4. **Baseline 明显弱于 treatment** — vanilla DeBERTa 的 GRU F1=0.737，主要问题是把 benign 误分为 jailbreak（benign 只有 3 条 test 样本，命中 1 条）
5. **TF-IDF baseline 出乎意料地强** — full conversation F1=1.0，但 early detection (K=2) 降到 0.894

### 注意事项

- Test set 只有 41 条（3 benign + 38 jailbreak），结果不具统计显著性
- Treatment 的完美分数可能反映数据太少 + 类别不平衡，而非方法的真实上限
- Baseline 训练时磁盘满导致提前终止（epoch 29/50），但 best.pt 已保存
- 下一步应扩充 benign 数据以获得更可靠的评估

---
