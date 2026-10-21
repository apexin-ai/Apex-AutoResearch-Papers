# analysis plan 004 eval metrics

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-004-eval-metrics_20260514T060351_result.json`
- **Structured JSON:** [`f183ab8a9b423be832c4.json`](../../sessions/f1/f183ab8a9b423be832c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是汇报：

## plan-004 Eval Metrics

### 训练配置
- 模型: Qwen3-1.7B + LoRA (r=16, alpha=32), trainable 6.4M / 1.73B (0.37%)
- 数据: train 1735, val 305 (split 15%), deterministic:internal = 1555:180
- Upsampling: WeightedRandomSampler 启用
- 3 epochs, batch_size=4, lr=2e-5, max_seq_len=2048

### Training Loss Curve

| Epoch | train_loss (avg of steps) | eval_loss |
|-------|--------------------------|-----------|
| ~1 | 5.25→4.77→3.14→1.60→0.97 | **0.7151** |
| ~2 | 0.71→0.54→0.47→0.40→0.41 | **0.3928** |
| ~3 | 0.41→0.35→0.33→0.30→0.31 | **0.3609** |

Overall train_loss (mean): 1.2555

### Classification Report

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|----|---------|
| **deterministic** | 0.9196 | 0.6703 | 0.7754 | 273 |
| **internal** | 0.1589 | 0.5152 | 0.2429 | 33 |

- **Overall accuracy**: 0.6536 (200/306)
- **Macro F1**: 0.5091
- **Balanced accuracy**: 0.5927
- **is_degenerate**: false

### Confusion Matrix

|  | Pred DET | Pred INT |
|--|----------|----------|
| **True DET** | 183 | 90 |
| **True INT** | 16 | **17** |

### 关键问题

1. **internal recall > 0?** — **是，0.5152**。退化问题已解决，模型确实在预测 internal 类（17/33 correct）。
2. **但 internal precision 极低 (0.1589)** — 模型把 90 个 deterministic 样本误判为 internal（false positive 率高）。这说明模型过度生成 `[SIMULATE]` token。
3. **deterministic recall 下降到 0.67** — 相应地有 33% 的 deterministic 被误分为 internal。
4. **与 plan-002 explicit router 对比**：
   - plan-002 是分类头直接输出 logits，precision/recall 通常更平衡
   - plan-004 implicit 是生成式（causal LM 生成 `[SIMULATE]` token），天然更容易出现 precision-recall 不平衡
   - Balanced accuracy 0.59 表明模型确实学到了区分信号，但 macro F1 0.51 说明整体分类质量偏低
5. **Qwen3 的 `&lt;think>` tag** 需要在推理时 strip 掉再检测 `[SIMULATE]`（eval 已处理）

---
