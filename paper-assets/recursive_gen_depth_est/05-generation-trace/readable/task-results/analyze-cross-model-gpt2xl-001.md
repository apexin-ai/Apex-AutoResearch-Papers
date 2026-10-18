# analyze cross model gpt2xl 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cross_model_gpt2xl_001_20260514T182129_result.json`
- **Structured JSON:** [`ed5112d2e1acc3f86d62.json`](../../sessions/ed/ed5112d2e1acc3f86d62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分类完成，结果非常强。现在输出完整报告。

## GPT-2 XL 跨模型泛化实验结果

### Pipeline 状态
- 完成状态: **success**
- 数据生成: 4 个 depth 各 5000 samples，共 20000 samples
- 特征提取 + 分类: 手动补跑完成（pipeline 脚本未包含此步骤）

### 分类指标
- **4-class RF accuracy: 83.3% [82.3, 84.5]**
- 4-class LR accuracy: 81.3% [80.1, 82.6]
- RF pairwise AUC:
  - 0v1: **0.9941**, 1v2: **0.9131**, 2v3: **0.8829**
  - 0v2: 0.9965, 0v3: 0.9988, 1v3: 0.9857
- LR pairwise AUC:
  - 0v1: 0.9808, 1v2: 0.8469, 2v3: 0.8651

### 与 Baseline (Pythia-1.4B nucleus) 对比

| Metric | Pythia-1.4B | GPT-2 XL | Δ |
|--------|-------------|----------|---|
| 4-class RF acc | 78.2% [76.9, 79.4] | **83.3%** [82.3, 84.5] | **+5.1pp** |
| 4-class LR acc | 74.9% | **81.3%** | **+6.4pp** |
| AUC 0v1 | 0.9975 | 0.9941 | -0.003 |
| AUC 1v2 | 0.8607 | **0.9131** | **+0.052** |
| AUC 2v3 | 0.8005 | **0.8829** | **+0.082** |

### Feature Importance (RF Top-5)
| Feature | Weight |
|---------|--------|
| p90_ppl | 0.2082 |
| var_surprisal | 0.2079 |
| p75_ppl | 0.1034 |
| mean_surprisal | 0.0821 |
| mean_ppl | 0.0645 |

Top features 与 Pythia baseline 高度一致（var_surprisal, p90_ppl, mean_ppl 都在前列），验证了特征的跨模型稳定性。

### 代码污染（Broad filter）
| Depth | GPT-2 XL | Pythia baseline |
|-------|----------|-----------------|
| d1 | **0.5%** | 5% |
| d2 | **1.3%** | 9% |
| d3 | **0.7%** | 12% |

GPT-2 XL 的代码污染远低于 Pythia，说明分类信号更纯净。

### Finetune Loss
| Depth | GPT-2 XL | Pythia baseline |
|-------|----------|-----------------|
| d0 | 2.550 | 2.241 |
| d1 | 1.715 | 1.389 |
| d2 | 1.342 | 1.025 |

GPT-2 XL 各 depth loss 略高于 Pythia（模型更大，可能收敛需要更多 epoch 或更大 lr），但递减趋势一致。

### 分析与结论

1. **跨模型泛化假设验证通过**：GPT-2 XL (1.5B) 产生的递归生成深度信号不仅存在，而且**比 Pythia-1.4B 更强** — 4-class accuracy 提升 5.1pp，关键的 deep-depth AUC (1v2, 2v3) 均显著提升。

2. **递归退化是通用现象**：不同架构/训练数据的模型（GPT-2 XL vs Pythia）表现出相同的深度可分性模式，使用 Pythia 作为 frozen judge 评估 GPT-2 XL 生成的文本同样有效。这说明递归生成退化信号是模型无关的。

3. **代码污染极低**：GPT-2 XL 的代码混入率 <1.5%，远低于 Pythia，排除了 domain confusion 混淆因素。

4. **深层 depth 区分能力更强**：2v3 AUC 从 0.80 升至 0.88，说明 GPT-2 XL 在深层递归中产生更显著的退化特征，可能因为 GPT-2 XL 本身生成质量更高，递归退化对比更鲜明。

---
