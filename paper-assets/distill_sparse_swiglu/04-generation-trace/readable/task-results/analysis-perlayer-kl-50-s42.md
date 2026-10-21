# analysis perlayer kl 50 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_50_s42_20260522T065424_result.json`
- **Structured JSON:** [`b5b07012c1377a77b306.json`](../../sessions/b5/b5b07012c1377a77b306.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

### 训练状态：正常完成
- 10000/10000 steps，EXIT_CODE=0，耗时 ~5.06 小时
- 最终 avg_kl=0.0282，model-level sparsity=0.496（32层均接近0.50目标）

### Eval PPL（已完成）
**WikiText-2 PPL = 34.85**

### Baseline 对比

| 方法 | Sparsity | PPL | vs E2E KL |
|------|----------|-----|-----------|
| E2E KL 50% | 50% | 11.84 | — |
| MSE 50% | 50% | 18.52 | +56% |
| **Per-layer KL 50%** | **50%** | **34.85** | **+194%** |

### 结论：**NEGATIVE**

假设被证伪。Per-layer KL 在 50% sparsity 下 PPL 灾难性退化（34.85），远差于 E2E KL（11.84）和 MSE（18.52）。2D 分解（signal type × coupling scope）在 50% sparsity 下不成立——coupling scope 成为主导因素，层间 mask 协调在高 sparsity 下不可或缺。

Per-layer KL 的 U-shaped KL 分布（早期层 0.041–0.055，中间层 0.018–0.024）也表明各层压缩难度差异大，但 per-layer 独立训练无法利用层间互补来缓解这一问题。

### 待完成
- Downstream eval（arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa）仍在运行中（`perlayer_kl_50_s42_downstream`），目前在跑 MMLU
- Analysis 已写入 artifact，registry 已更新 metrics + conclusion=negative

---
