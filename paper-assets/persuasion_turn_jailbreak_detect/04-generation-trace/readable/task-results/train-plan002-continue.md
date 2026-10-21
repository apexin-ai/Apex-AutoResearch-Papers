# train plan002 continue

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan002-continue_20260517T224944_result.json`
- **Structured JSON:** [`a00edf5acfdabcecb7eb.json`](../../sessions/a0/a00edf5acfdabcecb7eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 完成。最终结果：

```
K      Method                    F1       Prec     Rec      Acc      FPR@95   Δ(T-B)
─────────────────────────────────────────────────────────────────────────────────────
1      DeBERTa-FT + GRU          1.0000   1.0000   1.0000   1.0000   0.0000
1      DeBERTa-vanilla + GRU     0.9870   0.9744   1.0000   0.9868   0.0263   +0.013
1      TF-IDF + LR               1.0000   1.0000   1.0000   1.0000   0.0000

2      DeBERTa-FT + GRU          1.0000   1.0000   1.0000   1.0000   0.0000
2      DeBERTa-vanilla + GRU     0.9867   1.0000   0.9737   0.9868   0.0000   +0.013
2      TF-IDF + LR               1.0000   1.0000   1.0000   1.0000   0.0000

3      DeBERTa-FT + GRU          1.0000   1.0000   1.0000   1.0000   0.0000
3      DeBERTa-vanilla + GRU     0.9867   1.0000   0.9737   0.9868   0.0000   +0.013
3      TF-IDF + LR               1.0000   1.0000   1.0000   1.0000   0.0000

5      DeBERTa-FT + GRU          1.0000   1.0000   1.0000   1.0000   0.0000
5      DeBERTa-vanilla + GRU     1.0000   1.0000   1.0000   1.0000   0.0000   +0.000
5      TF-IDF + LR               1.0000   1.0000   1.0000   1.0000   0.0000

full   DeBERTa-FT + GRU          1.0000   1.0000   1.0000   1.0000   0.0000
full   DeBERTa-vanilla + GRU     1.0000   1.0000   1.0000   1.0000   0.0000   +0.000
full   TF-IDF + LR               1.0000   1.0000   1.0000   1.0000   0.0000
```

**Pass criteria: FAIL**（Treatment-Baseline Δ 仅 ~1.3pp，远低于要求的 5pp）

**根本原因：数据太容易分类。** TF-IDF 在所有 K 值都达到 F1=1.0，说明 jailbreak 和 benign 对话在词汇层面就完全可分。vanilla DeBERTa + GRU 也接近完美。persuasion-aware fine-tuning 无法展示增量价值，因为任务本身不需要理解说服策略就能解决。

**Checkpoints 已保存：**
- DeBERTa: `checkpoints/plan_002/deberta_multitask/best/`
- GRU Treatment: `checkpoints/plan_002/gru/treatment/best.pt`
- GRU Baseline: `checkpoints/plan_002/gru/baseline/best.pt`
- 评估结果: `results/plan_002_eval.json`

**需要更难的 benign 数据**（topic-anchored、与 jailbreak 话题对齐）才能让 treatment vs baseline 的差异显现。

---
