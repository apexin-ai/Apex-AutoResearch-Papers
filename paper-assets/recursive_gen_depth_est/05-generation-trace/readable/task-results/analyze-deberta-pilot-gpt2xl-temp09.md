# analyze deberta pilot gpt2xl temp09

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_deberta_pilot_gpt2xl_temp09_20260519T172248_result.json`
- **Structured JSON:** [`8b5d19e70f2e23d8cf5a.json`](../../sessions/8b/8b5d19e70f2e23d8cf5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No W&B logging, no checkpoints saved. I have all the data needed. Here's the full analysis:

---

## DeBERTa Pilot 实验结果

**Conclusion: success** — 实验正常完成（EXIT_CODE=0），hypothesis 被强烈验证。

### 关键指标

| Metric | Value |
|--------|-------|
| **4-class accuracy** | **53.14% ± 1.97%** (5-fold CV) |
| Balanced accuracy | 53.14% |
| **Macro-F1** | **0.484** (从 confusion matrix 计算) |
| Total time | 7467s (~2h) |

### Per-fold accuracy

| Fold | Acc | Bal-Acc | Time |
|------|-----|---------|------|
| 1 | 0.5152 | 0.5152 | 3457s |
| 2 | 0.5178 | 0.5177 | 766s |
| 3 | 0.5617 | 0.5617 | 1243s |
| 4 | 0.5142 | 0.5142 | 757s |
| 5 | 0.5483 | 0.5483 | 1242s |

### Per-class metrics（从 confusion matrix 计算）

| Class | Recall | Precision | F1 |
|-------|--------|-----------|-----|
| d0 | 0.812 | 0.900 | 0.854 |
| d1 | 0.288 | 0.538 | 0.375 |
| d2 | 0.084 | 0.265 | 0.128 |
| d3 | 0.942 | 0.419 | 0.581 |

### Confusion matrix（rows=true, cols=predicted, 每类 5000 样本）

```
        d0    d1    d2    d3
d0    4060   909     6    25
d1     366  1439   974  2221
d2      64   242   420  4274
d3      22    85   183  4710
```

### 与 RF baseline 对比

| | DeBERTa (LoRA) | RF + 19 features |
|--|---|---|
| 4-class acc | **53.1%** | **78.2%** |
| Gap | — | **+25.1pp** |

**Hypothesis 强烈成立**：DeBERTa-v3-base (LoRA) 4-class accuracy (53.1%) 远低于 RF+19-feature baseline (78.2%)，差距 25 个百分点。Hand-crafted perplexity-distribution features 对 depth signal 的捕捉远优于 neural text representations。

### 失败模式分析

模型严重偏向极端类：d0 和 d3 recall 高（81%/94%），但中间类 d1 (29%) 和 d2 (8%) 几乎分不出来。Confusion matrix 显示 d1→d3 (2221) 和 d2→d3 (4274) 存在大量误分类——模型倾向于将中间深度预测为 d3。这说明 DeBERTa 的文本表征无法区分中间递归深度的细微差异，而 RF 的 perplexity distribution features 可以。

### 文件路径

- **log_path**: `~/runs/recursive_gen_depth_est/deberta_pilot_gpt2xl_temp09.log`
- **results_json**: `/root/autodl-tmp/recursive_gen_depth_est/results/deberta_pilot/gpt2xl_temp09/results.json`
- **checkpoint_path**: 无（未保存 checkpoint）
- **W&B**: 未使用

### 模型配置

- Model: `microsoft/deberta-v3-base`
- LoRA: r=8, alpha=16, query_proj+value_proj
- Trainable params: 297,988 / 184.7M (0.16%)
- Samples: 20,000, 5-fold CV, 5 epochs

---
