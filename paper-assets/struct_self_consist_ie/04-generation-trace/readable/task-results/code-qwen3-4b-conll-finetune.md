# code qwen3 4b conll finetune

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen3_4b_conll_finetune_20260515T164745_result.json`
- **Structured JSON:** [`86e1f037bd412943785d.json`](../../sessions/86/86e1f037bd412943785d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全流程完成。总结：

## Scale Ablation 结果：Qwen3-4B vs 8B — CoNLL NER

### 5-Signal ρ 对比 (full split, n=2756)

| Signal | 8B ρ | 8B AUROC | 4B ρ | 4B AUROC | Δρ |
|--------|------|----------|------|----------|----|
| Voting | +0.4237 | 0.7889 | +0.4006 | 0.6880 | -0.023 |
| **SJ** | **+0.4357** | **0.8008** | **+0.4324** | 0.6931 | -0.003 |
| FK | +0.3998 | 0.7741 | +0.4244 | 0.6906 | +0.025 |
| EM | +0.4507 | 0.8156 | +0.4261 | 0.6919 | -0.025 |
| LP | +0.3157 | 0.7532 | +0.3295 | 0.7737 | +0.014 |

### 关键发现

1. **SJ > FK ordering 在 4B 保持** — SJ=0.4324 > FK=0.4244 (delta=+0.008)，与 8B 一致
2. **ρ 高度稳定** — 所有 5 信号的 ρ 在 4B/8B 间差异 < 0.03，结构一致性信号跨 scale 鲁棒
3. **AUROC 4B 全面下降约 0.1** — 4B 模型更高 greedy F1 (0.9208 vs 0.9079) 导致错误率更低，binary classification 更难
4. **LP tied fraction 严重恶化** — 4B: 71.5% vs 8B: 25.2%，小模型 logprob 区分度大幅退化
5. **Correlation-selection gap 缩小** — 4B oracle headroom +0.0176 vs 8B +0.0404，4B 更高 greedy F1 压缩了提升空间

---
