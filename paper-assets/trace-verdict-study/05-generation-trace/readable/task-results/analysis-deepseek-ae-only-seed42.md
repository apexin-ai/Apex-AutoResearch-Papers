# analysis deepseek ae only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_ae_only_seed42_20260519T230949_result.json`
- **Structured JSON:** [`4432adb16eb87e6d3e75.json`](../../sessions/44/4432adb16eb87e6d3e75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## deepseek_ae_only_seed42 实验结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | **98.74%** (95% CI: [98.07%, 99.33%]) |
| **Eval Loss** (epoch 2) | 0.1585 |
| **Eval Loss** (epoch 3, final) | 0.1934 |
| **Train Loss** (average) | 0.0694 |
| **Train Loss** (last step) | 0.0221 |

**Per-class metrics:**

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| pass | 0.984 | 0.999 | 0.991 |
| fail | 0.997 | 0.959 | 0.977 |

**Checkpoint:** `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_ae_only_seed42/final/` — confirmed (adapter_model.safetensors ~153MB + tokenizer + config)

**注意:** eval_loss 从 epoch 2→3 略升（0.1585→0.1934），存在轻微过拟合，但 accuracy 依然强劲。

---

### Tier 1 (ae_only) 跨模型对比

| Model | Accuracy | 结论 |
|-------|----------|------|
| Qwen-7B | 99.92% | ✓ |
| CodeLlama-13B | 99.08% | ✓ |
| **DeepSeek-6.7B** | **98.74%** | ✓ |

**Conclusion: SUCCESS.** 98.74% >> 95% 阈值。Tier 1 (ae_only) 在全部 3 个模型上均 ≥ 95%，**universality 得到验证**。MF2 表 Tier 1 行完成。

---
