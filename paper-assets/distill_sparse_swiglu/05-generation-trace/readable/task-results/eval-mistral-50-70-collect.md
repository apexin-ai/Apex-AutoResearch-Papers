# eval mistral 50 70 collect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mistral_50_70_collect_20260517T010355_result.json`
- **Structured JSON:** [`e6761ebd80c6fa299910.json`](../../sessions/e6/e6761ebd80c6fa299910.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results collected. 70% TEAL baseline PPL = 61.7160.

## 完整结果表

| Sparsity | KL per_token | KL teal_global | TEAL baseline | Dense |
|----------|-------------|----------------|---------------|-------|
| 0% | — | — | — | **5.5238** |
| 30% | **6.0480** | 6.7733 | 8.3807 | — |
| 50% | **7.2931** | 8.6489 | 18.3061 | — |
| 70% | **9.1086** | 13.3254 | 61.7160 | — |

**说明：**
- **KL per_token**: 使用 predictor 对每个 token 动态生成 sparse mask
- **KL teal_global**: 使用 predictor 生成 importance score 后用 TEAL 的全局阈值方式决定 mask（静态 calibrated mask）
- **TEAL baseline**: 无 predictor，vanilla TEAL 方法（原始 activation magnitude 阈值）

**关键观察：**
- 30% sparsity: KL per_token 仅比 dense 高 0.52 PPL (+9.5%)，TEAL baseline 高 2.86 (+51.8%)
- 50% sparsity: KL per_token 比 TEAL baseline 好 11.0 PPL（7.29 vs 18.31）
- 70% sparsity: KL per_token 比 TEAL baseline 好 52.6 PPL（9.11 vs 61.72），predictor 优势在高 sparsity 下急剧放大

70% 训练最终 loss=0.3945, 实际 sparsity=0.682, 1000 steps 完成。

---
